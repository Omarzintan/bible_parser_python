# PyPI Upload Guide

## ✅ Package Built Successfully!

Your distribution files are ready:
- `dist/bible_xml_parser-0.1.0-py3-none-any.whl` (19 KB)
- `dist/bible_xml_parser-0.1.0.tar.gz` (24 KB)

Both files passed `twine check` validation!

## Option 1: Upload to TestPyPI (Recommended First)

TestPyPI is a separate instance of PyPI for testing. This lets you verify everything works before publishing to the real PyPI.

### 1. Create TestPyPI Account
- Go to: https://test.pypi.org/account/register/
- Verify your email

### 2. Create API Token
- Go to: https://test.pypi.org/manage/account/token/
- Click "Add API token"
- Token name: "bible-xml-parser-upload"
- Scope: "Entire account" (or specific to bible-xml-parser)
- Copy the token (starts with `pypi-`)

### 3. Upload to TestPyPI
```bash
twine upload --repository testpypi dist/*
```

When prompted:
- Username: `__token__`
- Password: (paste your API token)

### 4. Test Installation from TestPyPI
```bash
# Create a test environment
python -m venv test_env
source test_env/bin/activate  # On Windows: test_env\Scripts\activate

# Install from TestPyPI
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ bible-xml-parser

# Test it works
python -c "from bible_parser import BibleParser; print('Success!')"

# Deactivate
deactivate
```

## Option 2: Upload to PyPI (Production)

Once you've tested on TestPyPI and everything works:

### 1. Create PyPI Account
- Go to: https://pypi.org/account/register/
- Verify your email

### 2. Create API Token
- Go to: https://pypi.org/manage/account/token/
- Click "Add API token"
- Token name: "bible-xml-parser-upload"
- Scope: "Entire account" (or specific to bible-xml-parser after first upload)
- Copy the token

### 3. Upload to PyPI
```bash
twine upload dist/*
```

When prompted:
- Username: `__token__`
- Password: (paste your API token)

### 4. Verify on PyPI
- Check: https://pypi.org/project/bible-xml-parser/
- Verify README displays correctly
- Check that metadata is correct

### 5. Test Installation
```bash
pip install bible-xml-parser
```

## Recommended Workflow

```bash
# 1. Test on TestPyPI first
twine upload --repository testpypi dist/*

# 2. Verify it works
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ bible-xml-parser

# 3. If everything looks good, upload to real PyPI
twine upload dist/*

# 4. Verify on PyPI
pip install bible-xml-parser
```

## After Publishing

1. **Update GitHub README** - Add PyPI badge:
   ```markdown
   ![PyPI](https://img.shields.io/pypi/v/bible-xml-parser)
   ![Python Versions](https://img.shields.io/pypi/pyversions/bible-xml-parser)
   ![Downloads](https://img.shields.io/pypi/dm/bible-xml-parser)
   ```

2. **Create GitHub Release** - Link to PyPI package

3. **Announce** - Share on relevant communities

4. **Monitor** - Watch for issues and feedback

## Troubleshooting

### Package Name Already Taken
If `bible-xml-parser` is taken, you'll get an error. Check availability at https://pypi.org/

Alternative names if needed:
- `python-bible-parser`
- `biblical-parser`
- `pybible-parser`

### Upload Fails
- Make sure you're using `__token__` as username (with two underscores)
- Token should start with `pypi-`
- Check you have the right permissions

### README Not Displaying
- Make sure `readme = "README.md"` is in pyproject.toml
- Check README is valid Markdown
- Rebuild and re-upload

## Security Best Practices

1. **Never commit API tokens** to git
2. **Use scoped tokens** when possible
3. **Rotate tokens** periodically
4. **Use 2FA** on your PyPI account

## Current Status

✅ Package built: `bible_xml_parser-0.1.0`
✅ Distribution files validated
✅ Ready to upload!

---

**Next Command:**
```bash
# Upload to TestPyPI first (recommended)
twine upload --repository testpypi dist/*

# Or upload directly to PyPI
twine upload dist/*
```
