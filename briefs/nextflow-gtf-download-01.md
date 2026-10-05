---
id: nextflow-gtf-download-01
title: Nextflow process that downloads a GTF
status: draft
target_files:
  - modules/download/main.nf
---

## Context
A nextflow module that downloads a file

## Inputs / Outputs
- **Inputs:** A URL (string)
- **Outputs:** The File (path)

## Requirements

- label 'process_single'
- an environment with wget
- use static typing conventions

## Out of Scope / Constraints
- Do not modify any file outside `target_files`.


## Acceptance Criteria
- The process has been verified by manual review or by running it outside
  this repo, and the log entry says which method was used.

## Definition of Done
- The log entry records how the process was verified and the result.
- No files outside `target_files` were modified.
- No TODOs, commented-out code, or unused parameters.

## Fix
*(left blank at brief time — filled in only for post-commit discoveries)*
