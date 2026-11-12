1. $y = 4^7 \bmod 23 = 8$. Then $g^k \bmod p = 13$, so $r = 13 \bmod 11 = 2$, $k^{-1} \bmod 11 = 5$ and $s = 5(9 + 7 \cdot 2) \bmod 11 = 5$. To verify, $w = 9$, $u_1 = 4$, $u_2 = 7$ and $(4^4 \cdot 8^7 \bmod 23) \bmod 11 = 13 \bmod 11 = 2 = r$, so it accepts. For $z = 8$, $u_1 = 6$ and the check gives 1, so it rejects. $r$ is $g^k \bmod p$ reduced once more modulo $q$.

3. (a) Key-only attack, universal forgery. (b) Known-message attack, total break. (c) Directed chosen-message attack, universal forgery. (d) Directed chosen-message attack, selective forgery: the queries come before any signature, and the target was fixed at the start.

4. v1.5: deterministic and unique. PSS: randomized. ECDSA with a random nonce: randomized, and not unique, since $(r, n - s)$ also verifies. ECDSA with RFC 6979: deterministic, still not unique. Ed25519: deterministic, and strongly unforgeable only because the verifier checks $S < L$. BLS: unique. Only the unique schemes, v1.5 with the range check and BLS, get SUF-CMA from EUF-CMA for free.

7. The path is $N_{0,4}$, $N_{1,3}$, $N_{2,0}$. The leaf $N_{0,5}$ is a right child, so the verifier hashes $N_{0,4} \| N_{0,5}$; the result $N_{1,2}$ is a left child, so it hashes $N_{1,2} \| N_{1,3}$; the result $N_{2,1}$ is a right child, so it hashes $N_{2,0} \| N_{2,1}$ and gets the root. The bits of 5, read from the bottom, are 1, 0, 1. The counter becomes 6.

9. Subtract the two signing equations: $k = (z_1 - z_2)(s_1 - s_2)^{-1} \bmod q$. Here $s_1 - s_2 = 250$, $z_1 - z_2 \equiv 908$, and $250^{-1} \equiv 697$. Then $x = (s_1 k - z_1) r^{-1} \bmod q$. You should get $k = 77$ and $x = 600$, and $4^{600} \bmod 2039 = 1297$.

12. $\ell_1 = 256 / \log_2 w$ and the largest checksum is $\ell_1(w - 1)$. For $w = 16$ that gives 64 chains, a checksum of at most 960, 3 checksum digits, 67 chains in all and 2,144 bytes. For $w = 256$ the signature shrinks to 34 chains and 1,088 bytes, but each chain has 255 steps, so signing and verifying cost far more hashes than at $w = 16$.

14. $X_2 = 363$ and $X_1 X_2 = 4^{100} \bmod 2039 = 1153$. The cheater knows $\beta = 100$, the discrete log of the aggregate key, so it signs for it with an ordinary Schnorr signature. In MuSig the coefficient $a_i = H(L, X_i)$ depends on the whole key list $L$, so no key chosen after seeing $X_1$ can cancel it.

16. The Bellare-Rogaway bound is about $q_h \varepsilon' = 2^{-20}$, far too weak. Coron's factor tends to $e \cdot q_s$, which gives about $2^{-48.6}$ and does not depend on $q_h$. The bound reaches $2^{-40}$ when $e \cdot q_s \cdot 2^{-70} = 2^{-40}$, at about $2^{28.6}$ signatures.

18. $p = 19 \equiv 3$ and $q = 23 \equiv 7 \pmod 8$. Pick $e = -1$ and $f = 1$, so $h' = -60 \bmod 437 = 377$, which is a square modulo both primes. Then $s_p = 4$, $s_q = 3$, and the four roots are 72, 118, 319 and 365. Two roots that are not negatives of each other differ by a multiple of one prime: $\gcd(118 - 72, 437) = 23$.

20. The challenge $e = H(R \| m)$ does not depend on the key. With $y' = y g^5 = 535$, the secret is $x + 5$, so $s' = s + 5e \bmod 1019 = 323$, and $g^{323} = 1366 = R \cdot y'^{e} \bmod 2039$. BIP 340 hashes the public key into the challenge, $e = H(R \| P \| m)$, so a change of key changes $e$.

21. The curve has two points with $x = 20$, namely $(20, 21)$ and $(20, 76)$. The value $j = 1$ would need $x = r + n = 99$, which is not below 97. The two candidates give $Q = (29, 7)$ and $Q = (65, 5)$, and the signature verifies under both. This is why Ethereum signatures carry a recovery byte.

22. A chain value can only be moved forward, so a forger can sign a digest when each of its six digits, checksum included, is at least the smaller of the two revealed digits at that place: $[0, 0, 3, 0, 1, 0]$. Count the digests whose digits pass this test; there are 42 besides the two signed, for example `0c`. With no checksum, any digest with third digit 3 works: 62 others. With one signature, raising a message digit lowers the checksum, so there are none; with no checksum there would be 7.

24. Because of the low-s rule, each published $s$ is either $k^{-1}(z + rd)$ or its negative. So $k = (z_1 - z_2)/(S_1 - S_2)$ or $k = (z_1 - z_2)/(S_1 + S_2)$ modulo 79. Compute $d = (S_1 k - z_1) r^{-1}$ for each candidate and keep the one with $dG = Q$. The first gives $d = 27$, which fails; the second gives $k = 4$ and $d = 11$.
