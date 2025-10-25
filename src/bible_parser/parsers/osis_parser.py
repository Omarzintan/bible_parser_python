"""OSIS format parser for Bible XML files."""

import sys
from typing import Optional
from io import BytesIO

# Python 3.9+ uses collections.abc, Python 3.8 uses typing
if sys.version_info >= (3, 9):
    from collections.abc import Generator
else:
    from typing import Generator

from defusedxml.ElementTree import iterparse

from bible_parser.models import Book, Chapter, Verse
from bible_parser.parsers.base_parser import BaseParser
from bible_parser.errors import ParseError


class OsisParser(BaseParser):
    """Parser for OSIS (Open Scripture Information Standard) Bible format.
    
    OSIS is a comprehensive XML standard for encoding Biblical texts and related materials.
    """

    def check_format(self, content: str) -> bool:
        """Check if content is in OSIS format.
        
        Args:
            content: XML content to check.
            
        Returns:
            True if content appears to be OSIS format.
        """
        return "<osis" in content.lower() or "<osisText" in content.lower()

    def _parse_osis_id(self, osis_id: str) -> tuple[str, int, int]:
        """Parse OSIS verse ID (e.g., 'Gen.1.1' or 'Matt.5.3').
        
        Args:
            osis_id: OSIS verse identifier.
            
        Returns:
            Tuple of (book_id, chapter_num, verse_num).
        """
        parts = osis_id.split(".")
        if len(parts) >= 3:
            book_id = parts[0].lower()
            chapter_num = int(parts[1]) if parts[1].isdigit() else 1
            verse_num = int(parts[2]) if parts[2].isdigit() else 1
            return book_id, chapter_num, verse_num
        return "", 1, 1

    def parse_books(self) -> Generator[Book, None, None]:
        """Parse OSIS content and yield Book objects.
        
        Yields:
            Book objects with chapters and verses.
            
        Raises:
            ParseError: If parsing fails.
        """
        content = self.get_content()
        
        # Fix malformed XML: nested tags with eID
        # Replace <verse eID="..."/> and <chapter eID="..."/> with closing tags
        import re
        content = re.sub(r'<verse\s+eID="[^"]*"\s*/>', '</verse>', content)
        content = re.sub(r'<chapter\s+eID="[^"]*"\s*/>', '</chapter>', content)
        
        content_bytes = content.encode("utf-8")
        
        books_dict = {}  # Store books by ID
        current_book_id: Optional[str] = None
        current_verse: Optional[Verse] = None
        inside_note = False
        
        try:
            for event, elem in iterparse(BytesIO(content_bytes), events=("start", "end")):
                tag = elem.tag.split("}")[-1]  # Remove namespace
                
                if event == "start":
                    if tag == "div" and elem.get("type") == "book":
                        # Start of a book
                        osis_id = elem.get("osisID", "")
                        if osis_id:
                            current_book_id = osis_id.lower()
                            if current_book_id not in books_dict:
                                # Get book title from <title> child if available
                                title = current_book_id.capitalize()
                                books_dict[current_book_id] = Book(
                                    id=current_book_id,
                                    num=len(books_dict) + 1,
                                    title=title,
                                )
                    
                    elif tag == "verse":
                        # Start of a verse
                        osis_id = elem.get("osisID", "")
                        if osis_id and current_book_id:
                            book_id, chapter_num, verse_num = self._parse_osis_id(osis_id)
                            
                            # Get text content from the element
                            verse_text = elem.text or ""
                            
                            current_verse = Verse(
                                num=verse_num,
                                chapter_num=chapter_num,
                                text=verse_text.strip(),
                                book_id=book_id or current_book_id,
                            )
                    
                    elif tag == "note":
                        inside_note = True
                
                elif event == "end":
                    if tag == "verse" and current_verse is not None:
                        # End of verse - add to appropriate book
                        book_id = current_verse.book_id
                        if book_id in books_dict:
                            books_dict[book_id].verses.append(current_verse)
                        
                        current_verse = None
                    
                    elif tag == "note":
                        inside_note = False
                    
                    elem.clear()
            
            # Organize verses into chapters and yield books
            for book in books_dict.values():
                # Group verses by chapter
                chapters_dict = {}
                for verse in book.verses:
                    if verse.chapter_num not in chapters_dict:
                        chapters_dict[verse.chapter_num] = Chapter(num=verse.chapter_num)
                    chapters_dict[verse.chapter_num].verses.append(verse)
                
                # Add chapters to book in order
                book.chapters = [chapters_dict[num] for num in sorted(chapters_dict.keys())]
                
                yield book
        
        except Exception as e:
            raise ParseError(f"Error parsing OSIS books: {e}")

    def parse_verses(self) -> Generator[Verse, None, None]:
        """Parse OSIS content and yield Verse objects directly.
        
        Yields:
            Verse objects.
            
        Raises:
            ParseError: If parsing fails.
        """
        for book in self.parse_books():
            for verse in book.verses:
                yield verse
