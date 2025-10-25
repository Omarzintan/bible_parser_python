# bible-xml-parser v0.1.0

First stable release of the **bible-xml-parser** package for Python! 🎉

## 📦 Installation

```bash
pip install bible-xml-parser
```

**PyPI**: https://pypi.org/project/bible-xml-parser/

## ✨ Features

### XML Parsers
- 📖 **USFX Parser** - Unified Standard Format XML
- 📖 **OSIS Parser** - Open Scripture Information Standard
- 📖 **Zefania Parser** - Zefania XML Bible Markup Language
- 🔍 **Auto-detection** - Automatically detects Bible format

### Performance & Storage
- 💾 **SQLite Database Caching** - Fast access with persistent storage
- 🔎 **Full-Text Search** - FTS5-powered search across verses
- ⚡ **Memory-Efficient** - Streaming XML parsing with generators
- 🔒 **Secure** - Uses defusedxml to protect against XXE attacks

### Developer Experience
- 📝 **Type Hints** - Full type coverage for better IDE support
- 🧪 **Well-Tested** - 27 tests with 71% coverage
- 📚 **Examples Included** - Working examples with sample Bible files
- 🐍 **Python 3.8+** - Supports Python 3.8 through 3.12

## 🚀 Quick Start

### Direct Parsing

```python
from bible_parser import BibleParser

# Parse a Bible XML file (format auto-detected)
parser = BibleParser("bible.xml")

# Iterate over books
for book in parser.books:
    print(f"{book.title} - {len(book.verses)} verses")

# Access specific verses
for verse in parser.verses:
    if verse.book_id == "gen" and verse.chapter_num == 1:
        print(f"{verse.num}: {verse.text}")
```

### Database Approach

```python
from bible_parser import BibleRepository

# Initialize with database caching
with BibleRepository(xml_path="bible.xml") as repo:
    repo.initialize("bible.db")
    
    # Get all books
    books = repo.get_books()
    
    # Get verses from a chapter
    verses = repo.get_verses("gen", 1)
    
    # Search with full-text search
    results = repo.search_verses("love")
```

## 📚 Documentation

- **README**: https://github.com/Omarzintan/bible_parser_python#readme
- **Examples**: See `examples/` directory with working code
- **API Docs**: Full docstrings in source code

## 🔧 What's Included

### Source Code
- 3 XML parsers (USFX, OSIS, Zefania)
- Database repository with FTS5 search
- Data models (Verse, Chapter, Book)
- Custom exception hierarchy

### Examples
- `direct_parsing.py` - Direct XML parsing
- `database_approach.py` - Database caching
- `search_example.py` - Full-text search
- Sample Bible XML files (Genesis)

### Tests
- 27 comprehensive tests
- 71% code coverage
- Tests for all parsers and formats

## 🛠️ Technical Details

### Dependencies
- **defusedxml** (>=0.7.1) - Secure XML parsing
- **typing-extensions** (>=4.0.0) - For Python 3.8 compatibility

### Supported Formats
- **USFX** - Unified Standard Format XML
- **OSIS** - Open Scripture Information Standard  
- **Zefania** - Zefania XML Bible Markup Language

### Python Support
- Python 3.8
- Python 3.9
- Python 3.10
- Python 3.11
- Python 3.12

## 📄 License

MIT License - See LICENSE file for details

## 🙏 Acknowledgments

Thanks to the Bible translation community for providing open XML formats and sample files.

## 🐛 Issues & Contributions

- **Issues**: https://github.com/Omarzintan/bible_parser_python/issues
- **Contributions**: Pull requests welcome!

---

**Full Changelog**: https://github.com/Omarzintan/bible_parser_python/commits/v0.1.0
