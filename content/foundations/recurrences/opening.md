[Merge sort](/merge-sort/) sorts $n$ items by sorting two halves and merging them, and the merge costs about $n$ steps. If $T(n)$ is its running time, then $T(n) = 2T(n/2) + n$. The equation is easy to write down from the program and says nothing directly about how large $T(n)$ is. Unrolled, it says that each of the $\lg n$ levels of recursion costs $n$ in total, so $T(n) = \Theta(n \log n)$. [Binary search](/binary-search/) gives $T(n) = T(n/2) + 1$ and so $\Theta(\log n)$. The naive recursive program for the Fibonacci numbers gives $T(n) = T(n-1) + T(n-2) + 1$, whose solution grows like $\varphi^n$ with $\varphi \approx 1.618$, so the program is exponential.

Every recursive algorithm in the handbook is analyzed this way: write a recurrence, then solve it. This chapter collects the methods of solution. Some give an exact formula; most give the order of growth, which is what an analysis usually needs.

## What the chapter covers

The chapter is in six groups, read in order.

1. **Recursion and recurrences.** [Recursion](/recursion/), the [recurrence relation](/recurrence-relation/) that describes its cost, and what counts as a [closed-form solution](/closed-form-solution/).
2. **The divide-and-conquer form.** The [divide-and-conquer recurrence](/divide-and-conquer-recurrence/) $T(n) = aT(n/b) + f(n)$ and its [watershed function](/watershed-function/) $n^{\log_b a}$.
3. **Three ways to solve a recurrence.** The [iteration method](/iteration-method/), the [recursion-tree method](/recursion-tree-method/) and the [substitution method](/substitution-method/).
4. **Linear recurrences.** [Linear recurrences with constant coefficients](/linear-recurrences-with-constant-coefficients/), solved by the characteristic polynomial, and the Fibonacci numbers with [Binet's formula](/binet-formula/) and [Cassini's identity](/cassini-identity/).
5. **The master theorem.** The [master theorem](/master-theorem/) for divide-and-conquer recurrences, and the [change of variables](/change-of-variables/) that brings other recurrences into its form.
6. **Beyond the master theorem.** The [Akra-Bazzi theorem](/akra-bazzi-theorem/), Roura's [continuous master theorem](/continuous-master-theorem/) and the [smoothness rules](/smoothness-rules/) for floors and ceilings.

## A first reading

For a first reading, take these entries in order: [recursion](/recursion/), [recurrence relation](/recurrence-relation/), [divide-and-conquer recurrence](/divide-and-conquer-recurrence/), [watershed function](/watershed-function/), [iteration method](/iteration-method/), [recursion-tree method](/recursion-tree-method/), [substitution method](/substitution-method/), [master theorem](/master-theorem/) and [change of variables](/change-of-variables/). With these you can solve almost every recurrence that the later volumes write down. Read the linear recurrences when you meet the Fibonacci numbers or a recurrence that looks back a fixed number of steps. The last group is for recurrences that the master theorem does not cover: subproblems of unequal size, or a sum over all smaller sizes.

## Before you start

You need [asymptotic notation](/asymptotic-notation/), [logarithms](/logarithms/) and the [geometric series](/geometric-series/) from Chapter 1.2, and [mathematical induction](/induction/) from Chapter 1.4, which every proof in this chapter uses. The Akra-Bazzi theorem uses [integral bounds for sums](/integral-bounds-for-sums/). The entries on linear recurrences assume the [Fibonacci numbers](/fibonacci-numbers/) and some algebra from Volumes 11 and 12, such as [partial fractions](/partial-fraction-decomposition/). The continuous master theorem takes its main example from [the expected running time of quicksort](/quicksort-expected-running-time/) in Chapter 1.6; you can read the theorem first and the example later.
