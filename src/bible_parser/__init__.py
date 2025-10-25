"""
Bible Parser - A Python package for parsing Bible texts in various XML formats.

This package provides tools to parse Bible texts in USFX, OSIS, and ZEFANIA formats
with both direct parsing and database-backed approaches.
"""

__version__ = "0.1.0"

from bible_parser.models import Verse, Book, Chapter
from bible_parser.errors import (
    BibleParserException,
    ParseError,
    FormatDetectionError,
    ParserUnavailableError,
)
from bible_parser.bible_parser import BibleParser
from bible_parser.bible_repository import BibleRepository

__all__ = [
    "Verse",
    "Book",
    "Chapter",
    "BibleParserException",
    "ParseError",
    "FormatDetectionError",
    "ParserUnavailableError",
    "BibleParser",
    "BibleRepository",
]
