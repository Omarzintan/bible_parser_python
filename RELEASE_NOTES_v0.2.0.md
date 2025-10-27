# Release Notes - v0.2.0

**Release Date:** October 26, 2025

## 🎉 Major New Feature: Bible Reference Formatter

This release introduces a powerful new Bible reference parsing module that allows you to parse and work with Bible references in various formats.

## ✨ What's New

### Bible Reference Parsing

Parse Bible references in multiple formats and retrieve verses:

```python
from bible_parser import BibleReferenceFormatter, BibleRepository

with BibleRepository(xml_path='bible.xml', format='OSIS') as repo:
    repo.initialize('bible.db')
    
    # Parse a simple verse reference
    ref = BibleReferenceFormatter.parse("John 3:16", repo)
    print(f"Book: {ref.book_id}, Chapter: {ref.chapter_num}, Verse: {ref.verse_num}")
    
    # Get verses directly (convenience method)
    verses = BibleReferenceFormatter.get_verses_from_reference("John 3:16-18", repo)
    for verse in verses:
        print(f"{verse.chapter_num}:{verse.num} - {verse.text}")
```

### Supported Reference Formats

- ✅ **Single verse**: `"John 3:16"`
- ✅ **Verse range**: `"John 3:16-18"`
- ✅ **Multi-chapter**: `"Genesis 1:1-2:3"`
- ✅ **Chapter only**: `"Psalm 23"`
- ✅ **Multi-chapter range**: `"Ruth 1-4"`
- ✅ **Complex patterns**: `"John 3:16,18,20-22"`
- ✅ **Semicolon-separated**: `"Genesis 1:1-3;2:3-4"`
- ✅ **With descriptions**: `"1 Samuel 17:1-58 (David and Goliath)"`

### Cross-Format Compatibility

The reference formatter works seamlessly with all supported Bible formats:
- **OSIS** (e.g., KJV)
- **USFX** (e.g., WEB)
- **Zefania** (e.g., ASV)

Different Bible formats use different book IDs, but the formatter handles this automatically through flexible matching.

### New API Methods

#### `BibleReferenceFormatter.parse(reference, bible_repository)`
Parse a reference string into a structured `BibleReference` object.

#### `BibleReferenceFormatter.get_verses_from_reference(reference, bible_repository)`
Parse a reference and retrieve all matching verses in one call.

#### `BibleReferenceFormatter.get_first_verse_in_reference(reference)`
Extract the first verse from a complex reference.

#### `BibleReferenceFormatter.is_valid_book(book_name)`
Check if a book name is valid.

### New Data Models

- **`BibleReference`**: Structured representation of a parsed Bible reference
  - `book_id`, `chapter_num`, `verse_num`
  - `end_chapter_num`, `end_verse_num` for ranges
  - `is_chapter_only` flag
  - `additional_verses` for complex patterns

- **`VerseRange`**: Representation of verse ranges
  - `chapter_num`, `start_verse`, `end_verse`

- **`ReferenceFormatError`**: Specific exception for reference parsing errors

### Security Features

- Input validation (max 500 characters)
- Complexity limits (max 50 comma-separated verses, max 20 semicolon-separated parts)
- Proper error handling with specific exception types
- Integer validation with clear error messages

### Testing & Quality

- **50 comprehensive tests** with 100% pass rate
- **70% code coverage** on reference formatter module
- Tests cover all reference formats, error handling, and security features
- Integration tests with BibleRepository

### Documentation & Examples

- Updated README with reference parsing section
- New comprehensive example file: `reference_formatter_example.py`
- Updated examples README with usage instructions
- API reference documentation updated

## 📦 Installation

```bash
pip install --upgrade bible-xml-parser
```

## 🔄 Migration Guide

This is a minor version update with new features. No breaking changes to existing APIs.

If you're upgrading from v0.1.x:
- All existing code will continue to work
- New reference parsing features are opt-in
- No changes required to existing code

## 📊 Statistics

- **Lines of Code Added**: ~880 lines (implementation + tests + examples)
- **Test Coverage**: 70% on new module, 62% overall
- **Supported Formats**: 8 reference formats
- **Supported Books**: All 66 Bible books + variants (Psalm/Psalms, etc.)

## 🙏 Acknowledgments

The Bible Reference Formatter implementation is based on the Dart version from the Salt project, adapted and enhanced for Python with cross-format compatibility.

## 🐛 Bug Reports & Feature Requests

Please report issues at: https://github.com/Omarzintan/bible_parser_python/issues

## 📝 Full Changelog

See [CHANGELOG.md](dev-docs/CHANGELOG.md) for complete details.

---

**Version**: 0.2.0  
**Previous Version**: 0.1.1  
**Release Type**: Minor (New Features)
