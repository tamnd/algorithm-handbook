1. $A = 2^5 = 32$, $B = 2^{13} = 14$, and the shared value is $14^5 = 32^{13} = 3 \bmod 47$. The check passes for 22 values: the elements of the subgroup of order 23 other than 1, which are the quadratic residues in $[2, 45]$; the 22 non-residues fail. Mallory sends $E = 2^7 = 34$. Alice gets $34^5 = 2^{35} = 2^{12} = 7$ and Bob gets $34^{13} = 2^{91} = 2^{22} = 24$. Mallory computes $A^7 = 7$ and $B^7 = 24$, so she holds both keys.

3. $2G = (5, 2)$, $3G = (8, 3)$, $4G = (10, 2)$, $5G = (3, 6)$, $6G = (7, 9)$, $7G = (7, 2)$, $8G = (3, 5)$, $9G = (10, 9)$, $10G = (8, 8)$, $11G = (5, 9)$, $12G = (2, 4)$, $13G = O$. $Q_A = 3G = (8, 3)$ and $Q_B = 5G = (3, 6)$. Since $15 \equiv 2 \pmod{13}$, the shared point is $2G = (5, 2)$ and the shared $x$-coordinate is 5. For $(3, 4)$, $y^2 = 5$ but $x^3 + x + 6 = 3$, so the point is not on the curve and must be rejected.

4. Alice makes $2^{20}$ puzzles. Bob opens one puzzle in about $(S + 1)/2 \approx 2^{19}$ trials. The eavesdropper opens about half the puzzles, $NS/4 = 2^{38}$ trials. With $N = S = 2^{31}$ the eavesdropper needs $2^{62}/4 = 2^{60}$, and Alice sends $2^{31} \cdot 40$ bytes, which is 80 GiB.

5. $a' = 19$ and $b' = 23$, since $3 \cdot 19 = 57 \equiv 1$ and $11 \cdot 23 = 253 \equiv 1 \pmod{28}$. The messages are $6^3 = 13$, $13^{11} = 4$ and $4^{19} = 9$, and Bob computes $9^{23} = 6$. The map $x \mapsto x^a$ is a permutation of $\mathbb{Z}_{29}^*$, and so can be undone, only if $\gcd(a, 28) = 1$.

9. The client sends $1184 + 32 = 1216$ bytes and the server $1088 + 32 = 1120$ bytes. The first 32 bytes of the concatenation are the whole ML-KEM secret, so the X25519 secret never reaches the KDF. A break of ML-KEM alone then gives the key, and the hybrid has lost its point: it should stay secure if either part holds.

11. Join the residues one at a time. $x \equiv 1 \pmod 2$ and $x \equiv 2 \pmod 3$ give $x \equiv 5 \pmod 6$; adding $x \equiv 4 \pmod 5$ gives $29 \pmod{30}$; adding $x \equiv 3 \pmod 7$ gives $59 \pmod{210}$. Four queries and at most $2 + 3 + 5 + 7 = 17$ trial exponents suffice. Since $210 > 101 > x$, $x = 59$. The check $Y^{101} \equiv 1 \pmod p$, with $2 \le Y \le p - 2$, rejects every query.

12. The reply to $Q_1$ is one of the 7 points $k Q_1$, and comparing hashes for $k = 0, \ldots, 6$ gives $d \bmod 7$; here $10 Q_1 = 3 Q_1 = (6, 6)$, so $d \equiv 3 \pmod 7$. The reply to $Q_2$ is $O$, so $d$ is even. With $d < 13$, the candidates are 3 and 10, and $d = 10$. The addition and doubling formulas use $a$ but never $b$, so the victim computes on whichever curve the point lies on.

13. $K_{ij} = g_i^T D g_j = 2 + 7(i + j) + 4ij \bmod 13$, which gives $K_{12} = 5$, $K_{13} = 3$ and $K_{23} = 9$. The colluders know $D M = (a_1 \; a_2)$ with $M = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}$, which is invertible, so $D = (a_1 \; a_2) M^{-1}$, and then $K_{34} = 8$.

16. $K$ needs only $g^{ab}$ and the public nonces. Eve computes $g^{ab} = B^a$ from Bob's public key, answers Alice in Bob's name, and gets the same key as Alice. The protocol has no forward secrecy either: a later theft of $a$ gives every recorded key. In station-to-station, Alice accepts only after a fresh signature of Bob over both ephemeral values, and Alice's private key does not help to make it.

19. At the moment of the copy Eve has the root key, Alice's ratchet secret and her sending chain key after $a_1$. The chain key gives $a_2$. Bob's new ratchet public key travels in the header of $b_0$, so Eve can compute Alice's side of the DH ratchet step, the new root key and Bob's chain, and so reads $b_0$ and $b_1$. She cannot read $a_0$ or $a_1$, because those keys were erased and the KDF chain runs one way. Once Alice makes a fresh ratchet key, the next DH output needs a secret that a passive Eve never saw, so the later messages are safe again.

20. A passive recorder needs one private key for each DH value that enters SK. (a) $DH_3$ needs $EK_A$ or $SPK_B$, both deleted, so SK is safe. (b) $DH_1$ follows from $SPK_B$, $DH_2$ from $IK_B$ and $DH_3$ from $SPK_B$, so SK is exposed. (c) $DH_4$ needs $EK_A$ or $OPK_B$, both deleted, so SK is safe.

24. Bob's key is a function of $m$ and his own random coins. Eve sees $m$ and runs Bob's algorithm with fresh coins of her own. Her coins have the same distribution as Bob's and are independent of Alice's coins and of $m$, so her output agrees with Alice's key with the same probability as Bob's, at least $1 - \varepsilon$.

25. For (a), the $k + 1$ users hold $D g_i$ for $k + 1$ distinct points, and the Vandermonde matrix of those points is invertible. For (b), take $h \ne 0$ orthogonal to the $k$ colluders' vectors $g_i$, and set $D' = D + c\, h h^T$. It is symmetric and gives the colluders the same data, and $K'_{uv} = K_{uv} + c\,(h^T g_u)(h^T g_v)$. Both factors are nonzero, because any $k + 1$ of the vectors are independent. So as $c$ runs over the field, $K_{uv}$ takes each value equally often.

26. With $u$ known in advance, the thief picks $a$ and sends $A = g^a v^{-u}$. The server computes $S = (A v^u)^b = g^{ab}$, and the thief computes $(B - kv)^a = g^{ab}$ without $x$. In the toy group, $v = 8$, $A = 20$, $B = 12$, and both sides get $S = 7$; an honest run with $A = 5^7$ gives $S = 19$ on both sides. In real SRP, $u$ depends on $A$, so $A$ cannot be chosen to cancel $v^u$.

27. Use hybrids $H_0, \ldots, H_n$. In $H_j$, the keys $mk_0, \ldots, mk_{j-1}$ are uniform, $ck_j$ is uniform, and the rest of the chain is computed from $ck_j$. $H_0$ is the real chain and $H_n$ gives uniform message keys with an independent $ck_n$. From $H_j$ to $H_{j+1}$, only the two outputs of $F(ck_j, \cdot)$ change, and $ck_j$ is uniform and used nowhere else, so a distinguisher breaks the PRF. Sum the $n$ gaps.

28. Write $n = 2^d + k$ with $0 \le k < 2^d$. Show by induction that the tree then has $2^d - k$ leaves at depth $d$ and $2k$ at depth $d + 1$. A join at a shallowest leaf turns one leaf at depth $d$ into two at depth $d + 1$. The height is $d$ when $k = 0$ and $d + 1$ otherwise, which is $\lceil \log_2 n \rceil$ in both cases.
