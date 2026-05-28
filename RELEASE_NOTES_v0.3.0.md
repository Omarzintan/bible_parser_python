# Release Notes - v0.3.0

## ✨ What's New

### Book Title Levels from USFX `<toc>` Tags

The `Book` model now exposes three optional title fields parsed from USFX `<toc>` tags:

| Field | Toc Level | Example |
|-------|-----------|---------|
| `long_title` | 1 | `"The First Book of Moses, Commonly Called Genesis"` |
| `short_title` | 2 | `"Genesis"` |
| `abbreviation` | 3 | `"Gen"` |

All fields default to `None` when not present in the source XML — fully backward compatible.

```python
from bible_parser import BibleParser

parser = BibleParser('bible.usfx.xml')
for book in parser.books:
    print(book.long_title or book.title)   # e.g. "The First Book of Moses..."
    print(book.short_title)                # e.g. "Genesis"
    print(book.abbreviation)               # e.g. "Gen"
```

### Database Support

The `books` table gains three new nullable columns: `long_title`, `short_title`, `abbreviation`.

- **New databases** are created with the columns automatically.
- **Existing databases** are migrated non-destructively via `ALTER TABLE` on first open — no data loss.

## 🔄 Breaking Changes

None — all new fields are optional and default to `None`.

## 🧪 Testing

Added `tests/test_usfx_toc.py` with 3 tests covering:
- Correct parsing of all three toc levels
- `None` fallback when toc tags are absent
- Toc text does not leak into verse text
