# Release Checklist - v0.2.0

## Pre-Release Verification

- [x] Version bumped to 0.2.0 in `pyproject.toml`
- [x] CHANGELOG.md updated with v0.2.0 entry
- [x] All tests passing (50/50 tests)
- [x] Code coverage acceptable (70% on new module)
- [x] Documentation updated (README.md)
- [x] Examples updated and tested
- [x] Release notes created
- [x] No hardcoded file paths in examples

## Release Process

### 1. Run Tests
```bash
./RELEASE_COMMANDS.sh
```

Or manually:
```bash
PYTHONPATH=src python -m pytest tests/ -v
```

### 2. Git Commit & Tag
```bash
git add .
git commit -F GIT_COMMIT_MESSAGE.txt
git tag -a v0.2.0 -m "Release v0.2.0 - Bible Reference Formatter"
```

### 3. Push to GitHub
```bash
git push origin main
git push origin v0.2.0
```

### 4. Create GitHub Release
1. Go to: https://github.com/Omarzintan/bible_parser_python/releases/new
2. Select tag: `v0.2.0`
3. Release title: `Release v0.2.0 - Bible Reference Formatter`
4. Description: Copy content from `RELEASE_NOTES_v0.2.0.md`
5. Publish release

### 5. Build Package
```bash
python -m build
```

### 6. Publish to PyPI
```bash
# Test PyPI first (optional)
python -m twine upload --repository testpypi dist/*

# Production PyPI
python -m twine upload dist/*
```

### 7. Verify Installation
```bash
pip install --upgrade bible-xml-parser
python -c "from bible_parser import BibleReferenceFormatter; print('Success!')"
```

## Post-Release

- [ ] Verify package on PyPI: https://pypi.org/project/bible-xml-parser/
- [ ] Test installation in clean environment
- [ ] Update project documentation if needed
- [ ] Announce release (if applicable)
- [ ] Close related issues/PRs

## Rollback Plan

If issues are discovered:

1. Remove PyPI package version (if possible)
2. Remove git tag:
   ```bash
   git tag -d v0.2.0
   git push origin :refs/tags/v0.2.0
   ```
3. Revert commit:
   ```bash
   git revert HEAD
   ```
4. Fix issues and re-release as v0.2.1

## Notes

- This is a **minor version** release (new features, no breaking changes)
- All existing v0.1.x code will continue to work
- New features are opt-in
- Tested with Python 3.8, 3.9, 3.10, 3.11, 3.12
- Cross-format compatibility verified (OSIS, USFX, Zefania)
