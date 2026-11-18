1. ◦ Alice holds $x \in \{0, 1, 2, 3\}$, Bob holds $y \in \{0, 1, 2, 3\}$, and $f(x, y) = 1$ when $x + y \ge 3$. (a) Write the $4 \times 4$ [communication matrix](/communication-matrix/) $M_f$. (b) Compute the real rank of $M_f$ and of $J - M_f$, and the bound that the refined [log-rank lower bound](/log-rank-lower-bound/) gives. (c) Give a protocol that meets it, and state $D^{cc}(f)$.

2. ◦ Run the [equality testing protocol](/equality-testing-protocol/) with $n = 6$, $x = 110100$ and $y = 110001$, using $A_s(z) = s_1 + s_2 z + \cdots + s_6 z^5$. (a) Find $q$ and the number of bits sent. (b) Alice draws $r = 5$. Compute $a$ and $b$ and the output. (c) For which $r$ does the protocol err on this pair, and what is its error? Compare with the bound $(n - 1)/q$.

3. ◦ The same protocol is used for strings of $n = 10^6$ bits. Without finding $q$ exactly, show that every element of $\mathbb{F}_q$ takes 40 bits, give the total number of bits sent, and bound the error. Use that $2^{40} = 1\,099\,511\,627\,776$ and that there is a prime between $10^{12}$ and $2^{40}$.

4. ◦ Let $f(x) = 1$ when at least two of the four bits $x_1, \ldots, x_4$ are 1. Find $\mathrm{s}(f)$, $\mathrm{bs}(f)$, $C_0(f)$, $C_1(f)$, $C(f)$, $D^{dt}(f)$ and $\deg(f)$, and check the bounds $C(f) \le \mathrm{s}(f)\, \mathrm{bs}(f)$ and $D^{dt}(f) \le C_0(f)\, C_1(f)$. For the degree, find the coefficient of $x_1 x_2 x_3 x_4$ in the multilinear polynomial of $f$.

5. ◦ The [index problem](/index-problem/) has $n = 1000$. Give the deterministic cost of a one-way protocol from Alice to Bob, of a one-way protocol from Bob to Alice, and of a two-way protocol. Then compute the lower bound $(1 - H_2(\delta))\, n$ for one-way randomized protocols from Alice with error $\delta = 0.1$ and with $\delta = 1/3$, rounded up to whole bits.

6. ◦ For $\mathrm{OR}_3$, a symmetric polynomial is a polynomial $q(k)$ in the weight $k = |x|$. (a) Find a linear $q(k) = a + bk$ with $|q(k) - \mathrm{OR}_3(k)| \le 1/3$ for $k = 0, 1, 2, 3$. (b) Show that no linear $q$ has error below $1/3$. What does this say about the [approximate degree](/approximate-degree/) of $\mathrm{OR}_3$ with $\varepsilon = 1/3$ and with $\varepsilon = 0.3$?

7. ◦ True or false, with a one-line reason. (a) $D^{cc}(\mathrm{EQ}_n) = n + 1$. (b) Equality has a fooling set of size $2^n$, so its public-coin randomized cost is at least $n$. (c) The [log-rank conjecture](/log-rank-conjecture/) has been proved for all Boolean functions. (d) Every total Boolean function has $D^{dt}(f) \le \mathrm{bs}(f)^3$. (e) $Q(\mathrm{OR}_n) = \Theta(\sqrt n)$. (f) The [sign rank](/sign-rank/) of a sign matrix is at least the rank of its 0-1 version minus one.

8. ◦ Four players each hold one 16-bit input. Give the cost of the trivial protocol in the [number-in-hand model](/number-in-hand-model/) and in the [number-on-forehead model](/number-on-forehead-model/), when the last bit written must be the value of an arbitrary function $f(x_1, x_2, x_3, x_4)$. Explain the difference in one sentence.

9. ◦ For $\mathrm{OR}_{400}$: (a) what integer lower bound on $\widetilde{\deg}(\mathrm{OR}_{400})$ does $\sqrt{n/6}$ give? (b) What degree does the Chebyshev construction $d = \lceil \sqrt{2(n - 1)} \rceil$ use? (c) What lower bound on $Q(\mathrm{OR}_{400})$ follows from the [polynomial method](/polynomial-method/)?

10. • Give a public-coin protocol for equality in which Alice sends $k$ random parities of $x$ and Bob answers with one bit. Show that it never errs when $x = y$ and errs with probability exactly $2^{-k}$ when $x \ne y$. How many bits does it need for error at most $10^{-6}$, and how does this compare with exercise 3?

11. • Show that the [greater-than problem](/greater-than-problem/) has a public-coin randomized protocol with $O(\log n \cdot \log \log n)$ bits. Use binary search for the first position where $x$ and $y$ differ, with a public-coin equality test on each prefix.

12. • Khrapchenko's bound says that a formula that is 1 on a set $A$ and 0 on a set $B$ has at least $|E|^2 / (|A||B|)$ leaves, where $E$ is the set of pairs in $A \times B$ at Hamming distance 1. For $\mathrm{MAJ}_n$ with $n$ odd, take $A$ and $B$ to be the inputs of weight $(n + 1)/2$ and $(n - 1)/2$. Compute the bound, and compare it for $n = 3$ with the formula $(x_1 \wedge x_2) \vee (x_3 \wedge (x_1 \vee x_2))$ on the [Karchmer-Wigderson relation](/karchmer-wigderson-relation/) page.

13. • In the trivial protocol for AND, Alice sends $x$ and Bob replies with $x \wedge y$. Let $X$ and $Y$ be independent, with $\Pr[X = 1] = p$ and $\Pr[Y = 1] = q$. (a) Show that the internal [information cost](/information-complexity/) is $H_2(p) + p\, H_2(q)$. (b) Compute it for $p = 1/4$, $q = 1/2$, and compare with the protocol in which Bob speaks first.

14. • Show that under the uniform distribution the greater-than function on $n$ bits has discrepancy at least $1/4$, by naming one rectangle. For $n = 2$, find a rectangle with discrepancy $7/16$. Why does the [discrepancy method](/discrepancy-method/) with the uniform distribution give only $O(1)$ for greater-than?

15. • Huang's theorem says that every induced subgraph of the cube $Q^n$ on more than $2^{n-1}$ vertices has a vertex of degree at least $\sqrt n$. (a) Prove the case $n = 3$ directly: every set of 5 vertices of $Q^3$ induces a vertex of degree at least 2. (b) Check that the 9 vertices $0000$, $0001$, $0010$, $0101$, $0110$, $1011$, $1100$, $1101$, $1110$ of $Q^4$ induce a subgraph of largest degree 2, so the bound is tight for $n = 4$.

16. • Prove that every symmetric Boolean function $f$ on $n$ bits that is not constant has $D^{dt}(f) = n$. Describe the adversary.

17. • Show that $Q_E(\mathrm{PARITY}_n) = \lceil n/2 \rceil$. For the lower bound use $\deg(f) \le 2 Q_E(f)$; for the upper bound, use that one quantum query computes $x_i \oplus x_j$ with certainty.

18. • Paturi's theorem gives $\widetilde{\deg}(f) = \Theta(\sqrt{n(n - \Gamma(f))})$ with $\Gamma(f) = \min\{|2k - n + 1| : f(k) \ne f(k + 1)\}$. For $n = 100$, compute $\Gamma$ and $\sqrt{n(n - \Gamma)}$ for: (a) $f = 1$ when $|x| \ge 10$; (b) $f = 1$ when $|x| \ge 50$; (c) $f = 1$ when $|x| = 0$.

19. • Prove that the [randomized query complexity](/randomized-query-complexity/) of $\mathrm{OR}_n$ with error $1/3$ is at least $n/3$. Put weight $1/2$ on $0^n$ and $1/(2n)$ on each unit vector $e_i$, and apply [Yao's minimax principle](/yao-minimax-principle/). Then give a one-sided algorithm with $\lceil 2n/3 \rceil$ queries.

20. • In the [simultaneous message model](/simultaneous-message-model/) with private coins, give a protocol for equality with $O(\sqrt n)$ bits. Encode $x$ and $y$ with an error-correcting code of length $m = O(n)$ and relative distance $\delta$, written as a $\sqrt m \times \sqrt m$ grid. Alice sends a random row of her codeword and Bob a random column of his.

21. ★ A private-coin protocol computes $f$ with error at most $1/3$ and sends $c$ bits. Show that $D^{cc}(f) \le 2^c (c + 3) + 1$, and conclude that the private-coin cost is $\Omega(\log D^{cc}(f))$. Use that, for each leaf $\ell$, the probability of reaching $\ell$ on $(x, y)$ is a product $p_A(x, \ell)\, p_B(y, \ell)$.

22. ★ Prove Newman's theorem: if $f$ on $n$-bit inputs has a public-coin protocol with error $\varepsilon$ and $c$ bits, then it has a private-coin protocol with error $\varepsilon + \delta$ and $c + O(\log n + \log(1/\delta))$ bits.

23. ★ Prove that $D^{cc}(f) = O(N^0(f)\, N^1(f))$, the bound of Aho, Ullman and Yannakakis. Start from a cover of the 0-entries by $2^{N^0}$ rectangles and of the 1-entries by $2^{N^1}$ rectangles, and use that a 0-rectangle and a 1-rectangle share no rows or share no columns.

24. ★ Let $f(x, y) = 1$ when $x, y \in \{0,1\}^n$ are at Hamming distance at most 1. Show that $D^{cc}(f) = n + 1$ for every $n \ge 2$. Use that $M_f = I + A$, where $A$ is the adjacency matrix of $Q^n$, whose eigenvalues are $n - 2j$ with multiplicity $\binom{n}{j}$, and apply the refined log-rank bound.

25. ★ Prove Nisan's bound $C(f) \le \mathrm{s}(f)\, \mathrm{bs}(f)$ for every total Boolean function $f$.
