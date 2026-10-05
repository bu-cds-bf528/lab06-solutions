---
id: nextflow-gtf-genes-01
title: Nextflow process wrapping the GTF gene parser
status: draft
target_files:
  - modules/gtf_genes.nf
---

<!--
  BLANK BRIEF — fill this in after gtf-genes-01 (Part 3) is implemented and
  you've checked it works. Do not start this until that function's logic is
  verified; any failure you hit here should be about Nextflow wrapping, not
  about the underlying parser.

  NOTE: there are no in-repo tests for this brief. Verification is
  either manual review of the process or running it outside this repo.
  Whichever you use, record it and its result in the log entry.

  Resolve each prompt into a declarative Requirements bullet, same as you
  did for the Python brief. Delete these prompts once done.
-->

## Context
One or two sentences: what this process does, and that it wraps the
already-verified `gtf_genes` function from `gtf-genes-01`.

## Inputs / Outputs
Process `GTF_GENES` in `modules/gtf_genes.nf`, which calls into
`src/gtf_genes.py`. You are deciding these, not just filling them in:

- **Inputs:** *(what comes in? a path to a GTF? a tuple with a name or
  genome build attached?)*
- **Outputs:** *(what goes out? a TSV of gene_id and gene_name? what is
  it called, and does it have a header row?)*

## Requirements

<!--
  1. I/O Contract — val/path/tuple types for input: and output:. Strict
     output filename or a glob? What columns, in what order, and is there
     a header?
  2. Boundary & Edge Behavior — what happens if the input channel is
     empty? What if the GTF has no gene records at all?
  3. Domain Semantics — most GTFs are downloaded gzipped (.gtf.gz). Does
     this process accept those, and if so, does the process or the Python
     function decompress them? Are version suffixes on gene IDs
     (ENSG00000141510.18 vs ENSG00000141510) kept or stripped, and is
     that this process's job or the function's?
  4. Parameterization — what's exposed as `params.x` (e.g. the GTF path,
     the output name) vs. hardcoded in the script block? Where do
     defaults live?
  5. Scale & Resources — a human GTF is over 1 GB uncompressed. What
     cpus/memory/time directives does this need? Does the parser read the
     whole file into memory?
  6. Failure Handling — what errorStrategy, and why that one? Critically:
     what's your plan for catching a case where the process exits 0 but
     produced an empty or wrong output (e.g. a GTF where no record has a
     gene_name, so the TSV has a header and no rows)?
  7. Composability — does this process's input match exactly what
     GTF_DOWNLOAD (briefs/nextflow-gtf-download-01.md) outputs (gzipped or
     not, filename)? And what does the next process in a real pipeline need?
     For example, joining these names onto a gene count matrix by gene_id:
     does the gene_id format here match the count matrix's?
  8. Usability / Reusability — how does the process find
     `src/gtf_genes.py` (a path relative to the project, Nextflow's `bin/`
     convention, a container)? Any hardcoded paths that only work on one
     machine?
-->

- *(your resolved requirements go here, one decision per line)*

## Out of Scope / Constraints
- Do not modify `src/gtf_genes.py` or `gtf-genes-01`'s log.
- Do not modify any file outside `target_files`.
- *(add anything else you're deliberately excluding)*

## Acceptance Criteria
- The process has been verified by manual review or by running it outside
  this repo, and the log entry says which method was used.
- Verification covers at least one case where the process completes
  successfully (exit 0) but the output has no genes in it — this is the
  deliberate break exercise. Confirm explicitly whether that case is
  treated as a pipeline error or silently allowed, and that your
  Requirements above said which.

## Definition of Done
- The log entry records how the process was verified and the result.
- No files outside `target_files` were modified.
- No TODOs, commented-out code, or unused parameters.

## Fix
*(left blank at brief time — filled in only for post-commit discoveries)*
