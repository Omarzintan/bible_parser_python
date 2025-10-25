# Release Notes - Version 0.1.1

**Release Date**: October 25, 2025  
**PyPI**: https://pypi.org/project/bible-xml-parser/0.1.1/

## 🎉 What's New

Version 0.1.1 is a **critical bug fix release** that adds support for modern OSIS and USFX Bible file formats used by major Bible translations.

## 🐛 Bug Fixes

### OSIS Parser - Modern Format Support
**Fixed parsing of modern OSIS files** (KJV, ASV, and other major translations)

Modern OSIS files use `sID`/`eID` verse markers instead of simple verse tags:
```xml
<!-- Modern OSIS (now supported) -->
<verse osisID="Gen.1.1" sID="Gen.1.1.seID.00002" n="1" />
In the beginning God created the heaven and the earth.
<verse eID="Gen.1.1.seID.00002" />
```

**Impact**: 
- ✅ King James Version (KJV) now loads correctly
- ✅ American Standard Version (ASV) now loads correctly
- ✅ All OSIS files with sID/eID markers now supported
- ✅ Backward compatibility maintained for old-style OSIS

### USFX Parser - Modern Format Support
**Fixed parsing of USFX files** (WEB and other translations)

USFX files use `<v>`/`<ve/>` verse markers:
```xml
<!-- Modern USFX (now supported) -->
<v id="1"/>In the beginning, God created the heavens and the earth.
<ve/>
```

**Impact**:
- ✅ World English Bible (WEB) now loads correctly
- ✅ All USFX files with v/ve markers now supported
- ✅ Backward compatibility maintained for old-style USFX

## 🔧 Technical Changes

### Parser Improvements
- Replaced XML tag conversion with text collection between markers
- Improved text extraction to handle inline elements (e.g., `<transChange>`)
- Better handling of element tail text
- Proper exclusion of footnotes and cross-references

### Code Quality
- Fixed deprecated `project.license` format in `pyproject.toml`
- Updated test fixtures to match real-world Bible file formats
- Added backward compatibility tests

## ✅ Testing

### Unit Tests
- **27/27 tests passing** (100%)
- Coverage: 72% overall, 85-92% for parsers

### Real-World Files Tested
- ✅ **KJV** (eng-kjv.osis.xml) - 9.6 MB, 81 books, 31,102 verses
- ✅ **ASV** (eng-asv.osis.xml) - 5.0 MB, 66 books
- ✅ **WEB** (eng-web.usfx.xml) - 5.9 MB, 86 books

All files load correctly with accurate verse text and working search functionality.

## 📦 Installation

### Upgrade from 0.1.0
```bash
pip install --upgrade bible-xml-parser
```

### Fresh Install
```bash
pip install bible-xml-parser
```

## 🚀 Usage Example

```python
from bible_parser import BibleRepository

# Works with KJV, ASV, WEB, and other major translations
repo = BibleRepository(xml_path="path/to/bible.xml")
repo.initialize("bible.db")

# Get books
books = repo.get_books()

# Get verses
verses = repo.get_verses("gen", 1)
print(verses[0].text)  # "In the beginning God created..."

# Search
results = repo.search_verses("faith")

repo.close()
```

## 🔄 Backward Compatibility

Version 0.1.1 maintains **full backward compatibility** with 0.1.0:
- ✅ All existing APIs unchanged
- ✅ Old-style OSIS format still supported
- ✅ Old-style USFX format still supported
- ✅ Zefania format unchanged
- ✅ No breaking changes

## 📊 Supported Formats

### OSIS (Open Scripture Information Standard)
- ✅ Old style: `<verse osisID="...">text</verse>`
- ✅ Modern style: `<verse sID="..."/>text<verse eID="..."/>`
- ✅ Tested with: KJV, ASV

### USFX (Unified Standard Format XML)
- ✅ Old style: `<v id="1">text</v>`
- ✅ Modern style: `<v id="1"/>text<ve/>`
- ✅ Tested with: WEB

### Zefania XML
- ✅ Standard format: `<VERS vnumber="1">text</VERS>`
- ✅ Unchanged from 0.1.0

## 🐛 Known Issues

None reported in this release.

## 📝 Migration Guide

No migration needed! Simply upgrade:
```bash
pip install --upgrade bible-xml-parser
```

Your existing code will continue to work without any changes.

## 🙏 Acknowledgments

Special thanks to the Bible Desktop App project for helping identify and test these critical parser fixes with real-world Bible files.

## 📄 Full Changelog

See [CHANGELOG.md](dev-docs/CHANGELOG.md) for complete details.

## 🔗 Links

- **PyPI**: https://pypi.org/project/bible-xml-parser/0.1.1/
- **GitHub**: https://github.com/Omarzintan/bible_parser_python
- **Documentation**: See README.md
- **Issues**: https://github.com/Omarzintan/bible_parser_python/issues

## 📈 What's Next

Future releases may include:
- Additional Bible format support
- Performance optimizations
- Enhanced search capabilities
- More comprehensive test coverage

---

**Version**: 0.1.1  
**Released**: October 25, 2025  
**License**: MIT
