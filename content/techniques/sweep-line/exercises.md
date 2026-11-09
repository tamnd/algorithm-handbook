1. ◦ Take the segments $a$ from $(0, 0)$ to $(6, 6)$, $b$ from $(0, 6)$ to $(6, 0)$ and $c$ from $(1, 4)$ to $(7, 4)$. Find all crossing points, and list all [event points](/event-point/) of the segment sweep in the order of the [event queue](/event-queue/), by $x$ and then by $y$. How many event points are there, and at how many distinct values of $x$?

2. ◦ For the segments of exercise 1, give the order of the segments in the [status structure](/sweep-status-structure/), from bottom to top, for the line at $x = 0.5$, $1.5$, $2.5$, $3.5$ and $5$. At which events does the order change, and which pair swaps at each?

3. ◦ Run the [skyline sweep](/skyline-sweep/) on the buildings $(L, R, H)$ equal to $(1, 6, 4)$, $(2, 4, 7)$, $(3, 9, 5)$, $(8, 12, 3)$, $(10, 11, 6)$ and $(13, 15, 2)$. Give the output skyline as a list of points $(x, h)$, the number of entries taken out of the heap in total, and the expired entries that stay in the heap for a while before they are removed.

4. ◦ Merge the skylines $[(1, 3), (4, 6), (7, 0)]$ and $[(2, 5), (5, 2), (9, 0)]$ as in the divide-and-conquer method of the [skyline problem](/skyline-problem/). Give the merged skyline without redundant points.

5. ◦ Run [Bentley's union sweep](/rectangle-union-sweep/) on $R_1 = [0, 4] \times [0, 3]$, $R_2 = [2, 6] \times [1, 5]$ and $R_3 = [3, 8] \times [4, 6]$. Give each strip between consecutive event coordinates with its covered length and its area, and the total area. Then find the area covered by at least two rectangles.

6. ◦ Five rectangles are $P = [0, 2] \times [0, 2]$, $Q = [2, 4] \times [1, 3]$, $R = [1, 3] \times [3, 5]$, $S = [5, 6] \times [0, 1]$ and $T = [3, 5.5] \times [0.5, 2]$. List the pairs that intersect when the rectangles are closed, and the pairs that intersect when they are open. In the [rectangle intersection sweep](/rectangle-intersection-sweep/) for closed rectangles, which event at $x = 2$ must come first?

7. ◦ Sort the points $(2, 2)$, $(-1, 2)$, $(0, -3)$, $(3, 0)$, $(-2, -2)$, $(1, 1)$, $(2, -1)$ and $(-3, 0)$ by angle around the origin, counterclockwise from the positive $x$-axis, as a [rotational sweep](/rotational-sweep/) does. Break ties of angle by distance. Which two points tie?

8. ◦ A bank has one teller. Customers arrive at times 0, 2, 3, 5 and 9 and need 4, 1, 2, 3 and 1 units of service. Run the [event-driven simulation](/event-driven-simulation/), with departures before arrivals at equal times. Give the start of each service, the time of the last departure, the wait of each customer and the mean wait, the number of events, and the longest line with the time when it occurs.

9. • The perimeter of a union of rectangles is the sum of the vertical and the horizontal parts of its boundary. Let a left-to-right sweep process each vertical edge as its own update, with starts before ends at equal $x$, and let $\ell$ be the covered length on the line. Show that the vertical part equals the sum of $|\Delta \ell|$ over the updates, and compute the perimeter of the union in exercise 5. Then take $[0, 2] \times [0, 1]$ and $[2, 4] \times [0, 1]$, and find the perimeter that the same formulas give with ends before starts at $x = 2$ and with starts before ends.

10. • The skyline sweep with lazy deletion takes out at most $n$ entries in total. Give, for every $n$, an input on which a single event takes out all $n$ entries, and say how many expired entries the heap holds just before that event.

11. • Take the segments $s_1$ from $(0, 0)$ to $(8, 8)$, $s_2$ from $(0, 8)$ to $(8, 0)$, $s_3$ from $(0, 4)$ to $(8, 4)$, $s_4$ from $(4, 4)$ to $(8, 6)$ and $s_5$ from $(0, 6)$ to $(4, 4)$, which all meet at $p = (4, 4)$. Give the sets $U(p)$, $L(p)$ and $C(p)$ of [degeneracy in sweeps](/degeneracy-in-sweeps/), the status just left and just right of $x = 4$ from bottom to top, and the number of intersecting pairs that the event reports.

12. • Run the segment sweep on the segments of exercise 1, testing each new pair of neighbours for a crossing to the right of the line. How many times is each crossing point found? What does the merge rule of the [event queue](/event-queue/) prevent here, and which crossing events are deleted and found again in the variant that deletes the event of two segments that stop being neighbours?

13. • In the unit box, disk $i$ is at $(0.2, 0.5)$ with velocity $(0.4, 0)$ and disk $j$ is at $(0.8, 0.58)$ with velocity $(-0.2, 0)$. Both have radius $0.05$ and mass 1. Use [collision prediction and resolution](/collision-prediction-and-resolution/) to find the time of their collision, their positions at that time, and their velocities after it. Check that the kinetic energy is kept, and that no wall is hit first.

14. • Two disks of equal mass collide with relative velocity $\Delta v$ parallel to the line between their centres. Show from the impulse formula of [collision prediction and resolution](/collision-prediction-and-resolution/) that they exchange their velocities.

15. • A ball is dropped from height 1 under gravity $g = 2$ and bounces with coefficient of restitution $1/2$, so each bounce halves its speed. Find the times of the first five bounces and their limit. How many bounces happen before $t = 2.9$, and what does this mean for an [event-driven simulation](/event-driven-simulation/) of the ball?

16. • Points move on a line with $x_i(t) = a_i + b_i t$. Show that the leftmost point changes at most $n - 1$ times over all $t$, and check that the bound is reached by $x_i(t) = i^2 - 2it$ for $i = 1, \ldots, n$, giving the times of the changes. Then show that, if each point exists only during an interval of time, two points can change the lead three times.

17. • Points $c = (0, 0)$, $(1, 0)$, $(0.6, 0.8)$, $(-0.5, 0.5)$, $(0, -1.2)$, $(1.5, -0.5)$ and $(2, 2)$ are given, with $r = 1$. Sweep the angle $\varphi$ of the centre of a circle of radius 1 through $c$, as in the [rotational sweep](/rotational-sweep/). Give the interval of angles for each other point, the largest number of points in such a circle, $c$ included, and all angles that reach it.

18. • Compute the [lower envelope](/lower-envelope-of-segments/) of the segments $a$ from $(0, 3)$ to $(8, 3)$, $b$ from $(1, 0)$ to $(5, 4)$, $c$ from $(2, 6)$ to $(9, -1)$ and $d$ from $(6, 1)$ to $(10, 1)$ over $[0, 10]$. Give the breakpoints and the sequence of labels, and point out a pair of segments that alternate four times on it.

19. ★ Extend the segment tree of Bentley's sweep so that each node keeps the length covered at least once and the length covered at least twice in its range. Give the update rule for a node with count 0, count 1 and count at least 2, and apply the sweep to the rectangles of exercise 5 to find the area covered exactly once.

20. ★ The rectangles $A = [0, 4] \times [0, 4]$, $B = [2, 6] \times [2, 6]$, $C = [3, 5] \times [0, 3]$, $D = [5, 8] \times [1, 2]$ and $E = [1, 3] \times [5, 7]$ are closed. Give an $O(n \log n)$ sweep that finds the largest number of rectangles with a common point, and apply it. Say how the events at one $x$ must be ordered.

21. ★ Give an $O(n \log n)$ sweep that counts the pairs of intersecting closed rectangles, with two [Fenwick trees](/fenwick-tree/) over the compressed $y$-coordinates. Run it on the rectangles of exercise 20, giving the count at each insertion and the total.

22. ★ Compute the volume of the union of the boxes $[0, 2]^3$, $[1, 3]^3$ and $[0, 1] \times [0, 4] \times [2, 3]$ by a sweep over $z$ that computes the area of each slab with a union sweep. What does this method cost for $n$ boxes?
