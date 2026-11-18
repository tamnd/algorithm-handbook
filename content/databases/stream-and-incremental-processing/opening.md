Most queries are asked once, about data that stands still. Some are asked again and again while the data changes: a dashboard that shows sales per region, a warehouse table of daily totals, a rule that flags a suspicious sequence of payments as it happens, a reachability relation over a graph that gains and loses edges. Running such a query from the start after every change wastes almost all of the work, since a small change in the input usually makes a small change in the answer.

This chapter is about computing that change directly. The same idea has two forms. A database keeps a stored query result, a materialized view, and updates it from the changes to the base tables. A stream system runs a standing query over data that arrives without end, keeps only a window or a summary of the past, and emits answers as it goes. The written entries of the chapter cover the first form.

## What the chapter covers

The chapter is in three groups, read in order.

1. **Stored results.** The [materialized view](/materialized-view/), what it stores, when a query can read it in place of the base tables, and why aggregate views are the most useful.
2. **Keeping a view up to date.** The [view maintenance problem](/view-maintenance/), with the choices between recomputation and deltas and between immediate and deferred maintenance. [Incremental view maintenance](/incremental-view-maintenance/), with a delta rule for each operator of relational algebra and the counting algorithm for deletions.
3. **Recursive views.** The [DRed algorithm](/dred-algorithm/), delete and rederive, which keeps the least model of a Datalog program correct under insertions and deletions of stored facts.

The entries on delta rules, deferred and self-maintainable views and higher-order incremental maintenance as separate topics, DBSP, differential and timely dataflow, the dataflow model, continuous queries and the CQL model, watermarks and punctuation, panes, stream slicing and FlatFAT for window aggregation, chain scheduling, the symmetric hash join and XJoin, asynchronous barrier snapshotting, and complex event processing with NFA-based pattern matching are not written yet. The view maintenance entry mentions some of them briefly.

## A first reading

There are four written entries, and they are best read in the order of the chapter: the materialized view, the view maintenance problem, incremental view maintenance and the DRed algorithm. The first three take an afternoon and give the whole idea for nonrecursive views.

The DRed algorithm needs Datalog and semi-naive evaluation and can wait until you have read them. It shows why counting is not enough once views are recursive, and why the cost of a deletion can be far larger than the change it causes.

## Before you start

You need [relational algebra](/relational-algebra/) from Chapter 40.1, since every delta rule is a rule of the algebra, and for the DRed algorithm [Datalog](/datalog/) and [semi-naive evaluation](/semi-naive-evaluation/) from the same chapter. Semi-naive evaluation is itself incremental computation: each round joins only the new facts of the round before. The [hash join](/hash-join/) of Chapter 40.3 evaluates most delta expressions, and the [query plan](/query-plan/) of Chapter 40.4 shows where a view can replace part of a query. The view that the DRed examples maintain is the [transitive closure](/transitive-closure/) of Volume 7.

The stream side of the subject rests on Volume 19. The [sliding window model](/sliding-window-model/), [sliding window aggregation](/sliding-window-aggregation/) with the [two-stacks queue](/two-stacks-queue/), and the [exponential histogram](/exponential-histogram/) keep answers over the recent past in small space; the [count-min sketch](/count-min-sketch/) and [HyperLogLog](/hyperloglog/) summarize a stream that cannot be stored. Consistent snapshots of a running dataflow are the [Chandy-Lamport snapshot](/chandy-lamport-snapshot/) of Volume 21.
