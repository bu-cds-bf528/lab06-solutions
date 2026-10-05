# Lab 06 - Agentic Coding

Today we're going to talk about how we can use LLM-based agentic coding 
harnesses to generate code. LLMs are unsurprisingly very good at generating
code based on a text input just due to the copious amounts of training material
on these topics. 

Just a note that this framework is specific to our class, and you may encounter
slightly different conventions if you go into a software engineering heavy role.
However, the high-level topics we're talking about as it relates to code (reusability,
types, input and output validation) are universally important for code that 
behaves as expected and code that works together coherently in a large code base.

This framework is intentionally more deliberate than say just prompting a LLM
in a conversation for a snippet of code. This framework is meant to force some
upfront decisions and validations to ensure that you can keep pace and ensure
correct function for the incredible volume of code that LLMs can theoretically
generate. 

The important concept to remember is that an agent telling you code works, and
tests passing, only tells you the code *ran* but it doesn't tell you if the code
did what *you* wanted. 

**Unit testing.** A unit test runs one function (one "unit") on an input
where you already know the right answer, and checks that the function
returns it. We'll mostly use toy data: inputs small enough that the answer
can be seen by eye, like the GC content of `"GCAT"` being 0.5. This works
because the function's logic doesn't depend on how big its input is. If it
behaves correctly on a tiny input of the same type and structure as the
real data (e.g. a short DNA string), the same code will behave the same way on
a whole chromosome. So a handful of toy inputs, each picked to check one
behavior (a normal case, an edge case like an empty string, an error
case), tests the function properly no matter what data it later runs on.
The one thing toy data can't check is behavior that only shows up at
scale, like running out of memory.

This also isn't a claim that you should write a formal spec for every line of
code you ever generate. For a one-off script, or a task simple enough that an
LLM will land on an obviously correct answer, a normal prompt conversation is
probably fine. Where this matters is when the code has to interface with other
code in a pipeline, a shared codebase, or a project that grows beyond a simple 
script or basic set of functions. 

As a codebase or project grows in scope, neither you nor the agent will likely
be able to consider all of it simultaneously and this is when understanding how
the code should work together based on your own documentation will be valuable.
And regardless of if the code works, you still need to ensure that the result is
"right" and the code is behaving as you intend. 

## When to use this (and when not to)

This workflow is deliberately heavier than a normal prompt, so it isn't the
right default for every task. Roughly:

- **One-off, throwaway work** — a quick script to reformat a file once, a
  one-time data pull, or some light file manipulation or parsing. If you're
  confident none of these have a meaningful effect on the actual data itself,
  a simple prompt might be enough. 
- **Simple, well-bounded tasks** where there's basically one obvious correct
  behavior (parsing a standard file format, computing a well-known
  statistic) — an LLM will usually land on an acceptable implementation on
  the first try without a formal spec, because the ambiguity space is
  small and the code for doing these operations is already built officially
  into already validated function calls. 

- **Where this framework becomes valuable:**
  - *Transparency* — the brief/log pair is what makes a piece of code
    checkable later by future-you, or a collaborator without having to 
    reverse-engineer what the agent assumed. That matters most whenever someone
    other than the author needs to trust the result.
  - *Code that interfaces with other code* — once something has to compose
    with a pipeline, a shared library, another person's code, or a
    long-lived codebase, an unstated assumption that you make on your own or an
    agent on your behalf stops being a local problem and starts compounding into
    other people's bugs. This is the practical reason Categories 7 (composability)
    and 8 (reusability) matter so much more here than they would in a disposable
    one time use script.

In short, you may not need to **always** write a brief, but this lab will introduce
you to the kinds of higher-level concepts you should be thinking of when asking
LLMs to generate code that works in a larger project. 

## Steps for today

The lab has four parts meant to be done in order. 

**Running a naive prompt:** whenever a step asks for one, run it **outside
this repo**, e.g. in a separate chat window. If you run it in Claude Code
inside this repo, the agent reads `CLAUDE.md` and can see your brief and
tests, so the result wouldn't really be naive. Open a browser-based chat
session with an LLM of your choice. 

### Part 1: GC content

Make a conda environment with the YML provided in `envs/`.

```bash
conda env create -f envs/pytest_env.yml
```

Make sure to activate it:

```bash
conda activate pytest_env
```

1. Read `tests/test_gc_content.py` and run it.

       pytest tests/test_gc_content.py -v

   Notice that each test checks one decision, using tiny toy sequences
   (`"GCAT"`, `"GCNNNN"`, `""`) chosen so the right answer is obvious by
   eye.
2. In `briefs/_EXERCISE-gc-content.md`, write one Requirement per decision
   the tests check. Then fill in Out of Scope: what should the function
   NOT do?
3. Open `briefs/_EXAMPLE-gc-content.md` and we'll compare as a class:
   - Which Requirements did you miss? Could you have found them in the
     tests?
4. Read `src/gc_content.py`. Above each line that handles a Requirement,
   add a comment saying which one, e.g.
   `# Requirement: counting is case-insensitive`. Do the same for Out of
   Scope items you can point to. Is there any Requirement you can't find
   a line for?
5. Read the first entry in `logs/gc-content-01.md`. This repo is setup to
   automatically record when a brief is used to generate code. You can consider
   employing similar strategies in the future for your own work. 

### Part 2: Sliding window (in groups)

Work in a group with a few people around you. YWhen asked to generate code with
a naive prompt, feel free to have different members use a different LLM (claude, chatGpt, etc.)

1. Read `briefs/sliding-window-01.md`. It has open questions instead of
   Requirements.
2. Open `tests/test_sliding_window.py` and work through it with the brief's
   questions. Each test is numbered to match a question. Start with
   decision 7 (what a window looks like), because it sets the shape of
   every other answer.
   - Replace each `___` with your group's answer.
   - Where two tests say "KEEP ONE", delete the one you disagree with.
3. Write each decision as a Requirement in the brief, under its question.
   Fill in Context and Out of Scope, then delete the question comments. A
   finished brief has no open questions.
4. **Spec version:** in this repo, start Claude Code and ask it to
   implement `briefs/sliding-window-01.md`. It writes
   `src/sliding_window.py`, runs your tests, and adds an entry to
   `logs/sliding-window-01.md`.
5. **Naive version:** outside this repo, ask: *"Write a Python function
   `sliding_window(seq, size, step=1)` that returns sliding windows over a
   sequence."* Save the code it gives you as `src/sliding_window_naive.py`.
6. Copy all your filled-in tests from `tests/test_sliding_window.py` into
   the bottom of `tests/test_sliding_window_naive.py`, then run both:

       pytest tests/test_sliding_window.py -v
       pytest tests/test_sliding_window_naive.py -v

7. Compare, as a group:
   - Which tests did the naive version fail? For each one: was its choice
     wrong, or just different from yours?
   - Without your tests, how would you have found out what it decided?
   - What does the spec version's log list as interpretation trust?

   **The point is not that the naive version does worse.** It may pass
   everything. The point is whether you can *tell*: with a spec and tests
   you know what the code was supposed to decide, and can check it.
   Another group's naive version may pass their tests and fail yours.

### Part 3: GTF parsing

Similar to above, this time try to use claude to develop a script that will
extract some information from the GTF file. 

1. **Naive version:** outside this repo, ask: *"Write a Python function
   that parses a GTF file and returns each gene's gene_id and
   gene_name."* Save the result as `src/gtf_genes_naive.py`.

2. **Spec version:** Use the `briefs/nextflow-gtf-genes-01.md` and fill in
   at least the following:
   - what to do with a record that has no `gene_name`;
   - how to handle comment lines, attribute quoting, and attributes in a
     different order;
   - what to do with a gene that appears many times;
   - what the function returns (a dict? a list of pairs? a file?)
   - How to accept inputs and how to write its outputs (e.g. argparse)
   - What libraries should it use? Standard only? Specialized libraries?

If you are unsure about any of the above, leave it blank and see what happens in
the resulting ode.

3. In this repo, ask Claude Code to implement `briefs/gtf-genes-01.md`.
4. Run both versions on the same small GTF file provided for you and compare: 
   for each decision in your brief, what did the naive version silently decide 
   instead? There are many more possible choices here than in GC content or 
   sliding window, so expect more differences.

### Part 4: Nextflow 

For this next part, I'll ask you to use briefs to have an agentic coding harness
(claude) develop two modules in nextflow for you. The templates
I've given you are not perfectly designed for every situation so feel free to 
change them. The point of this next part is that for this lab and for when you use
LLMs to generate nextflow, I'd like you to do so based on a brief where you specify
how you want the module to behave. This brief can be included in the repository
just like any of your other code. 

**What to put in a Nextflow brief.** The 8 categories in
`design-decisions.md` all carry over to Nextflow in some way. The most important
ones to remember are below:

1. **Inputs and outputs:** what the `input:` and `output:` blocks
   declare (a value, a file path, or a record with named fields), the
   exact output filename or pattern, and whether files are gzipped. This is why
   we spent so much time talking about records that define exactly what information
   flows in and out of processes.
2. **Parameters:** which values come from `params` (set in
   `nextflow.config` or on the command line) and which are fixed in the
   script. Should the tool use the default settings?
3. **Resources:** which `label` the process gets (e.g. `process_low`,
   `process_high`), with the cpus, memory and time for each label defined
   once in `nextflow.config`.
4. **Where it runs:** the `container` (or conda environment) the process
   runs in. 
5. **Composability** does the module include a `stub` command that will let you
   troubleshoot the workflow first before running it for real?
6. **Name of the process** 

Translate these to one-line statements that you can put in the requirements
for the first brief. 

**How we check Nextflow code.** We won't write automated tests for the
Nextflow parts. Instead, checking is two steps:

- **Did it finish?** Rely on Nextflow and the exit code. A run that exits
  0, with Nextflow reporting every process as completed, finished. A
  non-zero exit code means something failed: Nextflow's error message
  names the process that failed.
- **Is the output sensible?** Review the outputs by hand: open them,
  check a few values you know, and check the counts are plausible (see
  step 5 for ideas).

Exit code 0 only means no step *reported* an error. It doesn't mean the
output is right. We will rely on the fact that nextflow *itself* isn't doing
any of these operations: nextflow simply calls already validated tools. We will
not directly "unit" test the outputs, but instead choose to manually validate
the outputs (e.g. quality control evaluation, or spot-checking outputs, etc.)

Build two Nextflow modules, each from its own brief: one that downloads a
GTF, and one that wraps your verified GTF parser from Part 3. Start only
after Part 3's spec version works, so any problem here is about Nextflow,
not the parser.

1. Fill in both briefs side by side:
   - `briefs/nextflow-gtf-download-01.md` (process `GTF_DOWNLOAD`)
   - `briefs/nextflow-gtf-genes-01.md` (process `GTF_PARSE`)

   Check the two agree: what `GTF_DOWNLOAD` outputs (gzipped or not, the
   filename) must be exactly what `GTF_GENES` expects as input.
2. In this repo, ask Claude Code to implement the download brief. It
   writes `modules/gtf_download.nf`. 
3. Ask Claude Code to implement the parser brief. It writes
   `modules/gtf_genes.nf`. 
4. What would a brief for `main.nf`, the workflow connecting the
   two modules, need to say? Think about what passes between processes,
   what happens when one step fails, and where outputs end up.
5. This time, write your own `main.nf` that connects the two processes you had
   claude develop based on your input.
6. **Discussion**: how would you know the downloaded GTF, and the gene table you
   made from it, are actually right? Some options, from least to most
   effort:
   - Look at the first few lines: tab-separated, 9 columns, attributes in
     the last one.
   - Spot-check a few genes you know, e.g. does TP53 have gene_id
     ENSG00000141510? Compare a handful against the Ensembl website.
   - Check the count is plausible: a human GTF has roughly 60,000 genes,
     about 20,000 of them protein-coding.
   - Compare against the checksum file the source publishes next to the
     GTF (e.g. `CHECKSUMS` on Ensembl, `MD5SUMS` on GENCODE), which
     catches a corrupted or cut-short download.
   - Write automated tests.

## Using this for your own projects

For any project you build with an agent, use the same approach as today:

1. **Write one brief per module, plus one for the workflow.** Copy
   `briefs/_TEMPLATE.md` for each. Each module (a function, a script, a
   Nextflow process) gets its own brief. The workflow that connects them
   (e.g. `main.nf`) gets one more. Its `target_files` should not include
   the modules: the workflow brief only connects pieces that are already
   verified.
2. **Work through the 8 categories in `design-decisions.md` for every
   brief**, and write each answer as a Requirement. A finished brief has
   no open questions.
3. **Review each brief yourself before handing it to an agent**, whether
   you wrote it or the agent drafted it. Check:
   - every decision is stated, not left for the agent to guess;
   - one module's outputs match exactly what the next module expects as
     inputs;
   - Out of Scope says what the agent should *not* add.
4. **Decide how to validate each brief's output.** Match the effort to
   the risk:
   - **Automated tests with toy data:** for logic that will be reused,
     changed later, or has tricky edge cases (like the sliding window).
   - **A manual spot check:** for one-off steps with an obvious right
     answer, like downloading a file from a trusted source. Look at the
     output, check a few known values, check counts are plausible.
   - **A checksum or published reference:** for downloaded data.
   - **Review by hand:** for code that's hard to run in isolation, like a
     Nextflow process.
   - **Rely on previous validation:** Many well-used tools have sensible defaults
     that work well for the majority of cases. 
5. **Try to run it.** If it fails, determine what failed and if it was an issue 
   with something you specified. Decide whether it's easier or faster to fix it
   by hand or to re-try your prompt with more specificity. 