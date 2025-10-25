# 🐛 Bug Fix Release: v0.1.1

Critical bug fix release adding support for modern OSIS and USFX Bible file formats.

## 🔥 Key Fixes

### OSIS Parser - Modern Format Support
Fixed parsing of modern OSIS files that use `sID`/`eID` verse markers:
- ✅ **King James Version (KJV)** now loads correctly
- ✅ **American Standard Version (ASV)** now loads correctly
- ✅ All OSIS files with sID/eID markers now supported

### USFX Parser - Modern Format Support  
Fixed parsing of USFX files that use `<v>`/`<ve/>` verse markers:
- ✅ **World English Bible (WEB)** now loads correctly
- ✅ All USFX files with v/ve markers now supported

## ✅ Tested With Real-World Files

- **KJV** (9.6 MB, 81 books, 31,102 verses) ✅
- **ASV** (5.0 MB, 66 books) ✅
- **WEB** (5.9 MB, 86 books) ✅

## 📦 Installation

```bash
pip install --upgrade bible-xml-parser
```

## 🔄 Backward Compatibility

**Fully backward compatible** with v0.1.0:
- All existing APIs unchanged
- Old-style OSIS/USFX formats still supported
- No breaking changes

## 📊 Test Results

- **27/27 unit tests passing** (100%)
- **3/3 real-world Bible files passing** (100%)
- Code coverage: 72%

## 🔗 Links

- **PyPI**: https://pypi.org/project/bible-xml-parser/0.1.1/
- **Full Release Notes**: [RELEASE_NOTES_v0.1.1.md](RELEASE_NOTES_v0.1.1.md)
- **Changelog**: [CHANGELOG.md](dev-docs/CHANGELOG.md)

---

**What's Changed**
- Fixed OSIS parser for modern sID/eID verse markers by @Omarzintan
- Fixed USFX parser for v/ve verse markers by @Omarzintan
- Added backward compatibility for old-style formats by @Omarzintan
- Fixed deprecated license format in pyproject.toml by @Omarzintan
- Updated test fixtures to match real-world formats by @Omarzintan

**Full Changelog**: https://github.com/Omarzintan/bible_parser_python/compare/v0.1.0...v0.1.1
