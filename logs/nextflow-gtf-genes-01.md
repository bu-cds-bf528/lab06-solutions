## 2026-10-05 — nextflow-gtf-genes-01

- **Brief id:** nextflow-gtf-genes-01
- **Files changed:** `modules/gtf_genes.nf` (created). Process `GTF_GENES`: input `path gtf`; output `path "gene_names.csv"` (columns `gene_id`, `gene_name`, with a header row); `label 'process_single'`; `conda 'conda-forge::python=3.12'`; the parsing script is Python, embedded in the process; a `stub:` block that creates an empty `gene_names.csv`.
- **Verification method:** ran it outside this repo, with Nextflow 26.04.6, through small test workflows in a scratch directory.
- **Test result:**
  - Stub run, chained after `GTF_DOWNLOAD` → exit 0; `gene_names.csv` is 0 bytes.
  - Real run, chained after `GTF_DOWNLOAD` on the Ensembl 112 yeast GTF, with `-with-conda` → exit 0. The conda environment was created and activated (Python 3.12.14). The output has 41,879 data rows, equal to the GTF's 41,879 non-comment lines; `YFL039C,ACT1` appears 8 times (once per gene/transcript/exon/... line); 0 rows have an empty gene_name.
  - Real run on a plain (uncompressed) 200-line GTF → exit 0; 195 rows for 195 non-comment lines.
- **Choices the brief didn't state (my judgment):**
  - **`src/gtf_genes.py` doesn't exist yet**, so the parser is written inside the process instead of calling that script. The brief's own parsing rules ("parse every line, don't handle duplicates") are what it implements.
  - One CSV row per non-comment GTF line. A line with no `gene_id` or `gene_name` gets an empty value in that column.
  - Gzipped (`.gz`) input is read directly, so this module accepts `GTF_DOWNLOAD`'s output; plain `.gtf` works too.
  - The stub's CSV is fully empty (no header row), as the brief says.
- **Execution vs. interpretation trust:** The runs above verified stub output, the chained run on real data (row count, a known gene), plain-GTF input and conda activation. That the attribute parsing handles GTFs from other sources (GENCODE, RefSeq) is my judgment, not tested.

## 2026-10-05 — nextflow-gtf-genes-01 (rewritten brief: typed module calling bin/)

- **Brief id:** nextflow-gtf-genes-01
- **Files changed:** `modules/gtf_parse/main.nf` (created). Process `GTF_PARSE`, written as a typed process (`nextflow.enable.types = true`): input `gtf: Path`; output `file('gene_names.csv')`; `label 'process_single'`; `conda 'conda-forge::python=3.12'`; script runs `parse_gtf.py -i ${gtf} -o gene_names.csv` (from `bin/`); stub runs `touch gene_names.csv`. The earlier `modules/gtf_genes.nf` from this brief's previous version is no longer in the repo.
- **Verification method:** ran it outside this repo, with Nextflow 26.04.6, through a test pipeline in a scratch directory with `bin/` linked in (Nextflow puts a pipeline's `bin/` on the PATH).
- **Test result:**
  - Stub run → exit 0; `gene_names.csv`, 0 bytes.
  - Real run on the Ensembl 112 yeast GTF with `-with-conda` → exit 0; conda environment activated; the process ran `parse_gtf.py -i Saccharomyces_cerevisiae.R64-1-1.112.gtf.gz -o gene_names.csv`; 41,879 rows, byte-for-byte identical to the earlier output for the same file.
  - The calling script doesn't need the typing flag itself: an untyped workflow including this module also ran (exit 0).
- **Choices the brief didn't state (my judgment):** process name `GTF_PARSE`, from the folder name; output name `gene_names.csv`; Python 3.12 from conda-forge.
- **Execution vs. interpretation trust:** The runs above verified the typed syntax on Nextflow 26.04.6, the stub, and the real output. Static typing is a Nextflow preview feature (Nextflow prints a warning), so whether this syntax keeps working on other Nextflow versions is my judgment, not tested.
