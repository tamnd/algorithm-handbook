1. ◦ Write a [precondition](/precondition/) and a [postcondition](/postcondition/) for integer division, which returns $q$ and $r$ for inputs $a$ and $b$. Show that the postcondition $a = qb + r$ alone accepts a wrong answer for every input.

2. ◦ Which of these [Hoare triples](/hoare-triple/) are valid? (a) $\{x = 5\}\ x \leftarrow x + 1\ \{x = 6\}$. (b) $\{\mathit{true}\}\ \mathbf{while}\ \mathit{true}\ \mathbf{do}\ \mathbf{skip}\ \{x = 1\}$. (c) $\{x > 0\}\ x \leftarrow x - 1\ \{x > 0\}$. (d) $\{\mathit{false}\}\ S\ \{Q\}$ for any $S$ and $Q$. (e) The total-correctness triple $[x \ge 0]\ \mathbf{while}\ x > 0\ \mathbf{do}\ x \leftarrow x - 1\ [x = 0]$, over the integers.

3. ◦ Compute the [weakest preconditions](/weakest-precondition/) (a) $\mathrm{wp}(x \leftarrow x + 1,\ x > 5)$, (b) $\mathrm{wp}(x \leftarrow 2x;\ y \leftarrow y + x,\ y = 10)$ and (c) $\mathrm{wp}(\mathbf{if}\ x < 0\ \mathbf{then}\ x \leftarrow -x\ \mathbf{else}\ \mathbf{skip},\ x \ge 1)$, over the integers.

4. ◦ The loop `m ← A[0]; for i ← 1 to n−1: if A[i] > m then m ← A[i]` finds the largest item of $A[0 \ldots n-1]$, $n \ge 1$. State a [loop invariant](/loop-invariant/) that holds before the test for each $i$, and check its three parts.

5. ◦ Euclid's algorithm `while b ≠ 0: (a, b) ← (b, a mod b)` runs on integers $a, b \ge 0$. Give a [variant function](/variant-function/) and show that it decreases in each pass and stays in $\mathbb N$.

6. ◦ Which of these relations are [well-founded](/well-founded-relation/)? (a) $<$ on $\mathbb N$. (b) $<$ on $\mathbb Z$. (c) Proper inclusion on the finite subsets of $\mathbb N$. (d) The dictionary order on all finite strings over $\{a, b\}$, where $u$ is below $v$ if $u$ comes first in a dictionary. (e) "Is a proper suffix of" on finite strings. For each one that is not, give an infinite descending chain.

7. ◦ The [representation invariant](/representation-invariant/) of a binary min-heap stored in $A[0 \ldots n-1]$ is $A[\lfloor (i-1)/2 \rfloor] \le A[i]$ for $1 \le i < n$. Which of the arrays $[2, 5, 3, 9, 6, 4]$ and $[2, 5, 3, 4, 6, 1]$ satisfy it? For a violation, name the index.

8. ◦ The loop `while n ≠ 1: if n is even then n ← n/2 else n ← 3n + 1` runs on an integer $n \ge 1$. Is it [partially correct](/partial-correctness/) for the postcondition $n = 1$? Is it [totally correct](/total-correctness/)?

9. ◦ A set of integers is stored as a list. In representation A any list is allowed; in representation B the list must be strictly increasing. Give the [abstraction function](/abstraction-function/) and the representation invariant of each, and say whether the list $[3, 1, 3]$ is a valid representation in each, and of which set.

10. ◦ In [separation logic](/separation-logic/), $e \mapsto f$ says that the heap is the single cell $e$, holding $f$. Decide: (a) does $x \mapsto 1 * y \mapsto 2$ imply $x \ne y$? (b) Is $x \mapsto 1 * x \mapsto 1$ satisfiable? (c) Does $x \mapsto 1 \wedge y \mapsto 1$ imply $x = y$?

11. • In a sorted array $A[0 \ldots n-1]$, the loop `lo ← 0; hi ← n; while lo < hi: mid ← ⌊(lo + hi)/2⌋; if A[mid] ≤ x then lo ← mid + 1 else hi ← mid` returns `lo`. State the postcondition, an invariant and a variant, and prove the loop correct. What goes wrong if $mid$ is computed as $\lceil (lo + hi)/2 \rceil$?

12. • In Euclid's algorithm of Exercise 5, show that $a \bmod b < a/2$ whenever $0 < b \le a$. Deduce that two passes of the loop at least halve the first component, so that the loop makes $O(\log a)$ passes when $a \ge b$.

13. • The [Dutch national flag](/dutch-national-flag/) problem rearranges an array of items coloured red, white and blue so that all red items come first, then white, then blue, with one pass and constant extra space. Give the invariant of the usual three-index algorithm in terms of four regions of the array, and a variant that shows the loop stops after at most $n$ passes.

14. • Use the assignment rule $\mathrm{wp}(x \leftarrow E, Q) = Q[E/x]$ to prove $\{x = a \wedge y = b\}\ x \leftarrow x + y;\ y \leftarrow x - y;\ x \leftarrow x - y\ \{x = b \wedge y = a\}$ over the integers. Is the triple still valid when the arithmetic wraps around modulo $2^w$? When an overflow stops the program with an error?

15. • The loop `r ← 1; b ← B; e ← E; while e > 0: (if e is odd then r ← r · b); b ← b · b; e ← ⌊e/2⌋` computes $B^E$ for an integer $E \ge 0$. Find an invariant that links $r$, $b$ and $e$, prove it, and bound the number of passes.

16. • In Dijkstra's [guarded command language](/guarded-commands/), the loop $\mathbf{do}\ q_1 > q_2 \to q_1, q_2 := q_2, q_1 \mathbin{[\,]} q_2 > q_3 \to q_2, q_3 := q_3, q_2 \mathbin{[\,]} q_3 > q_4 \to q_3, q_4 := q_4, q_3\ \mathbf{od}$ chooses any guard that is true in each pass. Prove that it stops for every choice and that it leaves $q_1 \le q_2 \le q_3 \le q_4$. What is the largest number of passes it can make?

17. • Prove by [structural induction](/structural-induction/) that a binary tree of height $h$ has at most $2^{h+1} - 1$ nodes, where the empty tree has height $-1$ and a single node height 0.

18. • Use the [well-ordering principle](/well-ordering-principle/), in the form of a least counterexample, to prove that every integer $n \ge 12$ is a sum of 4s and 5s. Which cases does the argument have to check directly?

19. • A [certifying](/certifying-algorithms/) gcd algorithm returns $g$ together with integers $s$ and $t$. What should the checker test so that it accepts only $g = \gcd(a, b)$, and why is that enough? Which algorithm produces $s$ and $t$?

20. • A [property-based test](/property-based-testing/) of a function `rev` on lists checks that `rev(rev(L)) = L` for random lists $L$. Give a wrong function that passes. Add the property `rev(A ++ B) = rev(B) ++ rev(A)` and give a wrong function that passes both properties. What third property makes the three together determine `rev`?

21. • A program sorts three numbers with three compare-and-swap steps: `if x > y then swap(x, y); if y > z then swap(y, z); if x > y then swap(x, y)`. In [symbolic execution](/symbolic-execution/) on symbolic inputs, how many of the $2^3$ combinations of test outcomes give a satisfiable path condition? Name the impossible ones.

22. • An algorithm for maximum matching in a bipartite graph returns a matching $M$ and a set $C$ of vertices with $|C| = |M|$. Explain why this pair proves that $M$ is a maximum matching when every edge has an end in $C$, and say what the checker must test and how long it takes. The existence of such a $C$ is [König's theorem](/konig-theorem/).

23. ★ The Boyer-Moore [majority vote](/boyer-moore-majority/) algorithm keeps a candidate $c$ and a counter $k$: for each item $x$, if $k = 0$ it sets $c \leftarrow x$ and $k \leftarrow 1$, else if $x = c$ it sets $k \leftarrow k + 1$, else $k \leftarrow k - 1$. State an invariant about the items read so far that implies: if some value occurs in more than half of the items, it is $c$ at the end. Prove the invariant.

24. ★ McCarthy's 91 function is $M(n) = n - 10$ for $n > 100$ and $M(n) = M(M(n + 11))$ for $n \le 100$, on the integers. Prove that $M$ terminates on every input and that $M(n) = 91$ for every $n \le 101$.

25. ★ A bag holds finitely many natural numbers. In each step you remove one number $k > 0$ and put in any finite number of numbers smaller than $k$, as many as you like. Prove that the process stops whatever choices are made, and show that no bound on the number of steps depends only on the starting bag.

26. ★ For deterministic programs, $\mathrm{wp}(S, Q_1 \vee Q_2) = \mathrm{wp}(S, Q_1) \vee \mathrm{wp}(S, Q_2)$. Give a guarded command $S$ and postconditions $Q_1$ and $Q_2$ for which the left side is $\mathit{true}$ and the right side is $\mathit{false}$, and explain what the difference means for a program.

27. ★ The loop `y ← nil; while x ≠ nil: t ← x.next; x.next ← y; y ← x; x ← t` reverses a singly linked list in place. Using the predicate $\mathrm{list}(x, \alpha)$, "$x$ points to a list holding the sequence $\alpha$ and the heap is exactly that list", write the loop invariant in separation logic in terms of the initial sequence $\alpha_0$, and show that it gives $\mathrm{list}(y, \mathrm{rev}(\alpha_0))$ at the end.
