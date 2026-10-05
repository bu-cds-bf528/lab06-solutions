---
id: gc-content-01
title: GC content of a sequence window
status: ready
target_files:
  - src/gc_content.py
---

<!--
  WORKED EXAMPLE — read this before writing your own brief.
  This file is prefixed with "_" so the log checker ignores it; it is not
  something you implement, only something you read. Every one of the 8
  design categories below has already been resolved — no open questions
  remain. As you read, ask yourself: what would this function have done
  instead if this line weren't here?
-->

## Context
Computes GC content for a single sequence string.

## Inputs / Outputs
Function `gc_content` in `src/gc_content.py`.

- **Input:** `seq` (`str`): a DNA sequence.
- **Output:** `float`: the GC content of `seq`.

## Requirements
- Returns the fraction of G/C bases as a float in `[0.0, 1.0]` — not a
  percentage.
- Counting is case-insensitive (`g`, `G`, `c`, `C` all count).
- The denominator is the count of unambiguous bases only (`A`, `C`, `G`,
  `T`, case-insensitive). Ambiguous IUPAC codes (`N`, `R`, `Y`, etc.) are
  excluded from both numerator and denominator — they are neither counted
  as GC nor counted as sequence length.
- `seq` must be a `str`. Non-string input raises `TypeError`.
- If `seq` contains zero unambiguous bases (empty string, or entirely
  ambiguous codes), raises `ValueError` — GC content is undefined with a
  zero denominator, and silently returning `0.0` would be indistinguishable
  from "contains only A/T."
- Performs a single O(n) pass over the input string. Does not pre-scan,
  does not build an intermediate list of bases.

## Out of Scope / Constraints
- No support for streaming or chunking large sequences internally — this
  function always receives a complete string and processes exactly that
  string in one pass. If the caller is iterating over a larger sequence in
  pieces (e.g. an entire chromosome processed in chunks), that responsibility
  belongs entirely to the caller; `gc_content` does not know or care whether
  it's being called once on a 20bp fragment or once on a 2kb chunk — it has
  no special-case logic for input size and should not be given any. Do not
  add batching, buffering, or a "large sequence" code path.
- No parameter to change how ambiguous bases are handled — behavior above
  is fixed, not configurable.
- No percentage-vs-fraction toggle — always returns a fraction.
- No third-party dependencies — standard library only.
- Do not modify any file outside `target_files`.

## Acceptance Criteria
- All tests in `tests/test_gc_content.py` pass:
  `pytest tests/test_gc_content.py -v`
- No additional tests should be written by the agent — the test file is
  fixed and provided.

## Definition of Done
- The tests named in Acceptance Criteria pass.
- No files outside `target_files` were modified.
- Implementation contains no TODOs, commented-out code, or unused imports.

## Fix
*(left blank at brief time — filled in only for post-commit discoveries)*
