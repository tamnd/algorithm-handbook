The entries of the set share one notation. This chapter collects it in one place. Each item links to the entry that explains it in full.

## Growth of functions

The cost of an algorithm is a function of the size of its input, written $n$ unless the entry says otherwise. The entries compare such functions with [asymptotic notation](/asymptotic-notation/):

| Notation | Read as | Means, for all large $n$ and some constant $c > 0$ |
|---|---|---|
| $f(n) = O(g(n))$ | $f$ grows at most as fast as $g$ | $f(n) \le c\, g(n)$ |
| $f(n) = \Omega(g(n))$ | $f$ grows at least as fast as $g$ | $f(n) \ge c\, g(n)$ |
| $f(n) = \Theta(g(n))$ | $f$ and $g$ grow at the same rate | both $O(g(n))$ and $\Omega(g(n))$ |
| $f(n) = o(g(n))$ | $f$ grows more slowly than $g$ | $f(n) / g(n) \to 0$ |
| $f(n) = \omega(g(n))$ | $f$ grows faster than $g$ | $f(n) / g(n) \to \infty$ |
| $f(n) \sim g(n)$ | $f$ is asymptotic to $g$ | $f(n) / g(n) \to 1$ |

: Asymptotic notation.

$O$ gives an upper bound and $\Omega$ a lower bound; neither says the bound is tight. When an entry says an algorithm runs in $O(n \log n)$ time, the claim is an upper bound, and the entry says whether it is tight. The [tilde notation](/tilde-notation/) $f \sim g$ keeps the constant factor, and is used when constants matter, as in counts of comparisons. Bounds in several variables, such as $O(n + m)$ for a graph with $n$ vertices and $m$ edges, follow [multivariate asymptotic notation](/multivariate-asymptotic-notation/).

The [common growth rates](/common-growth-rates/), from slowest to fastest, are constant $O(1)$, [iterated logarithm](/iterated-logarithm/) $O(\log^* n)$, logarithmic $O(\log n)$, polylogarithmic $O(\log^k n)$, [sublinear](/sublinear-time/) $O(n^c)$ with $c < 1$, linear $O(n)$, [linearithmic](/linearithmic-time/) $O(n \log n)$, quadratic $O(n^2)$, cubic $O(n^3)$, [polynomial](/polynomial-time/) $n^{O(1)}$, and exponential $2^{O(n)}$ and beyond.

## Logarithms, floors and sums

- $\lg n$ is the logarithm to base 2, $\ln n$ the natural logarithm, and $\log_b n$ the logarithm to base $b$. Inside $O$, $\Theta$ and $\Omega$, the base changes only a constant factor, and the entries write $\log n$. See [logarithms](/logarithms/).
- $\log^k n$ means $(\log n)^k$, and $\log^* n$ is the [iterated logarithm](/iterated-logarithm/): the number of times $\lg$ must be applied to $n$ to reach a value at most 1.
- $\lfloor x \rfloor$ is the largest integer at most $x$, and $\lceil x \rceil$ the smallest integer at least $x$.
- $H_n = 1 + \frac12 + \cdots + \frac1n$ is the $n$-th harmonic number, and $H_n = \ln n + O(1)$; see the [harmonic series](/harmonic-series/).
- $n! \sim \sqrt{2\pi n}\,(n/e)^n$ by [Stirling's approximation](/stirling-approximation/), so $\lg n! = n \lg n - n \lg e + O(\log n)$.
- $\binom{n}{k}$ is the number of subsets of size $k$ of a set of size $n$.
- $[n]$ is the set $\{1, 2, \ldots, n\}$, and $|S|$ is the size of a set $S$.
- $a \bmod m$ is the remainder of $a$ on division by $m$, in the range $0$ to $m - 1$, and $a \equiv b \pmod m$ says that $m$ divides $a - b$.

## Arrays, sequences and strings

- $A[i]$ is the item at index $i$ of an array $A$. $A[i..j]$ is the subarray from index $i$ to index $j$, both included, and $A[i..j)$ leaves out index $j$. An empty range such as $A[i..i)$ has no items.
- Arrays in pseudocode start at index 0 in some entries and at 1 in others, as their sources do. The first lines of each block show which: a loop `for i ← 1 to n` reads $A[1..n]$, and a loop `for i ← 0 to n − 1` reads $A[0..n-1]$. The Python code always starts at 0.
- $\langle a_1, a_2, \ldots, a_n \rangle$ is a sequence, and $|A|$ or $n$ its length.
- A string is a sequence of characters over an alphabet $\Sigma$ of size $\sigma$. A text $T$ has length $n$ and a pattern $P$ has length $m$. $T[i..j]$ is a substring, $\varepsilon$ the empty string, and $uv$ the concatenation of the strings $u$ and $v$.

## Graphs

A graph is $G = (V, E)$, with $n = |V|$ vertices and $m = |E|$ edges. An edge is $(u, v)$ in a [directed graph](/directed-graph/) and $\{u, v\}$ in an [undirected graph](/undirected-graph/), and $w(u, v)$ is its weight in a [weighted graph](/weighted-graph/). $\deg(v)$ is the [degree](/degree/) of $v$, $N(v)$ its set of neighbours, $\delta(u, v)$ the distance from $u$ to $v$, and $\operatorname{Adj}[u]$ the adjacency list of $u$. A path is a sequence of vertices joined by edges.

## Pseudocode

Every algorithm has pseudocode in a numbered block, so that the text, the proofs and the code can point to its lines. Each line starts with a label `L1`, `L2`, …; the Python code under the entry marks with a comment `# @line L4` the line of the pseudocode it carries out. The vocabulary is small:

| Form | Meaning |
|---|---|
| `x ← e` | assign the value of `e` to `x` |
| `if … then … else` | a choice |
| `while … do`, `repeat … until` | a loop that tests before or after each round |
| `for i ← a to b do` | a loop with `i = a, a + 1, …, b`; `downto` counts down |
| `for each x in S do` | a loop over the items of a set or a list |
| `return e` | end the procedure with the value `e` |
| `PROCEDURE(a, b)` | a call; names of procedures are in small capitals |
| `▷ text` | a comment |
| `nil` | the empty pointer, also written `NIL` |
| `∞` | a value larger than every other |

: The words and signs of the pseudocode.

Indentation shows which lines belong to a loop or a branch. A line may say in words what it does, such as "extract the vertex $u$ with the least $d[u]$ from $Q$", when the entry names the data structure that does it; the cost of such a line is given in the analysis.

## Models of computation and costs

A bound on time counts the steps of a model of computation, and the facts box of each entry names the model. Most entries use the [random-access machine](/random-access-machine/) in its [word RAM](/word-ram/) form: a memory of words of $w \ge \lg n$ bits, any one of which can be read or written in one step, and arithmetic, comparison and bit operations on words in one step each. Other models count other things: the [comparison model](/comparison-model/) counts only comparisons between keys, the [external-memory model](/external-memory-model/) counts transfers of blocks between a fast memory and a disk, and the [decision tree model](/decision-tree-model/) is used to prove lower bounds.

The facts box gives each cost with its case:

- **worst**: the most the algorithm takes on any input of size $n$;
- **average**: the mean over a stated distribution of inputs, usually all orders of distinct keys equally likely;
- **expected**: the mean over the random choices of a [randomized algorithm](/randomized-algorithm/), on the worst input;
- **amortized**: the [amortized cost](/amortized-cost/) of an operation, the total cost of any sequence of operations divided by their number;
- **best**: the least it takes on any input of size $n$;
- **extra** space: the memory used besides the input.

## Probability

$\Pr[A]$ is the probability of an event $A$, $\operatorname{E}[X]$ the [expected value](/expected-value/) of a random variable $X$, and $\operatorname{Var}[X]$ its [variance](/variance/). An event happens *with high probability* when it fails with probability at most $n^{-c}$, for a constant $c > 0$ that the entry states (often $c \ge 1$). See [high-probability bounds](/high-probability-bounds/).
