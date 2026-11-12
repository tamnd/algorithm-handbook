1. ◦ Take the toy [DSA](/dsa/) parameters $p = 23$, $q = 11$, $g = 4$ and the secret key $x = 7$. Compute the public key $y$. Sign the hash value $z = 9$ with the nonce $k = 9$, and verify the signature. Then check whether the same signature verifies for $z = 8$. Why is $r$ not equal to $g^k \bmod p$ here?

2. ◦ Textbook RSA uses the toy key $N = 3233$, $e = 17$, $d = 2753$ and signs a message $m \in \mathbb{Z}_N$ as $m^d \bmod N$, with no hash. Without using $d$, find the message $m$ whose signature is $\sigma = 3$. Name the attack and the kind of break in the terms of the [key-only attack](/key-only-attack/) entry, and say why signing $H(m)$ instead stops this forgery.

3. ◦ Name the attack (key-only, known-message, directed chosen-message or adaptive chosen-message) and the break (total break, universal, selective or existential forgery) in each case, as the entries classify them. (a) Java 15 to 18 accepts the ECDSA signature $r = s = 0$ for every message and key. (b) From two PlayStation 3 update signatures with the same nonce, an attacker computes Sony's secret key. (c) After seeing $N$ and $e$, an attacker asks a textbook RSA signer for the signature of $m r^e \bmod N$ and divides by $r$ to sign any target $m$ it likes. (d) An attacker fixes the target 35 before it sees the key. After it sees $N$ and $e$, and before it gets any signature, it asks a textbook RSA signer for the signatures of 5 and 7, and multiplies them to sign 35.

4. ◦ For each scheme, say whether honest signing is deterministic and whether signatures are unique (one valid signature per key and message): RSA PKCS #1 v1.5 with a range check, RSA-PSS, ECDSA with a random nonce, ECDSA with RFC 6979 nonces, Ed25519, BLS. Which of them get [SUF-CMA](/strong-unforgeability/) from EUF-CMA with no further argument?

5. ◦ A [Lamport signature](/lamport-signature/) signs the 384-bit digest of SHA-384, and every secret and public value is a 48-byte SHA-384 output. How many bytes are the secret key, the public key and one signature? Compare with the sizes for SHA-256 in the entry.

6. ◦ Compute the signature size in bytes of XMSS-SHA2_16_256 ($n = 32$, $len = 67$, height 16) and of a single LMS tree with LMS height 10 and LMOTS_SHA256_N32_W8 ($n = 32$, $p = 34$), following the field layouts of the [XMSS](/xmss/) and [LMS](/leighton-micali-signature/) entries.

7. ◦ A [Merkle signature scheme](/merkle-signature-scheme/) has height $h = 3$, and the signer's counter is 5. List the authentication path of the next signature, as nodes $N_{i,j}$ (level $i$, index $j$, leaves at level 0). For each step of the verifier's climb, say whether the current node goes on the left or on the right. What is the counter afterwards?

8. ◦ On the toy curve $y^2 = x^3 + 7$ over $\mathbb{F}_{97}$ of the [signature malleability](/signature-malleability/) entry ($n = 79$, $G = (1, 28)$, $d = 11$, $Q = (65, 5)$), the [ECDSA](/ecdsa/) signature of $z = 30$ with $k = 5$ is $(20, 50)$. Give the second valid signature on the same $z$ that anyone can compute, say which nonce it corresponds to, and say which of the two a signer that applies the low-s rule outputs.

9. • In the toy DSA group $p = 2039$, $q = 1019$, $g = 4$ with public key $y = 1297$, a signer publishes $(r, s_1) = (360, 676)$ on the hash $z_1 = 111$ and $(r, s_2) = (360, 426)$ on $z_2 = 222$. Recover the nonce and the secret key with the [nonce reuse attack](/nonce-reuse-attack/), and check your key against $y$.

10. • In the group of order $q = 1019$ in $\mathbb{Z}_{2039}^*$ with $g = 4$, a [Schnorr](/schnorr-signature/) signer with public key $y = 277$ signs "yes" and "no" with the same nonce. The signatures are $(R, s) = (2020, 689)$ and $(2020, 474)$, and the challenges are $e_1 = 753$ and $e_2 = 722$. Recover the secret key and the nonce, and check both.

11. • Use the textbook RSA key of exercise 2. An attacker asks for the signatures of 5 and 7 and gets 385 and 2667. Without further queries, sign 35 and 125. Check one of your answers with $e$. Which of the two forgeries would still work against [RSA-FDH](/rsa-fdh/), where the signer signs $H(m)$?

12. • A [Winternitz](/winternitz-one-time-signature/) key signs a 256-bit digest with 32-byte chain values. For chain length $w = 4$, $16$ and $256$, compute $\ell_1$, the largest checksum, $\ell_2$, the number of chains $\ell$, and the signature size in bytes. Which choice gives the smallest signature, and what does it cost the signer?

13. • Threshold BLS with $t = 3$ uses shares of the polynomial $f(z) = 7 + 3z + 2z^2$ over $\mathbb{Z}_{11}$ (the key is $f(0) = 7$). Parties 1, 2 and 4 sign. Compute their shares and their Lagrange coefficients modulo 11, and check that the combination gives back $f(0)$. How does the combiner use the same coefficients on the partial signatures $H(m)^{x_i}$ of [threshold signatures](/threshold-signature/)?

14. • In the group of order 1019 in $\mathbb{Z}_{2039}^*$ with $g = 4$, an honest signer announces the key $X_1 = 1458$. A cheater picks $\beta = 100$ and announces $X_2 = g^{\beta} X_1^{-1}$. Compute $X_2$ and the naive aggregate key $X_1 X_2$, and say why the cheater can now sign alone for both under the naive [multisignature](/multisignature-problem/) rule. Why does the [MuSig](/musig/) key coefficient stop this?

15. • Run [Chaum's blind signature](/chaum-blind-signature/) with the key $N = 3233$, $e = 17$, $d = 413$, the encoded message $m = 200$ and the blinding factor $r = 3$. Give the blinded message, the signer's answer, $r^{-1} \bmod N$ and the final signature, and check it with $e$.

16. • For RSA-FDH, take $q_s = 2^{20}$, $q_h = 2^{50}$ and an RSA inversion probability $\varepsilon' = 2^{-70}$. What forging probability does the Bellare-Rogaway bound $(q_s + q_h + 1)\varepsilon'$ allow, and what does Coron's bound $(1 + 1/q_s)^{q_s + 1} q_s \varepsilon'$ allow? With Coron's bound, about how many signatures can the key make before the bound reaches $2^{-40}$?

17. • A Lamport key with an $n$-bit digest has signed $k$ messages with random digests. A forger wants to sign a fresh random digest using only revealed secrets. Compute its chance for $n = 128$ with $k = 3$ and $k = 4$, as powers of 2. For $n = 256$, what is the smallest $k$ that gives a chance of at least $1/2$?

18. • A Rabin-Williams key has $p = 19$ and $q = 23$, so $N = 437$. Following the algorithm of the [Rabin signature](/rabin-signature/) entry, sign $h = 60$: find $e$, $f$, $h'$, $s_p$, $s_q$ and the CRT value before line L5. List the four square roots of $h'$. A faulty signer gives out 72 and 118 for this $h$; factor $N$.

19. • In the tightness example of the [forking lemma](/forking-lemma/), $A$ returns the first index $i$ with $h_i$ in a fixed set $S$. Take $q = 4$ oracle answers, $h = 16$ possible answers and $|S| = 4$. Compute $acc$, the exact fork probability $frk$, and the lower bound $acc(acc/q - 1/h)$.

20. ★ The toy Schnorr signature of the Schnorr signature entry has $x = 123$, $y = 572$, and the signature $(R, s) = (1777, 368)$ on "hi" with $e = H(R \| m) = 1010$; the key is not hashed. Without $x$, turn this into a valid signature on "hi" under the related key $y' = y g^5$. Give $y'$ and the new $s$, verify it, and say what BIP 340 changes so that the attack fails.

21. ★ Recover the possible public keys from the ECDSA signature $(r, s) = (20, 50)$ on $z = 30$ over the toy curve of exercise 8, using $Q = r^{-1}(sR - zG)$. How many candidates for $R$ are there, and why is $j = 1$ impossible here? Check that the signature verifies under every key you find.

22. ★ A toy Winternitz key has $w = 4$, signs one-byte digests as four base-4 digits (most significant first), and appends the checksum $C = \sum (3 - b_i)$ as two base-4 digits, as in the example of the Winternitz entry. The key signs the digests `8f` and `3c`. How many other digests can a forger now sign? Give one. How many could it sign with no checksum? How many after only the signature on `8f`?

23. ★ Run blind Schnorr from the [blind signature](/blind-signature/) entry in the toy group of exercise 10, with $H$ as in the Schnorr entry (SHA-256 of $R$ as two bytes followed by the message, reduced mod 1019). The signer has $x = 5$, $X = 1024$ and picks $k = 50$. The user wants a signature on "hi" and picks $\alpha = 7$, $\beta = 11$. Compute $R$, $R'$, $c' = H(R' \| \text{hi}) = 337$, the challenge $c$ that the user sends, the answer $s$, and $s'$. Check that $(R', s')$ is a valid Schnorr signature.

24. ★ On the toy curve of exercise 8, a signer with public key $Q = (65, 5)$ reuses one nonce and applies the low-s rule. It publishes $(67, 14)$ on $z_1 = 30$ and $(67, 2)$ on $z_2 = 45$. The low-s rule may have negated either $s$. Recover the secret key, and say how you know which candidate is right.
