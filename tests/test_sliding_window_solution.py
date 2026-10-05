# SOLUTION for tests/test_sliding_window.py.
#
# There's no single right answer: this is one consistent set of decisions,
# with a short reason for each. Another group's different choices can be
# just as valid, as long as their tests and Requirements agree with each
# other.
#
# Implementation under test: src/sliding_window.py
# Run with: pytest tests/test_sliding_window_solution.py -v

# ---------------------------------------------------------------------------
# HOW PYTEST WORKS
# Run:  pytest tests/test_sliding_window_solution.py -v
#
# pytest finds every function whose name starts with test_ and runs it.
# With -v it prints each test's name followed by PASSED or FAILED.
#
# A test PASSES if its function runs to the end without an error.
# A test FAILS if:
#   - an assert line turns out to be false, or
#   - the code raises an error the test didn't expect.
#
# The building blocks used below:
#
#   assert A == B
#       Checks that A equals B. If it doesn't, the test fails and pytest
#       prints both values, so you can see what the code actually returned.
#
#   with pytest.raises(ValueError):
#       some_code()
#       Checks that the indented code raises a ValueError. If it raises no
#       error, or a different one, the test fails.
#
#   list(sliding_window(...))
#       Collects all the windows into a list so they can be compared with
#       an expected list. Works whether sliding_window returns a list or a
#       generator.
#
#   len(...)
#       Counts how many items are in a list.
#
# The lines from "import sys" down to "from ... import ..." are setup: they
# let Python find the code in src/. They aren't tests.
# ---------------------------------------------------------------------------

import sys
from pathlib import Path

import pytest

# src/ is not a package, so add it to the import path to import sliding_window.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from sliding_window import sliding_window  # noqa: E402

# ---------------------------------------------------------------------------
# Already filled in: these don't depend on any decision.
# ---------------------------------------------------------------------------

def test_number_of_windows_with_step_1():
    # Read from the inside out: get the windows, collect them into a list,
    # count them, and check the count is 4.
    assert len(list(sliding_window("ACGTAC", 3))) == 4


def test_number_of_windows_with_step_2():
    assert len(list(sliding_window("ACGTAC", 2, step=2))) == 3


# ---------------------------------------------------------------------------
# Decision 7 (Composability): just the slice.
# Simplest for whatever uses the windows next, e.g. gc_content(window). A
# caller that needs positions can get them with enumerate().
# ---------------------------------------------------------------------------

def test_window_shape():
    assert list(sliding_window("ACGTAC", 3)) == ["ACG", "CGT", "GTA", "TAC"]


# ---------------------------------------------------------------------------
# Decision 1 (I/O contract): generator.
# Windows are produced one at a time, so a whole chromosome doesn't need
# every window held in memory at once (see decision 5).
# ---------------------------------------------------------------------------

def test_returns_a_generator():
    result = sliding_window("ACGTAC", 3)
    # iter(result) asks for something that hands out the windows one at a
    # time. A generator already is that, so it hands back itself; a list
    # hands back a new object. So this line is true only for a generator.
    assert iter(result) is result


# ---------------------------------------------------------------------------
# Decision 2 (Boundary and edge behavior)
# ---------------------------------------------------------------------------

# Empty sequence: no windows. Nothing to window over isn't an error, and
# callers looping over the result just do nothing.
def test_empty_sequence_gives_no_windows():
    assert list(sliding_window("", 3)) == []


# Leftover at the end: dropped. A short window would have a different size
# from all the others, which could silently skew anything computed per
# window. Every window is exactly `size` long.
def test_leftover_at_end():
    assert list(sliding_window("ACGTA", 2, step=2)) == ["AC", "GT"]


# ---------------------------------------------------------------------------
# Decision 3 (Domain semantics): lowercase kept as-is.
# Windowing only cuts the sequence up. Changing letters is a separate job,
# and lowercase often carries meaning (e.g. soft-masked repeats in genome
# files).
# ---------------------------------------------------------------------------

def test_lowercase_input():
    assert list(sliding_window("acgt", 2)) == ["ac", "cg", "gt"]


# ---------------------------------------------------------------------------
# Decision 4 (Parameterization): the default step is 1 (fixed by the brief).
# ---------------------------------------------------------------------------

def test_default_step_is_1():
    assert list(sliding_window("ACGTAC", 3)) == list(sliding_window("ACGTAC", 3, step=1))


# ---------------------------------------------------------------------------
# Decision 5 (Scale and resource behavior): no test here.
# The generator choice in decision 1 is what makes this hold up on large
# input. That's checked by reading the code (interpretation trust).
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Decision 6 (Failure handling): size 0 raises an error.
# A window of size 0 is almost certainly a mistake by the caller. Returning
# [] would hide it.
# ---------------------------------------------------------------------------

def test_size_zero_raises_error():
    # Passes only if this raises a ValueError. list(...) is needed here too:
    # a generator doesn't run any of its code until its windows are asked for.
    with pytest.raises(ValueError):
        list(sliding_window("ACGT", 0))


# ---------------------------------------------------------------------------
# Decision 8 (Usability and reusability): works on any letters.
# Nothing about windowing is DNA-specific, so the same function can be
# reused for RNA or protein sequences.
# ---------------------------------------------------------------------------

def test_works_on_protein_sequence():
    assert len(list(sliding_window("MKVLA", 2))) == 4
