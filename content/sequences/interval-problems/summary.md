## What to remember

- **Sort, then scan.** Almost every problem here is solved by sorting the intervals, or their $2n$ end points, and making one pass with $O(1)$ state or a small heap. The sort costs $\Theta(n \log n)$ and the pass $O(n)$.
- **The sort cannot be avoided in general.** Point intervals $[x_j, x_j]$ reduce [element distinctness](/element-distinctness/) to merging, containment, maximum overlap, piercing and weighted scheduling, so each needs $\Omega(n \log n)$ operations in the algebraic decision tree model.
- **Touching end points decide the tests.** $[1, 3]$ and $[3, 5]$ meet; $[1, 3)$ and $[3, 5)$ do not, but their union is one interval; $(1, 3)$ and $(3, 5)$ neither meet nor merge. In a sweep, put starts before ends at equal coordinates for closed intervals, and ends before starts for half-open ones.
- **Depth equals the number of colors.** For intervals of one type, $\chi(G) = \omega(G) = d$: the fewest resources equals the largest number of intervals through one point. The [partitioning greedy](/interval-partitioning-greedy/), in order of left end, reaches $d$. By the [Helly property](/helly-property-intervals/), intervals that meet in pairs share a point, so the cliques of an interval graph are points of the line.
- **Two greedy rules and a min-max theorem.** For [covering](/interval-covering-greedy/), take the interval that reaches farthest from the covered prefix. For [piercing](/interval-piercing-greedy/), put a point at the earliest right end; the intervals that open new points are pairwise disjoint, so the fewest piercing points equals the most pairwise disjoint intervals, $\tau = \nu$.
- **Weights call for dynamic programming.** Sorted by right end, $M[j] = \max(M[j-1],\ w_j + M[p(j)])$, where $p(j)$ counts the intervals that end in time for $I_j$, found by binary search. With $k$ machines the problem is a minimum cost flow, solved in $O(kn \log n)$ time.
- **Queries cost $O(\log n + k)$.** After $O(n \log n)$ preprocessing, a centered interval tree or a priority search tree reports the $k$ intervals that contain a point, or meet a range, in $O(\log n + k)$ time and $O(n)$ space. The augmented search tree of [interval tree search](/interval-tree-search/) gives $O(\min(n, (k + 1) h))$ and supports updates.

## The main problems side by side

| Problem | Method | Time | Key step |
|---|---|---|---|
| [Merging](/interval-merging/) | [sort and scan](/interval-merging-sort/) | $\Theta(n \log n)$ | extend the last component or start a new one |
| [Union length](/interval-union-length/) | [sweep](/sweep-union-length/) | $\Theta(n \log n)$ | add each gap where the count is at least 1 |
| [List intersection](/interval-list-intersection/) | [two pointers](/interval-list-intersection-two-pointers/) | $\Theta(m + n)$ | drop the interval that ends first |
| [Containment](/interval-containment/) | [sort and scan](/interval-containment-sort/) | $\Theta(n \log n)$ | running maximum of the right ends |
| [Maximum overlap](/maximum-overlap/) | [sweep](/sweep-maximum-overlap/) | $\Theta(n \log n)$ | count open intervals, with the tie rule |
| [Interval partitioning](/interval-partitioning/) | [greedy with a heap](/interval-partitioning-greedy/) | $\Theta(n \log n)$ | reuse the resource that frees first |
| [Covering](/interval-covering/) | [greedy](/interval-covering-greedy/) | $\Theta(n \log n)$ | farthest reach |
| [Piercing](/interval-piercing/) | [greedy](/interval-piercing-greedy/) | $\Theta(n \log n)$ | point at the earliest right end |
| [Weighted scheduling](/weighted-interval-scheduling/) | [dynamic program](/weighted-interval-dp/) | $\Theta(n \log n)$ | take $j$ or skip it |
| [$k$ machines](/k-machine-interval-scheduling/) | minimum cost flow | $O(k n \log n)$ | $k$ units along the sorted end points |
| [Stabbing](/interval-stabbing-query/), [overlap](/interval-overlap-query/) | [interval tree search](/interval-tree-search/) | $O(\min(n, (k + 1) h))$ per query | prune by the largest right end below |

: The main interval problems, for $n$ intervals ($m$ and $n$ for the two lists of the intersection). All times except the last two rows are for the whole problem, and the sort dominates; with the input already sorted in the right order, merging, covering and piercing take $O(n)$ time. In the last row $k$ is the number of reported intervals and $h$ the height of the tree.

## Choosing a method

- Decide the type of the end points first, and write it down. Most interval bugs are a test of the wrong type.
- If you need the pieces of a union, or a clean input for other algorithms, merge first.
- If you need only the count at the busiest point, sweep the end points. If you also need to assign the intervals to rooms or registers, use the partitioning greedy.
- If intervals have weights and must be disjoint, do not look for a greedy rule: use the dynamic program.
- If the end points are small integers, a [difference array](/difference-array/) over the coordinates replaces the sort and gives $O(n + U)$ time for depth and coverage, where $U$ is the size of the range.
