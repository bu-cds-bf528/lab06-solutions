---
id: <short-slug, e.g. gc-content-01>
title: <one line>
status: draft            # draft | ready | in-progress | done
target_files:
  - <path/to/implementation.py>
---

## Context
One or two sentences: what this is, what (if anything) it plugs into.

## Inputs / Outputs
Function `<name>` in `<path/to/implementation.py>`. Not negotiable by the
agent.

- **Inputs:** each parameter, its type, and its default if it has one.
- **Output:** what is returned (or yielded), and its type.

## Requirements
Declarative, resolved statements — one per line, one decision per line.
Pull these from the 8-category design checklist (`01-general-template.md`),
translated from checklist-answer to statement form.

## Out of Scope / Constraints
Explicit negative space — what the agent should NOT add.

## Acceptance Criteria
- All tests in `tests/test_<name>.py` pass:
  `pytest tests/test_<name>.py -v`
- No additional tests should be written by the agent — the test file is
  fixed and provided.

## Definition of Done
- The tests named in Acceptance Criteria pass.
- No files outside `target_files` were modified.
- Implementation contains no TODOs, commented-out code, or unused imports.

## Fix
*(left blank at brief time — filled in only for post-commit discoveries)*
