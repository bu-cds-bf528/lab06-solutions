# Project Instructions

This repository uses a brief-driven workflow. Work is defined in `briefs/`,
verified by tests in `tests/`, and logged in `logs/`. This applies to every
brief in this repository — not just the one you're currently working on.

Whenever you implement or modify code in response to a brief in `briefs/`,
before you consider the task done:

1. Read the brief's frontmatter for its `id` and `target_files`.
2. Implement only within `target_files`. Do not modify files outside that
   list, and do not modify other briefs or other briefs' logs.
3. Run the tests named in the brief's Acceptance Criteria.
4. Append an entry to `logs/<id>.md` (create the file if it doesn't exist
   yet) with:
   - Timestamp
   - Brief id
   - Files changed
   - Test result (pass/fail, with output if failed)
   - One line distinguishing what you verified by running tests (execution
     trust) from what you're asserting is correct by your own judgment,
     without a test behind it (interpretation trust)

Do this automatically, without being asked, for every brief. Do not
consider a brief complete until its log entry exists and its tests pass
(or you've stated clearly in the log why they don't).

Do not add functionality, parameters, files, or dependencies beyond what a
brief's Requirements and Out of Scope sections specify, even if it seems
like a reasonable improvement.
