1. (a) Proved: a machine that runs for $t$ steps visits at most $t$ cells. (b) Proved, by the time hierarchy theorem. (c) Open. (d) Proved: $\mathsf{L} \subseteq \mathsf{DSPACE}(\log n) \subsetneq \mathsf{DSPACE}(n) \subseteq \mathsf{PSPACE}$ by the space hierarchy theorem. (e) Proved, by the Immerman-Szelepcsényi theorem. (f) Open. (g) Proved: try all certificates, in time $2^{p(n)} q(n)$. (h) False, by the space hierarchy theorem.

2. (a) Ten runs, since $2^{-10} = 1/1024$. (b) The error is $\sum_{j > k/2} \binom{k}{j} 3^{-j} (2/3)^{k-j}$. The smallest odd $k$ with error at most $1/10$ is $15$, with error about $0.088$. For $1/100$ it is $47$, with error about $0.0090$. Exact rational arithmetic in a short program gives these values.

3. (a) $2^{20} = 1{,}048{,}576$ bits. (b) The length bound halves at each level, from $2^{20}$ to $1$, so there are about 20 levels, and each frame takes $4 \cdot 20 = 80$ bits. The total is about $1600$ bits. (c) The current vertex and a step counter, $40$ bits.

4. (a) Yes, since $n \log n = o(n^2)$. (b) No: $f \log f = 2 n^2 \log n$, which is not $o(n^2 \log n)$. (c) Yes, since $2 n^2 \log n = o(n^2 \log^2 n)$. (d) No: $f \log f = n 2^n$, which is not $o(n 2^n)$. (e) Yes, since $n = o(n \log n)$. (f) Yes, since $\log n = o(\log^2 n)$ and $\log^2 n \ge \log n$.

5. (a) $\exists$ a set $S$ of $k$ vertices such that all pairs in $S$ are edges: $\Sigma_1^p = \mathsf{NP}$. (b) $\forall$ sets $S$ of $k$ vertices, some pair is not an edge: $\Pi_1^p = \mathsf{coNP}$. (c) $\exists$ a circuit $D$ with at most $s$ gates $\forall$ inputs $x$, $C(x) = D(x)$: $\Sigma_2^p$. (d) $\forall$ colorings, some edge has equal colors: $\Pi_1^p$. For graphs with at least three vertices this says that $G$ is not 3-colorable.

6. P, L, PSPACE, BPP and ZPP: swap the answers of the machine, which keeps the bounds and the error. NL: by the Immerman-Szelepcsényi theorem. NP and RP: open. NP is closed under complement if and only if $\mathsf{NP} = \mathsf{coNP}$, and RP if and only if $\mathsf{RP} = \mathsf{coRP}$.

7. (a) Every integer $N \ge 2$ has a prime factorization, and primality is checked in polynomial time. (b) Every move strictly increases the cut weight, and there are finitely many cuts, so a cut of maximum weight is locally optimal. (c) Nash's theorem: every finite game has a mixed equilibrium. For two players there is one with rational probabilities of polynomial size. (d) The pigeonhole principle: $2^n$ inputs map to $2^{n-1}$ outputs.

8. Solve $(1 - 1/160)^k \le 1/2$: $k = 111$ runs. For $1/100$: $k = 735$ runs.

13. (a) With $h_4 = 0$, $h_0 = 1 + h_1$ and $h_i = 1 + (h_{i-1} + h_{i+1})/2$ for $i = 1, 2, 3$, the solution is $h = (16, 15, 12, 7, 0)$. (b) The bound is $2 \cdot 4 \cdot 4 = 32$, twice the true value. (c) If $T \ge h_0$, then $\Pr[\text{not reached in } 2T \text{ steps}] \le h_0 / 2T \le 1/2$. A logspace machine stores only the current vertex and a step counter up to $2T$, which is polynomial in $n$, so it accepts with probability at least $1/2$ when $t$ is reachable and never otherwise.

14. (a) Moving vertex 2 gains 9, giving cut weight 9. Then moving vertex 5 gains 7, giving 16. No move helps after that. The cut $\{2, 5\}$ against $\{1, 3, 4\}$ has weight 16, which is the maximum. (b) There are four local optima, two cuts counted from both sides: $\{2, 5\}$ with weight 16, and $\{2, 3\}$ against $\{1, 4, 5\}$ with weight 14. The second is a local optimum and not a maximum cut.

15. (a) $0 \to 3$, $3 \to 5$ and $6 \to 2$. Vertex 1 has $S(1) = 4$ but $P(4) = 4$, so there is no edge. (b) The other ends are the sink $5$, the source $6$ and the sink $2$. The walk from $0$ reaches $5$. (c) PPAD asks for any other end, and the parity argument shows that one exists. Finding one may still take exponential time when the graph has $2^n$ vertices.

16. (a) $H = 34$, and $34 \equiv 6 \pmod 7$. (b) Over the integers $g_1(X) = 8X + 13$, so $g_1(X) = X + 6$ modulo 7, and $g_1(0) + g_1(1) = 13 \equiv 6$. Then $g_1(3) = 2$, $g_2(X) = 6X + 5$ with $g_2(0) + g_2(1) = 16 \equiv 2$, and $g_2(5) = 0$. Then $g_3(X) = 5X + 1$ with $g_3(0) + g_3(1) = 7 \equiv 0$. Finally $g_3(2) = 11 \equiv 4$, and the verifier checks $g(3, 5, 2) = 46 \equiv 4$. Every check passes.

19. Take $B \in \mathsf{DSPACE}(n^2) \setminus \mathsf{DSPACE}(n)$, from the space hierarchy theorem, and $B' = \{x 0^{|x|^2 - |x|} : x \in B\}$. Then $B' \in \mathsf{DSPACE}(n)$ and $B \le_m^p B'$. P and NP are closed under Karp reductions. So if either equals $\mathsf{DSPACE}(n)$, then $B \in \mathsf{DSPACE}(n)$, which is false. The argument shows only that the classes have different closure properties, so it does not give a problem in one class and not in the other.

20. There are at most $2^{O(n^k \log n)}$ circuits of size $n^k$ and $2^{2^m}$ functions of $m = c \log n$ variables. For a constant $c > k$ the second number is larger, so some function of the first $m$ bits has no such circuit. "The first such function in lexicographic order of truth tables" has a $\Sigma_4^p$ definition. If SAT has no polynomial-size circuits, SAT itself works. If it has them, then $\mathsf{PH} = \Sigma_2^p = \Pi_2^p$ by Karp-Lipton, so the $\Sigma_4^p$ language is in $\Sigma_2^p \cap \Pi_2^p$.

21. Map $\varphi$ to $\psi$ by the reduction and ask the oracle whether $\psi$ has an odd number of solutions. If $\varphi$ is unsatisfiable, $\psi$ has 0 solutions and the machine never accepts. If $\varphi$ is satisfiable, $\psi$ has exactly one, an odd number, with probability at least $1/(8n)$. Repeat $8n$ times to reach probability at least $1 - e^{-1} > 1/2$.

22. Amplify the BPP algorithm for SAT to error below $2^{-2n}$. Fix $x_1, x_2, \ldots$ one at a time, keeping the value for which the algorithm says that the rest is satisfiable. By the union bound, all $n$ answers are right with high probability, and then the result satisfies $\varphi$. Accept only if it does. An unsatisfiable formula is never accepted, so SAT is in RP, and RP is closed under Karp reductions.
