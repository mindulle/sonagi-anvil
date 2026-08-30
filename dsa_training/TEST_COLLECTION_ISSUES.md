# DSA Training Test Collection Issues

The DSA training repository has issues with `pytest` collection and Python imports due to duplicate filenames across subdirectories (`test_*.py` and `*.py`).

## Conflicting Filenames
- `test_coin_change.py` exists in multiple directories.
- `test_course_schedule.py` exists in multiple directories.
- `test_binary_search.py` exists in multiple directories.
- ... and many others.

## Impact
- `pytest` collection fails due to `ImportError` when modules are incorrectly resolved across subdirectories.
- Python imports (`from X import Y`) import from the wrong subdirectory if multiple files have the same name.

## Proposed Solution
- Rename all conflicting `test_*.py` files and their corresponding logic files (`*.py`) to be unique (e.g., adding a prefix/suffix based on the subdirectory name).
- Or, make each subdirectory a Python package by adding `__init__.py` and restructuring imports to be absolute or relative within packages.
