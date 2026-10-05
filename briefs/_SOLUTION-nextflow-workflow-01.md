---
id: nextflow-workflow-01
title: Nextflow workflow connecting GTF download and gene parsing
status: ready
target_files:
  - main.nf
  - nextflow.config
---

<!--
  SOLUTION — a filled-in version of briefs/nextflow-workflow-01.md. This is
  one consistent set of decisions, not the only right one.

  It assumes the two module briefs were filled in with these interfaces:
    - GTF_DOWNLOAD: receives a record { url }; emits a record { url, gtf },
      where gtf is the downloaded file, still gzipped. Fails if the
      download fails.
    - GTF_GENES: receives a record { url, gtf }; emits a record
      { url, genes }, where genes is a tab-separated table with a header
      row and columns gene_id, gene_name.
-->

## Context
Downloads one GTF from a fixed URL and produces a table of gene_id and
gene_name. Connects the already-verified `GTF_DOWNLOAD` and `GTF_GENES`
modules without changing them.

## Inputs / Outputs
Workflow in `main.nf`, with settings in `nextflow.config`.

- **Inputs:**
  - `params.gtf_url`: the GTF to download, hardcoded in `nextflow.config`
    to a specific Ensembl release:
    `https://ftp.ensembl.org/pub/release-112/gtf/saccharomyces_cerevisiae/Saccharomyces_cerevisiae.R64-1-1.112.gtf.gz`
  - `params.outdir`: where outputs go, default `results`.
- **Outputs:**
  - `<outdir>/genes.tsv`: tab-separated, header row, columns `gene_id`,
    `gene_name`, one row per gene.

## Workflow
1. Make a record `{ url }` from `params.gtf_url`.
2. `GTF_DOWNLOAD` receives `{ url }` → emits `{ url, gtf }`.
3. `GTF_GENES` receives `{ url, gtf }` → emits `{ url, genes }`.
4. Check `genes` has at least one gene row, then publish it to
   `<outdir>/genes.tsv`.

## Requirements
- Every step passes a record with named fields, as listed in the Workflow
  section, not a positional tuple. The `url` field travels to the end, so
  the output can always be traced back to its source.
- The GTF URL is set once, in `nextflow.config`, and pinned to a specific
  Ensembl release, so the same run always produces the same table.
- The modules never read `params` directly. The workflow passes in
  everything they need.
- If the download fails, the run stops. `GTF_GENES` never runs on a
  failed download.
- After `GTF_GENES`, the workflow checks the table has at least one row
  below the header. If not, the run fails with an error naming the URL,
  rather than exiting 0 with an empty table.
- Outputs are copied to `<outdir>`, not symlinked into `work/`, so they
  survive cleaning `work/`.

## Out of Scope / Constraints
- One GTF per run.
- No resource tuning, profiles, or retries: Nextflow's defaults are fine
  for a yeast GTF.
- Do not modify anything in `modules/` or `src/`.
- Do not modify any file outside `target_files`.

## Acceptance Criteria
- The workflow has been verified by running it outside this repo, and the
  log entry says so.
- `nextflow run main.nf` produces `results/genes.tsv`, and it passes a
  manual spot check:
  - a known gene is present with the right name, e.g. `YFL039C` → `ACT1`;
  - the row count is plausible for yeast (roughly 6,000–7,500 genes).
- Break case: `nextflow run main.nf --gtf_url <a URL that doesn't exist>`
  stops with an error. It must not exit 0 or produce an empty table.

## Definition of Done
- The log entry records how the workflow was verified and the result.
- No files outside `target_files` were modified.
- No TODOs, commented-out code, or unused parameters.

## Fix
*(left blank at brief time — filled in only for post-commit discoveries)*
