## What to remember

- A sweep turns a static problem in the plane into a sequence of updates on a line. It needs a set of event points, an event queue that gives them in order, and a status structure that holds the objects crossing the line.
- The proof is a [sweep invariant](/sweep-invariant/): after the events at coordinate $x$ are processed, the status is correct for the line just right of $x$, and the answer is correct for everything left of it.
- The status decides the cost and the questions that a sweep can answer. A counter gives depth, a balanced search tree gives order and neighbours, a [segment tree](/segment-tree/) gives covered length, and a max-heap gives the highest active object.
- In the segment sweep two segments can only cross after they have become neighbours in the status, so the sweep tests only neighbours and finds every crossing with $O(1)$ tests per event.
- The order of events at one coordinate is part of the algorithm. For closed objects, starts come before ends; for open ones, ends come before starts. With many segments through one point, the sweep deletes the ending and passing ones and inserts the starting and passing ones in their new order.
- Lazy deletion keeps a heap simple: an entry that is no longer valid stays in the heap until it reaches the top, and it is thrown away there. Each entry is removed once, so the total cost stays the same.
- The $\Omega(n \log n)$ lower bounds for rectangle intersection, the skyline and the union area come from [element distinctness](/element-distinctness/) and from the union of intervals, so the $\Theta(n \log n)$ sweeps are optimal in their models.
- A simulation is a sweep over time. An event-driven simulation jumps from one predicted event to the next and must throw away predictions that a later event has made stale; a time-driven one checks at fixed steps and can miss short events.

## The sweeps side by side

| Entry | Status | Time | Extra space | Events |
|---|---|---|---|---|
| [Rectangle intersection sweep](/rectangle-intersection-sweep/) | search tree of $y$-intervals | $\Theta(n \log n)$ | $\Theta(n)$ | $2n$ |
| [Bentley's union sweep](/rectangle-union-sweep/) | segment tree on compressed $y$ | $\Theta(n \log n)$ | $\Theta(n)$ | $2n$ |
| [Skyline sweep](/skyline-sweep/) | max-heap of heights | $\Theta(n \log n)$ | $\Theta(n)$ | $2n$, at most $n$ lazy removals |
| [Segment intersection with the event queue](/event-queue/) | search tree of segments | $O((n + k) \log n)$ | $O(n)$ | at most $2n + k$ |
| [Rotational sweep](/rotational-sweep/) | search tree along the ray | $O(n \log n)$ per centre | $O(n)$ | at most $2n$ |
| [Lower envelope](/lower-envelope-of-segments/) | none (Hershberger's method) | $O(n \log n)$ | | output of at most $\lambda_3(n) = \Theta(n \alpha(n))$ pieces |
| [Collision prediction](/collision-prediction-and-resolution/) | binary heap of predicted events | $O((n^2 + kn) \log(n + k))$ | $O(n^2 + kn)$ | $k$ |
| [Time-driven simulation](/time-driven-simulation/) | none | $\Theta((T/\Delta t)\, n^2)$ | | $\lceil T/\Delta t \rceil$ steps |

: The bounds are worst case. For segments, $k$ is the number of crossings; for the simulation, $k$ is the number of events taken from the queue, $T$ the length of the run and $\Delta t$ the step. The space $O(n)$ of the segment sweep needs the rule that deletes a crossing event when its two segments stop being neighbours. The rotational sweep costs $O(n^2 \log n)$ when it runs from each of the $n$ vertices, as in the visibility graph.

## Choosing a sweep

First decide what the line must know about the objects it crosses. If it only needs how many, a counter is enough. If it needs the order along the line, for neighbours or for crossings, use a balanced search tree with a comparator that evaluates each object at the current position. If it needs the measure of the covered part, use a segment tree with a count and a covered length at each node. If it needs the highest active object, use a max-heap with lazy deletion.

Then fix the tie rule before writing the loop, and test it on objects that touch: two rectangles that share an edge, two segments that share an endpoint, a building that ends where another starts. Most wrong sweeps are wrong only there.

When the objects move, sweep over time instead. Prefer the event-driven form when events are rare and can be predicted exactly, as for disks in straight flight; prefer the time-driven form when forces act at every instant and no event can be predicted. For angular questions around one point, turn the line instead of moving it.
