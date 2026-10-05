## 2026-10-05 — nextflow-gtf-download-01

- **Brief id:** nextflow-gtf-download-01
- **Files changed:** `modules/gtf_download.nf` (created). Process `GTF_DOWNLOAD`: input `val url`; output `path` named after the last part of the URL (e.g. `Saccharomyces_cerevisiae.R64-1-1.112.gtf.gz`); `label 'process_single'`; no container or conda environment; a `stub:` block that writes a one-line fake GTF (gzipped if the filename ends in `.gz`).
- **Verification method:** ran it outside this repo, with Nextflow 26.04.6, through a small test workflow in a scratch directory.
- **Test result:**
  - Stub run (`-stub-run`), `.gz` URL → exit 0; output is a gzipped one-line GTF with 9 tab-separated columns. Plain `.gtf` URL → exit 0; same line, not gzipped.
  - Real run, Ensembl 112 yeast GTF → exit 0; 595,453 bytes, passes `gzip -t`, 9 columns, 7,127 gene lines, `YFL039C` → `ACT1`.
  - URL that 404s → process fails (exit 1, `curl: (22) ... 404`).
  - **Break case:** `https://example.com/` (returns 200 with an HTML page) → **exit 0**; the HTML page is saved as the output file `example.com`. This is **silently allowed**: the Requirements don't say whether a non-GTF download should be an error, so no check was added. To make it an error, add a Requirement (e.g. "fails if the downloaded file isn't a gzipped GTF").
- **Choices the brief didn't state (my judgment):** download with `curl` (`-f` so HTTP errors like 404 fail the process, `-L` to follow redirects); output filename taken from the URL.
- **Execution vs. interpretation trust:** The runs above verified stub output, a real download, the 404 failure and the break case. That `curl` is available wherever this runs (the brief says no environment is needed), and that naming the file after the URL suits `GTF_GENES`, are my judgment, not tested.

## 2026-10-05 — nextflow-gtf-download-01 (rewritten brief: typed module with wget)

- **Brief id:** nextflow-gtf-download-01
- **Files changed:** `modules/download/main.nf` (created). Process `GTF_DOWNLOAD`, written as a typed process (`nextflow.enable.types = true`): input `url: String`; output `file(...)` named after the last part of the URL; `label 'process_single'`; `conda 'conda-forge::wget=1.25.0'`; script runs `wget -O <filename> '<url>'`. No stub block: this version of the brief doesn't ask for one. The earlier `modules/gtf_download.nf` (curl, untyped) from this brief's previous version is no longer in the repo.
- **Verification method:** ran it outside this repo, with Nextflow 26.04.6, through a test pipeline in a scratch directory.
- **Test result:**
  - Real run, Ensembl 112 yeast GTF, with `-with-conda` → exit 0; the conda environment was created (GNU Wget 1.25.0); 595,453 bytes, passes `gzip -t`. Nextflow prints its "static typing is a preview feature" warning.
  - URL that 404s → process fails (wget exit status 8, run exit 1).
  - Chained into `GTF_PARSE` (`modules/gtf_parse/main.nf`) with `-with-conda` → exit 0; 41,879 rows, `YFL039C,ACT1` 8 times.
- **Choices the brief didn't state (my judgment):** process name `GTF_DOWNLOAD`, matching the workflow briefs; output filename taken from the URL; wget pinned to 1.25.0, the version conda resolved on the first run, so the environment can't change later.
- **Not covered:** a URL that returns 200 with something that isn't a GTF (e.g. an HTML page) would still exit 0 and be saved as the output. The brief doesn't say whether that should be an error, so there's no check.
- **Execution vs. interpretation trust:** The runs above verified the typed syntax, the conda environment, a real download, the 404 failure and the connection to `GTF_PARSE`. That the typed syntax keeps working on other Nextflow versions (it's a preview feature) is my judgment, not tested.
