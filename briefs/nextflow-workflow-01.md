---
id: nextflow-workflow-01
title: Nextflow workflow connecting GTF download and gene parsing
status: draft
target_files:
  - main.nf
  - nextflow.config
---

<!--
  BLANK BRIEF — fill this in after both module briefs are implemented and
  verified:
    - briefs/nextflow-gtf-download-01.md (GTF_DOWNLOAD)
    - briefs/nextflow-gtf-genes-01.md (GTF_GENES)
  This brief only connects those modules. Any failure you hit here should
  be about how they're connected, not about the modules themselves.

  NOTE: there are no in-repo tests for this brief. Verification is
  either manual review of the workflow or running it outside this repo.
  Whichever you use, record it and its result in the log entry.

  Resolve each prompt into a declarative Requirements bullet, same as you
  did for the module briefs. Delete these prompts once done.
-->

## Context
One or two sentences: what the pipeline produces, and that it connects
the already-verified `GTF_DOWNLOAD` and `GTF_GENES` modules without
changing them.

## Inputs / Outputs
Workflow in `main.nf`, with settings in `nextflow.config`. You are
deciding these, not just filling them in:

- **Inputs:** *(which params does a user set on the command line? e.g.
  species, release, output directory. Which are required, and which have
  defaults?)*
- **Outputs:** *(what ends up in the output directory? what is each file
  called, and can you tell from the name which species and release it
  came from?)*

## Workflow
One numbered step per process. For each, say what it receives and what it
emits (the exact shape: a path? a record with the name and file?).

1. Build the input from params → *(what shape?)*
2. `GTF_DOWNLOAD` receives *(…)* → emits *(…)*
3. `GTF_GENES` receives *(…)* → emits *(…)*

## Out of Scope / Constraints
- Do not modify anything in `modules/` or `src/`.
- Do not modify any file outside `target_files`.


## Acceptance Criteria
- The workflow has been verified by manual review or by running it
  outside this repo, and the log entry says which method was used.
- A run on a small example (e.g. subsetted version of the full file)
  produces exactly the output files listed in Inputs / Outputs, and the
  output passes the validation chosen for it (e.g. a spot check of a few
  known genes and a plausible gene count).

## Definition of Done
- The log entry records how the workflow was verified and the result.
- No files outside `target_files` were modified.
- No TODOs, commented-out code, or unused parameters.

## Fix
*(left blank at brief time — filled in only for post-commit discoveries)*
