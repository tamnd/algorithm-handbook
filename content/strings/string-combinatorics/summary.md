## What to remember

- A **border** of $w$ is a proper prefix that is also a suffix, and $p$ is a **period** when $w[i] = w[i + p]$ wherever both exist. A border of length $b$ is the same as the period $|w| - b$, so the prefix function gives all periods in linear time.
- **Fine and Wilf**: a word with periods $p$ and $q$ and length at least $p + q - \gcd(p, q)$ also has the period $\gcd(p, q)$, and the bound is tight. The uniqueness of the primitive root rests on it.
- Every word is a power of exactly one **primitive** word. Two words are **conjugate** when one is a rotation of the other, and $v$ is a rotation of $u$ exactly when $|u| = |v|$ and $v$ occurs in $uu$.
- A **Lyndon word** is strictly smaller than all its proper rotations. Every word factors in exactly one way into Lyndon words that do not increase, and **Duval's algorithm** finds this factorization in linear time and constant extra space. The least rotation and the least suffix come out of the same scan.
- **Necklaces** and Lyndon words are counted by sums over divisors, $\sum_{d \mid n} d\,L_k(d) = k^n$, and listed in lexicographic order in constant amortized time. Joining the Lyndon words whose length divides $n$, in lexicographic order, gives a **de Bruijn sequence**.
- A de Bruijn sequence of order $n$ is an Eulerian circuit in the de Bruijn graph on the words of length $n - 1$. Superstrings in general are NP-hard, and greedy merging is the standard approximation.
- A string of length $n$ has fewer than $n$ **runs** and fewer than $n$ distinct squares, although it can have $\Theta(n^2)$ square occurrences. Runs are found in linear time from Lyndon arrays.
- Repetitions can be avoided: squares over three letters, overlaps over two (the **Thue-Morse word**), and Abelian squares over four. Infinite words like these are built by iterating a **morphism**.
- An infinite word with at most $n$ factors of some length $n$ is eventually periodic. **Sturmian words** have exactly $n + 1$, and they are the balanced aperiodic words.

## The main algorithms side by side

| Problem | Method | Time | Extra space | Notes |
|---|---|---|---|---|
| All periods | [prefix function](/periodicity-detection/) | $\Theta(n)$ | $\Theta(n)$ | border chain |
| Rotation test | [search in $uu$](/word-conjugacy-testing/) | $\Theta(n)$ | $\Theta(n)$ | any linear matcher |
| Least rotation | [Booth](/booth-algorithm/) | $\Theta(n)$ | $\Theta(n)$ | failure function on $ss$ |
| Least rotation | [Shiloach](/shiloach-least-rotation/) | $O(n)$ | $O(1)$ | fewer than $3n$ comparisons |
| Lyndon factorization | [Duval](/duval-algorithm/) | $\Theta(n)$ | $O(1)$ | also least suffix |
| Lyndon array | [next smaller suffix](/lyndon-array/) | $O(n)$ | $\Theta(n)$ | after a suffix array |
| All necklaces | [FKM](/fkm-algorithm/) | $O(1)$ amortized each | $\Theta(n)$ | lexicographic order |
| de Bruijn sequence | FKM, Lyndon words joined | $\Theta(k^n)$ | $\Theta(n)$ | also by an Eulerian circuit |
| Short superstring | [greedy merge](/greedy-superstring-merge/) | $O(mN + m^2 \log m)$ | $O(N + m^2)$ | at most 4 times optimal |
| All squares | [Main-Lorentz](/main-lorentz-algorithm/) | $O(n \log n)$ | $\Theta(n)$ | output in groups |
| All runs | [Lyndon roots](/lyndon-based-runs-computation/) | $O(n)$ | $\Theta(n)$ | two letter orders |
| Minimal absent words | [suffix automaton](/minimal-absent-words-algorithm/) | $O(n + \sigma + z)$ | $O(n)$ | $z$ words reported |

: Algorithms on a word of length $n$ over $k$ or $\sigma$ letters, and for superstrings on $m$ strings of total length $N$. The Lyndon array time assumes an integer alphabet; the minimal absent words time is expected, with hash maps.

## Choosing a method

- For the periods of a single word, compute the prefix function. For a quick test of whether a word is a power, search for it in its own square with the first and last letters removed.
- For a canonical name of a rotation class, take the least rotation. Booth's algorithm is the simplest to get right; Duval's algorithm on $ss$ or Shiloach's algorithm use constant space.
- To list necklaces, Lyndon words or a de Bruijn sequence, use FKM or its recursive form; never filter all $k^n$ words.
- For all squares of a moderate string, Main-Lorentz is short and fast. For runs, distinct squares or any linear-time bound, compute the runs from the Lyndon arrays.
- For a short superstring, merge greedily. For assembly from many short reads, a de Bruijn graph of $k$-mers is the usual alternative.
- To describe which words occur in a text, list its minimal absent words with the suffix automaton.
