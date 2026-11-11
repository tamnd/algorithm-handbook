A distributed algorithm runs on many machines that share no memory and talk only by sending messages. A bank keeps three copies of its ledger so that one crash loses nothing, and the copies must agree on the order of every payment. A ring of processes must pick one of them to coordinate, although each one sees only its two neighbours. A data centre must know which of its ten thousand servers are alive, and it cannot afford to ask each of them every second. In each case no machine sees the whole system, messages take an unknown time, and some machines fail while the rest carry on.

This volume is about the algorithms that work under those conditions and about the limits that no algorithm can pass. It starts with consensus, the problem at the centre of fault-tolerant computing, and with leader election, its simpler relative. It then treats time and order without a shared clock, replication of data, algorithms whose input is the network graph itself, agreement among processes that may lie, and gossip, which spreads information by random contacts.

## Why distributed algorithms get a volume of their own

The usual measures of an algorithm, its steps and its memory, matter little here. A few other ideas recur in every chapter:

- **The model decides the answer.** The same problem can be easy, costly or impossible depending on what the network promises. With synchronous rounds, [consensus](/consensus-problem/) with crashes takes $f + 1$ rounds. In the [asynchronous model](/asynchronous-model/), the [FLP theorem](/flp-impossibility/) rules out every deterministic protocol, even with one crash. Without signatures, agreement with liars is impossible once a third of the processes lie, by the [Byzantine resilience bound](/byzantine-resilience-bound/).
- **Knowledge comes only from messages.** A process knows only its own state and what it has received. The [happened-before](/happened-before/) relation replaces real time, and [vector clocks](/vector-clocks/) capture it exactly. A [global snapshot](/global-snapshot/) must be assembled from local pieces without stopping the system.
- **Quorums meet.** If every decision needs a majority, any two decisions share a witness. This fact carries [Paxos](/paxos/), [Raft](/raft/), [quorum replication](/quorum-replication/) and, with larger quorums of $2f + 1$ out of $3f + 1$, [PBFT](/pbft/).
- **Symmetry must be broken.** Identical processes running identical code stay identical. [Angluin's theorem](/anonymous-ring-impossibility/) shows that no deterministic algorithm elects a leader on an anonymous ring, and unique ids, random coins or the bits of ids, as in the [Cole-Vishkin algorithm](/cole-vishkin/), break the tie.
- **Messages and rounds are the costs.** Ring election needs $\Theta(n \log n)$ messages, a graph problem in the [LOCAL model](/local-model/) is measured by its rounds, and in the [CONGEST model](/congest-model/) also by the size of its messages.
- **Convergence without coordination.** Some problems need no agreement at all. A [CRDT](/crdt/) merges concurrent updates in any order to the same state, and [push gossip](/push-gossip/) informs all $n$ nodes in $\log_2 n + \ln n + O(1)$ rounds with no one in charge.

## How this volume relates to the others

- **Volume 7, graphs**, gives the sequential versions of the problems of Chapter 21.5: [breadth-first search](/breadth-first-search/), [spanning trees](/spanning-tree/) and the [minimum spanning tree](/minimum-spanning-tree/). The distributed versions solve them when each vertex is a processor that knows only its neighbours.
- **Volume 16, logic and constraints**, defines [safety](/safety-property/) and [liveness](/liveness-property/) properties. Most correctness statements in this volume are one or the other, and the FLP theorem is a conflict between them.
- **Volume 17, randomized algorithms**, has the [Las Vegas algorithms](/las-vegas-algorithm/) and [Markov chains](/markov-chain/) behind randomized election, Ben-Or's consensus and the analysis of gossip.
- **Volume 20, parallel algorithms**, studies processors that share memory and a clock. Its [maximal independent set](/maximal-independent-set/) algorithm by [Luby](/luby-mis/) runs almost unchanged in the LOCAL model, and its rounds of shuffles resemble the rounds of the CONGEST model.
- **Volume 22, concurrency**, covers processes that share memory and may be slow or fail. Consensus appears there too, as the measure of the power of synchronization primitives.

## The chapters

**Chapter 21.1, Consensus**, covers the models of time and failure, the consensus problem, quorums and ballots, FloodSet and the round lower bound, the FLP theorem and the ways around it by coin flips and failure detectors, Paxos, Raft and the replicated log, the operational parts of a replicated service, the variants of Paxos, atomic commit, weaker forms of agreement, and blockchains.

**Chapter 21.2, Leader election**, covers election on rings, from [Chang-Roberts](/chang-roberts/) with $O(n^2)$ messages to [Hirschberg-Sinclair](/hirschberg-sinclair/), Franklin, Peterson and Dolev-Klawe-Rodeh with $O(n \log n)$, and the [lower bound](/ring-election-lower-bound/) that matches them. It also covers anonymous rings and randomized election, election in trees and complete networks, and the bully algorithm.

**Chapter 21.3, Clocks and ordering**, covers physical clocks and their drift, clock synchronization by Cristian's algorithm, the Berkeley algorithm, NTP and PTP, and its [lower bound](/clock-synchronization-lower-bound/). It then treats logical time: Lamport clocks, vector and version vectors, causal and FIFO broadcast, global snapshots by [Chandy-Lamport](/chandy-lamport-snapshot/), hybrid logical clocks, TrueTime, and virtual time for parallel simulation.

**Chapter 21.4, Replication and CRDTs**, covers the [CAP theorem](/cap-theorem/) and the consistency models, primary-backup, chain, quorum and Dynamo-style replication with their repair mechanisms, and the conflict-free replicated data types, from the [G-counter](/g-counter/) to the OR-set and the sequence types for collaborative editing, with operational transformation as the older alternative.

**Chapter 21.5, Distributed graph algorithms**, covers the LOCAL and CONGEST models, flooding, broadcast and convergecast, spanning trees and BFS, [synchronizers](/synchronizer/), termination detection, the [Gallager-Humblet-Spira](/gallager-humblet-spira/) minimum spanning tree, symmetry breaking by colouring and maximal independent sets, network decomposition, and the lower bounds of Linial, of Kuhn, Moscibroda and Wattenhofer, and of Peleg and Rubinovich.

**Chapter 21.6, Byzantine agreement**, covers processes that may send anything. It covers the oral and signed message models, the $n > 3t$ bound, the oral messages and Dolev-Strong algorithms, phase king and phase queen, Bracha's reliable broadcast and asynchronous agreement, randomized agreement, and the replication protocols [PBFT](/pbft/), [HotStuff](/hotstuff/), Tendermint, Zyzzyva and HoneyBadger.

**Chapter 21.7, Gossip**, covers the random phone call model, push, pull and push-pull rumor spreading with their bounds, rumor mongering, gossip averaging and push-sum, peer sampling services, membership protocols such as [SWIM](/swim/), failure detection, and the conductance bounds that link spreading time to the structure of the graph.

## How to read this volume

If this is your first course on distributed algorithms, read these entries in this order. From Chapter 21.1: the [asynchronous model](/asynchronous-model/), [crash failures](/crash-failure/), the [consensus problem](/consensus-problem/), the [quorum](/quorum/), [FloodSet](/floodset/), the [FLP theorem](/flp-impossibility/), [Paxos](/paxos/) and [two-phase commit](/two-phase-commit/). From Chapter 21.2: the [Chang-Roberts algorithm](/chang-roberts/) and the [Hirschberg-Sinclair algorithm](/hirschberg-sinclair/). From Chapter 21.3: [happened-before](/happened-before/), [Lamport clocks](/lamport-clocks/), [vector clocks](/vector-clocks/) and the [Chandy-Lamport snapshot](/chandy-lamport-snapshot/). From Chapter 21.4: the [CAP theorem](/cap-theorem/) and the [G-counter](/g-counter/). From Chapter 21.5: [flooding](/flooding/) and [convergecast](/convergecast/). From Chapter 21.6: the [oral messages algorithm](/oral-messages-algorithm/). From Chapter 21.7: [push gossip](/push-gossip/). Do the exercises marked ◦ and • at the end of these chapters. That is a complete first unit on distributed algorithms.

Chapter 21.1 comes first, since the rest of the volume uses its models and its failure vocabulary. Chapter 21.6 needs Chapter 21.1, and the replication entries of Chapter 21.4 use its quorums and logs. Chapters 21.2, 21.3, 21.5 and 21.7 can be read in any order after the first group of Chapter 21.1. If you already know the basics, start with the opening page of each chapter. It names the groups in the chapter and the order to read them.

Each entry stands on its own. Its facts box lists what it needs, with the number of the entry where each prerequisite is explained. Entries in other volumes are cited by number too.

## What you need first

You should be able to read a short program and follow a proof by induction. From Volume 1 you need asymptotic notation, basic probability with the geometric distribution and the Chernoff bound, and harmonic numbers for the average cases of ring election. From Volume 7 you need graphs, trees, breadth-first search and minimum spanning trees. The idea of safety and liveness properties from Volume 16 helps throughout, and some familiarity with how programs run on a network of machines helps in Chapters 21.1 and 21.4, but neither is required.

## The exercises

Each chapter ends with exercises in three bands. Exercises marked ◦ check that you read the entries closely; you should be able to do them in a few minutes. Exercises marked • ask you to use an idea in a new place; each takes some thought, and some need a short program. Exercises marked ★ are harder; some are results from research papers. Hints for many exercises are in the appendix *Hints to the exercises* at the end of the volume.
