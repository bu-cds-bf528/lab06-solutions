---
id: nextflow-gtf-genes-01
title: Nextflow process wrapping the GTF gene parser
status: draft
target_files:
  - modules/gtf_parse/main.nf
---


## Context
A nextflow module that calls the script in the bin

## Inputs / Outputs

- **Inputs:** A GTF file (Path)
- **Outputs:** A CSV containing gene_id and gene_name (Path)

## Requirements

- use static typing conventions
- use an environment with python available
- label 'process_single'
- a stub run that creates a fake .csv with touch
- uses bin/parse_gtf.py (called as just parse_gtf.py)

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
