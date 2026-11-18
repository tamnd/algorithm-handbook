## What to remember

- A parameterized problem is fixed-parameter tractable (FPT) if it has an algorithm with time $f(k) \cdot n^{c}$, for a computable $f$ and a constant $c$. Time $f(k) + n^{c}$ gives the same class. The class XP allows time $f(k) \cdot n^{g(k)}$, and $\mathsf{FPT} \subsetneq \mathsf{XP}$ is a theorem.
- A bounded search tree that branches into subproblems with parameters $k - d_1, \ldots, k - d_r$ has $O(\lambda^k)$ leaves, where $\lambda$ is the largest root of $x^{d} = \sum_i x^{d - d_i}$ with $d = \max_i d_i$. The vector $(1,1)$ gives 2, and $(1,2)$ gives the golden ratio $1.618$.
- Vertex cover is the model FPT problem: edge branching takes $O(2^k (n+m))$ time, the best known bound is $O(1.2738^k + kn)$ (Chen, Kanj and Xia), the Buss kernel has at most $k^2$ edges and $k^2 + k$ vertices, and the crown and LP kernels have $3k$ and $2k$ vertices.
- A decidable problem is FPT if and only if it has a kernel. Whether it has a polynomial kernel is a finer question: $k$-path has none unless $\mathsf{NP} \subseteq \mathsf{coNP/poly}$, and vertex cover has no kernel of $O(k^{2-\varepsilon})$ bits under the same assumption.
- Hardness is relative. $\mathsf{FPT} \subseteq \mathsf{W}[1] \subseteq \mathsf{W}[2] \subseteq \cdots \subseteq \mathsf{XP}$, clique and independent set are $\mathsf{W}[1]$-complete, and dominating set is $\mathsf{W}[2]$-complete. A $\mathsf{W}[1]$-hard problem has no FPT algorithm unless $\mathsf{FPT} = \mathsf{W}[1]$; that is open, and $\mathsf{FPT} \ne \mathsf{W}[1]$ would imply $\mathsf{P} \ne \mathsf{NP}$.
- Under the Exponential Time Hypothesis, clique has no $f(k) \cdot n^{o(k)}$ algorithm and vertex cover has no $2^{o(k)} n^{O(1)}$ algorithm. A para-NP-hard problem, such as coloring with $q$ colors, is not in XP unless $\mathsf{P} = \mathsf{NP}$.
- Color coding: a random coloring with $k$ colors makes a fixed $k$-set colorful with probability $k!/k^k > e^{-k}$, so $e^{k}$ trials of an $O(2^k m)$ dynamic program find a $k$-path in randomized time $O((2e)^k (n+m))$.
- A graph has at most $4^k$ important $(X, Y)$-separators of size at most $k$. This bound drives the FPT algorithms for several cut problems.
- Courcelle's theorem decides a fixed property $\varphi$ of monadic second-order logic on graphs of treewidth $t$ in time $f(\lVert \varphi \rVert, t) \cdot n$, but $f$ is not elementary unless $\mathsf{P} = \mathsf{NP}$. Bidimensionality gives time $2^{O(\sqrt{k})} n^{O(1)}$ for problems such as vertex cover on planar graphs.

## Problems and their status

| Problem | Parameter | Bound in the entries | Kernel | Status |
|---|---|---|---|---|
| Vertex cover | cover size $k$ | $O(1.2738^k + kn)$ | $2k$ vertices | FPT |
| Feedback vertex set | $k$ | $3.460^k n^{O(1)}$; randomized $2.7^k n^{O(1)}$ | $4k^2$ vertices | FPT |
| Cluster editing | edits $k$ | $O(1.62^k + n + m)$ | $2k$ vertices | FPT |
| $d$-hitting set | $k$, fixed $d$ | $O(d^k \cdot d\,\lvert \mathcal{F} \rvert)$ | $O(d!\,k^d)$ sets | FPT |
| $k$-path | path length $k$ | randomized $O^*(2^k)$ | none unless $\mathsf{NP} \subseteq \mathsf{coNP/poly}$ | FPT |
| Edge clique cover | cliques $k$ | $2^{2^{O(k)}} + n^{O(1)}$ | $2^k$ vertices | FPT |
| Clique | clique size $k$ | $O(n^{\omega k/3})$ | none unless $\mathsf{FPT} = \mathsf{W}[1]$ | $\mathsf{W}[1]$-complete |
| Dominating set | $k$ | $n^{k + o(1)}$ for $k \ge 7$ | none unless $\mathsf{FPT} = \mathsf{W}[2]$ | $\mathsf{W}[2]$-complete |
| Coloring | colors $q$ | NP-complete for $q = 3$ | none unless $\mathsf{P} = \mathsf{NP}$ | para-NP-hard |

: Running examples of the chapter with the bounds their entries give. $O^*$ hides factors polynomial in the input size, and $\omega < 2.372$ is the matrix multiplication exponent.

## Using the chapter

To show that a problem is FPT, try these tools in order. Branch on a small set of local choices, one of which every solution makes, and compute the branching number. Look for safe reduction rules that bound the instance once none applies. If the solution is a small connected or path-like object, try color coding. If the solution is a deletion set for a hereditary property, try iterative compression; if it is a cut, try important separators. If the input has small treewidth, write a dynamic program over a tree decomposition, or express the property in monadic second-order logic and use Courcelle's theorem for a first, very slow, algorithm.

To argue that no FPT algorithm exists, give a parameterized reduction from multicolored clique, clique or dominating set, and check that the new parameter is bounded by a function of the old one alone. For kernels, give an OR-cross-composition or a polynomial parameter transformation from a problem with no polynomial kernel. Each of these results is conditional on its own assumption, and the statement should name it.
