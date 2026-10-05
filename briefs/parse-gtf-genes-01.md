---
id: parse-gtf-genes-01
title: Python script for parsing a GTF
status: draft
target_files:
  - bin/parse_gtf.py
---

## Context
A python script that extracts gene_id and gene_name from the GTF file

## Inputs / Outputs

- **Inputs:** a GTF file (gzipped)
- **Outputs:** a csv with gene_id and gene_name as columns

## Requirements

- uses argparse to specify inputs and outputs
- label 'process_single'

## Out of Scope / Constraints
- Do not modify any file outside `target_files`.
- do not remove duplicates, just parse every line

## Acceptance Criteria
- The process has been verified by manual review or by running it outside
  this repo, and the log entry says which method was used.

## Definition of Done
- The log entry records how the process was verified and the result.
- No files outside `target_files` were modified.
- No TODOs, commented-out code, or unused parameters.

## Fix
*(left blank at brief time — filled in only for post-commit discoveries)*
