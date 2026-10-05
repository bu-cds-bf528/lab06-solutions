# Tests for briefs/_EXAMPLE-gc-content.md.
#
# Each test checks one decision from the brief's Requirements, using toy
# sequences short enough that the right answer is obvious by eye. If a test
# fails, its name tells you which decision the implementation got wrong.
#
# ---------------------------------------------------------------------------
# HOW PYTEST WORKS
# Run:  pytest tests/test_gc_content.py -v
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
# The lines from "import sys" down to "from ... import ..." are setup: they
# let Python find the code in src/. They aren't tests.
# ---------------------------------------------------------------------------

import sys
from pathlib import Path

import pytest

# src/ is not a package, so add it to the import path to import gc_content.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from gc_content import gc_content  # noqa: E402


# Sanity checks at the two extremes: all G/C gives 1.0, no G/C gives 0.0.
def test_all_gc_returns_one():
    # Calls gc_content("GGCC") and checks the result equals 1.0.
    assert gc_content("GGCC") == 1.0


def test_all_at_returns_zero():
    assert gc_content("AATT") == 0.0


# 2 of 4 bases are G/C, so the answer is 0.5. A percentage version would
# return 50.
def test_returns_fraction_not_percentage():
    assert gc_content("GCAT") == 0.5


# Gives the same answer as the uppercase sequence.
def test_counting_is_case_insensitive():
    assert gc_content("gcAT") == gc_content("GCAT") == 0.5


# Counting the Ns in the length would give 2/6 ≈ 0.33 instead.
def test_ambiguous_bases_excluded_from_denominator():
    assert gc_content("GCNNNN") == 1.0


# could be G or C, but must not be counted as GC. Unambiguous bases are
# G, A, T, so the answer is 1/3.
def test_mixed_iupac_codes_excluded():
    assert gc_content("GARYTN") == 1 / 3


# "" would look the same as a sequence of only A/T.
def test_empty_string_raises_value_error():
    # Passes only if gc_content("") raises a ValueError. Returning any value,
    # even 0.0, makes this test fail.
    with pytest.raises(ValueError):
        gc_content("")


def test_all_ambiguous_raises_value_error():
    with pytest.raises(ValueError):
        gc_content("NNRY")


# Note: pytest.raises passes for a TypeError raised anywhere, including one
# the code hits by accident. Read the error message to confirm the type was
# checked on purpose.
def test_non_string_raises_type_error():
    with pytest.raises(TypeError):
        gc_content(None)


