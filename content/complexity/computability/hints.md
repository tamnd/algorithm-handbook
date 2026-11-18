1. (a) $\pi(4, 6) = \tfrac{1}{2} \cdot 10 \cdot 11 + 6 = 61$. (b) Find the largest $d$ with $\tfrac{1}{2} d(d + 1) \le 57$; it is $d = 10$, with $55$. Then $y = 57 - 55 = 2$ and $x = d - y = 8$, so the pair is $(8, 2)$. (c) $d = 13$ gives $91$, so $y = 9$, $x = 4$, and $\pi(4, 9) = 100$.

2. (a) $2^2 \cdot 3 \cdot 5^3 = 1500$. (b) $4500 = 2^2 \cdot 3^2 \cdot 5^3$ codes $(2, 2, 3)$. $1050 = 2 \cdot 3 \cdot 5^2 \cdot 7$ codes $(1, 1, 2, 1)$. $350 = 2 \cdot 5^2 \cdot 7$ is not a code: the prime $3$ is missing, and the entries must be positive, so the primes of a code have no gap.

3. The run is A0, B0, A1, B0, A0, B1. In step $6$ the machine reads $1$ in state $B$ and halts. It makes $6$ steps and leaves $3$ ones, on the tape $1101$. So it ties $S(2) = 6$ but does not reach $\Sigma(2) = 4$.

4. (a) Decidable: read the code. (b) c.e. but not decidable: simulate, and the halting problem on the empty word reduces to it. (c) Co-c.e. but not c.e.: its complement, "some word is accepted", is c.e. by dovetailing, and the set is undecidable by Rice's theorem. (d) Decidable: simulate for $1000$ steps. (e) Neither; see exercises 11 and 23.

6. A match must start with a domino whose top and bottom agree as far as the shorter one goes. Domino $1$ starts with $a$ over $b$ and domino $2$ with $ab$ over $aa$, so only domino $3$ can start. The shortest match is $3, 2, 3, 1$, of length $4$: both rows read $bbaabbbaa$. A search over all sequences of length at most $5$ finds no other match.

7. $abba$, $babbab$ and $ababab$ equal the identity. $abab$ is the 3-cycle that $ba$ also gives, so its shortest word is $ba$. $bab$ is the transposition $(1\,3)$; it equals $aba$, and no word of length at most $2$ gives it, since those give only $1$, $a$, $b$, $ab$ and $ba$.

10. (a) $\exists x\, \exists s\, [x \in W_{e,s}]$, so $\Sigma_1$. (b) $\forall s\, [0 \notin W_{e,s}]$, so $\Pi_1$. (c) Three distinct witnesses and one stage, so $\Sigma_1$. (d) $\forall x\, \exists s\, [\varphi_{e,s}(x) = 0]$, so $\Pi_2$. (e) $\forall x\, \forall s\, [x \notin W_{e,s}]$, which is one block of universal quantifiers, so $\Pi_1$.

13. There are $2^{22} - 1 = 4{,}194{,}303$ programs shorter than $22$ bits, and each prints at most one string. So at most $4{,}194{,}303$ of the $2^{30}$ strings have $C(x) < 22$, a fraction below $2^{22} / 2^{30} = 1/256$.

16. Any two-state machine that halts on the blank tape does so within $S(2) = 6$ steps. After $6$ steps this machine is in state $A$ with two ones on the tape, so it never halts. For six states the method needs $S(6)$, which is not known; it is not even known which six-state machines halt.

17. (a) No program is a prefix of another. $\Omega = \tfrac{1}{2} + \tfrac{1}{4} + \tfrac{1}{16} + \tfrac{1}{32} = \tfrac{27}{32} = 0.11011_2$. (b) The first three bits give $\tfrac{3}{4} \le \Omega < \tfrac{7}{8}$. Once $1$ and $01$ have halted, the sum found is $\tfrac{3}{4}$. A further halting program of length at most $3$ would add at least $\tfrac{1}{8}$, making $\Omega \ge \tfrac{7}{8}$, which is impossible.

20. (a) A column alternating the two tiles fits, since each tile's north color is the other's south color, and all east and west colors are $0$, so equal columns fit side by side. (b) Every column of height $3$ contains the third tile, and its east color $1$ matches no west color, so it can only sit in the last column. So $n = 2$ is the largest, with both columns $(1, 0, 2, 0)$ below $(0, 0, 1, 0)$. A tiling of the plane would tile the $3 \times 3$ square.

21. Count the steps of one round of the outer loop. The fraction $\tfrac{11}{2}$ takes one $2$. Then each $3$ is moved to a $7$ while a $5$ is added, at two steps per $3$ ($\tfrac{455}{33}$, then $\tfrac{11}{13}$). Then $\tfrac{1}{11}$ ends the inner loop, and $\tfrac{3}{7}$ moves the $b$ sevens back, one step each. That gives $3b + 2$ steps per unit of $a$, and $\tfrac{1}{3}$ removes the $b$ threes at the end.

22. Only lengths count. The first domino gains $2$ letters on top and the second loses $3$, so a match with $x$ and $y$ copies needs $2x = 3y$. The least solution is $x = 3$, $y = 2$, and the order does not matter in one letter.

23. Map $\langle M, w \rangle$ to the machine that, on input $s$, runs $M$ on $w$ for $s$ steps, halts if $M$ has not halted yet, and loops otherwise.

24. By the s-m-n theorem there is a total computable $g$ such that program $g(e)$ halts exactly on the inputs $x \le e$. Apply the recursion theorem to $g$.
