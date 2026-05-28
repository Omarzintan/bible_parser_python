"""Tests for USFX <toc> tag parsing into Book title fields."""

import pytest
from bible_parser.parsers.usfx_parser import UsfxParser


TOC_XML = """<?xml version="1.0" encoding="UTF-8"?>
<usfx>
  <book id="GEN">
    <toc level="1">The First Book of Moses, Commonly Called Genesis</toc>
    <toc level="2">Genesis</toc>
    <toc level="3">Gen</toc>
    <c id="1"/>
    <v id="1"/>In the beginning God created the heavens and the earth.<ve/>
  </book>
</usfx>
"""

NO_TOC_XML = """<?xml version="1.0" encoding="UTF-8"?>
<usfx>
  <book id="GEN">
    <c id="1"/>
    <v id="1"/>In the beginning God created the heavens and the earth.<ve/>
  </book>
</usfx>
"""


class TestUsfxTocParsing:
    def test_parses_all_three_toc_levels(self):
        parser = UsfxParser(TOC_XML)
        books = list(parser.parse_books())

        assert len(books) == 1
        book = books[0]
        assert book.long_title == "The First Book of Moses, Commonly Called Genesis"
        assert book.short_title == "Genesis"
        assert book.abbreviation == "Gen"

    def test_toc_fields_are_none_when_absent(self):
        parser = UsfxParser(NO_TOC_XML)
        books = list(parser.parse_books())

        assert len(books) == 1
        book = books[0]
        assert book.title == "Genesis"
        assert book.long_title is None
        assert book.short_title is None
        assert book.abbreviation is None

    def test_toc_does_not_bleed_into_verse_text(self):
        parser = UsfxParser(TOC_XML)
        books = list(parser.parse_books())

        verse = books[0].verses[0]
        assert "Moses" not in verse.text
        assert "Genesis" not in verse.text
        assert "In the beginning" in verse.text
