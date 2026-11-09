1. At least $4! = 24$ leaves, so height at least $\lceil \lg 24 \rceil = 5$. Five comparisons suffice, so 5 is the least height.

2. (a) $N/B = 10^7$ transfers. (b) $N/M = 1000$ runs; since $M/B - 1 = 9999 \ge 1000$, one merge pass finishes the sort. (c) Binary search costs about $\lg(N/B) \approx 24$ transfers, since only the last few probes fall in one block; a B-tree costs about $\log_{100} 10^9 = 4.5$, so 5.

3. A line holds 8 items, so a sequential scan misses $2^{20}/8 = 131072$ times. In a random order almost every access misses, so close to $2^{20}$ misses.

4. $(\lambda x.\,x\,x)(\lambda y.\,y) \to (\lambda y.\,y)(\lambda y.\,y) \to \lambda y.\,y$. The term $(\lambda x.\,y)\,\Omega$ reduces to $y$ in one step, but reducing $\Omega$ first gives $\Omega$ again, forever. Normal-order reduction, leftmost outermost first, finds the normal form.

5. $11$, then $111$, then $1101$. The pattern grows to the left; the right end stays at the cell of the first 1.

6. At most $2^t$ paths. Trying them one at a time costs $O(t \cdot 2^t)$ steps.

7. (a) The error after $k$ runs is at most $2^{-k}$, and $2^{-30} \approx 9.3 \times 10^{-10}$, so $k = 30$. (b) The majority is wrong when at least two runs are wrong: $3 \cdot (1/3)^2 (2/3) + (1/3)^3 = 7/27$.

8. $n \le 2^{32}$. Without $w \ge \lg n$ a word could not hold an index into the input, and one could not even address all of it in constant time.

9. Unit cost: $\Theta(n)$. Logarithmic cost: each partial sum is at most $n^2$, so each addition costs $O(\log n)$ and the total is $O(n \log n)$.

10. $(a \wedge b) \vee (c \wedge (a \vee b))$: gates $a \wedge b$, $a \vee b$, $c \wedge (a \vee b)$ and the final OR. Depth 3.

12. (a) `1: JZ R1 5; 2: DEC R1; 3: INC R2; 4: JMP 1`. (b) Decrement $R_1$ twice for each increment of $R_2$, testing $R_1$ for zero before each decrement. Both take $\Theta(x)$ steps, while $x$ has only about $\lg x$ bits.

13. Move right turning each 1 into 0 until the first 0 or blank, and write 1 there. An input of $n$ ones takes $n + 1$ steps. With the most significant bit first, $11\cdots1$ becomes $100\cdots0$, one cell longer, and the result must be shifted or the carry written before the first cell.

15. Sort with [radix sort](/radix-sort/) in base $n$: each key has two digits, so two passes of counting sort, $O(n)$ in all, and then compare neighbours. The counting step uses a key's digit as an array index, which a decision tree cannot do.

18. At most $1 + k + k^2 + \cdots + k^t < k^{t+1}$ records are within $t$ steps of the start. For all $n$ to be within $t$ steps you need $k^{t+1} \ge n$. The pointer machine cannot compute an address.

19. Run formation is one pass. Two-way merging then needs $\lceil \lg 1000 \rceil = 10$ passes, 11 passes in all at $2 \times 10^7$ transfers each: $2.2 \times 10^8$. The multiway sort needs 2 passes, $4 \times 10^7$.

20. Sorting costs about $\frac{N}{B} \log_{M/B} \frac{N}{B}$, so it wins when $\log_{M/B}(N/B) < B$, up to constant factors. Here $\log_{10^4} 10^7 = 1.75$ and $B = 100$, so sorting wins by far.

21. Keep two nodes per variable, one for "even so far" and one for "odd so far"; reading $x_i = 1$ swaps them. That is $2n - 1$ inner nodes and two sinks. For the second part use the full decision tree of depth $n$.

22. With the head moving right in every step, the machine never reads a cell it has written. Its state after reading a prefix is all it knows, so it is a finite automaton; conversely any finite automaton is such a machine.

23. Induction on $t$: the rule is $x_{t+1}(i) = x_t(i-1) \oplus x_t(i+1)$, which is Pascal's rule mod 2. Row $2^k$ of Pascal's triangle mod 2 has only its two end entries odd, so exactly 2 cells are 1.

24. $\mathrm{MULT}\;c_m\;c_n \to \lambda f.\,c_m\,(c_n\,f)$, and $c_n\,f \to \lambda x.\,f^n\,x$, so $c_m$ applies the $n$-fold composition of $f$ $m$ times.

25. Given RP machines for $L$ and for its complement, run both in turn. An accepting run of either one is proof of the answer, and each round gives a proof with probability at least $1/2$, so the expected number of rounds is at most 2. For the converse, stop a ZPP machine after twice its expected time and use Markov's inequality.

26. For each length $k$ the language has either no string or exactly the string $1^k$. The circuit for length $k$ is the constant 0 or the AND of its inputs; which one it is, is a single bit of advice.
