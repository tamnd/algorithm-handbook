1. ◦ The [affine cipher](/affine-cipher/) on 26 letters has 312 keys. How many keys does it have on an alphabet of 29 symbols? Using a redundancy of $D \approx 3.2$ bits per letter of English, estimate the unicity distance $H(K)/D$ of the 26-letter affine cipher.

2. ◦ Use Friedman's estimate of the [index of coincidence](/index-of-coincidence/) for a long ciphertext ($n \gg m$), with $\kappa_p = 0.066$ and $\kappa_r = 0.0385$, to find the expected index of a [Vigenère](/vigenere-cipher/) ciphertext with period $m = 1$, $2$ and $5$.

3. ◦ The two-byte message `NO` (ASCII `4E 4F`) was encrypted with a [one-time pad](/one-time-pad/) to `3A 21`. Find the key bytes. Then give the ciphertext that an attacker who does not know the key should send so that it decrypts to `GO`.

4. ◦ With [PKCS #7 padding](/pkcs7-padding/) and a block length of 16 bytes, give the padding bytes for messages of 13, 16 and 31 bytes. How long is each [CBC](/cbc-mode/) ciphertext if the IV is sent as its first block?

5. ◦ In $\mathrm{GF}(2^8)$ with the AES polynomial $x^8 + x^4 + x^3 + x + 1$, compute $\{02\} \cdot \{d4\}$, $\{03\} \cdot \{d4\}$ and $\{02\} \cdot \{80\}$.

6. ◦ Find the inverse of $\{02\}$ in the AES field, and use it to compute the AES [S-box](/s-box/) value $S(\{02\})$.

7. ◦ [DES](/data-encryption-standard/) maps the plaintext `5CD54CA83DEF57DA` under the key `0131D9619DC1376E` to `7A389D10354BD271`. Without running DES, give a second key, plaintext and ciphertext that are also a correct DES triple.

8. ◦ A key search machine tests $2^{40}$ keys per second. How long does it need on average and at worst for a 56-bit key? How long on average for a 128-bit key? How many cipher evaluations does Grover search need for the 128-bit key on a quantum computer?

9. ◦ A sender picks a uniformly random 64-bit [nonce](/nonce/) for each of $2^{24}$ messages under one key. Bound the probability that some nonce repeats. Do the same for 96-bit nonces.

10. ◦ DESX adds two 64-bit [whitening keys](/key-whitening/) to a 56-bit DES key. In the ideal cipher model, what effective key length does the Kilian-Rogaway bound give against an attacker with $2^{20}$ known pairs, and how many key bits does DESX have in all?

11. • A [Hill cipher](/hill-cipher/) with a $2 \times 2$ key encrypts column vectors as $c = Kp \bmod 26$. The known plaintext `JUMP` encrypts to `XFYP`. Recover $K$.

12. • A Vigenère ciphertext has repeated trigrams at distances 18, 30, 42, 54 and 25. Use [Kasiski examination](/kasiski-examination/) with a count of divisors to pick the period, and say which distance is a false hit.

13. • An [Enigma](/enigma-machine/) ciphertext begins `QWEKTRXETNWAIP`, and the crib `WETTER` is believed to lie somewhere in it. Since Enigma never encrypts a letter to itself, which of the 9 possible alignments of the crib survive?

14. • Compute AES MixColumns on the columns $(01, 00, 00, 00)$ and $(01, 01, 01, 01)$. For each, count the nonzero bytes of input and output together, and compare with the branch number 5.

15. • DES with the weak key `0101010101010101` maps `0123456789ABCDEF` to `617B3A0CE8F07100`. Without running DES, find the encryption of `617B3A0CE8F07100` under the same key, and explain why.

16. • Two 4-byte messages were encrypted in [CTR mode](/ctr-mode/) under one key with the same initial counter block, giving `C9 79 3D AE` and `D2 73 3D A6`. The first message is `SELL`. Find the second.

17. • [CBC-MAC](/cbc-mac/) with a zero IV gives the tag $T_1$ on the one-block message $M_1$ and the tag $T_2$ on the one-block message $M_2$. Give a two-block message, not queried, whose tag is known, and prove that the tag is correct.

18. • A scheme encrypts $m$ with randomized CTR mode under $K_1$ and appends $\mathrm{HMAC}_{K_2}(m)$ (encrypt-and-MAC). Show that it is not IND-CPA secure, with one oracle query, and give the advantage of your adversary.

19. • For $n = 3$ and $q = 4$, compute the exact optimal advantage $C(N, q)$ in the [switching lemma](/prp-prf-switching-lemma/) and compare it with the bound $q(q-1)/2^{n+1}$. Then evaluate the bound for a 64-bit block cipher and $q = 2^{30}$ queries.

20. • A linear approximation of a cipher is the XOR of three round approximations with biases $1/4$, $-1/8$ and $1/4$. Use the piling-up lemma to find its bias $\varepsilon$, and give $1/\varepsilon^2$, the scale of the number of known plaintexts that [linear cryptanalysis](/linear-cryptanalysis/) needs.

21. • A [Poly1305](/poly1305/) one-time key tags messages of $L = 1000$ bytes. Bound the success of one forgery attempt, and use the union bound to bound $2^{64}$ attempts.

22. • In [CMAC](/cmac/) with AES, $K_1 = 2L$ and $K_2 = 4L$ in $\mathrm{GF}(2^{128})$, where doubling shifts left and XORs `87` into the last byte when the top bit falls off. Compute $K_1$ and $K_2$ for $L = 8000\ldots00$ and for $L = 7FFF\ldots FF$ (hex, 16 bytes).

23. ★ A Vigenère cipher with period 2 encrypts 3-letter messages with a uniform key in $\mathbb{Z}_{26}^2$, and the message is uniform over the $26^3$ strings. Find $\Pr[M = \texttt{AAA} \mid C = \texttt{AAB}]$, the number of plaintexts consistent with `AAB`, and their posterior probability. Is the scheme perfectly secret, and how does this fit [Shannon's theorem](/shannon-perfect-secrecy-theorem/)?

24. ★ An [LFSR](/lfsr/) of length 4 has the connection polynomial $C(x) = 1 + x^2 + x^4$, so $s_t = s_{t-2} \oplus s_{t-4}$. Find the cycle lengths of its 15 nonzero states, explain from a factorization of $C(x)$ why it is not a maximal-length register, and say how many output bits Berlekamp-Massey needs to recover it.

25. ★ A 128-bit SPN uses 4-bit S-boxes whose best differential probability is $2^{-2}$, and its linear layer forces at least 25 active S-boxes in any 4-round trail. Bound the probability of a 4-round differential trail. How many rounds, in multiples of 4, are needed before every trail has probability below $2^{-128}$? Compare with AES, whose S-box has best probability $2^{-6}$.

26. ★ For [key recovery](/key-recovery/) on three-key Triple DES ($k = 168$, $n = 64$), find the expected number of wrong keys that agree with $t = 1, 2, 3$ known pairs, assuming each wrong key acts as a random permutation. How many pairs fix the key, and how does this compare with the rule $\lceil k/n \rceil + 1$?

27. ★ The one-key Even-Mansour cipher $E(x) = K \oplus P(x \oplus K)$ uses a public random permutation $P$ on 64 bits. The slide attack matches $x \oplus E(x)$ with $u \oplus P(u)$. With $2^{20}$ known pairs, how many evaluations of $P$ give a true match with constant probability? Why does the same attack fail on the two-key cipher, and what kind of data does Daemen's attack on it need instead?

28. ★ The PRESENT S-box is `C 5 6 B 9 0 A D 3 E F 8 4 7 1 2`. Compute its differential uniformity, the distribution of the DDT entries over the 15 nonzero input differences, and its nonlinearity. Is it optimal among 4-bit bijections?
