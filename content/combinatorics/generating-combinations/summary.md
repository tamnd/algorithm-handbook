## What to remember

- **Counting.** An $n$-set has $2^n$ subsets and $\binom{n}{k}$ subsets of size $k$; a $k$-subset is the same thing as a bit string of length $n$ with $k$ ones. Choosing $k$ items from $n$ kinds with repetition allowed gives $\binom{n+k-1}{k}$ multisets, and the shift $b_i \mapsto b_i + i - 1$ turns them into $k$-subsets of $[n+k-1]$.
- **The cost model.** A generator is charged for the work between two visits, not for the visit. It is CAT when the total work is $O(1)$ per object, and loopless when every step is $O(1)$. The [binary counter](/power-set-by-recursion/) is CAT but not loopless: its $2^n - 1$ increments write $2^{n+1} - n - 2$ bits, yet the step from $0111\cdots1$ to $1000\cdots0$ writes all $n$.
- **The lexicographic successor** of $a_1 < \cdots < a_k$ finds the rightmost $a_i$ below its ceiling $n - k + i$, adds 1 to it, and resets the entries after it to $a_i + 1, a_i + 2, \ldots$. Its amortized cost is $\Theta(n/(n-k+1))$, which is $O(1)$ for $k \le n/2$ but grows to $\Theta(n)$ when $k$ is close to $n$.
- **Colex order** compares subsets by their largest elements. Its list for $[n]$ is a prefix of the list for $[n+1]$, and the first $m$ sets of it have the smallest shadow among all families of $m$ $k$-sets, which is the Kruskal-Katona theorem.
- **The colex rank** of $c_k > \cdots > c_1 \ge 0$ is $\binom{c_k}{k} + \cdots + \binom{c_1}{1}$, and every integer has exactly one such form: the [combinatorial number system](/combinatorial-number-system/). Unranking is greedy: take the largest $c_k$ with $\binom{c_k}{k}$ at most the rank, subtract, and go on with $k-1$. Lexicographic rank follows by the reflection $a \mapsto n + 1 - a$.
- **The revolving door order** takes one element out and puts one in at each step. It is the binary reflected Gray code restricted to strings of weight $k$, it satisfies $R(n,k) = R(n-1,k)$ followed by the reverse of $R(n-1,k-1)$ with $n-1$ added, and [Ehrlich's loopless combination generation](/ehrlich-loopless-combinations/) lists it with $O(1)$ work per step.
- **Cool-lex order** rotates the shortest prefix that ends in $010$ or $011$ one place to the right, or the whole string if there is none. It starts at $1^k 0^{n-k}$, is cyclic, changes two or four bits per step, and needs only two indices of state.

## The generators side by side

| Method | Objects | Order | Change per step | Amortized time per step | Worst step | Extra space |
|---|---|---|---|---|---|---|
| [Binary counter](/power-set-by-recursion/) | all subsets | binary counting | a run of trailing ones and one zero | $\Theta(1)$ | $\Theta(n)$ | $\Theta(1)$ |
| [Take-or-skip recursion](/recursive-combination-generation/) | $k$-subsets | lexicographic | varies | $\Theta(n/(n-k+1))$ | $\Theta(n)$ | $\Theta(n)$ |
| [Lexicographic successor](/lexicographic-combinations/) | $k$-subsets | lexicographic | a suffix of the array | $\Theta(n/(n-k+1))$ | $\Theta(k)$ | $\Theta(1)$ |
| [Unranking](/combinatorial-ranking-and-unranking/) each rank in turn | $k$-subsets | colex, lex or others | the whole array | $O(n)$ | $O(n)$ | $O(nk)$ for a table |
| [Ehrlich's loopless generation](/ehrlich-loopless-combinations/) | $k$-subsets | revolving door | one element out, one in | $\Theta(1)$ | $O(1)$ | $\Theta(1)$ |
| [Cool-lex](/cool-lex-order/) | $k$-subsets as bit strings | cool-lex | two or four bits | $\Theta(1)$ | $O(1)$ | $\Theta(1)$ |

: Generators of subsets and combinations, with times in the visit model, where the visit itself is free. The times for unranking assume a table of binomial coefficients, or binomials updated by one multiplication and one division per step, and count arithmetic on them as $O(1)$. On a word RAM with $n \le 64$, [Gosper's hack](/gospers-hack/) gives the colex successor of a fixed-weight word in a constant number of word operations.

## Choosing a method

- When you need every subset of a small set and the work per subset is the main cost, run a binary counter over the integers $0$ to $2^n - 1$. Use [submask enumeration](/submask-enumeration/) when the subsets must lie inside a given mask.
- When you need the $k$-subsets in sorted order, or must resume from a given subset, use the [lexicographic successor](/lexicographic-combinations/). It keeps no state between calls.
- When $n$ fits in a machine word, store the subset as a word and step it in colex order with [Gosper's hack](/gospers-hack/), or in cool-lex order with a few shifts and masks.
- When you need random access, to split the list among workers, to restart a long run, or to store a $k$-subset as one integer, use colex order with the [combinatorial number system](/combinatorial-number-system/).
- When the caller keeps a value computed from the subset, such as a sum of weights, and can update it after one element leaves and one enters, use the revolving door order with [Ehrlich's loopless generation](/ehrlich-loopless-combinations/).
- When the caller needs a hard bound on the time between two subsets, as in a real-time loop, use a loopless generator. Otherwise the CAT methods are simpler and as fast in total.
