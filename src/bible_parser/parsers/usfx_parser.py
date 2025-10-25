"""USFX format parser for Bible XML files."""

import sys
from typing import Dict, Optional

# Python 3.9+ uses collections.abc, Python 3.8 uses typing
if sys.version_info >= (3, 9):
    from collections.abc import Generator
else:
    from typing import Generator

try:
    from defusedxml.ElementTree import iterparse, ParseError as XMLParseError
except ImportError:
    from xml.etree.ElementTree import iterparse, ParseError as XMLParseError

from bible_parser.models import Book, Chapter, Verse
from bible_parser.parsers.base_parser import BaseParser
from bible_parser.errors import ParseError


class UsfxParser(BaseParser):
    """Parser for USFX (Unified Standard Format XML) Bible format.
    
    USFX is a simple XML format for Bible text that uses short element names
    for efficiency. It's commonly used for Bible translations.
    """

    # USFX book ID to canonical book name mapping
    BOOK_NAMES: Dict[str, str] = {
        "GEN": "Genesis",
        "EXO": "Exodus",
        "LEV": "Leviticus",
        "NUM": "Numbers",
        "DEU": "Deuteronomy",
        "JOS": "Joshua",
        "JDG": "Judges",
        "RUT": "Ruth",
        "1SA": "1 Samuel",
        "2SA": "2 Samuel",
        "1KI": "1 Kings",
        "2KI": "2 Kings",
        "1CH": "1 Chronicles",
        "2CH": "2 Chronicles",
        "EZR": "Ezra",
        "NEH": "Nehemiah",
        "EST": "Esther",
        "JOB": "Job",
        "PSA": "Psalms",
        "PRO": "Proverbs",
        "ECC": "Ecclesiastes",
        "SNG": "Song of Solomon",
        "ISA": "Isaiah",
        "JER": "Jeremiah",
        "LAM": "Lamentations",
        "EZK": "Ezekiel",
        "DAN": "Daniel",
        "HOS": "Hosea",
        "JOL": "Joel",
        "AMO": "Amos",
        "OBA": "Obadiah",
        "JON": "Jonah",
        "MIC": "Micah",
        "NAM": "Nahum",
        "HAB": "Habakkuk",
        "ZEP": "Zephaniah",
        "HAG": "Haggai",
        "ZEC": "Zechariah",
        "MAL": "Malachi",
        "MAT": "Matthew",
        "MRK": "Mark",
        "LUK": "Luke",
        "JHN": "John",
        "ACT": "Acts",
        "ROM": "Romans",
        "1CO": "1 Corinthians",
        "2CO": "2 Corinthians",
        "GAL": "Galatians",
        "EPH": "Ephesians",
        "PHP": "Philippians",
        "COL": "Colossians",
        "1TH": "1 Thessalonians",
        "2TH": "2 Thessalonians",
        "1TI": "1 Timothy",
        "2TI": "2 Timothy",
        "TIT": "Titus",
        "PHM": "Philemon",
        "HEB": "Hebrews",
        "JAS": "James",
        "1PE": "1 Peter",
        "2PE": "2 Peter",
        "1JN": "1 John",
        "2JN": "2 John",
        "3JN": "3 John",
        "JUD": "Jude",
        "REV": "Revelation",
    }

    # Book order for numbering
    BOOK_ORDER = list(BOOK_NAMES.keys())

    def check_format(self, content: str) -> bool:
        """Check if content is in USFX format.
        
        Args:
            content: XML content to check.
            
        Returns:
            True if content appears to be USFX format.
        """
        return "<usfx" in content.lower() or "<book" in content.lower()

    def _get_book_name(self, book_id: str) -> str:
        """Get the canonical book name from USFX book ID.
        
        Args:
            book_id: USFX book identifier (e.g., 'GEN', 'MAT').
            
        Returns:
            Canonical book name (e.g., 'Genesis', 'Matthew').
        """
        return self.BOOK_NAMES.get(book_id.upper(), book_id)

    def _get_book_num(self, book_id: str) -> int:
        """Get the book number from USFX book ID.
        
        Args:
            book_id: USFX book identifier.
            
        Returns:
            Book number (1-based index).
        """
        try:
            return self.BOOK_ORDER.index(book_id.upper()) + 1
        except ValueError:
            return 0

    def parse_books(self) -> Generator[Book, None, None]:
        """Parse USFX content and yield Book objects.
        
        Uses streaming XML parsing to minimize memory usage.
        
        Yields:
            Book objects with chapters and verses.
            
        Raises:
            ParseError: If parsing fails.
        """
        content = self.get_content()
        
        # Fix malformed XML: <ve/> tags inside verse text
        # Replace <ve/> with </v> to make it valid XML
        import re
        content = re.sub(r'<ve\s*/>', '</v>', content)
        
        # Use BytesIO for iterparse
        from io import BytesIO
        content_bytes = content.encode("utf-8")
        
        current_book: Optional[Book] = None
        current_chapter: Optional[Chapter] = None
        current_verse: Optional[Verse] = None
        inside_footnote = False
        inside_xref = False
        
        try:
            # Use iterparse for streaming parsing
            for event, elem in iterparse(BytesIO(content_bytes), events=("start", "end")):
                # Remove namespace from tag if present
                tag = elem.tag.split("}")[-1] if "}" in elem.tag else elem.tag
                
                if event == "start":
                    if tag == "book":
                        # Start of a new book
                        book_id = elem.get("id", "").lower()
                        if not book_id:
                            continue
                        
                        book_num = self._get_book_num(book_id)
                        book_name = self._get_book_name(book_id.upper())
                        
                        current_book = Book(
                            id=book_id,
                            num=book_num,
                            title=book_name,
                        )
                    
                    elif tag == "c" and current_book is not None:
                        # Start of a new chapter
                        chapter_num_str = elem.get("id", "1")
                        chapter_num = int(chapter_num_str) if chapter_num_str.isdigit() else 1
                        
                        # If we have a previous chapter, add it to the book
                        if current_chapter is not None and chapter_num != current_chapter.num:
                            current_book.chapters.append(current_chapter)
                            current_chapter = None
                        
                        current_chapter = Chapter(num=chapter_num)
                    
                    elif tag == "v" and current_book is not None and current_chapter is not None:
                        # Start of a new verse
                        verse_num_str = elem.get("id", "1")
                        verse_num = int(verse_num_str) if verse_num_str.isdigit() else 1
                        
                        # Get text content from the element
                        verse_text = elem.text or ""
                        
                        current_verse = Verse(
                            num=verse_num,
                            chapter_num=current_chapter.num,
                            text=verse_text.strip(),
                            book_id=current_book.id,
                        )
                    
                    elif tag == "f":
                        # Footnote start - skip content
                        inside_footnote = True
                    
                    elif tag == "x":
                        # Cross-reference start - skip content
                        inside_xref = True
                
                elif event == "end":
                    if tag == "book" and current_book is not None:
                        # End of book - add last chapter if exists
                        if current_chapter is not None:
                            current_book.chapters.append(current_chapter)
                        
                        # Flatten verses for easy access
                        for chapter in current_book.chapters:
                            current_book.verses.extend(chapter.verses)
                        
                        yield current_book
                        current_book = None
                        current_chapter = None
                    
                    elif tag == "v" and current_verse is not None and current_chapter is not None:
                        # End of verse - collect any tail text and add to chapter
                        if elem.tail and not inside_footnote and not inside_xref:
                            tail_text = elem.tail.strip()
                            if tail_text and current_verse.text:
                                current_verse.text += " " + tail_text
                        
                        current_chapter.verses.append(current_verse)
                        current_verse = None
                    
                    elif tag == "f":
                        inside_footnote = False
                    
                    elif tag == "x":
                        inside_xref = False
                    
                    # Clear element to free memory
                    elem.clear()
        
        except Exception as e:
            raise ParseError(f"Error parsing USFX books: {e}")

    def parse_verses(self) -> Generator[Verse, None, None]:
        """Parse USFX content and yield Verse objects directly.
        
        Yields:
            Verse objects.
            
        Raises:
            ParseError: If parsing fails.
        """
        for book in self.parse_books():
            for verse in book.verses:
                yield verse
