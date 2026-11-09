1. ◦ A rod sells in pieces of length 1 to 8 at the prices $p = (2, 5, 8, 9, 11, 14, 16, 18)$. Use the bottom-up table of [rod cutting](/rod-cutting-problem/) to find the best revenues $r_1, \ldots, r_8$, the first piece $s_j$ chosen for each length (take the shortest piece when there is a tie), and a best way to cut a rod of length 8. Is that best way unique?

2. ◦ The coins are $D = \{1, 5, 6, 9\}$. Find the least number of coins $f(t)$ for $t = 11, 12, 13$, and the number of coins the greedy rule (largest coin first) uses for the same amounts. What is the smallest amount for which greedy is not optimal? Check that it lies in the range that the [coin change](/coin-change-problem/) entry gives for the smallest counterexample.

3. ◦ A building has 50 floors. With two eggs, what is the least number of drops that finds the highest safe floor in the worst case? Which floors can the first drop use without losing that bound? How many drops are needed with three eggs? Use the counting form of [egg dropping](/egg-dropping-problem/).

4. ◦ In a grid of 5 rows and 5 columns, a path starts at the cell $(1, 1)$, moves only right or down, and ends at $(5, 5)$. The cells $(2, 2)$, $(3, 4)$ and $(4, 2)$ are blocked, where $(i, j)$ is row $i$ and column $j$. Fill the table of [grid paths with obstacles](/grid-paths-with-obstacles/) and give the number of paths. How many are there without obstacles?

5. ◦ Five matrices have the dimensions $p = (4, 10, 3, 12, 20, 7)$. Fill the table $m[i, j]$ of [matrix-chain multiplication](/matrix-chain-multiplication/), give the least number of scalar products and an optimal parenthesization, and compare with the cost of multiplying from left to right.

6. ◦ A product of 7 matrices is to be computed. How many [parenthesizations](/parenthesization/) does it have? How many subproblems $(i, j)$ with $i \le j$ does the bottom-up program of [matrix-chain multiplication](/matrix-chain-multiplication/) fill? How many calls does the plain recursion without a table make?

7. ◦ Count the ways to split the string `catsanddogs` into words from the dictionary $\{$`a`, `an`, `and`, `cat`, `cats`, `sand`, `dog`, `dogs`, `s`, `do`, `gs`$\}$, with the counting table of [text segmentation](/text-segmentation/): $N(j)$ is the number of splittings of the first $j$ letters. Give $N(0), \ldots, N(11)$ and list the splittings.

8. ◦ A tree has the edges 1-2, 1-3, 1-4, 2-5, 2-6, 3-7, 4-8 and 4-9, and the vertex weights $w = (6, 5, 2, 4, 3, 4, 3, 2, 1)$ for vertices 1 to 9. Root it at 1 and use [tree DP](/tree-dynamic-programming/) with two values per vertex, the best weight of an independent set of the subtree with the vertex in and with it out, to find a maximum-weight independent set.

9. ◦ Items have the (weight, value) pairs $(2, 3)$, $(3, 5)$, $(4, 7)$, $(5, 8)$, and the capacity is 9. Fill the table $K(0), \ldots, K(9)$ of the [unbounded knapsack](/unbounded-knapsack/), and the one-row table of the 0/1 knapsack on the same items. At which capacity do the two rows first differ, and why?

10. ◦ Let $n = 3$ and $f = (3, 1, 4, 1, 5, 9, 2, 6)$ for the masks $000, 001, \ldots, 111$. Compute $F(S) = \sum_{T \subseteq S} f(T)$ for all $S$ by the method of [sum over subsets DP](/sum-over-subsets-dp/), one bit at a time, and show the table after each pass. Then compute the sums over supersets, $G(S) = \sum_{T \supseteq S} f(T)$.

11. • With the prices of exercise 1, the saw may make at most $k$ cuts. Write a recurrence with the state (length left, pieces still allowed), and find the best revenue for a rod of length 8 with $k = 0, 1, 2, 3$. Why does the table of exercise 1 not give these values?

12. • Find the contiguous block of $(2, -3, -2, 4, -1, 3)$ with the largest product. A student keeps, for each position $i$, only the largest product of a block that ends at $i$. Show that this gives a wrong answer on this array, say which part of [optimal substructure](/optimal-substructure/) fails, and repair the method with two values per position.

13. • Five keys $k_1 < \cdots < k_5$ are searched with the frequencies $(5, 4, 1, 3, 2)$, and no search fails. The cost of a tree is the sum of the frequency times the depth of each key, with the root at depth 1. Find an [optimal binary search tree](/optimal-binary-search-tree/) and its cost. What does the rule "put the most frequent key at the root, then repeat in each subtree" cost?

14. • Four workers and four jobs have the cost matrix with rows $(8, 4, 7, 6)$, $(5, 2, 3, 9)$, $(4, 6, 8, 5)$ and $(7, 3, 9, 8)$, one row per worker. Solve the assignment problem by [bitmask DP](/bitmask-dp/), where $f(S)$ is the least cost of giving the jobs in $S$ to the first $|S|$ workers. How many states are there, and how many terms does the program evaluate? Compare with giving each worker in turn the cheapest free job.

15. • Five cities have the symmetric distances $d(1,2) = 3$, $d(1,3) = 4$, $d(1,4) = 2$, $d(1,5) = 7$, $d(2,3) = 4$, $d(2,4) = 6$, $d(2,5) = 3$, $d(3,4) = 5$, $d(3,5) = 8$, $d(4,5) = 6$. Run the [Held-Karp algorithm](/held-karp-algorithm/) from city 1. How many pairs $(S, v)$ does its table hold? Give the values $C(\{2, 3, 4, 5\}, v)$ for each last city $v$, the shortest tour, and the tour that the nearest-neighbour rule builds from city 1.

16. • Set the sentence `to be or not to be that is the question` on lines of $M = 12$ characters by the rules of [printing neatly](/printing-neatly/): the cost is the sum of the cubes of the extra spaces at the ends of all lines but the last. Give the optimal layout and its cost, and the cost of the layout that fills each line as far as it can.

17. • The vertices of a convex hexagon carry the labels 3, 7, 4, 5, 1, 6 in order around it. The weight of a triangle is the product of the labels of its corners. Find a triangulation of least total weight with the program of [optimal polygon triangulation](/optimal-polygon-triangulation/), and say how many triangulations there are in all.

18. • Count the integers from 1 to 5000 whose decimal digits never decrease from left to right, such as 1129 and 4, but not 5000 or 1210. Design a [digit DP](/digit-dynamic-programming/) for it with the state (position, last digit, tight), and check the answer by a direct count of multisets of digits.

19. • Use [broken-profile DP](/broken-profile-dp/) with $m = 3$ rows to count the domino tilings of a $3 \times n$ board for $n = 2, 4, 6, 8$. Why is the count 0 for odd $n$? Check that your values satisfy $T(n) = 4T(n - 2) - T(n - 4)$.

20. • In a [convex hull trick](/convex-hull-trick/) for a minimum, the lines $y = 2x$, $y = x + 2$, $y = 5$, $y = -x + 6$ and $y = -2x + 11$ arrive in this order, by decreasing slope. Which lines stay on the lower envelope and on which ranges of $x$? Which lines does the deque drop, and when? Give the minimum at $x = 0, 1, \ldots, 6$.

21. • Make the sequence $(5, 1, 4, 2, 3)$ nondecreasing by changing its terms, at the least total cost $\sum |a_i - b_i|$. Run the heap form of the [slope trick](/slope-trick/) and give the state of the heap and the cost after each term. Give one optimal sequence $b$, and show that it is not unique.

22. • Over four months the demands are $(40, 60, 30, 70)$. Each month with production pays a set-up cost of 80, and each unit held at the end of a month costs 1. Use the Wagner-Whitin recurrence from [inventory planning](/inventory-planning/) to find the cheapest plan: its cost, the months with production and the amounts.

23. • Test the matrices with rows $(3, 5, 8, 12)$, $(4, 4, 6, 9)$, $(7, 5, 5, 7)$, $(11, 8, 6, 6)$ and with rows $(3, 5, 8, 12)$, $(4, 4, 6, 9)$, $(7, 6, 5, 7)$, $(11, 6, 7, 6)$ for the [Monge property](/monge-property/) with the adjacent $2 \times 2$ test. Give the column of the leftmost minimum of each row in both, and say what this shows about [totally monotone](/row-minima-of-totally-monotone-matrices/) matrices.

24. ★ Show from the counting form of [egg dropping](/egg-dropping-problem/) that with $e \ge d$ eggs and $d$ drops, $2^d - 1$ floors can be handled, and that no number of eggs does better. Deduce that 100 floors need 7 drops however many eggs there are, and find the least number of eggs for which 7 drops suffice.

25. ★ A dominating set of a graph contains, for each vertex, the vertex or one of its neighbours. For the weighted tree of exercise 8, find a dominating set of least weight by [tree DP](/tree-dynamic-programming/). Two states per vertex are not enough; give three states, their recurrences, and the table at each vertex.

26. ★ Six points have the symmetric distances given by the rows $(0, 4, 7, 3, 8, 6)$, $(4, 0, 5, 9, 2, 7)$, $(7, 5, 0, 6, 4, 9)$, $(3, 9, 6, 0, 8, 5)$, $(8, 2, 4, 8, 0, 6)$, $(6, 7, 9, 5, 6, 0)$. Find a perfect matching (three disjoint pairs) of least total distance by [bitmask DP](/bitmask-dp/) over the set of matched points, in $O(n 2^n)$ time and not $O(n^2 2^n)$. How many perfect matchings are there, and what does the rule "take the cheapest pair left" give?

27. ★ A row of balloons has the values $(2, 4, 3, 5)$. Bursting a balloon earns the product of its value and the values of its current left and right neighbours, where a missing neighbour counts as 1, and the neighbours close up after each burst. Find the largest total over all orders. Splitting at the first balloon burst does not give independent parts; show that splitting at the last one does, and write the [interval DP](/interval-dp/).

28. ★ An array $a_1, \ldots, a_n$ of positive numbers is cut into contiguous groups; a group with sum $s$ costs $s^2 + C$. With prefix sums $S_j$, write $E(j) = \min_{i < j} \bigl( E(i) + (S_j - S_i)^2 + C \bigr)$ as a minimum of lines in $x = S_j$, as in the [convex hull trick](/convex-hull-trick/), and show that the slopes and the queries come in sorted order. Then solve the instance $a = (3, 1, 4, 1, 5)$, $C = 10$.

29. ★ The greedy rule fills each line with as many words as fit. Prove that it uses the fewest lines of any layout with lines of width at most $M$. Then use exercise 16 to explain where the same argument breaks for the cost of [printing neatly](/printing-neatly/).
