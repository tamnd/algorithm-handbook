1. ◦ A company has 200 users who must be able to talk in pairs. How many long-term keys are needed with a key for each pair and with a key distribution center, and how many does each user store in each design? How many new keys does each design need when user 201 joins?

2. ◦ A dealer shares a secret over $\mathbb{F}_{13}$ with threshold $t = 3$ using $f(X) = 5 + 4X + 2X^2$. Give the shares of parties 1, 2 and 4, the Lagrange coefficients at 0 for the set $\{1, 2, 4\}$, and the secret they reconstruct.

3. ◦ In the subgroup of order $q = 11$ of $\mathbb{Z}_{23}^*$ take $g = 4$ and $h = 9$. Compute the Pedersen commitments $\mathrm{Com}(3; 5)$ and $\mathrm{Com}(4; 1)$, their product, and $\mathrm{Com}(7; 6)$. What property does the result show?

4. ◦ Run the Schnorr identification protocol in the group of exercise 3 with secret $x = 3$, nonce $k = 6$ and challenge $c = 5$. Give $y$, the first message $a$, the answer $z$, and both sides of the verifier's check.

5. ◦ A verifier wants a cheating prover to pass with probability at most $2^{-40}$. How many rounds does it need with the graph isomorphism protocol, with the Feige-Fiat-Shamir scheme with $k = 5$ secrets, and with one run of the Schnorr protocol whose challenge has $t$ bits (give $t$)?

6. ◦ A server accepts 6-digit HOTP codes with a look-ahead window of $s = 3$ and locks the account after $v = 10$ failed attempts. By the bound of RFC 4226, what is the chance that an attacker who guesses gets in?

7. ◦ The BGW protocol runs with $n = 7$ parties. What is the largest number of corrupted parties it tolerates with perfect security against semi-honest parties, and against malicious parties? How many field elements and rounds does one multiplication cost in the version of Gennaro, Rabin and Rabin, and in the original? Give the two thresholds for $n = 4$ as well.

8. ◦ After a traffic analysis, an attacker assigns the four possible senders of a message the probabilities $1/2$, $1/4$, $1/8$ and $1/8$. Give the entropy of this distribution and the effective size of the anonymity set.

9. ◦ In Blum's coin flip, Alice wants the output 1 and may refuse to open her commitment after she sees Bob's bit. What is her chance of getting 1 if Bob outputs a fresh random bit when she aborts? If instead Bob outputs the fixed bit 0 on abort, what is her best chance of getting 0, and of getting 1?

10. ◦ List by name and type number the handshake messages of a full TLS 1.3 handshake with a server certificate, in order, and of a PSK resumption. Which messages does the resumption leave out, and why can it?

11. • In exercise 2, party 2 hands in its share plus 1 and the other two are honest. What secret comes out? Which value should party 2 add to its share to make the result 0?

12. • In the group of exercise 3, a prover with public key $y = 12$ sends $a = 18$, answers the challenge $c = 4$ with $z = 1$, and, after a fault makes it reuse its nonce, answers $c' = 7$ with $z' = 5$. Check both transcripts and compute the secret key.

13. • In the group of exercise 3, find $\tau = \log_4 9$ by trying exponents. Use $\tau$ to open the commitment $\mathrm{Com}(3; 5)$ of exercise 3 as a commitment to 9, and check the opening. Why must nobody know $\tau$ in real use?

14. • Feldman's VSS runs in the group of exercise 3 with secret $s = 6$, threshold $t = 2$ and $f(X) = 6 + 3X$ over $\mathbb{Z}_{11}$. Give the commitments $C_0, C_1$ and the shares of parties 1 to 4. Check party 4's share, and show that the wrong share 8 fails the check.

15. • Feige-Fiat-Shamir with $n = 77 = 7 \cdot 11$ and one secret $s = 10$ publishes $v = s^{-2} \bmod 77$. A prover sends $x = 16$ and then answers both challenges, with $y = 4$ for $e = 0$ and $y' = 40$ for $e = 1$. Give $v$, check both answers, and compute $s$ from them.

16. • In the zero-knowledge proof of 3-colorability, a prover tries to convince the verifier that $K_4$ is 3-colorable. What is its best chance of passing one round? How many rounds make its chance at most $2^{-40}$? How many rounds does the general bound $(1 - 1/|E|)^{k|E|} \le e^{-k}$ ask for?

17. • A circuit has 1000 AND gates and 5000 XOR gates, and labels have $k = 128$ bits. How many bits of garbled tables are sent with four rows per gate and no free XOR, with three rows per gate (GRR3) and no free XOR, with free XOR and GRR3, with half gates, and with three halves at $1.5k + 5$ bits per AND gate?

18. • Two parties add two 32-bit numbers with GMW on a ripple-carry adder with a 33-bit result, in which each carry $c_{i+1} = ((a_i \oplus c_i) \wedge (b_i \oplus c_i)) \oplus c_i$ costs one AND gate and $c_0 = 0$. How many rounds do the gates take, and how many $\binom{4}{1}$-OTs are used? With Beaver triples, how many bits are sent online for the AND gates, and how many random OTs make the triples if each triple takes two?

19. • IKNP extension makes $m = 10^6$ OTs of $\ell = 128$-bit strings with $\kappa = 128$. How many base OTs are needed? How many megabytes does the receiver send and the sender send, and how many hash calls are made?

20. • A database $x = 01101001$ (bits $x_1$ to $x_8$) is held by two servers that do not collude. The client wants $x_3$ and draws $S = \{1, 4, 6, 8\}$. Give both queries, both answers and the result. How many bits go each way?

21. • BGW runs with $n = 3$, $t = 1$ over $\mathbb{F}_{11}$ on $a = 2$ shared by $f_a(X) = 2 + X$ and $b = 4$ shared by $f_b(X) = 4 + 2X$. Give each party's shares and the local products. Combine the products with the Lagrange coefficients for $\{1, 2, 3\}$. Why must the parties reduce the degree before the next multiplication?

22. • Threshold ElGamal runs in the group of exercise 3 with key $x = 6$ shared by $f(X) = 6 + 2X$ over $\mathbb{Z}_{11}$ among three servers, threshold 2. The ciphertext of $m = 13$ uses $r = 3$. Give $y$, the ciphertext, the partial decryptions of servers 1 and 3, their Lagrange coefficients, and the combined value. Check that $m$ comes out.

23. • In FRI, a polynomial is folded by $f(X) = E(X^2) + X\,O(X^2) \mapsto E + \alpha O$. Over the field $\mathbb{F}_p$ with $p = 3 \cdot 2^{30} + 1$, fold $g(X) = 5 + X + 7X^2 + 2X^3$ with $\alpha_0 = 3$, and fold the result with $\alpha_1 = 4$. What constant must the prover send?

24. ★ Blum's protocol is run $r = 7$ times and the output is the majority of the seven coins. Alice wants 1, sees each coin before Bob does, and may abort once; Bob then tosses the current coin and all later ones himself. Compute her best chance of getting 1 exactly with a short program, and compare its bias times $\sqrt{7}$ with the values for $r = 5$ and $r = 9$.

25. ★ A garbler sends $s = 12$ circuits. The evaluator opens $c$ of them at random, aborts if any opened circuit is bad, and takes the majority output of the others. The garbler wins if no opened circuit is bad and bad circuits form a strict majority of the evaluated ones, and it picks the number $k$ of bad circuits to suit $c$. Which $c$ gives the garbler the smallest chance, and what are $k$ and the chance?

26. ★ In the EGL oblivious transfer with $N = 3233$, $e = 17$, $d = 413$, $x_0 = 123$, $x_1 = 2500$, $m_0 = 1000$ and $m_1 = 2000$, a malicious receiver picks $c = 2$ and sends $v = (x_0 - c^e x_1)(1 - c^e)^{-1} \bmod N$. Compute $v$, $k_0$ and $k_1$, show that $k_0 = c\,k_1$, and say what the receiver learns from the two masked messages.

27. ★ Five parties sit on a cycle $1, 2, 3, 4, 5$ and run a DC-net in which each neighbouring pair shares a key. What do the corrupted parties 1 and 3 together learn about which of the others sent a message? What do the corrupted parties 1 and 2 learn?

28. ★ Write out Lowe's attack on the Needham-Schroeder public-key protocol, in which $A$ starts a session with the intruder $I$ and $I$ uses it to pose as $A$ to $B$. Which check in Lowe's fixed protocol stops it, and at which message?

29. ★ Show that in every perfect 2-out-of-2 secret sharing scheme for a secret with $q$ possible values, each share must take at least $q$ values. Give a scheme that meets the bound.
