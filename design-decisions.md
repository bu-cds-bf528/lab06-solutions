# Design Checklist: General Coding Concepts

| # | Category | The core question |
|---|----------|-------------------|
| 1 | Input/Output Contract | What goes in, what comes out, and in what shape or type? |
| 2 | Boundary & Edge Behavior | What happens at the limits: empty input, minimal input, a remainder that doesn't fit evenly? |
| 3 | Domain Semantics | What does "correct" mean in this field, independent of the code? (Inclusive vs. exclusive, 0- vs. 1-based, how ties are resolved) |
| 4 | Parameterization | What are values that should be adjustable by the user, and what are fixed assumptions? |
| 5 | Scale & Resource Behavior | Does this behave the same on 10 items and 10 million? (Eager vs. lazy, memory footprint) |
| 6 | Failure Handling | What happens on invalid or unexpected input: raise, warn, skip, or silently coerce? |
| 7 | Composability | How does this piece's output become the next piece's input? |
| 8 | Usability / Reusability | Could someone else, or future you, use this without reading the source? |

# Design Checklist: Nextflow Process

For each category: what Nextflow handles automatically, and what still
requires a decision from you.

| # | Category | Nextflow mechanism | Automatic | Still requires a decision |
|---|----------|--------------------|-----------|----------------------------|
| 1 | I/O Contract | `input:` / `output:` blocks; `val`, `path`, `tuple` | Type mismatches often fail loudly at parse or run time | Strict filename vs. glob (`*.bam` can over- or under-match); does the output tuple structure match what the next process declares as input? |
| 2 | Boundary & Edge Behavior | Channel closing, dataflow semantics | An empty channel means downstream processes don't fire, with no crash | Is "zero items reached this process" a valid state or a silent data-loss bug? If it's a bug, it needs explicit handling (`ifEmpty()`, `branch{}`) |
| 3 | Domain Semantics | None | Nothing; Nextflow has no opinion on biology | Fully manual: what the wrapped tool's flags mean, whether thresholds suit this data |
| 4 | Parameterization | `params`, `nextflow.config`, CLI overrides, profiles | The override plumbing itself is free once wired up | What is a `params.x` vs. hardcoded in the script block? Where do defaults live: config, profile, or CLI? |
| 5 | Scale & Resources | `cpus`, `memory`, `time` directives; executor; `-resume` | Parallelization across channel elements and cache-based resume | Right-sizing resources per process; does it need different resourcing at 5 samples vs. 500? |
| 6 | Failure Handling | Non-zero exit fails the process; `errorStrategy` (`terminate`, `retry`, `ignore`, `finish`) | A non-zero exit halts the pipeline by default | **The trap:** exit 0 with empty, truncated, or wrong output still counts as success. "Did it succeed" is not "was the output correct," so you need an explicit verify step. Is `retry` even appropriate, or does it just rerun a deterministic bug? |
| 7 | Composability | Channel operators: `join`, `combine`, `groupTuple`, `cross` | Dataflow scheduling and parallelism once shapes match | Do producer and consumer channel shapes match (join keys, cardinality)? A mismatch usually doesn't error; it silently mispairs or drops items |
| 8 | Usability / Reusability | Modules (`include`), `meta.yml` (nf-core convention), profiles | None of this is enforced | Is the process a standalone, importable module or hardcoded to one pipeline? Does it depend on portable `params`/profiles or on hardcoded paths? Does `publishDir` organize output for a human to find later, separate from the channel shape the next process needs? |

