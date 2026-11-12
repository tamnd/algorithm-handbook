1. $a$ ranges over the 28 units modulo 29 and $b$ over 29 values, so $28 \cdot 29 = 812$ keys. For 26 letters, $\log_2 312 \approx 8.29$ bits, and $U \approx 8.29 / 3.2 \approx 2.6$ letters.

3. The key is $4E \oplus 3A = 74$ and $4F \oplus 21 = 6E$. The attacker XORs the ciphertext with `NO` $\oplus$ `GO` and sends `33 21`, which decrypts to `GO`.

5. $\{02\} \cdot \{d4\} = \{b3\}$, since the shift overflows and $\{a8\} \oplus \{1b\} = \{b3\}$. Then $\{03\} \cdot \{d4\} = \{b3\} \oplus \{d4\} = \{67\}$, and $\{02\} \cdot \{80\} = \{1b\}$.

7. DES has the complementation property $E_{\bar K}(\bar x) = \overline{E_K(x)}$. Under the key `FECE269E623EC891`, the plaintext `A32AB357C210A825` encrypts to `85C762EFCAB42D8E`.

9. The union bound gives $q(q-1)/2^{\nu+1}$. For $q = 2^{24}$ this is about $2^{48}/2^{65} = 2^{-17}$ with $\nu = 64$, and about $2^{-49}$ with $\nu = 96$.

11. Put the plaintext blocks $(9, 20)$ and $(12, 15)$ as the columns of $P$ and the ciphertext blocks as the columns of $C$, so $K = C P^{-1}$. Here $\det P \equiv 25$, which is its own inverse modulo 26, and the result is $K = \begin{pmatrix} 5 & 8 \\ 17 & 3 \end{pmatrix}$.

15. A weak key makes all 16 round keys equal. Decryption is encryption with the round keys in reverse order, so it is the same map, and $E_K$ is an involution: the answer is `0123456789ABCDEF`.

18. Ask for the encryption of $m_0$ and keep its tag. Submit $(m_0, m_1)$ and output 0 if the challenge tag equals the stored one. The MAC is deterministic, so the advantage is $1$ minus the chance that the tags of $m_0$ and $m_1$ collide.

20. The lemma gives $\varepsilon = 2^{2} \cdot \tfrac14 \cdot (-\tfrac18) \cdot \tfrac14 = -1/32$, so $1/\varepsilon^2 = 1024$; the attack needs a small multiple of this.

23. The first and third letters use the same shift, so $c_1 - p_1 \equiv c_3 - p_3$ for every consistent plaintext. `AAA` fails this test against `AAB`. Count the plaintexts that pass: the first two letters are free, and the third is fixed by them.

24. Run the recurrence from each nonzero state, or note that $1 + x^2 + x^4 = (1 + x + x^2)^2$ over $\mathrm{GF}(2)$. A reducible polynomial cannot be primitive, so the 15 states split into several cycles.

25. Every 4 rounds contribute at least 25 active S-boxes, each with probability at most $2^{-2}$. Find the smallest multiple of 4 rounds with $2^{-50 j} < 2^{-128}$.

26. Each wrong key matches one pair with probability $2^{-64}$, so after $t$ pairs about $2^{168 - 64t}$ wrong keys survive. Find the first $t$ that makes this far below 1.

27. A true match needs one of the known plaintexts $x$ and one of the evaluated points $u$ to satisfy $u = x \oplus K$, so the product of the two counts must be about $2^{64}$. In the two-key cipher, $x \oplus E(x)$ no longer equals $u \oplus P(u)$, and only a difference $E(x) \oplus E(x \oplus \Delta)$ cancels $K_2$.
