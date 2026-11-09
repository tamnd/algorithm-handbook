# Brief: write the learner layer of one volume (or part of one)

You are writing pages of **The Handbook of Algorithms**, a book built from the entries of the site
<https://algorithm.tamnd.com> (the content repo is `~/github/tamnd/algorithm`). The builder turns each top area
of the site into a volume and each sub-area into a chapter; the entries (nodes) are already written. Your job
is the *learner layer*: the pages that turn a pile of entries into a textbook a person can learn from alone.

Read this whole brief before you write anything. Then read the gold sample (below) closely.

## Where things are

- The handbook repo: `~/github/tamnd/algorithm-handbook`. Work only in `content/<area-id>/` for the area you
  are given. Do not edit anything else: not `hb/`, not `tex/`, not other areas, not `prompts/`.
- The content repo `~/github/tamnd/algorithm` is **read-only**. Never edit, commit or run git commands that
  change it. Do not touch `~/github/tamnd/algorithm-write`, `algorithm-work` or `algorithm-pr`; another session
  is working there.
- An entry lives at `~/github/tamnd/algorithm/nodes/<area>/<sub-area>/<slug>/node.md` (front matter plus body);
  proofs are in `proofs/*.md` next to it. Use `find ~/github/tamnd/algorithm/nodes -path "*/<slug>/node.md"` to
  locate one by slug.
- Do not run `git` in the handbook repo either. Do not commit. Do not build PDFs.

## Tools

Run these from `~/github/tamnd/algorithm-handbook` (each takes about 15 seconds to load the corpus):

    python3 -m hb brief --volume N                  # every chapter: entries, summaries, costs, prerequisites
    python3 -m hb brief --volume N --chapter K      # one chapter
    python3 -m hb brief --volume N --chapter K --sections   # also the section headings of each entry
    python3 -m hb check --volume N                  # outline warnings and link/exercise problems; must be clean

The brief prints each entry as `4.1.12 Merge sort` with its slug. The numbers in the brief are the numbers
*before* your outline; your outline will renumber the chapter, so never write a number by hand. Write links
only, as `[merge sort](/merge-sort/)`, and the builder adds the number.

## The files, per chapter

For a volume with area id `A` and a chapter (sub-area) with id `S`, write in `content/A/S/`:

| File | What it is | Size |
|---|---|---|
| `outline.yaml` | The order of the chapter: groups with a title, a short intro and the entry slugs | every written entry, once |
| `opening.md` | The chapter's opening pages | 450–900 words |
| `summary.md` | What to remember, a comparison table where one makes sense, guidance for choosing | 300–800 words |
| `exercises.md` | Numbered exercises in three bands | 15–30 exercises |
| `hints.md` | Hints and short answers for about half the exercises | as needed |
| `notes.md` | History and further reading | 300–700 words |

And once per volume, `content/A/volume.md`: the volume introduction, 900–1500 words. Write it only if your
assignment says you own the volume introduction.

A chapter with **no written entries** (only stubs) gets only `opening.md` (250–450 words: what the topic is,
why it matters, what the planned entries will cover, what to read meanwhile) and no other file.

## Gold sample: read it first

`content/sorting/volume.md` and the six files in `content/sorting/comparison-sorts/` are the model. Match their
voice, their structure, their density and their care with facts. Read all of them before writing.

## The outline (`outline.yaml`)

```yaml
groups:
  - title: Merge sort            # a short title in sentence case
    intro: >                     # 2–4 sentences: what the group is about and how its entries relate
      Merging two sorted lists is easy and fast. Merge sort turns that into a sort ...
    entries:                     # slugs, in reading order
      - merging-sorted-lists
      - merge-sort
```

- List **every written entry of the chapter exactly once** (the brief lists them; stubs are not listed by it
  and must not be listed). `hb check` warns about missing, doubled or unknown slugs; fix every warning.
- Make 3 to 10 groups. Order the groups and the entries so a reader meets each idea before it is used: the
  problem before its algorithms, the simple method before its refinements, the definitions before the
  theorems that use them. `hb check` warns when an entry comes before a prerequisite *in the same chapter*;
  fix those warnings unless the order is clearly better for the reader (then leave at most a few).
- Within a group, put intro and core entries before advanced and research ones, unless the topic flows
  otherwise.
- Group intros may contain links and `$math$`.

## The opening (`opening.md`)

The reader has just turned to the chapter. Tell them, in this order:

1. What the chapter is about, concretely, with one or two examples of where it matters. No throat-clearing.
2. `## What the chapter covers`: the groups in order, as a numbered list, one or two sentences each, with
   links to the key entries.
3. `## A first reading`: the 6–15 entries to read first, in order, as links. Say what can be skipped at first.
4. `## Before you start`: the prerequisites from other volumes, as links, and anything else assumed.

## The summary (`summary.md`)

- `## What to remember`: 5–9 bullets, each a fact or idea stated precisely, with the key bounds in math.
- A table comparing the main methods of the chapter (costs, properties) when the chapter has such methods. Give
  it a caption line `: …` after the table. Every number in it must match the entries; check them.
- A short section of practical guidance (`## Choosing a method`, or what fits the chapter), when it makes
  sense.

## The exercises (`exercises.md`)

- A plain numbered list `1.`, `2.`, … with one blank line between exercises. The builder renumbers them as
  `4.1.7` and links hints to them.
- Each exercise starts with its band mark: `◦` (check: a few minutes, tests close reading, often a small hand
  computation on a concrete input), `•` (practice: use an idea in a new place, prove a small claim, write a
  short program) or `★` (challenge: a real proof, a known result from the literature, a design problem). Aim
  for about 35% ◦, 45% •, 20% ★, ordered by band.
- Concrete inputs, exact questions. Every exercise must have a definite answer you know. Work each one out
  yourself before you write it. Do not pose open problems as exercises.
- Do not copy exercises from textbooks. Classic facts (such as "merging needs $2n-1$ comparisons in the worst
  case") are fine to ask about in your own words.
- Do not repeat an exercise that already sits at the end of an entry (many entries have their own short
  `## Exercises` section: look before you write).
- Link to entries where it helps: `Run [insertion sort](/insertion-sort/) on …`.

## The hints (`hints.md`)

- A numbered list whose numbers are the numbers of the exercises they belong to (not 1, 2, 3 … in order; skip
  exercises with no hint). Give hints to about half the exercises, including most ★ ones.
- For ◦ exercises, give the answer. For • and ★, give the key idea in one to four sentences, and the answer
  when it is short.

## The notes (`notes.md`)

- `## History`: who found the main ideas, when, and how the topic grew. Three to five paragraphs of plain
  narrative. Use the `history` fields and the `sources` of the entries as your base; every name, year and
  title must be one you are sure of. If you are not sure of a year, leave the year out. Never invent a paper.
- `## Further reading`: 3–6 items, books and survey papers, each with one sentence on what it is good for.
  Prefer works cited in the entries' sources. Use full, correct titles.

## The volume introduction (`volume.md`), when assigned

Follow `content/sorting/volume.md`: what the area is and where it shows up; `## Why … gets a volume of its
own` or a section on the big ideas the volume teaches; `## The chapters`, one paragraph per chapter with key
links; `## How to read this volume` with a first-course path through 10–20 key entries; `## What you need
first` with prerequisites from other volumes; `## The exercises` (copy the band explanation from the sample).

## The writing standard

- **Plain words and short sentences**, like the entries of the site. Explain; do not decorate. Write "uses",
  not "leverages"; "shows", not "showcases". No marketing words (powerful, elegant, seamless, crucial,
  robust, delve, landscape, journey). No rhetorical questions as section openers. No exclamation marks.
- Active voice, present tense. Address the reader as "you" sparingly, in guidance.
- Every claim must agree with the entries. When the opening says an algorithm runs in $O(n \log n)$ time,
  check its entry. Read the key entries of each group in full (body and front matter); for the rest, the brief
  and the section headings are usually enough, but open the entry whenever you state a specific fact from it.
- Mathematics in `$…$` or `$$…$$` (KaTeX syntax, as on the site). Names of algorithms in plain text, not code.
- Links: only `[text](/slug/)` with a slug that exists (`hb check` verifies). Link an entry the first time
  a page mentions it; do not link every mention. Do not link to external sites in the body text (notes may
  name papers and books without URLs).
- British or American spelling: follow the sample (it uses "licence" but "-ize"; be consistent within a file).
- Do not write "In this chapter, we will…". Do not end with a summary of what you just said.
- Do not mention AI, agents or how the text was made.

## Finish

1. Run `python3 -m hb check --volume N` and fix every problem it reports for your chapters (problems in other
   areas are not yours).
2. Re-read each file once against this brief.
3. Report back: the files written (with word counts, `wc -w`), the number of exercises per chapter, any entry
   you think is misplaced in the site's areas, and any factual doubt you could not settle.
