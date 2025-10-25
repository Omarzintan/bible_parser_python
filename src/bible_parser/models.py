"""Data models for Bible content."""

import sys
from dataclasses import dataclass, field
from typing import Dict, Any, List

# Python 3.9+ uses collections.abc, Python 3.8 uses typing
if sys.version_info >= (3, 9):
    pass  # Can use list[Verse] directly in 3.9+
else:
    pass  # Use List[Verse] from typing


@dataclass
class Verse:
    """Represents a single verse in the Bible.
    
    Attributes:
        num: The verse number within the chapter.
        chapter_num: The chapter number this verse belongs to.
        text: The text content of the verse.
        book_id: The book identifier (e.g., 'gen', 'mat').
    """

    num: int
    chapter_num: int
    text: str
    book_id: str

    def to_dict(self) -> Dict[str, Any]:
        """Convert verse to dictionary representation.
        
        Returns:
            Dictionary with verse data suitable for database storage.
        """
        return {
            "verse_num": self.num,
            "chapter_num": self.chapter_num,
            "text": self.text,
            "book_id": self.book_id,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Verse":
        """Create a Verse instance from a dictionary.
        
        Args:
            data: Dictionary containing verse data (typically from database).
            
        Returns:
            A new Verse instance.
        """
        return cls(
            num=data["verse_num"],
            chapter_num=data["chapter_num"],
            text=data["text"],
            book_id=data["book_id"],
        )

    def __str__(self) -> str:
        """Return a human-readable string representation."""
        return f"{self.book_id} {self.chapter_num}:{self.num} - {self.text}"


@dataclass
class Chapter:
    """Represents a chapter in a Bible book.
    
    Attributes:
        num: The chapter number.
        verses: List of verses in this chapter.
    """

    num: int
    verses: List[Verse] = field(default_factory=list)

    def __str__(self) -> str:
        """Return a human-readable string representation."""
        return f"Chapter {self.num} ({len(self.verses)} verses)"


@dataclass
class Book:
    """Represents a book of the Bible.
    
    Attributes:
        id: The book identifier (e.g., 'gen', 'exo', 'mat').
        num: The book number (1-66 for Protestant canon).
        title: The full title of the book (e.g., 'Genesis', 'Matthew').
        chapters: List of chapters in this book.
        verses: Flat list of all verses in this book.
    """

    id: str
    num: int
    title: str
    chapters: List[Chapter] = field(default_factory=list)
    verses: List[Verse] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        """Convert book to dictionary representation.
        
        Returns:
            Dictionary with book data suitable for database storage.
        """
        return {
            "id": self.id,
            "num": self.num,
            "title": self.title,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Book":
        """Create a Book instance from a dictionary.
        
        Args:
            data: Dictionary containing book data (typically from database).
            
        Returns:
            A new Book instance (without chapters/verses).
        """
        return cls(
            id=data["id"],
            num=data["num"],
            title=data["title"],
        )

    def __str__(self) -> str:
        """Return a human-readable string representation."""
        return f"{self.title} ({self.id}) - {len(self.chapters)} chapters, {len(self.verses)} verses"
