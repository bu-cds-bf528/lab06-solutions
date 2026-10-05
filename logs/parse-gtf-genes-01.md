## 2026-10-05 — parse-gtf-genes-01

- **Brief id:** parse-gtf-genes-01
- **Files changed:** `bin/parse_gtf.py` (created, executable). Takes `-i/--input` (gzipped GTF) and `-o/--output` (CSV), both required, via argparse. Writes a header row `gene_id,gene_name`, then one row per non-comment GTF line. Standard library only.
- **Verification method:** ran it outside this repo (system Python 3) on real and toy data.
- **Test result:**
  - `--help` prints usage; running with no arguments exits 2 with a message naming both missing arguments.
  - Ensembl 112 yeast GTF (`.gtf.gz`) → exit 0; 41,879 rows for 41,879 non-comment lines; `YFL039C,ACT1` appears 8 times (duplicates kept, as the brief says). The output is byte-for-byte identical to the `GTF_GENES` module's output for the same file.
  - Toy gzipped GTF with a comment line, a line with no `gene_name`, and attributes in reversed order → comment skipped; `G2,` (empty gene_name); `G3,BETA` read correctly despite the order.
  - Plain (not gzipped) GTF → fails with `gzip.BadGzipFile`, exit 1. The brief says the input is gzipped, so plain input isn't supported.
- **Not implemented:** `label 'process_single'`. It's a Nextflow process directive and has no meaning in a Python script. It belongs in the brief of the Nextflow process that calls this script.
- **Choices the brief didn't state (my judgment):** a header row in the CSV; a line missing `gene_id` or `gene_name` gets an empty value rather than being skipped; option names `-i/--input` and `-o/--output`.
- **Execution vs. interpretation trust:** The runs above verified argument handling, real-data output (row count, a known gene) and the toy edge cases. That the attribute parsing works for GTFs from other sources (GENCODE, RefSeq) is my judgment, not tested.
