An operating system has more runnable threads than processors. A disk has a queue of requests scattered over its surface. The control computer of a car must finish each periodic task before its next period begins. Each of these is a scheduling problem: decide which job uses which resource, and when. The goals differ: short response times on a desktop, throughput in a batch system, every deadline in a real-time system, fairness in a shared cluster.

Some of the rules are simple and provably optimal. Shortest job first minimizes the average waiting time of jobs that are all ready at the start and run to completion, and earliest deadline first meets every deadline on one preemptive processor whenever any schedule does. Rate-monotonic priorities meet all deadlines of $n$ periodic tasks whenever their total utilization is at most $n(2^{1/n} - 1)$, a bound that falls toward $\ln 2 \approx 0.693$. Other rules, such as round robin, are judged by measurement more than by theorem.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **The problem and its measures.** Jobs, preemption, work-conserving schedulers, and turnaround, waiting and response time.
2. **CPU scheduling.** First-come first-served, shortest job first, round robin, priorities with aging, the multilevel feedback queue, and proportional share by lottery and stride scheduling and by the Completely Fair Scheduler of Linux.
3. **Real-time scheduling.** Periodic and sporadic tasks, cyclic executives, rate-monotonic and deadline-monotonic priorities, earliest deadline first and least laxity first, the Liu-Layland bound, response-time analysis, and priority inversion with the inheritance and ceiling protocols that bound it.
4. **Machine and project scheduling.** Smith's rule and the Moore-Hodgson algorithm on one machine, Johnson's rule for two machines in sequence, the critical path method, and projects under resource limits.
5. **Disks, clusters and energy.** Disk head scheduling by shortest seek time first, SCAN and LOOK, timing wheels, gang scheduling, backfilling, dominant resource fairness, and speed scaling with the YDS algorithm.

## What to read meanwhile

The theory of machine scheduling is in Chapter 18.2. Read [scheduling notation](/scheduling-notation/), [list scheduling](/list-scheduling/) and, for Johnson's rule, [flow shop scheduling](/flow-shop-scheduling/). Volume 2 proves the exact single-machine rules by exchange: [Smith's rule](/smith-rule/), [minimizing the number of late jobs](/minimizing-number-of-late-jobs/) and [minimizing maximum lateness](/minimizing-maximum-lateness/).

Chapter 19.2 treats jobs that arrive over time. The [deadline](/deadline/) entry explains why EDF is safe on one machine and not on two, [SRPT](/srpt/) is optimal for total flow time, and [online speed scaling](/online-speed-scaling/) introduces the energy problem. The [PERT chart](/pert-chart/) entry of Volume 7 has the critical path method. Ready queues are [priority queues](/priority-queue/), and the [calendar queue](/calendar-queue/) of Volume 3 is close to a timing wheel. For [starvation](/starvation/) and locks, read Chapter 22.1.
