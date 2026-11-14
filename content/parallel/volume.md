A parallel algorithm divides its work among many processors that run at the same time. Adding a million numbers one after another takes a million steps. Adding them in pairs, then adding the pair sums in pairs, takes twenty rounds, and the number of additions stays the same. A breadth-first search can expand a whole frontier of vertices at once. A graphics processor runs the same instruction on 32 threads in lockstep and hides the wait for memory by switching among thousands of them. A cluster of a thousand machines counts the words of the web by mapping each document to pairs, shuffling the pairs by key and reducing each key on its own machine. In each case the question is the same: how much of the work can happen at once, and what does it cost to coordinate it.

This volume is about algorithms designed for that question. It starts with the cost models that make parallel running time something you can analyse on paper, builds the short list of primitives that most parallel algorithms are made of, and applies them to graphs. It then turns to two kinds of real machine: the graphics processor, with its warps and its memory hierarchy, and the cluster, programmed in MapReduce or in bulk synchronous supersteps.

## Why parallel algorithms get a volume of its own

A parallel algorithm is not a sequential one run faster. The best sequential method is often a poor parallel one, and the ideas that work in parallel recur across chapters:

- **Two costs, not one.** The [work](/work-and-span/) is the total number of steps and the span is the longest chain of steps that depend on each other. A [greedy scheduler](/greedy-scheduling/) runs any computation on $p$ processors in time at most $T_1/p + T_\infty$, so these two numbers describe the algorithm on every machine at once.
- **Work efficiency first.** An algorithm that does $\lg n$ times too much work needs more than $\lg n$ processors just to match the sequential one. The [Blelloch scan](/blelloch-scan/) does linear work and the [Hillis-Steele scan](/hillis-steele-scan/) does not, and the difference matters more than their spans.
- **Associativity buys parallelism.** [Reduce](/parallel-reduce/) and [scan](/all-prefix-sums/) need only an [associative operator](/associative-operator/), and with them come [pack](/parallel-pack/), radix-sort splits, histograms and the carries of an adder.
- **Breaking symmetry.** Processors that look alike must sometimes choose different roles. Random coins in [Luby's algorithm](/luby-mis/) and in random-mate contraction, or deterministic coin tossing in list ranking, settle the choice in a few rounds.
- **Contraction.** Shrink the input by a constant factor in each round, solve the small problem, and expand the answer again. Lists, trees and graphs all yield to it, and it gives logarithmic numbers of rounds.
- **Communication is the cost.** On a GPU the cost is in [coalescing](/memory-coalescing/) and in the [roofline](/roofline-model/). On a cluster it is in the shuffle and in the $g \cdot h + L$ of the [BSP model](/bsp-model/). An algorithm that moves less data usually wins, even when it does more arithmetic.

## How this volume relates to the others

Several other volumes hold material that this one builds on or touches.

- **Volume 1, models of computation**, gives the [random-access machine](/random-access-machine/) that the PRAM extends, and the [boolean circuit](/boolean-circuit/), whose depth plays the part that span plays here.
- **Volume 4, sorting**, has its own chapters on [sorting networks](/sorting-network/) and on parallel sorting, from [bitonic sort](/bitonic-sort/) to [parallel merge sort](/parallel-merge-sort/) and sample sort. Those entries use the cost models of Chapter 20.1 and the merges and scans of Chapter 20.2.
- **Volume 18, approximation**, proves Graham's [list scheduling bound](/list-scheduling-bound/) for tasks of any length. The greedy bound of Chapter 20.1 is its special case for unit tasks.
- **Volume 21, distributed algorithms**, studies machines that share no memory and no clock, where messages may be slow or lost. Its [CONGEST model](/congest-model/) counts synchronous rounds of small messages on a network, much as Chapter 20.5 counts rounds of shuffles; the rest of that volume puts failures and asynchrony at the centre.
- **Volume 22, concurrency**, covers locks, [race conditions](/race-condition/) and lock-free data structures, including the [Chase-Lev deque](/chase-lev-deque/) that work-stealing runtimes use. This volume assumes that the runtime provides such structures and analyses the algorithms built on top of it.
- **Volume 38, complexity**, defines the class [NC](/nc/) of problems with polylogarithmic span and polynomial work, and the P-complete problems that are believed to have no such algorithm.

## The chapters

**Chapter 20.1, Work-span models**, sets up the cost models. It covers the PRAM and its EREW, CREW and CRCW variants, the computation DAG with its work and span, fork-join programs and determinacy races, the work and span laws with the measures built on them, Amdahl's and Gustafson's laws, and greedy and work-stealing schedulers with the bounds they meet.

**Chapter 20.2, Parallel primitives**, is the toolkit. It covers parallel loops and maps, reduce and scan with their work-efficient forms, segmented scans, scatter, gather and pack, parallel merging, parallel matrix multiplication and Strassen's method, and pointer jumping, list ranking and tree contraction.

**Chapter 20.3, Parallel graph algorithms**, applies the primitives to graphs. It covers frontier-based breadth-first search and its direction-optimizing form, delta-stepping for shortest paths, graph contraction, Shiloach-Vishkin connectivity, parallel minimum spanning trees, Tarjan-Vishkin biconnectivity, maximal independent sets, matchings and colourings by symmetry breaking, strongly connected components, parallel push-relabel, and the limits of parallel depth-first search.

**Chapter 20.4, GPU algorithms**, programs one real kind of parallel machine. It covers the SIMT model, warps and divergence, the memory hierarchy with coalescing and bank conflicts, occupancy and latency hiding, the roofline model, streams and transfers, tiled kernels for matrices and stencils, kernel fusion, single-pass scans with decoupled look-back, and warp-level control.

**Chapter 20.5, MapReduce and BSP**, programs clusters. It covers the MapReduce model with its combiner, partitioner and shuffle, the first jobs such as word count and the inverted index, skew, failures and speculative execution, joins, the bulk synchronous parallel model with supersteps, barriers and $h$-relations, iterative and graph frameworks such as Pregel and resilient distributed datasets, and lower bounds on rounds and communication.

## How to read this volume

If this is your first course on parallel algorithms, read these entries in this order. From Chapter 20.1: the [work-span model](/work-span-model/), [work and span](/work-and-span/), the [fork-join model](/fork-join-model/), [greedy scheduling](/greedy-scheduling/) and the [PRAM model](/pram-model/). From Chapter 20.2: [parallel reduction](/parallel-reduce/), the [Blelloch scan](/blelloch-scan/), [parallel pack](/parallel-pack/), [parallel merge](/parallel-merge/) and [list ranking](/list-ranking/). From Chapter 20.3: [parallel BFS](/parallel-bfs/), [Luby's algorithm](/luby-mis/) and [Shiloach-Vishkin](/shiloach-vishkin/). From Chapter 20.4: the [SIMT model](/simt-model/), [memory coalescing](/memory-coalescing/) and [shared-memory tiling](/shared-memory-tiling/). From Chapter 20.5: the [MapReduce model](/mapreduce-model/), [word count](/word-count/) and the [BSP model](/bsp-model/). Do the exercises marked ◦ and • at the end of these chapters. That is a complete first unit on parallel algorithms.

Chapters 20.1 and 20.2 come first; the rest of the volume quotes their costs and calls their primitives. After them, Chapters 20.3, 20.4 and 20.5 can be read in any order. If you already know the basics, start with the opening page of each chapter. It names the groups in the chapter and the order to read them.

Each entry stands on its own. Its facts box lists what it needs, with the number of the entry where each prerequisite is explained. Entries in other volumes are cited by number too.

## What you need first

You should be able to read a short program and follow a proof by induction. From Volume 1 you need asymptotic notation, recurrences and the master theorem, and, for the randomized algorithms, linearity of expectation and the Chernoff bound. From Volume 7 you need directed acyclic graphs, breadth-first search, connected components and minimum spanning trees in their sequential forms. Some familiarity with how a processor uses caches helps in Chapter 20.4, and some with how programs run on a network of machines helps in Chapter 20.5, but neither is required.

## The exercises

Each chapter ends with exercises in three bands. Exercises marked ◦ check that you read the entries closely; you should be able to do them in a few minutes. Exercises marked • ask you to use an idea in a new place; each takes some thought, and some need a short program. Exercises marked ★ are harder; some are results from research papers. Hints for many exercises are in the appendix *Hints to the exercises* at the end of the volume.
