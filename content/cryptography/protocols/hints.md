2. The shares are $f(1) = 11$, $f(2) = 8$ and $f(4) = 1$. For $\{1, 2, 4\}$ the coefficients at 0 are $\lambda = (7, 11, 9)$ mod 13, and $7 \cdot 11 + 11 \cdot 8 + 9 \cdot 1 = 174 \equiv 5$, the secret.

4. $y = 4^3 = 18$, $a = 4^6 = 2$, $z = k + cx = 6 + 15 \equiv 10 \pmod{11}$. The check: $g^z = 4^{10} = 6$ and $a\,y^c = 2 \cdot 18^5 = 6$.

5. Graph isomorphism has error $1/2$ per round, so 40 rounds. FFS with $k = 5$ has error $2^{-5}$ per round, so 8 rounds. Schnorr has error $2^{-t}$ for a $t$-bit challenge, so $t = 40$ in one run.

11. Lagrange reconstruction is linear, so the result moves by $\lambda_2 \delta$. With $\delta = 1$ the secret becomes $5 + 11 = 16 \equiv 3$. To get 0 it needs $11 \delta \equiv -5 \equiv 8$, so $\delta = 8 \cdot 11^{-1} = 8 \cdot 6 \equiv 9 \pmod{13}$.

12. Both transcripts satisfy $4^z = 18 \cdot 12^c$. Subtract the two answers: $z - z' = (c - c')x$, so $x = (1 - 5)(4 - 7)^{-1} = (-4)(-3)^{-1} \equiv 5 \pmod{11}$, and indeed $4^5 = 12$. This is the extractor of special soundness.

13. $4^8 \equiv 9$, so $\tau = 8$. To open $C = g^m h^r$ as $m'$, take $r' = r + (m - m')\tau^{-1} \bmod q$, which keeps $m + \tau r$ fixed: $r' = 7$, and $4^9 \cdot 9^7 \equiv 6$. Whoever knows $\tau$ can open any commitment to anything, so binding rests on nobody knowing it.

15. $v = s^{-2} = 100^{-1} \equiv 67 \pmod{77}$. Checks: $4^2 = 16 = x$, and $40^2 \cdot 67 \equiv 16$. Since $y = r$ and $y' = rs$, the ratio $y'/y = 40 \cdot 4^{-1} = 10$ is $s$.

16. Any coloring of $K_4$ with three colors has at least one bad edge, so the best chance is $5/6$. Then $\lceil 40 / \log_2(6/5) \rceil = 153$ rounds. The general bound needs $e^{-k} \le 2^{-40}$, so $k = 28$ and $28 \cdot 6 = 168$ rounds.

21. Shares of $a$: 3, 4, 5. Shares of $b$: 6, 8, 10. Local products: 18, 32, 50, that is 7, 10, 6 mod 11. With $\lambda = (3, -3, 1)$: $21 - 30 + 6 = -3 \equiv 8 = ab$. The products lie on a polynomial of degree 2, which needs all three points; a second product would have degree 3 or more, which three points cannot fix.

22. $y = 4^6 = 2$; $c_1 = 4^3 = 18$, $c_2 = 13 \cdot 2^3 \equiv 12$. Shares: $8, 10, 1$. For $\{1, 3\}$, $\lambda_1 = 3 \cdot 2^{-1} \equiv 7$ and $\lambda_3 = -1 \cdot 2^{-1} \equiv 5 \pmod{11}$. Partials $18^8 = 16$ and $18^1 = 18$; $16^7 \cdot 18^5 \equiv 8 = c_1^x$, and $12 \cdot 8^{-1} \equiv 13$.

24. Use dynamic programming on (index, number of ones so far). At each coin, after seeing it, Alice compares the chance of a majority of ones if she continues with the chance if Bob tosses the rest. The value is $163/256$ for $r = 7$, a bias of $35/256 \approx 0.137$, and bias times $\sqrt{r}$ is about $0.349$, $0.362$ and $0.369$ for $r = 5, 7, 9$: the bias falls like $1/\sqrt{r}$, well above Cleve's lower bound of order $1/r$.

25. With $c$ opened and $e = 12 - c$ evaluated, the garbler needs $k > e/2$ bad circuits all among the unopened ones, which has chance $\binom{12 - k}{c} / \binom{12}{c}$; it takes the smallest such $k$. The minimum is at $c = 10$, $k = 2$, chance $1/66$. Close values: $c = 8$ gives $1/55$, $c = 6$ gives $1/33$, $c = 11$ gives $1/12$.

26. $c^e = 1752$ and $v = 1436$. Then $k_b = (v - x_b)^d$ gives $k_0 = 101$ and $k_1 = 1667$, and $k_0 \equiv 2 k_1 \pmod N$ because $v - x_0 = c^e (v - x_1)$. The masked values are $1101$ and $434$; the receiver computes $1101 - 2 \cdot 434 \equiv 233 \equiv m_0 - 2m_1$. It learns a linear relation between both messages, which no ideal OT gives, though not either message alone. The protocol is only semi-honest secure.

27. Remove the corrupted parties and their keys. With 1 and 3 corrupted the honest parties fall into $\{2\}$ and $\{4, 5\}$; each component's sum of announcements is known, so the coalition learns which component sent, and if it was $\{2\}$, it knows the sender. With 1 and 2 corrupted, $\{3, 4, 5\}$ stays connected, and all senders in it look the same.

28. $A \to I: \{N_A, A\}_{pk_I}$; $I(A) \to B: \{N_A, A\}_{pk_B}$; $B \to I(A): \{N_A, N_B\}_{pk_A}$; $I \to A$: the same; $A \to I: \{N_B\}_{pk_I}$; $I(A) \to B: \{N_B\}_{pk_B}$. Now $B$ thinks it talks with $A$, and $I$ knows $N_B$. In Needham-Schroeder-Lowe message 2 is $\{N_A, N_B, B\}_{pk_A}$; $A$ expects the name $I$, sees $B$, and stops.

29. Fix any value of share 1 that occurs. Perfect secrecy says every secret is still possible given it, and correctness says share 2 then determines the secret. So distinct secrets need distinct values of share 2, at least $q$ of them, and the same argument with the shares swapped bounds share 1. One-time pad sharing over $\mathbb{Z}_q$, $s_1$ uniform and $s_2 = s - s_1$, meets the bound.
