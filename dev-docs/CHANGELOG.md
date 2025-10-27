# Changelog

All notable changes to the bible-xml-parser project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2025-10-26

### Added
- **Bible Reference Formatter** - New module for parsing Bible references
  - Parse simple verse references (e.g., "John 3:16")
  - Parse verse ranges (e.g., "John 3:16-18")
  - Parse multi-chapter ranges (e.g., "Genesis 1:1-2:3")
  - Parse complex patterns with commas (e.g., "John 3:16,18,20-22")
  - Parse chapter-only references (e.g., "Psalm 23")
  - Parse multi-chapter ranges (e.g., "Ruth 1-4")
  - Parse semicolon-separated references (e.g., "Genesis 1:1-3;2:3-4")
  - Handle parenthetical descriptions (e.g., "1 Samuel 17:1-58 (David and Goliath)")
  - Extract first verse from complex references
  - Validate book names
  - Cross-format compatibility (OSIS, USFX, Zefania)
- **New Data Models**:
  - `BibleReference` - Structured representation of parsed references
  - `VerseRange` - Representation of verse ranges for complex patterns
  - `ReferenceFormatError` - Specific exception for reference parsing errors
- **Convenience Method**: `get_verses_from_reference()` - Parse and retrieve verses in one call
- **Comprehensive Tests**: 50 tests with 70% code coverage for reference formatter
- **Examples**: New `reference_formatter_example.py` with 11 usage examples
- **Documentation**: Updated README with reference parsing section and API reference

### Changed
- Updated package description to mention reference parsing capability
- Enhanced examples README with reference formatter documentation

### Security
- Input validation for reference strings (max 500 characters)
- Complexity limits to prevent abuse (max 50 comma-separated, max 20 semicolon-separated)
- Proper error handling with specific exception types

## [0.1.1] - 2025-10-25

### Fixed
- **OSIS Parser**: Fixed parsing of modern OSIS files (KJV, ASV, etc.) that use `sID`/`eID` verse markers
  - Parser now correctly collects text between verse start and end markers
  - Maintains backward compatibility with old-style OSIS format
  - Tested with KJV (9.6 MB, 81 books, 31,102 verses)
- **USFX Parser**: Fixed parsing of USFX files (WEB, etc.) that use `<v>`/`<ve/>` verse markers
  - Parser now correctly collects text between verse markers
  - Properly handles footnotes and cross-references
  - Tested with WEB (5.9 MB, 86 books)

### Changed
- Removed XML tag conversion approach in favor of text collection between markers
- Improved text extraction to handle inline elements and tail text correctly

## [0.1.0] - 2025-10-25

### Added
- Initial release of bible-parser Python package
- Support for three Bible XML formats: USFX, OSIS, and ZEFANIA
- Automatic format detection
- Direct parsing approach with streaming XML
- Database-backed approach with SQLite caching
- Full-text search using SQLite FTS5
- Secure XML parsing with defusedxml
- Type hints throughout the codebase
- Context manager support for BibleRepository
- Comprehensive documentation and examples
- Python 3.8+ support with conditional imports for type hints

### Security
- Uses defusedxml to protect against XXE attacks
- Parameterized SQL queries to prevent SQL injection
- Input validation and sanitization

[0.1.0]: https://github.com/yourusername/bible_parser_python/releases/tag/v0.1.0
