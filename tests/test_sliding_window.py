
# HOW TO USE THIS FILE
# Each test below asks one design question from the brief. There's no single
# right answer: your group decides.
#
#   - Where you see ___ , replace it with the answer your group chose.
#   - Where you see "KEEP ONE", two tests give opposite answers. Delete the
#     one you disagree with.
#   - Then write the same decision as a Requirement in the brief, under the
#     matching question number.
#
# The first two tests are already filled in: their answers don't depend on
# any decision, so they show the pattern.



# ---------------------------------------------------------------------------
# HOW PYTEST WORKS
# Run:  pytest tests/test_sliding_window.py -v
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

# For example, a window of 2 moving 1 at a time over "ABCDE" fits 4 times:
# AB, BC, CD, DE.
def test_number_of_windows_with_step_1():
    # Read from the inside out: get the windows, collect them into a list,
    # count them, and check the count is 4.
    assert len(list(sliding_window("ACGTAC", 3))) == 4


# For example, a window of 2 moving 2 at a time over "ABCDEFGH" fits 4 times:
# AB, CD, EF, GH.
def test_number_of_windows_with_step_2():
    assert len(list(sliding_window("ACGTAC", 2, step=2))) == 3


# ---------------------------------------------------------------------------
# Decision 7 (Composability): what does each window look like?
# Decide this one first: your answer sets the shape of every answer below.
# For example, windows of 2 over "ABCD" could look like:
#   Just the slice:              ["AB", "BC", "CD"]
#   Slice with start position:   [(0, "AB"), (1, "BC"), (2, "CD")]
# ---------------------------------------------------------------------------

def test_window_shape():
    assert list(sliding_window("ACGTAC", 3)) == ___


# ---------------------------------------------------------------------------
# Decision 1 (I/O contract): list or generator?
# A list holds every window at once. A generator produces them one at a time
# as they're used.
# KEEP ONE of these two tests.
# ---------------------------------------------------------------------------

def test_returns_a_list():
    # isinstance(x, list) is true if x is a list.
    assert isinstance(sliding_window("ACGTAC", 3), list)


def test_returns_a_generator():
    result = sliding_window("ACGTAC", 3)
    # iter(result) asks for something that hands out the windows one at a
    # time. A generator already is that, so it hands back itself; a list
    # hands back a new object. So this line is true only for a generator.
    assert iter(result) is result


# ---------------------------------------------------------------------------
# Decision 2 (Boundary and edge behavior)
# ---------------------------------------------------------------------------

# An empty sequence: no windows ([]), or an error?
# KEEP ONE of these two tests.
def test_empty_sequence_gives_no_windows():
    assert list(sliding_window("", 3)) == []


def test_empty_sequence_raises_error():
    # Passes only if this raises a ValueError. list(...) is needed here too:
    # a generator doesn't run any of its code until its windows are asked for.
    with pytest.raises(ValueError):
        list(sliding_window("", 3))


# A step that doesn't land exactly on the end. For example, windows of 3
# moving 3 at a time over "ABCDEFG" give "ABC", "DEF" and then a leftover
# "G". Is the leftover dropped, or kept as a short window?
def test_leftover_at_end():
    assert list(sliding_window("ACGTA", 2, step=2)) == ___


# ---------------------------------------------------------------------------
# Decision 3 (Domain semantics): does the function treat DNA specially?
# Is lowercase kept as-is, or changed to uppercase?
# ---------------------------------------------------------------------------

def test_lowercase_input():
    assert list(sliding_window("acgt", 2)) == ___


# ---------------------------------------------------------------------------
# Decision 4 (Parameterization): the default step.
# Already filled in: the brief fixes the default as 1, so leaving step out
# must give the same windows as step=1.
# ---------------------------------------------------------------------------

def test_default_step_is_1():
    assert list(sliding_window("ACGTAC", 3)) == list(sliding_window("ACGTAC", 3, step=1))


# ---------------------------------------------------------------------------
# Decision 5 (Scale and resource behavior): no test here.
# Whether the function holds up on a whole chromosome is hard to test with
# toy data. Like the "single pass" requirement in the GC content example, it
# is checked by reading the code and recorded in the log as interpretation
# trust.
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Decision 6 (Failure handling): bad size or step values.
# ---------------------------------------------------------------------------

# A window of size 0: no windows, or an error?
# KEEP ONE of these two tests.
def test_size_zero_gives_no_windows():
    assert list(sliding_window("ACGT", 0)) == []


def test_size_zero_raises_error():
    with pytest.raises(ValueError):
        list(sliding_window("ACGT", 0))


# ---------------------------------------------------------------------------
# Decision 8 (Usability and reusability): does it work on sequences that
# aren't DNA, like a protein sequence ("MKVLA"), or only on A/C/G/T?
# KEEP ONE of these two tests.
# ---------------------------------------------------------------------------

# Works on any letters, not just A/C/G/T.
def test_works_on_protein_sequence():
    assert len(list(sliding_window("MKVLA", 2))) == 4


# DNA only: letters other than A/C/G/T are rejected with an error.
def test_rejects_protein_sequence():
    with pytest.raises(ValueError):
        list(sliding_window("MKVLA", 2))
