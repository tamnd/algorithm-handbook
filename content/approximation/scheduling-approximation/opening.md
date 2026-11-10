A print shop has $m$ identical printers and a list of jobs, each with a running time, and wants the last job to finish as early as possible. This is makespan scheduling, and it is NP-hard already for two machines. Problems of this kind arise in factories, compilers, operating systems and computing clusters. They were also among the first problems studied for their worst-case ratio: Ronald Graham analyzed list scheduling in 1966.

The methods are close to those of bin packing. A schedule with makespan $T$ on $m$ machines is a packing of the jobs into $m$ bins of size $T$, and the two lower bounds on OPT are the same in spirit: the average load, and the longest job.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Identical machines.** List scheduling and Graham's bound $2 - 1/m$, the longest processing time rule and its ratio $\frac43 - \frac{1}{3m}$, the MULTIFIT method, and a polynomial-time approximation scheme by the dual approximation of Hochbaum and Shmoys.
2. **Related and unrelated machines.** Machines of different speeds, and the LP-rounding algorithm of Lenstra, Shmoys and Tardos with ratio 2 for unrelated machines, together with its lower bound of $3/2$.
3. **Precedence constraints.** Jobs that must wait for others, Graham's anomalies, and the algorithms of Hu and of Coffman and Graham for unit jobs.
4. **Other objectives.** Total and weighted completion time with the shortest processing time rule, due dates and the earliest due date rule, release dates, and Lawler's algorithm.
5. **Shop scheduling.** Flow shop, job shop and open shop, with the three-field notation that names all these problems.

## What to read meanwhile

The ideas behind the first two groups are in Chapter 18.1. Read [bin packing](/bin-packing/), its [lower bounds](/bin-packing-lower-bound/) and [first fit decreasing](/first-fit-decreasing/): sorting the jobs by decreasing length is the same idea as sorting items by decreasing size. The [local ratio technique](/local-ratio-technique/) treats a weighted scheduling problem of its own.

Exact scheduling algorithms for simpler problems are in Volume 2, with [activity selection](/activity-selection/) and [job sequencing with deadlines](/job-sequencing-with-deadlines/), and in Volume 6, with [weighted interval scheduling](/weighted-interval-scheduling/) and [interval scheduling on $k$ machines](/k-machine-interval-scheduling/). Precedence constraints form a directed acyclic graph, so read [topological sort](/topological-sort/) in Volume 7. For the LP rounding of unrelated machines, read the [LP relaxation](/lp-relaxation/) and [basic feasible solutions](/basic-feasible-solution/) in Volume 15.
