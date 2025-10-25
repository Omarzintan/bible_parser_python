# Release 0.1.1 - Pre-Upload Checklist

**Date**: October 25, 2025  
**Version**: 0.1.1  
**Status**: Ready for PyPI Upload

## Changes in This Release

### Fixed
- ✅ **OSIS Parser**: Modern OSIS files (KJV, ASV) now parse correctly
  - Fixed sID/eID verse marker handling
  - Tested with KJV (9.6 MB, 81 books, 31,102 verses)
  
- ✅ **USFX Parser**: USFX files (WEB) now parse correctly
  - Fixed v/ve verse marker handling
  - Tested with WEB (5.9 MB, 86 books)

### Changed
- Improved text extraction to handle inline elements
- Better handling of footnotes and cross-references

## Pre-Upload Checklist

### Version & Documentation
- ✅ Version bumped to 0.1.1 in `pyproject.toml`
- ✅ CHANGELOG.md updated with release notes
- ✅ README.md is up to date (no changes needed)

### Code Quality
- ✅ All parser fixes implemented
- ✅ Code compiles without errors
- ✅ No syntax errors

### Testing
- ✅ KJV OSIS file loads successfully
- ✅ ASV OSIS file loads successfully
- ✅ WEB USFX file loads successfully
- ✅ All 3 Bible files tested (100% pass rate)
- ✅ Genesis 1:1 displays correctly in all formats
- ✅ Search functionality works
- ✅ Database creation works

### Build
- ✅ Old build artifacts cleaned
- ✅ Package built successfully with `python -m build`
- ✅ Wheel file created: `bible_xml_parser-0.1.1-py3-none-any.whl` (20K)
- ✅ Source distribution created: `bible_xml_parser-0.1.1.tar.gz` (25K)

### Files Modified
1. `src/bible_parser/parsers/osis_parser.py` - Fixed sID/eID handling
2. `src/bible_parser/parsers/usfx_parser.py` - Fixed v/ve handling
3. `pyproject.toml` - Version bump to 0.1.1
4. `dev-docs/CHANGELOG.md` - Added release notes

## Upload Commands

### Test Upload (TestPyPI)
```bash
python -m twine upload --repository testpypi dist/*
```

### Production Upload (PyPI)
```bash
python -m twine upload dist/*
```

You'll be prompted for:
- Username: `__token__`
- Password: Your PyPI API token

## Post-Upload Verification

After uploading, verify:

1. **Check PyPI page**: https://pypi.org/project/bible-xml-parser/
2. **Install from PyPI**:
   ```bash
   pip install --upgrade bible-xml-parser
   ```
3. **Test installation**:
   ```python
   from bible_parser import BibleRepository
   print(BibleRepository.__module__)  # Should show bible_parser
   ```
4. **Test with Bible app**:
   ```bash
   cd bible_app_python
   pip install --upgrade bible-xml-parser
   python src/main.py
   # Load KJV, WEB, ASV files
   ```

## Expected Results

After upload:
- ✅ Package version 0.1.1 visible on PyPI
- ✅ Can install with `pip install bible-xml-parser`
- ✅ KJV, ASV, WEB files load correctly
- ✅ All verses parse with correct text
- ✅ Search works across all formats

## Rollback Plan

If issues are found after upload:
1. Document the issue
2. Fix in code
3. Bump to 0.1.2
4. Upload new version
5. Note: Cannot delete/replace existing PyPI versions

## Notes

- This is a bug fix release (patch version bump)
- No breaking changes
- Backward compatible with 0.1.0
- All existing functionality preserved
- New functionality: Support for modern OSIS and USFX formats

---

**Ready to Upload**: ✅ YES  
**Tested**: ✅ YES  
**Documented**: ✅ YES  
**Built**: ✅ YES

**Next Step**: Run `python -m twine upload dist/*`
