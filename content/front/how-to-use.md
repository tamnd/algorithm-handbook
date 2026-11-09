The handbook is a set of volumes with one numbering. Each volume can be read from its first page, and each entry can be read on its own. This chapter explains the parts that all volumes share.

## Volumes, chapters and entries

The set follows the areas of the site. Volume 1 is Foundations, Volume 4 is Sorting, Volume 7 is Graphs, and so on up to Volume 31, Complexity. This volume, the guide, is Volume 0. A volume has one chapter for each sub-area of its area: Chapter 4.1 is *Comparison sorts*, the first chapter of Volume 4.

An entry is one topic: an algorithm, a data structure, a problem, a theorem, a definition, a concept, a technique, a model of computation or an abstract type. Its number has three parts, volume, chapter and place in the chapter. Entry 4.1.12, say, is the twelfth entry of the first chapter of Volume 4. Every cross-reference in the set gives this number in small grey type after the name of the entry, so you can tell at a glance which volume a reference points to. When it points into another volume, the link goes to the entry's page on the site.

The numbers belong to one edition. When a later edition adds entries, numbers can move. The name of an entry, and its address on the site, do not change; the address is the name in lower case with hyphens, such as <https://algorithm.tamnd.com/merge-sort/>.

## The parts of a volume

A volume opens with its **introduction**: what the area is about, why it matters, one paragraph on each chapter, a first-course path through the volume and the prerequisites from other volumes. A table lists the chapters with their sizes, and a figure shows how the chapters depend on each other.

Each **chapter** has the same parts in the same order:

1. The **opening**: what the chapter is about, the groups of entries it holds, a short list of entries to read first, and what you should know before you start.
2. A **table of the entries**, with the kind and the level of each, and, when the chapter is large enough, a **concept map**: a figure of the entries with an arrow from each one to the entries that build on it.
3. The **entries**, in groups. Each group has a title and a few lines on what its entries have in common. Within the chapter, an entry comes after the entries it needs, as far as that is possible.
4. **Further topics**: the topics of the chapter whose entries are not yet written, with a line on each and its address on the site.
5. The **summary**: what to remember, a table that compares the main methods, and advice on choosing among them.
6. The **exercises**, in three bands.
7. **Notes and further reading**: the history of the chapter's ideas, and the books and papers to read next.

At the end of the volume come the appendices: hints to the exercises, a table of the problems of the volume and the algorithms that solve them, the bibliography, an index of names and the index.

## The parts of an entry

An entry begins with its number, its name, its kind and its level, and a short summary in italics. Then comes the **facts box**: the problem the algorithm solves or the abstract type a data structure implements, the model of computation, the costs, the properties (stable, in place, online), what the entry needs, with the numbers of those entries, and the year and the people of its origin.

The body has a fixed order for each kind. An algorithm entry, for instance, explains the idea in plain words, states the problem, gives the pseudocode and walks through it, works an example, proves the algorithm correct, analyses its cost, lists its properties and its variants, says when to use it and what goes wrong in practice, and gives its history. A data structure entry gives the representation and its invariant, then each operation with its cost. A problem entry defines the problem exactly, then lists the algorithms that solve it in a table, with their costs, and gives the known bounds. A theorem entry gives the statement, then the proof. Proofs stand in shaded boxes; a proof marked *sketch* gives the main steps and leaves routine checks to the reader.

Most algorithm and data structure entries end with code in Python, the one the site tests. The site has the same code in several other languages, all tested against the same cases, and its address is printed under the code. Each entry ends with its references, which are collected into the bibliography of the volume, and with a list of related entries.

## Levels

Each entry has one of four levels.

- **Intro** entries need only the prerequisites they list and some programming. They are the material of a first course.
- **Core** entries are the standard material of a full undergraduate course and of the main textbooks.
- **Advanced** entries go further: graduate courses, specialist books and the methods of production systems.
- **Research** entries present results from the research literature, often recent ones, with their sources.

A first pass through a chapter can skip the advanced and research entries. Nothing at the intro or core level depends on them.

## The exercises

Each chapter ends with exercises in three bands. Exercises marked ◦ check that you read the entries closely; you should be able to do them in a few minutes. Exercises marked • ask you to use an idea in a new place; each takes some thought, and some need a short program. Exercises marked ★ are harder; some are results from research papers. An exercise has a number like 4.1.7, the seventh exercise of Chapter 4.1. Hints and short answers to about half of them are in the appendix *Hints to the exercises* of the volume. Each hint starts with the number of its exercise, which links back to it.

Many entries also end with a few exercises of their own. The chapter exercises do not repeat them.

## Four ways in

There are four ways to find what you need in the set.

**By area.** Chapter 0.3 of this volume lists the volumes and their chapters. The introduction of each volume says how its chapters fit together.

**By problem.** If you have a problem to solve, find it in Chapter 0.5, *Problems and their algorithms*. It lists each problem of the set with the algorithms that solve it and the time each takes. Problem entries carry the same table, with the space each algorithm uses as well.

**By name.** The *Index of entries* at the end of this volume lists every entry of the set by name and by its other names, with its number. The *Index of names* lists the people in the history of the entries. The index of each volume is finer: it also lists the entries of other volumes that the volume uses, and, for each entry, the entries of the volume that link to it.

**By path.** Chapter 0.4 gives learning paths: ordered lists of chapters and entries for a goal, such as a first course, interview preparation or scientific computing. Each step has a box to tick.

## The site and the book

The site and the book have the same text. The site has more: the code in every language, interactive figures that step through the algorithms, and the short pages of the topics that are not yet written. The book has the order: openings, groups, summaries, exercises and indexes that put the entries in a sequence for learning. Use the book to learn and the site to look things up and to run the code.
