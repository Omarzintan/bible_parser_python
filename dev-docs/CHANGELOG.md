# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
