This handbook sets out to hold what is known about algorithms in a form a person can learn from alone. It covers the classic material of a first course, the methods that real libraries and systems use, and a good part of the research literature, from Euclid's algorithm to the latest bounds on matrix multiplication. It is arranged so that a reader can start at the beginning of any volume and keep going, or open it at any entry and find what they need.

## Where the handbook comes from

The handbook is built from the Algorithm project, a website at <https://algorithm.tamnd.com> with one page for each topic: each algorithm, data structure, problem, theorem and definition. Each page has a summary, an explanation with worked examples, pseudocode, the costs, the proofs, the history, the sources it rests on, and code in several programming languages that is run against tests. The pages link to each other through their prerequisites. The site arranges its pages into 39 areas, from Foundations to Complexity, and each area into sub-areas.

The handbook takes the pages that are written in full and sets them as a book. Each area of the site is a volume, each sub-area a chapter, and each page an entry with a fixed number. Then it adds what a reference site does not need and a textbook does: an introduction to each volume, an opening and a reading order for each chapter, groups of entries with short introductions, a summary at the end of each chapter, exercises with hints, notes on the history, figures of how the entries depend on each other, and indexes. These learner pages are the only text written for the book; everything else is the text of the site.

Pages that are not yet written in full are not entries. They appear at the end of their chapter as *further topics*, one line each, with the address of their short page on the site. A volume whose area has no written page yet is listed in this guide as forthcoming. The handbook grows with the site: each edition is built from the site's content at a known commit, named on the copyright page.

## How it was made

Most of the text of the site, and the learner pages of this book, were drafted by AI agents. Each agent works from a fixed brief and from the sources it cites: textbooks, papers and survey articles, listed at the end of each entry. The code is checked by its tests in each language. The pages are reviewed against a written standard before they join the site, and the book's learner pages are checked by a program that tests every link, every exercise number and the order of every chapter. Errors remain all the same. The issue tracker of the project, <https://github.com/tamnd/algorithm/issues>, is the place to report them; a fix to the site reaches the next edition of the book.

The text is licensed under Creative Commons Attribution-ShareAlike 4.0 and the code under the MIT licence. You may copy, adapt and share both, as those licences allow.

## What is in this volume

This volume, the *Guide and Index*, is the way into the set. Chapter 0.1 explains how the handbook works: the numbers, the parts of an entry, the levels and the exercises. Chapter 0.2 fixes the notation that all volumes share. Chapter 0.3 lists the volumes, with the chapters of each and how much of each is written, and draws how they depend on each other. Chapter 0.4 gives learning paths: ordered lists of chapters and entries, across volumes, for a first course, for interviews, for contests and for several other goals. The rest of the volume is reference: a catalogue of the problems and the algorithms that solve them, a glossary of the definitions, a timeline of the history, the bibliography of the whole set, and two indexes, of people and of entries.

If you are new to algorithms, read Chapter 0.1, look up notation in Chapter 0.2 when you need it, and then follow the first path of Chapter 0.4, *A first course in algorithms*. It starts in Volume 1.
