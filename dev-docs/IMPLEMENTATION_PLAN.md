# Bible Parser Python - Implementation Plan

## Overview

This document outlines the plan to create a Python version of the bible_parser package, mirroring the functionality of the Flutter implementation. The Python package will parse Bible texts in various XML formats (USFX, OSIS, ZEFANIA) with both direct parsing and database-backed approaches.

## Project Goals

1. **Feature Parity**: Match all core features from the Flutter version
2. **Pythonic Design**: Use Python idioms (generators, context managers, type hints)
3. **Performance**: Memory-efficient streaming XML parsing
4. **Production Ready**: Proper error handling, logging, and testing
5. **Easy to Use**: Simple API with comprehensive documentation

## Architecture

### Core Components

#### 1. Data Models (`models.py`)

**Verse**
```python
@dataclass
class Verse:
    num: int
    chapter_num: int
    text: str
    book_id: str
    
    def to_dict(self) -> dict
    @classmethod
    def from_dict(cls, data: dict) -> 'Verse'
```

**Chapter**
```python
@dataclass
class Chapter:
    num: int
    verses: List[Verse]
```

**Book**
```python
@dataclass
class Book:
    id: str
    num: int
    title: str
    chapters: List[Chapter]
    verses: List[Verse]
    
    def to_dict(self) -> dict
    @classmethod
    def from_dict(cls, data: dict) -> 'Book'
```

#### 2. Custom Exceptions (`errors.py`)

```python
class BibleParserException(Exception):
    """Base exception for bible parser"""
    
class ParseError(BibleParserException):
    """Raised when parsing fails"""
    
class FormatDetectionError(BibleParserException):
    """Raised when format cannot be detected"""
    
class ParserUnavailableError(BibleParserException):
    """Raised when parser for format is not available"""
```

#### 3. Base Parser (`parsers/base_parser.py`)

```python
from abc import ABC, abstractmethod
from collections.abc import Generator  # Use collections.abc instead of typing for Python 3.9+
from typing import Union
from pathlib import Path

class BaseParser(ABC):
    def __init__(self, source: Union[str, Path]):
        self.source = source
    
    @abstractmethod
    def parse_books(self) -> Generator[Book, None, None]:
        """Parse and yield books"""
        
    @abstractmethod
    def parse_verses(self) -> Generator[Verse, None, None]:
        """Parse and yield verses"""
        
    @abstractmethod
    def check_format(self, content: str) -> bool:
        """Check if content matches this parser's format"""
        
    def get_content(self) -> str:
        """Get XML content from source"""
```

#### 4. Format-Specific Parsers

**USFX Parser** (`parsers/usfx_parser.py`)
- Parses USFX format XML
- Uses streaming XML parser (defusedxml.ElementTree.iterparse)
- Book name mapping from USFX codes to canonical names
- Handles footnotes and cross-references

**OSIS Parser** (`parsers/osis_parser.py`)
- Parses OSIS format XML
- Streaming XML parsing
- Handles OSIS-specific tags and structure

**Zefania Parser** (`parsers/zefania_parser.py`)
- Parses Zefania XML Bible Markup Language
- Streaming XML parsing
- Handles Zefania-specific structure

#### 5. Main Parser (`bible_parser.py`)

```python
class BibleParser:
    def __init__(self, source: Union[str, Path], format: Optional[str] = None):
        self.source = source
        self.format = format or self._detect_format()
        self._parser = self._get_parser()
    
    @classmethod
    def from_string(cls, xml_content: str, format: Optional[str] = None):
        """Create parser from XML string"""
        
    @property
    def books(self) -> Generator[Book, None, None]:
        """Iterate over all books"""
        
    @property
    def verses(self) -> Generator[Verse, None, None]:
        """Iterate over all verses"""
        
    def _detect_format(self) -> str:
        """Auto-detect Bible format from XML content"""
        
    def _get_parser(self) -> BaseParser:
        """Get appropriate parser for format"""
```

#### 6. Database Repository (`bible_repository.py`)

```python
class BibleRepository:
    def __init__(self, xml_path: Optional[str] = None, 
                 xml_string: Optional[str] = None,
                 format: Optional[str] = None):
        self.xml_path = xml_path
        self.xml_string = xml_string
        self.format = format
        self._db = None
    
    def initialize(self, database_name: str) -> bool:
        """Initialize database, create if needed"""
        
    def get_books(self) -> List[Book]:
        """Get all books from database"""
        
    def get_verses(self, book_id: str, chapter_num: int) -> List[Verse]:
        """Get verses for specific chapter"""
        
    def get_chapter_count(self, book_id: str) -> int:
        """Get number of chapters in book"""
        
    def search_verses(self, query: str, limit: int = 100) -> List[Verse]:
        """Search for verses containing query"""
        
    def get_verse(self, book_id: str, chapter_num: int, 
                  verse_num: int) -> Optional[Verse]:
        """Get specific verse"""
        
    def close(self):
        """Close database connection"""
        
    def __enter__(self):
        """Context manager support"""
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager cleanup"""
```

## Implementation Steps

### Phase 1: Project Setup
- [ ] Create project directory structure
- [ ] Set up `pyproject.toml` with dependencies (primary configuration)
- [ ] Create minimal `setup.py` for backward compatibility (optional)
- [ ] Create `.gitignore` for Python
- [ ] Initialize `__init__.py` files

**Note:** `setup.py` as a configuration file is NOT deprecated, but running `python setup.py install` IS deprecated. Use `pip install .` instead.

**Dependencies:**
- Python 3.8+
- defusedxml (for secure XML parsing - REQUIRED for security)
- sqlite3 (stdlib)
- typing-extensions (for Python 3.8 compatibility with collections.abc types)

### Phase 2: Core Models & Exceptions
- [ ] Implement `Verse` dataclass with serialization
- [ ] Implement `Chapter` dataclass
- [ ] Implement `Book` dataclass with serialization
- [ ] Create custom exception hierarchy
- [ ] Add type hints throughout

### Phase 3: Parser Infrastructure
- [ ] Implement `BaseParser` abstract class
- [ ] Add XML content reading logic
- [ ] Add format checking interface
- [ ] Implement generator-based parsing interface

### Phase 4: Format Parsers
- [ ] Implement `UsfxParser`
  - Book name mapping
  - Streaming XML parsing
  - Chapter and verse extraction
  - Footnote handling
- [ ] Implement `OsisParser`
  - OSIS tag handling
  - Streaming parsing
  - Verse extraction
- [ ] Implement `ZefaniaParser`
  - Zefania structure handling
  - Streaming parsing

### Phase 5: Main Parser
- [ ] Implement `BibleParser` class
- [ ] Add format auto-detection
- [ ] Add parser factory logic
- [ ] Implement `from_string` factory method
- [ ] Add book and verse generators

### Phase 6: Database Repository
- [ ] Implement SQLite schema creation
- [ ] Add database initialization logic
- [ ] Implement XML to database import with transaction batching
- [ ] Add query methods (get_books, get_verses, etc.)
- [ ] Add search functionality with FTS5 (Full-Text Search version 5)
- [ ] Add context manager support (`__enter__` and `__exit__`)
- [ ] Add proper connection management and cleanup
- [ ] Use parameterized queries to prevent SQL injection

### Phase 7: Documentation
- [ ] Create comprehensive README.md
  - Installation instructions
  - Quick start guide
  - API documentation
  - Usage examples (both approaches)
  - Performance comparison
- [ ] Add docstrings to all classes and methods
- [ ] Create CHANGELOG.md
- [ ] Add LICENSE file (MIT)

### Phase 8: Testing
- [ ] Set up pytest configuration
- [ ] Create test fixtures with sample XML data
- [ ] Unit tests for data models
- [ ] Unit tests for each parser
- [ ] Integration tests for BibleParser
- [ ] Integration tests for BibleRepository
- [ ] Performance benchmarks

### Phase 9: Examples
- [ ] Create example script for direct parsing
- [ ] Create example script for database approach
- [ ] Add sample XML files (from open-bibles)
- [ ] Create Jupyter notebook tutorial

### Phase 10: Package Distribution
- [ ] Finalize `pyproject.toml`
- [ ] Create `MANIFEST.in` for package data
- [ ] Test package installation locally
- [ ] Prepare for PyPI publication (optional)

## Security Considerations

### XML Security
**Critical:** Bible XML files may come from untrusted sources. Standard Python XML libraries are vulnerable to:
- **XXE (XML External Entity) attacks** - Can read local files or make network requests
- **Billion Laughs attack** - Exponential entity expansion causing DoS
- **Quadratic blowup** - Large entity expansion causing memory exhaustion

**Solution:** Use `defusedxml` library which provides secure defaults:
```python
from defusedxml.ElementTree import parse, iterparse
# Instead of: from xml.etree.ElementTree import parse, iterparse
```

### SQL Injection Prevention
Always use parameterized queries:
```python
# GOOD
cursor.execute("SELECT * FROM verses WHERE book_id = ?", (book_id,))

# BAD - Never do this!
cursor.execute(f"SELECT * FROM verses WHERE book_id = '{book_id}'")
```

### Input Validation
- Validate book IDs, chapter numbers, verse numbers before database queries
- Sanitize search queries to prevent FTS injection
- Limit result set sizes to prevent memory exhaustion

## Technical Decisions

### XML Parsing Library
**Security Note:** Standard library XML parsers (xml.etree.ElementTree, xml.dom, etc.) are vulnerable to XML attacks (XXE, billion laughs, etc.). We MUST use defusedxml.

**Options:**
1. **defusedxml.ElementTree** (wraps stdlib)
   - ✅ Secure against XXE and DoS attacks
   - ✅ Drop-in replacement for xml.etree.ElementTree
   - ✅ Good performance
   - ✅ Streaming support with iterparse
   - ⚠️ Small external dependency (pure Python)

2. **defusedxml with lxml backend**
   - ✅ Secure and faster
   - ✅ More features (XPath, validation)
   - ❌ Requires C extension compilation

**Decision:** Use `defusedxml.ElementTree` as the primary parser for security. This is a REQUIRED dependency, not optional. Bible XML files may come from untrusted sources.

### Database
**SQLite3** (stdlib)
- ✅ No external dependencies
- ✅ Serverless, file-based
- ✅ Full-text search support
- ✅ Perfect for local caching

### Type Hints
Use comprehensive type hints with:
- `collections.abc` for Generator, Iterator, Iterable, Sequence, Mapping (Python 3.9+)
- `typing` module for Union, Optional, Any, TypeVar, Protocol
- `typing-extensions` for backports to Python 3.8 (e.g., TypeAlias)
- Return type annotations
- Parameter type annotations

**Note:** As of Python 3.9 (PEP 585), many types from `typing` are deprecated in favor of `collections.abc`. For Python 3.8 compatibility, we'll use conditional imports:

```python
import sys
if sys.version_info >= (3, 9):
    from collections.abc import Generator, Iterator
else:
    from typing import Generator, Iterator
```

### Dataclasses
Use standard library `dataclasses` (Python 3.7+):
- ✅ Built-in, no dependencies
- ✅ Good for simple data models
- ✅ Supports `__post_init__` for validation
- ✅ Works well with type hints

**Note:** We don't need Pydantic for this use case since:
- No complex validation needed
- No API serialization required
- Simpler is better for a parsing library

### Async Support
**Decision:** Start with synchronous implementation. Consider adding async version in future (using `aiofiles`, `aiosqlite`).

## API Design Examples

### Direct Parsing Approach

```python
from bible_parser import BibleParser

# From file
parser = BibleParser('path/to/bible.xml')

# From string with explicit format
parser = BibleParser.from_string(xml_content, format='USFX')

# Iterate over books
for book in parser.books:
    print(f"{book.title} ({book.id})")
    for chapter in book.chapters:
        for verse in chapter.verses:
            print(f"{book.id} {verse.chapter_num}:{verse.num} - {verse.text}")

# Or iterate over verses directly
for verse in parser.verses:
    print(f"{verse.book_id} {verse.chapter_num}:{verse.num} - {verse.text}")
```

### Database Approach

```python
from bible_parser import BibleRepository

# Create repository
repo = BibleRepository(xml_path='path/to/bible.xml', format='USFX')

# Initialize (only needed once)
repo.initialize('my_bible.db')

# Use context manager for automatic cleanup
with BibleRepository(xml_path='path/to/bible.xml') as repo:
    repo.initialize('my_bible.db')
    
    # Get all books
    books = repo.get_books()
    for book in books:
        print(f"{book.title} ({book.id})")
    
    # Get specific chapter
    verses = repo.get_verses('gen', 1)
    for verse in verses:
        print(f"{verse.book_id} {verse.chapter_num}:{verse.num} - {verse.text}")
    
    # Search
    results = repo.search_verses('love')
    print(f"Found {len(results)} verses")
```

## Performance Considerations

### Direct Parsing
- **Pros:** Simple, no setup, always fresh data
- **Cons:** CPU intensive, slower, higher memory for large files

**Optimizations:**
- Use streaming XML parsing (iterparse)
- Yield results as generators
- Minimize memory footprint

### Database Approach
- **Pros:** Fast queries, efficient search, low memory
- **Cons:** Initial setup time, disk space

**Optimizations:**
- Batch inserts during initialization
- Proper indexes on book_id, chapter_num, verse_num
- Full-text search index for verse text
- Connection pooling if needed

## Testing Strategy

### Unit Tests
- Test each parser with sample XML snippets
- Test data model serialization/deserialization
- Test format detection logic
- Test error handling

### Integration Tests
- Test full parsing workflow with real Bible files
- Test database initialization and queries
- Test search functionality
- Test edge cases (empty books, special characters)

### Performance Tests
- Benchmark parsing speed for each format
- Benchmark database query performance
- Memory usage profiling
- Compare with Flutter implementation

## Success Criteria

1. ✅ All three formats (USFX, OSIS, Zefania) parse correctly
2. ✅ Database caching works efficiently
3. ✅ Search functionality returns accurate results
4. ✅ Memory usage is reasonable for large Bible files
5. ✅ API is intuitive and well-documented
6. ✅ Test coverage > 80%
7. ✅ Compatible with Python 3.8+
8. ✅ Package can be installed via pip

## Future Enhancements

- Async/await support for non-blocking I/O
- Additional Bible formats (USX, ThML)
- Verse reference parsing (e.g., "John 3:16")
- Export to different formats (JSON, CSV)
- Web API wrapper (FastAPI/Flask)
- CLI tool for Bible queries
- Parallel parsing for multi-file Bibles
- Caching layer for frequently accessed verses

## Timeline Estimate

- **Phase 1-2:** 1 day (Setup + Models)
- **Phase 3-4:** 2-3 days (Parser infrastructure)
- **Phase 5:** 1 day (Main parser)
- **Phase 6:** 2 days (Database repository)
- **Phase 7:** 1 day (Documentation)
- **Phase 8:** 2 days (Testing)
- **Phase 9:** 1 day (Examples)
- **Phase 10:** 1 day (Package prep)

**Total:** ~11-12 days of focused development

## Key Changes from Original Plan

### ✅ Security Improvements
1. **Added `defusedxml` as required dependency** - Protects against XXE and DoS attacks
2. **Emphasized parameterized SQL queries** - Prevents SQL injection
3. **Added input validation requirements** - Prevents various attack vectors

### ✅ Modernization
1. **Use `collections.abc` instead of `typing`** - Following PEP 585 (Python 3.9+)
2. **Conditional imports for Python 3.8 compatibility** - Backward compatible
3. **Clarified setup.py usage** - Configuration file OK, but don't run as script
4. **Use FTS5 instead of generic FTS** - Latest full-text search version

### ✅ Best Practices
1. **Standard library dataclasses** - No need for Pydantic overhead
2. **Context managers for database** - Proper resource cleanup
3. **Transaction batching** - Better database performance
4. **Type hints throughout** - Better IDE support and type checking

## References

- Flutter implementation: `/bible_parser_flutter/`
- Ruby bible_parser: https://github.com/seven1m/bible_parser
- Open Bibles XML files: https://github.com/seven1m/open-bibles
- USFX Specification: http://ebible.org/usfx/
- OSIS Specification: http://www.bibletechnologies.net/
- defusedxml documentation: https://pypi.org/project/defusedxml/
- PEP 585 (Type Hinting Generics): https://peps.python.org/pep-0585/
- Python Packaging Guide: https://packaging.python.org/
