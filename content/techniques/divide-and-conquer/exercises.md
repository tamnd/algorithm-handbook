1. ◦ Solve each recurrence, with $T(1) = \Theta(1)$, and say whether the work is concentrated in the leaves of the recursion tree, spread evenly over its levels, or concentrated at the root: (a) $T(n) = 4T(n/2) + \Theta(n)$; (b) $T(n) = 2T(n/2) + \Theta(n)$; (c) $T(n) = 2T(n/2) + \Theta(n^2)$; (d) $T(n) = 8T(n/2) + \Theta(n^2)$.

2. ◦ How many multiplications does [exponentiation by squaring](/binary-exponentiation/), as given in [decrease and conquer](/decrease-and-conquer/), use to compute $a^{25}$? To compute $a^{32}$? Write the chain of exponents for each.

3. ◦ Run [Euclid's algorithm](/euclidean-algorithm/) on $(252, 105)$ and on $(89, 55)$. List the pairs and count the division steps. Why does the second pair, though smaller, take more steps?

4. ◦ Use the recurrence $J(1) = 1$, $J(2k) = 2J(k) - 1$, $J(2k+1) = 2J(k) + 1$ of the Josephus problem to find the survivor $J(100)$. Show the chain of arguments.

5. ◦ In [divide and conquer over time](/divide-and-conquer-on-queries/) with $q = 8$ operations, at which nodes of the segment tree over $[1, 8]$ does INSERT-INTERVAL store an item with lifetime $[2, 7]$? With lifetime $[3, 6]$? With lifetime $[1, 8]$?

6. ◦ Count the inversions of $\langle 6, 3, 5, 1, 4, 2 \rangle$ the way [counting inversions](/counting-inversions/) does: the inversions inside each half of three items, and the inversions with one item in each half, found during the merge. Check the total against a direct count.

7. ◦ On four vertices, run the offline connectivity method of [divide and conquer on queries](/divide-and-conquer-on-queries/) on these eight operations: 1 add 1-2, 2 add 2-3, 3 is $1 \sim 3$?, 4 remove 1-2, 5 is $1 \sim 3$?, 6 add 3-4, 7 remove 2-3, 8 is $1 \sim 4$?. Give the lifetime of each edge, the nodes of the segment tree over $[1, 8]$ where each edge is stored, and the three answers.

8. • Let $T(1) = 1$ and $T(n) = T(n/2) + n$ for $n$ a power of 2. Find $T(n)$ exactly, and use it to explain why a decrease by half with linear work per step, as in quickselect with good pivots, costs linear time and not $\Theta(n \log n)$.

9. • Exponentiation by squaring is a decrease-and-conquer method, but it does not always use the fewest multiplications. How many multiplications does it use for $a^{23}$? Find a way to compute $a^{23}$ with fewer, by computing a different sequence of powers, each the product of two earlier ones. (See [addition chains](/addition-chain/).)

10. • The binomial coefficients satisfy $\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$ with $\binom{n}{0} = \binom{n}{n} = 1$. Show that the naive recursive procedure based on this rule makes exactly $2\binom{n}{k} - 1$ calls to compute $\binom{n}{k}$. How many calls does it make for $\binom{10}{5}$, and how many distinct subproblems does it meet? What does this say about the method?

11. • The [divide-and-conquer maximum subarray algorithm](/maximum-subarray-divide-and-conquer/) runs in $\Theta(n \log n)$ because its crossing step scans the array. Change the algorithm so that each call returns four numbers for its range: the total, the best prefix sum, the best suffix sum and the best subarray sum. Show that the combine step then takes $O(1)$ time, and solve the new recurrence.

12. • Two sorted arrays $A$ and $B$ hold $n$ numbers each. Give a decrease-and-conquer algorithm that finds the $k$-th smallest of the $2n$ numbers in $O(\log n)$ time, without merging. Say what each step discards and why the answer cannot be in the discarded part.

13. • An array $A[1..n]$ of distinct numbers has a *local minimum* at $i$ if $A[i]$ is smaller than each of its neighbours that exist. Show that a local minimum always exists, and find one with $O(\log n)$ reads of the array by decrease and conquer. State the invariant your loop keeps.

14. • A closest-pair algorithm that splits the points by a vertical line sorts the points of the strip by $y$ again in every call, instead of passing down lists already sorted by $y$. Write its recurrence and solve it by the recursion-tree method. By what factor is it slower than the algorithm with presorting?

15. • Show that counting inversions by merge sort is a case of CDQ divide and conquer: say what the updates, the queries and the contributions are, with the index as time, and what the step CROSS does. Why does CROSS cost only a merge here, and what total time does that give?

16. • In the work-span model, merge sort with a serial merge has span $\Theta(n)$. Suppose instead that the merge of $n$ items has span $\Theta(\log^2 n)$, as the [parallel merge sort](/parallel-merge-sort/) entry shows for its merge. Write the span recurrence of the sort and solve it. What is the parallelism, work divided by span?

17. • The *reflected binary Gray code* $G_n$ lists all $2^n$ strings of $n$ bits: $G_1 = 0, 1$, and $G_n$ is $G_{n-1}$ with a 0 in front of each string, followed by $G_{n-1}$ in reverse order with a 1 in front of each string. Write out $G_3$. Prove by induction on $n$ that any two strings next to each other in $G_n$ differ in exactly one bit, and that so do the last and the first.

18. ★ In [median of medians](/median-of-medians/), groups of 5 give the recurrence $T(n) \le T(n/5) + T(7n/10) + O(n)$, up to rounding. Redo the counting argument for groups of 7 and for groups of 3. Show that groups of 7 still give linear time, and that for groups of 3 the same argument gives only the recurrence $T(n) \le T(n/3) + T(2n/3) + O(n)$, whose solution is $\Theta(n \log n)$.

19. ★ In the combine step of the divide-and-conquer closest-pair algorithm, $\delta$ is the smallest distance found in the two halves, and the strip holds the points within $\delta$ of the dividing line, sorted by $y$. Prove that each point of the strip needs to be compared only with the next 7 points in this order.

20. ★ [Toom-Cook multiplication](/toom-cook-multiplication/) with three parts splits each $n$-digit factor into three pieces of $n/3$ digits. Explain why five products of pieces of about $n/3$ digits, plus linear work, are enough to form the product, and solve the recurrence $T(n) = 5T(n/3) + \Theta(n)$. Compare the exponent with that of [Karatsuba multiplication](/karatsuba-multiplication/).

21. ★ Adapt the offline connectivity method of [divide and conquer on queries](/divide-and-conquer-on-queries/) to answer "is the graph bipartite now?" under edge insertions and deletions. Say what each union-find node stores, what ADD does, and what the undo record holds. Then run it on: 1 add 1-2, 2 add 2-3, 3 add 1-3, 4 bipartite?, 5 remove 1-2, 6 bipartite?.
