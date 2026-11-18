A query in SQL says what answer it wants, not how to compute it. The system must choose how: in which order to join the tables, which join algorithm to use for each pair, whether to read a table in full or through an index, and where to apply each filter. These choices are the plan, and for one query the cheapest and the most expensive plans can differ by several orders of magnitude. Query planning is the part of a database system that makes the choice.

The planner never knows the true cost of a plan before it runs it. It estimates the size of each intermediate result from statistics, prices each plan with a cost model, and searches a space of plans that grows faster than exponentially with the number of tables. Each of the three steps has its own algorithms, and each can fail in its own way. This chapter takes them in turn.

## What the chapter covers

The chapter is in four groups, read in order.

1. **Plans, sizes and rewrites.** What a [query plan](/query-plan/) is, logical and physical, and how many join trees there are. How the [selectivity](/selectivity/) of a predicate gives the size of a result, and the assumptions of uniformity and independence behind the usual formulas. [Predicate pushdown](/predicate-pushdown/), the rewrite that applies filters early and turns products into joins.
2. **Costs and the search problems.** The [cost model](/cost-model/), from System R's page fetches and CPU weight to PostgreSQL's cost units and the simple measure $C_{\mathrm{out}}$. The [join ordering problem](/join-ordering/), NP-hard in general and polynomial for some query shapes, and the wider [query optimization problem](/query-optimization/).
3. **Statistics and the System R search.** The [histogram](/histogram/) as a summary of one column, with equi-width, equi-depth and V-optimal buckets. [System R join enumeration](/selinger-join-enumeration/), the dynamic program over subsets with interesting orders.
4. **Hard estimates and stored views.** [Cardinality estimation](/cardinality-estimation/) for joins, how its errors grow and how they are measured. [View selection](/view-selection/), which chooses the precomputed results to keep under a space budget.

The entries on the dynamic programs DPccp and DPhyp, the IKKBZ algorithm, greedy operator ordering, interesting orders, the Volcano optimizer generator and Cascades, subquery unnesting, eager aggregation, eddies, mid-query, parametric and multiple-query optimization, wander join, and pessimistic, guaranteed-error and learned estimation are not written yet. Several of them are described briefly inside the entries on join ordering, query optimization and cardinality estimation.

## A first reading

For a first reading, take these seven entries in order: the query plan, selectivity, predicate pushdown, the cost model, the join ordering problem, System R join enumeration and cardinality estimation. They show what is chosen, how each choice is priced, how the best left-deep order is found exactly, and why the result is still only as good as the estimates.

Leave the histogram for when you need to know where the selectivities come from, and the query optimization problem for when you want the whole picture, with rewrites and top-down search. View selection belongs to data warehouses and can wait until you have read the [materialized view](/materialized-view/) in Chapter 40.9.

## Before you start

You need [relational algebra](/relational-algebra/) from Chapter 40.1, since every plan is an algebra expression, and the join algorithms of Chapter 40.3: the [nested-loop join](/nested-loop-join/), the [block nested-loop join](/block-nested-loop-join/), the [index nested-loop join](/index-nested-loop-join/), the [sort-merge join](/sort-merge-join/) and the [hash join](/hash-join/), with the [iterator model](/iterator-model/) that runs a plan. The cost formulas count page reads, so the [external memory model](/external-memory-model/) of Volume 1 helps, and the [B+ tree](/b-plus-tree/) of Volume 3 is the index the access paths use.

The dynamic programs of this chapter are close to the [matrix chain multiplication](/matrix-chain-multiplication/) program of Volume 2, which chooses the order of a chain of products. The hardness results use [NP-hardness](/np-hard/) from Volume 39. Estimates of join sizes and distinct counts from one pass over the data use the [AMS sketch](/ams-sketch/), [HyperLogLog](/hyperloglog/) and the [join size estimation problem](/join-size-estimation-problem/) of Volume 19.
