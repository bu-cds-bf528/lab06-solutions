---
id: gc-content-exercise
title: GC content of a sequence window (Part 1 exercise)
status: draft
target_files:
  - src/gc_content.py
---

## Context
Computes GC content for a single sequence string.

## Inputs / Outputs
Function `gc_content` in `src/gc_content.py`.

- **Input:** `seq` (`str`): a DNA sequence.
- **Output:** `float`: the GC content of `seq`.

## Requirements
- *(one decision per line, from the tests)*

## Out of Scope / Constraints
- *(what the function should NOT do or have)*

## Acceptance Criteria
- All tests in `tests/test_gc_content.py` pass:
  `pytest tests/test_gc_content.py -v`
- No additional tests should be written by the agent — the test file is
  fixed and provided.

## Definition of Done
- The tests named in Acceptance Criteria pass.
- No files outside `target_files` were modified.
- Implementation contains no TODOs, commented-out code, or unused imports.
