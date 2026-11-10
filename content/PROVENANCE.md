# Provenance of the learner pages

This file says how the pages in `content/` were made, so that readers and anyone who reuses them know what they
are. It is not part of any volume.

## What is here

`content/front/` holds the text of Volume 0 (preface, how to use the handbook, notation, the introduction to the
volumes, the learning paths). Each `content/<area>/` holds the learner pages of one volume: the volume
introduction, and for each chapter an outline (the groups and order of its entries), an opening, a summary,
exercises, hints and notes. None of these pages is on the site; the entries themselves are the text of the site
and are not stored here.

## How the pages were written

All pages in this directory were drafted by AI agents (Anthropic's Claude), in November 2026:

1. A brief, [`prompts/area.md`](../prompts/area.md), fixes the files, their sizes, the voice, the exercise
   bands, the rules for hints and notes, and the checks.
2. A sample chapter (`content/sorting/comparison-sorts/` and `content/sorting/volume.md`) was written first and
   used as the model for all other chapters.
3. For each volume, one agent wrote the volume introduction and the first chapter, and helper agents wrote the
   other chapters from the same brief and sample. Each writer read the entries of its chapter (the summary and
   section headings of all of them, the full text of the key entries and of any entry whose fact it states).
4. Each writer worked the exercises it set; numerical answers were checked with short scripts.
5. `python -m hb check` verifies every link, the outline of every chapter, the numbering and bands of exercises,
   the hints, and a list of banned words. The coordinator of each volume spot-checked its helpers' pages.

For edition 0.13.0, the eight chapters that the site's release v0.13.0 filled (13.4, 13.6, 13.7, 13.9 and
14.3 to 14.6) were written the same way, one agent per chapter, and the introductions of Volumes 13 and 14 were
rewritten by the coordinating agent.

For edition 0.16.0, the four volumes that the site's release v0.16.0 opened (15 *Optimization*, 16 *Logic and
constraints*, 17 *Randomized* and 18 *Approximation*) were written the same way. Six agents shared them: two for
Volume 15, two for Volume 16, one for Volume 17 and one for Volume 18, each with helper agents for single
chapters. In Volume 18 only Chapter 18.1 has entries so far; the other five chapters have an opening only, written
from the site's short pages. Two learning paths through the new volumes were added to Volume 0.

## What was not done

- No person has yet read every page. Spot checks found the pages accurate, but errors remain likely, most of all
  in **notes and further reading**: dates, editions and section numbers there are sometimes from the model's
  memory rather than from the entries. The writers listed such facts in their reports; they are to be checked
  against the sources before edition 1.0.
- The pages do not copy text from textbooks or papers. They name books and papers as further reading.

## Errors in the entries

While writing, the agents noted claims in the entries that look wrong or inconsistent. The pages avoid those
claims. The list is kept with the project's notes, to be reported to `tamnd/algorithm`.
