1. ◦ The [Cantor pairing function](/godel-numbering/) is $\pi(x, y) = \tfrac{1}{2}(x + y)(x + y + 1) + y$. (a) Compute $\pi(4, 6)$. (b) Find the pair $(x, y)$ with $\pi(x, y) = 57$. (c) Find the pair with $\pi(x, y) = 100$.

2. ◦ A finite sequence $(a_1, \ldots, a_k)$ of positive integers has the prime-power code $2^{a_1} 3^{a_2} 5^{a_3} \cdots p_k^{a_k}$. (a) Compute the code of $(2, 1, 3)$. (b) For each of $4500$, $1050$ and $350$, say whether it is a code, and if so decode it.

3. ◦ In the notation of the [busy beaver function](/busy-beaver-function/) entry, run the two-state machine `1RB0LB_1LA1RZ` on a blank tape. How many steps does it make before it halts, and how many ones does it leave? Compare with $S(2)$ and $\Sigma(2)$.

4. ◦ For each set of machine codes, say whether it is decidable, c.e. but not decidable, co-c.e. but not c.e., or neither. (a) Machines with at most $5$ states. (b) Machines that halt on the empty word. (c) Machines $M$ with $L(M) = \emptyset$. (d) Machines that halt on the empty word within $1000$ steps. (e) Machines that halt on every input.

5. ◦ For each property, say whether [Rice's theorem](/rice-theorem/) shows it undecidable; if it does not apply, say why and whether the property is decidable. (a) $L(M)$ contains the word $ab$. (b) $M$ has an even number of states. (c) $L(M)$ is regular. (d) $L(M) = \Sigma^*$. (e) $M$, started on the empty word, halts within $100$ steps.

6. ◦ Find the shortest match of the [Post correspondence](/post-correspondence-problem/) instance with dominoes $1 = (a / baa)$, $2 = (ab / aa)$ and $3 = (bba / bb)$, written top over bottom, and show that the match must start with domino $3$.

7. ◦ The presentation $\langle a, b \mid a^2, b^2, (ab)^3 \rangle$ defines the symmetric group $S_3$, with $a = (1\,2)$ and $b = (2\,3)$. Solve the [word problem](/word-problem-for-groups/) for the words $abba$, $abab$, $babbab$, $bab$ and $ababab$: which of them equal the identity? For those that do not, give a shortest word for the same element.

8. ◦ Prove that if a language $L$ and its complement are both c.e., then $L$ is decidable. Deduce that the complement of the halting set $K$ is not c.e.

9. ◦ Define $h$ by $h(x, 0) = x$ and $h(x, y + 1) = h(x, y) + 2y + 1$. (a) Compute $h(3, 4)$. (b) Find a closed form for $h$ and prove it by induction on $y$. (c) Explain why $h$ is [primitive recursive](/primitive-recursive-function/).

10. • Write each set with as few alternating quantifiers in front of a decidable relation as you can, and give its level in the [arithmetical hierarchy](/arithmetical-hierarchy/). Use $W_{e,s}$, the finite set of inputs below $s$ on which program $e$ halts within $s$ steps, and $\varphi_{e,s}(x)$, the output of program $e$ on $x$ if it halts within $s$ steps. (a) $\{ e : W_e \ne \emptyset \}$. (b) $\{ e : \varphi_e(0) \text{ is undefined} \}$. (c) $\{ e : W_e \text{ has at least three elements} \}$. (d) $\{ e : \varphi_e(x) = 0 \text{ for every } x \}$. (e) $\{ e : W_e = \emptyset \}$.

11. • Give a [many-one reduction](/many-one-reducibility/) from the halting problem to $\mathrm{TOT} = \{ \langle M \rangle : M \text{ halts on every input} \}$. Deduce that the complement of $\mathrm{TOT}$ is not c.e.

12. • Show that $\overline{K} \le_T K$ but $\overline{K} \not\le_m K$. Which property of c.e. sets does a Turing reduction fail to preserve?

13. • Use the counting argument for [Kolmogorov complexity](/kolmogorov-complexity/). How many binary strings of length $30$ can have $C(x) < 22$ at most? Show that more than $255/256$ of the strings of length $30$ have $C(x) \ge 22$.

14. • Show that $\sqrt{3}$ is a [computable real](/computable-real-numbers/): with $a_n = \lfloor \sqrt{3 \cdot 4^n} \rfloor$, computed with integers only, prove $|a_n / 2^n - \sqrt{3}| \le 2^{-n}$. Compute $a_5 / 2^5$ and $a_{10} / 2^{10}$.

15. • Prove that $\Sigma(n + 1) \ge \Sigma(n) + 1$ for every $n \ge 1$, by changing a machine that leaves $\Sigma(n)$ ones.

16. • Using $S(2) = 6$, decide whether the two-state machine `1RB1LB_0LA1RZ` halts on a blank tape. Explain why the same method cannot be used today for every machine with six states.

17. • A prefix machine halts on exactly the programs $1$, $01$, $0010$ and $00110$. (a) Check that this set is prefix-free and compute its halting probability $\Omega$ in binary. (b) You are told only the first three bits of $\Omega$ and you run all programs in parallel. After which programs have halted can you stop, and why does no other program of length at most $3$ halt?

18. • Use the [s-m-n theorem](/s-m-n-theorem/) to build a total computable $f$ with $W_{f(e)} = W_e \cup \{0\}$ for every $e$.

19. • Over the natural numbers, give an existential formula with one polynomial equation for each relation: (a) $x \le y$; (b) $x$ divides $y$; (c) $x$ is composite; (d) $x \ne y$. These are the first steps of the Diophantine definitions behind [Hilbert's tenth problem](/hilberts-tenth-problem/).

20. • Wang tiles are written $(n, e, s, w)$; a tile placed above another must have its south color equal to the north color of the one below, and a tile to the right must have its west color equal to the east color of its left neighbor. (a) Show that $T_1 = \{(0, 0, 1, 0), (1, 0, 0, 0)\}$ tiles the plane. (b) For $T_2 = \{(0, 0, 1, 0), (1, 0, 2, 0), (2, 1, 0, 0)\}$, find the largest $n$ such that $T_2$ tiles the $n \times n$ square, and conclude that $T_2$ does not tile the plane.

21. ★ The FRACTRAN program $\tfrac{455}{33}, \tfrac{11}{13}, \tfrac{1}{11}, \tfrac{3}{7}, \tfrac{11}{2}, \tfrac{1}{3}$ of the [Turing completeness](/turing-completeness/) entry multiplies: started on $2^a 3^b$, it stops at $5^{ab}$. Find the exact number of steps as a function of $a$ and $b$, and check it on $36 = 2^2 \cdot 3^2$.

22. ★ Over a one-letter alphabet, take the dominoes $(aaa / a)$ and $(a / aaaa)$. Find the length of the shortest match and the number of copies of each domino in it, and state a rule that decides every unary instance.

23. ★ Show that $\overline{K} \le_m \mathrm{TOT}$. With exercise 11, conclude that neither $\mathrm{TOT}$ nor its complement is c.e.

24. ★ Use [Kleene's recursion theorem](/kleene-recursion-theorem/) to show that there is a program $n$ with $W_n = \{0, 1, \ldots, n\}$.

25. ★ Show that $\mathrm{FIN} = \{ e : W_e \text{ finite} \}$ is computable from $\emptyset''$, both from its quantifier form with [Post's theorem](/posts-theorem/) and by a direct oracle algorithm.
