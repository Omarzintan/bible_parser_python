#!/bin/bash
# Release Commands for v0.2.0

echo "=========================================="
echo "Bible Parser Python - Release v0.2.0"
echo "=========================================="
echo ""

# 1. Run all tests
echo "1. Running all tests..."
PYTHONPATH=src python -m pytest tests/ -v
if [ $? -ne 0 ]; then
    echo "❌ Tests failed! Please fix before releasing."
    exit 1
fi
echo "✅ All tests passed!"
echo ""

# 2. Check git status
echo "2. Checking git status..."
git status
echo ""

# 3. Stage all changes
echo "3. Staging changes..."
git add .
echo "✅ Changes staged"
echo ""

# 4. Commit with message
echo "4. Creating commit..."
git commit -F GIT_COMMIT_MESSAGE.txt
echo "✅ Commit created"
echo ""

# 5. Create git tag
echo "5. Creating git tag v0.2.0..."
git tag -a v0.2.0 -m "Release v0.2.0 - Bible Reference Formatter

Major new feature: Bible reference parsing and formatting

See RELEASE_NOTES_v0.2.0.md for full details."
echo "✅ Tag created"
echo ""

# 6. Show what will be pushed
echo "6. Changes ready to push:"
git log --oneline -1
git tag -l "v0.2.0"
echo ""

# 7. Build package
echo "7. Building package..."
python -m build
if [ $? -ne 0 ]; then
    echo "❌ Build failed!"
    exit 1
fi
echo "✅ Package built"
echo ""

# 8. Instructions for pushing
echo "=========================================="
echo "✅ Release prepared successfully!"
echo "=========================================="
echo ""
echo "Next steps:"
echo ""
echo "1. Push to GitHub:"
echo "   git push origin main"
echo "   git push origin v0.2.0"
echo ""
echo "2. Create GitHub Release:"
echo "   - Go to: https://github.com/Omarzintan/bible_parser_python/releases/new"
echo "   - Tag: v0.2.0"
echo "   - Title: Release v0.2.0 - Bible Reference Formatter"
echo "   - Description: Copy from RELEASE_NOTES_v0.2.0.md"
echo ""
echo "3. Publish to PyPI:"
echo "   python -m twine upload dist/*"
echo ""
echo "4. Verify installation:"
echo "   pip install --upgrade bible-xml-parser"
echo "   python -c 'from bible_parser import BibleReferenceFormatter; print(\"Success!\")'"
echo ""
