A user posts a question on one server and a friend answers it on another. The log collector sorts the two lines by their timestamps, and the answer comes out first, because the second server's clock runs 40 ms behind. Nothing went wrong with the messages. The clocks disagree, and they always will a little: a crystal that is off by 20 parts per million gains or loses 1.7 seconds a day, and the delay of a message is known only within bounds. This chapter is about the two ways to live with that. One keeps physical clocks close enough to trust, and it knows how close is possible. The other drops physical time and tracks the order that matters, the order of cause and effect, with counters carried on the messages.

Both show up everywhere. NTP keeps the clocks of the Internet within milliseconds, and PTP keeps those of a power grid or a trading floor within a microsecond. Vector clocks and version vectors tell a replicated store which writes conflict. Snapshots of a running system detect deadlock and termination and checkpoint stream processors. Spanner waits out the uncertainty of its clocks so that transaction timestamps respect real time.

## What the chapter covers

The chapter is in nine groups, read in order.

1. **Physical clocks.** [Clock drift](/clock-drift/), the [skew](/clock-skew/) between two clocks, and the [monotonic clock](/monotonic-clock/) that programs should use for timeouts.
2. **Clock synchronization.** The [problem](/clock-synchronization/), [Cristian's algorithm](/cristian-algorithm/), the [Berkeley algorithm](/berkeley-algorithm/), [Marzullo's algorithm](/marzullo-algorithm/), [NTP](/ntp/) and the [Precision Time Protocol](/precision-time-protocol/), with the [lower bound](/clock-synchronization-lower-bound/) of Lundelius and Lynch.
3. **Causality.** The [space-time diagram](/space-time-diagram/), the [happened-before relation](/happened-before/), [concurrent events](/concurrent-events/) and the problem of [event ordering](/event-ordering/).
4. **Logical clocks.** [Lamport clocks](/lamport-clocks/) and the [total order](/total-order/) built on them, the [clock condition](/lamport-clock-condition/), [vector clocks](/vector-clocks/) and the [theorem](/vector-clock-characterization/) that they capture causality exactly, then [matrix clocks](/matrix-clocks/) and [plausible clocks](/plausible-clocks/).
5. **Message ordering.** FIFO and causal order, each as a property, a problem and an algorithm: [FIFO ordering](/fifo-ordering/), [FIFO delivery](/fifo-delivery/), [FIFO broadcast](/fifo-broadcast/), [causal ordering](/causal-ordering/), [causal order delivery](/causal-order-delivery/) and [causal broadcast](/causal-broadcast/).
6. **Cuts and snapshots.** [Consistent cuts](/consistent-cut/), the [global snapshot](/global-snapshot/) problem, the [Chandy-Lamport](/chandy-lamport-snapshot/) and [Lai-Yang](/lai-yang-snapshot/) algorithms, and [predicate detection](/distributed-predicate-detection/) with its fast case for [conjunctions](/weak-conjunctive-predicate-detection/).
7. **Versions of replicated data.** [Version vectors](/version-vectors/), [dotted version vectors](/dotted-version-vectors/) and [interval tree clocks](/interval-tree-clocks/).
8. **Logical clocks with real time.** [Hybrid logical clocks](/hybrid-logical-clocks/), [external consistency](/external-consistency/) and [TrueTime](/truetime/).
9. **Virtual time and simulation.** [Virtual time](/virtual-time/), [parallel discrete event simulation](/parallel-discrete-event-simulation/), the conservative [Chandy-Misra-Bryant algorithm](/chandy-misra-bryant/), the optimistic [Time Warp](/time-warp/) and [global virtual time](/global-virtual-time/).

## A first reading

Read these twelve entries in order: clock drift, clock synchronization, Cristian's algorithm, NTP, the space-time diagram, happened-before, concurrent events, Lamport clocks, vector clocks, consistent cuts, the Chandy-Lamport algorithm and causal broadcast. They give the error model of a physical clock, the round-trip idea that every synchronization protocol uses, the partial order of events, the two clocks that track it, the cuts on which a global state makes sense, and the two classic algorithms built from these. Draw every example as a space-time diagram and stamp it by hand with both clocks; the rules take a minute to learn and the diagrams make the theorems obvious.

Skip the lower bound, plausible clocks, interval tree clocks and the predicate detection entries at first; they are research-level and assume the rest. The simulation group stands apart from the others. Read it after Lamport clocks if parallel simulation is what you came for, and otherwise leave it for last.

## Before you start

The entries work in the [asynchronous model](/asynchronous-model/) of Chapter 21.1, with reliable channels and unbounded delays; the synchronization entries add bounds on the delays. The broadcast entries assume the [broadcast problem](/broadcast-problem/) of Chapter 21.5, and the simulation group assumes sequential [event-driven simulation](/event-driven-simulation/) from Volume 2. A space-time diagram is a [directed acyclic graph](/directed-acyclic-graph/), and happened-before is its reachability relation. Several proofs are by [induction](/induction/) along a run.

Other chapters use these results. [Total-order broadcast](/total-order-broadcast/) in Chapter 21.1 orders messages with the total order of this chapter, and the [leader lease](/leader-lease/) depends on a bound on clock drift. In Chapter 21.4, [causal consistency](/causal-consistency/) is defined by happened-before and kept with vector clocks, and [last-writer-wins](/last-writer-wins/) registers use Lamport or hybrid timestamps.
