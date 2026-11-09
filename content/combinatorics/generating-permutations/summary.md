## What to remember

- **Counting.** There are $n!$ permutations of $n$ distinct items and $n!/(m_1! \cdots m_r!)$ of a multiset with multiplicities $m_1, \ldots, m_r$. A full listing is practical only for small $n$: $12!$ is about $4.8 \times 10^8$, and $21!$ no longer fits in 64 bits.
- **The lexicographic successor** finds the largest $i$ with $a_i < a_{i+1}$, exchanges $a_i$ with the smallest larger item to its right, and reverses the suffix after position $i$. One step takes $\Theta(n)$ time in the worst case, but over the whole list the first scan makes $e - 1 \approx 1.72$ tests per step and the program makes $\cosh 1 \approx 1.54$ exchanges per step. With the tests written as $\ge$ and $\le$, the same code lists a multiset without repeats.
- **The lexicographic rank** is the Lehmer code read in the factorial number system: $r = \sum_i c_i (n - i)!$, where $c_i$ counts the later items smaller than $a_i$. A [Fenwick tree](/fenwick-tree/) gives rank and unrank in $O(n \log n)$ time. Myrvold and Ruskey rank and unrank in $O(n)$ time in an order of their own.
- **Cycles** determine the shape of a permutation. There are $n!/\prod_k k^{m_k} m_k!$ permutations with $m_k$ cycles of length $k$, the order of a permutation is the lcm of its cycle lengths, and its sign is $(-1)^{n - c}$ for $c$ cycles.
- **The sign** is $(-1)^{\mathrm{inv}(\pi)}$, and every transposition flips it. So a list that moves by single exchanges alternates between even and odd permutations, and exactly $n!/2$ permutations are even for $n \ge 2$.
- **Minimal change** is possible: [Heap's algorithm](/heaps-algorithm/) makes one exchange per step, and the [Steinhaus-Johnson-Trotter algorithm](/steinhaus-johnson-trotter/) one exchange of neighbors, each $n! - 1$ exchanges in all. In the Steinhaus-Johnson-Trotter order the largest value makes $(n-1)/n$ of the moves, and the list ends at $2\,1\,3 \cdots n$, one adjacent exchange from the start.
- **Involutions** satisfy $t_n = t_{n-1} + (n-1)\,t_{n-2}$. Backtracking on the smallest free item lists them in lexicographic order with fewer than $3 t_n$ nodes, so in constant amortized time.

## The generators side by side

| Method | Order | Change per step | Amortized time per step | Worst step | Extra space |
|---|---|---|---|---|---|
| [Next permutation](/next-permutation/) | lexicographic | an exchange and a suffix reversal | $\Theta(1)$ | $\Theta(n)$ | $\Theta(1)$ |
| [Heap's algorithm](/heaps-algorithm/) | Heap's order | one exchange | $\Theta(1)$ | $\Theta(n)$ | $\Theta(n)$ |
| [Steinhaus-Johnson-Trotter](/steinhaus-johnson-trotter/) | plain changes | one exchange of neighbors | $\Theta(1)$ | $\Theta(n)$ | $\Theta(n)$ |
| [Unranking](/permutation-unranking/) each rank in turn | any order with an unrank function | the whole array | $O(n \log n)$ | $O(n \log n)$ | $\Theta(n)$ |
| [Involution backtracking](/generating-involutions/) | lexicographic, involutions only | varies | $\Theta(1)$ | $\Theta(n)$ | $\Theta(n)$ |

: Generators of permutations, with times in the visit model, where the visit itself is free. Ehrlich (1973) gave loopless forms of plain changes, whose worst step is $O(1)$; Knuth's Algorithm P lists plain changes with a counter and a direction for each value, and needs no array of positions.

## Choosing a method

- When you need sorted output, when the items can repeat, or when you must resume from a given permutation, use [next permutation](/next-permutation/). It needs no memory between calls, and it is the function `next_permutation` of the C++ library.
- When you only need every permutation once and the work per permutation can be updated after one exchange, use Heap's algorithm. Sedgewick's survey of 1977 found it the fastest of the simple methods.
- When only neighbors may change places, for example when the caller keeps an inversion count that moves by exactly one at each step, use the Steinhaus-Johnson-Trotter algorithm.
- When you need random access, use [ranking](/permutation-ranking/) and [unranking](/permutation-unranking/): to split the list among workers, to restart a long run, or to store a permutation as one integer.
- When only some permutations are wanted, generate them directly with a search that never builds the others, as the [involution generator](/generating-involutions/) does. Filtering all $n!$ permutations wastes almost all the work.
