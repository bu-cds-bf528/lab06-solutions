# Tests for the NAIVE version of sliding_window: the one produced from a
# plain prompt (e.g. "write a sliding window function"), with no brief.
#
# Implementation under test: src/sliding_window_naive.py
# Run with: pytest tests/test_sliding_window_naive.py -v
#
# HOW TO USE THIS FILE
# First fill in tests/test_sliding_window.py. Then copy every test from it
# (everything below the "from sliding_window import sliding_window" line)
# and paste it at the bottom of this file, so both versions are checked
# against the same decisions.
#
# For how pytest works (assert, pytest.raises, list(...)), see the
# explanation at the top of tests/test_sliding_window.py.
#
# The naive prompt never saw your group's decisions, so a failure here shows
# what the naive version decided instead. A pass means it happened to decide
# the same way you did.

import sys
from pathlib import Path

import pytest  # noqa: F401  (used by the tests you paste in)

# src/ is not a package, so add it to the import path to import
# sliding_window_naive.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from sliding_window_naive import sliding_window  # noqa: E402, F401

# Paste your filled-in tests below this line.
