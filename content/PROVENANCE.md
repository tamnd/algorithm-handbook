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

For edition 0.18.0, the site's release v0.18.0 wrote the entries of Chapters 18.2 to 18.6 and opened Volume 19
*Online and streaming*. Two agents shared the work, one for Volume 18 and one for Volume 19, each with helper
agents for single chapters. The five new chapters of Volume 18 got their full pages, their openings were
rewritten, and the volume introduction now covers the whole volume; Volume 19 was written in full. Two learning
paths, *Approximation algorithms* and *Online and streaming algorithms*, were added to Volume 0.

For edition 0.19.0, the site's release v0.19.0 opened Volume 20 *Parallel*. One agent wrote its volume
introduction and first chapter and helper agents wrote the other four chapters, the same way; a learning path
*Parallel algorithms* was added to Volume 0.

For edition 0.20.0, the site's release v0.20.0 opened Volume 21 *Distributed*. Two agents shared it, one writing
the volume introduction and Chapters 21.1, 21.2, 21.3 and 21.6, the other Chapters 21.4, 21.5 and 21.7, each with
helper agents for single chapters; a learning path *Distributed algorithms* was added to Volume 0.

Edition 0.20.1 is built from the same release of the site as 0.20.0, with a new typesetting of the entries: their
definitions, theorems and algorithms are numbered, and each volume has a list of its theorems and definitions. The
section *Statements, algorithms and proofs* of Chapter 0.1 and the note on numbering in each volume introduction
were written for it the same way.

For edition 0.21.0, the site's release v0.21.0 opened Volume 22 *Concurrency*. Four agents shared it, one per
chapter, the first also writing the volume introduction; a learning path *Concurrent algorithms* was added to
Volume 0. The paragraphs that the section *Statements, algorithms and proofs* of Chapter 0.1 gained on the
numbered definitions and the boxes *In plain words* were written the same way.

For edition 0.22.0, the site's release v0.22.0 opened Volume 23 *Cryptography*. Seven agents shared it, one per
chapter, the writer of Chapter 23.7 also writing the volume introduction; the coordinating agent added a learning
path *Cryptography* to Volume 0. Edition 0.21.0 was built but not released, so its Volume 22 first appears in
0.22.0.

For edition 0.23.0, the site's release v0.23.0 wrote Volume 24 *Compression and coding*. Five agents shared it,
one per chapter, the writer of Chapter 24.1 also writing the volume introduction; the coordinating agent added a
learning path *Compression and coding* to Volume 0.

For edition 0.24.0, the site's release v0.24.0 wrote Volume 25 *Machine learning* and Chapter 26.1 *Caching
policies* of Volume 26 *Systems*. Eight agents shared them: one per chapter of Volume 25, the writer of Chapter
25.1 also writing the volume introduction; one for Chapter 26.1 and the introduction of Volume 26; and one for the
openings of Chapters 26.2 to 26.8, which have no entries yet. The coordinating agent added a learning path
*Machine learning* to Volume 0.

For edition 0.25.0, the site's release v0.25.0 wrote Chapters 26.2 to 26.8 of Volume 26 *Systems*. Seven agents
shared them, one per chapter, the writer of Chapter 26.8 also rewriting the volume introduction to cover the whole
volume; each chapter's opening, written from the site's short pages for 0.24.0, was replaced. The coordinating
agent added a learning path *Systems* to Volume 0.

For edition 0.26.0, the site's release v0.26.0 wrote Volume 27 *Biology* and Chapters 28.1 *Rasterization* and
28.3 *Visibility* of Volume 28 *Graphics and signals*. Seven agents shared them: one per chapter of Volume 27, the
writer of Chapter 27.1 also writing the volume introduction; one for Chapter 28.1 and the introduction of Volume
28; one for Chapter 28.3; and one for the openings of Chapters 28.2 and 28.4 to 28.6, which have no entries yet.
The coordinating agent added a learning path *Biology* to Volume 0.

## What was not done

- No person has yet read every page. Spot checks found the pages accurate, but errors remain likely, most of all
  in **notes and further reading**: dates, editions and section numbers there are sometimes from the model's
  memory rather than from the entries. The writers listed such facts in their reports; they are to be checked
  against the sources before edition 1.0.
- The pages do not copy text from textbooks or papers. They name books and papers as further reading.

## Errors in the entries

While writing, the agents noted claims in the entries that look wrong or inconsistent. The pages avoid those
claims. The list is kept with the project's notes. Most of the errors found up to edition 0.24.0 were fixed in
the site by pull requests to `tamnd/algorithm` in November 2026; the site's release v0.26.0, and so edition
0.26.0, has the fixes.
