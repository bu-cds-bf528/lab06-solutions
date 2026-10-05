---
id: sliding-window-01
title: Sliding window over a sequence
status: draft
target_files:
  - src/sliding_window.py
---

<!--
  BLANK BRIEF — fill this in before handing it to Claude Code.
  Read briefs/_EXAMPLE-gc-content.md first if you haven't.

  Work through each prompt below and write your decision as a single
  declarative statement in ## Requirements — not a question, not a list of
  options, a decision. When you're done, every prompt here should have
  produced exactly one bullet below (or more, if a category needed more
  than one decision). Delete these prompts once your Requirements section
  is complete; a finished brief has no open questions in it.
-->

## Context
One or two sentences: what this is, what it's for.

## Inputs / Outputs
Function `sliding_window` in `src/sliding_window.py`. The name is fixed so
the tests can import it.

- **Inputs:**
  - `seq` (a string): the sequence to slide the window over.
  - `size` (a whole number): the length of each window.
  - `step` (a whole number): how far each window advances from the last
    (default `1`).
- **Output:** successive windows of `size` over `seq`, advancing by `step`.
  What a window looks like, and whether they come back as a list or a
  generator, are decided in Requirements below.

## Requirements

<!--
  Resolve each of the following before writing your Requirements bullets.
  Write each answer as a test there AND as a Requirement
  here.
  1. I/O Contract — list vs. generator return?
  2. Boundary & Edge Behavior — empty `seq`? `len(seq) < size`? A remainder
     that doesn't divide evenly into `step`?
  3. Domain Semantics — does this treat DNA specially (e.g. change the
     case of letters), or return the letters exactly as given?
  4. Parameterization — what should `step`'s default mean? Is padding a
     parameter, or out of scope entirely?
  5. Scale & Resource Behavior — does your answer to (1) hold up if `seq`
     were very large?
  6. Failure Handling — `size` of 0?
  7. Composability — if another function consumes each window, what shape
     does it need? Does a window carry its start index, or just the slice?
  8. Usability / Reusability — would this work unmodified on sequences
     that aren't DNA, like protein, or only on A/C/G/T?
-->

- *(your resolved requirements go here, one decision per line)*

## Out of Scope / Constraints
- No third-party dependencies — standard library only.
- No checks on input types: callers always pass a string for `seq` and
  whole numbers for `size` and `step`.
- Do not modify any file outside `target_files`.
- *(add anything else you're deliberately excluding)*

## Acceptance Criteria
- All tests in `tests/test_sliding_window.py` pass:
  `pytest tests/test_sliding_window.py -v`
- No additional tests should be written by the agent — the test file is
  provided, with its blanks filled in by your group.

## Definition of Done
- The tests named in Acceptance Criteria pass.
- No files outside `target_files` were modified.
- Implementation contains no TODOs, commented-out code, or unused imports.

## Fix
*(left blank at brief time — filled in only for post-commit discoveries)*
