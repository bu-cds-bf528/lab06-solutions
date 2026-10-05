---
id: nextflow-gtf-download-01
title: Nextflow process that downloads a GTF
status: draft
target_files:
  - modules/gtf_download.nf
---

<!--
  BLANK BRIEF — fill this in at the start of Part 4. Its output becomes the
  input to GTF_GENES (briefs/nextflow-gtf-genes-01.md), so fill the two
  briefs in side by side.

  NOTE: there are no in-repo tests for this brief. Verification is
  either manual review of the process or running it outside this repo.
  Whichever you use, record it and its result in the log entry.

  Resolve each prompt into a declarative Requirements bullet, same as you
  did for the Python briefs. Delete these prompts once done.
-->

## Context
One or two sentences: what this process downloads, from where, and what
uses its output.

## Inputs / Outputs
Process `GTF_DOWNLOAD` in `modules/gtf_download.nf`. You are deciding
these, not just filling them in:

- **Inputs:** *(a full URL? or a species and release number that the
  process turns into a URL?)*
- **Outputs:** *(the GTF file: what is it called, and is it still gzipped
  or decompressed?)*

## Requirements

<!--
  1. I/O Contract — val/path types for input: and output:. Strict output
     filename or a glob? Gzipped or decompressed output?
  2. Boundary & Edge Behavior — what happens if the URL doesn't exist
     (a 404)? If the connection drops halfway?
  3. Domain Semantics — which source: Ensembl, GENCODE, or RefSeq? They
     differ in ways that matter downstream: chromosome names (1 vs chr1),
     which attributes are present, and what gene_id looks like. Is the
     release pinned to a specific number, or "latest"? A "latest" URL gives
     a different file next year, so the same pipeline gives different
     results.
  4. Parameterization — what's exposed as `params.x` (URL, species,
     release) vs. hardcoded? Where do defaults live?
  5. Scale & Resources — a human GTF is around 50 MB gzipped. What time
     limit is reasonable? Should a rerun download it again, or reuse the
     file it already has?
  6. Failure Handling — what errorStrategy, and why that one? Network
     errors are often temporary: retry, and how many times? Critically:
     what's your plan for catching a case where the process exits 0 but
     the file is wrong (e.g. the server returned an HTML error page that
     got saved as the GTF, or the download was cut short)?
  7. Composability — does the output match exactly what GTF_GENES expects
     as input (gzipped or not, filename)? Check the two briefs agree.
  8. Usability / Reusability — which download tool does the script use
     (wget, curl), and is it available wherever this runs (a container)?
     Any hardcoded paths that only work on one machine?
-->

- *(your resolved requirements go here, one decision per line)*

## Out of Scope / Constraints
- Do not modify any file outside `target_files`.
- *(add anything else you're deliberately excluding)*

## Acceptance Criteria
- The process has been verified by manual review or by running it outside
  this repo, and the log entry says which method was used.
- Verification covers at least one case where the process completes
  successfully (exit 0) but the file it produced isn't a valid GTF — this
  is the deliberate break exercise. Confirm explicitly whether that case
  is treated as a pipeline error or silently allowed, and that your
  Requirements above said which.

## Definition of Done
- The log entry records how the process was verified and the result.
- No files outside `target_files` were modified.
- No TODOs, commented-out code, or unused parameters.

## Fix
*(left blank at brief time — filled in only for post-commit discoveries)*
