1. ◦ For each of MD5, SHA-1, RIPEMD-160 and SHA-256, give the generic cost of a collision and of a preimage for an ideal function of the same output size, and the best collision result that the entries report for the real function. Say which of the four are broken for [collision resistance](/collision-resistance/).

2. ◦ A protocol uses a 64-bit hash as an identifier. Using the estimate $1 - e^{-q(q-1)/2N}$ from the [birthday attack](/birthday-attack/), with $N = 2^{64}$, how many random inputs give a collision with probability $1/2$? What is the probability of a collision after $2^{32}$ inputs, and what does the upper bound $q(q-1)/2N$ give for the same $q$?

3. ◦ SHA-256 pads a message of $L$ bytes with a byte `80`, zero bytes, and an 8-byte length, to a multiple of 64 bytes. How many calls of the compression function does it make for $L = 0, 64, 119, 120$ and $1000$? SHA-512 uses 128-byte blocks and a 16-byte length; how many calls does it make for $L = 111$ and $L = 112$?

4. ◦ [SHA-3](/sha-3/) uses Keccak-f[1600] with capacity $c = 2d$ for a $d$-bit digest. Give the rate in bytes and the collision and preimage security levels of FIPS 202 for SHA3-224, SHA3-384 and SHA3-512. Then give the collision and preimage levels of SHAKE128 and of SHAKE256 with a 512-bit output.

5. ◦ For each of the following, say whether an attacker who knows $H(K \| m)$ and the length of $K$, but not $K$, can compute $H(K \| m \| \text{glue} \| x)$ for an $x$ of its choice: SHA-256, MD5, SHA-224, SHA-384, SHA-512/256, SHA3-256, BLAKE2b, and $\text{SHA-256}(\text{SHA-256}(\cdot))$. Use the [length extension](/length-extension-attack/) entry.

6. ◦ Count the SHA-256 compression calls that [HMAC](/hmac/)-SHA-256 makes for a 100-byte key and a 100-byte message, starting from the key. Then count the calls per message when the two padded key states are computed once and stored.

7. ◦ A [Merkle tree](/merkle-tree/) in the style of RFC 6962 has 1000 leaves. How many hash calls compute the root, and how many hashes can an inclusion proof contain at most? What do the one-byte prefixes `00` for leaves and `01` for inner nodes prevent?

8. ◦ A site stores [PBKDF2](/pbkdf2/)-HMAC-SHA-256 with 600,000 iterations, a 32-byte output and a random salt per user. How many bits does the iteration count add, by the rule of RFC 8018? How many SHA-256 compression calls does one guess cost the attacker? How many compression calls does it take to try $10^9$ guesses against each of 1000 users, and how many would it take if the hashes were unsalted?

9. ◦ [scrypt](/scrypt/) is run with $N = 2^{14}$, $r = 8$ and $p = 1$. How much memory does ROMix use, and how many Salsa20/8 calls does one evaluation make? How do both change with $N = 2^{15}$, and with $p = 4$ when the four ROMix calls run one after another?

10. • Compute the Hamming distance between SHA-256("abc") and SHA-256("abd"). For an ideal 256-bit hash, what are the mean and standard deviation of this distance, and how far from the mean is your value? Explain why MD5, which passes such a test, is still broken for collisions, using the [avalanche effect](/avalanche-effect/) entry.

11. • Write a program that hashes the decimal strings "0", "1", "2", ... with SHA-256, keeps the first 32 bits of each digest, and stops at the first repeated value. Report the two strings and the shared 32 bits, and compare the number of hashes with the mean and the median of the birthday attack.

12. • A server sets $\mathrm{tag} = \text{SHA-256}(K \| m)$ with a secret 13-byte key $K$ and $m$ = `amount=10`. Give the glue padding byte by byte, the length of the forged message $m \| \text{glue} \| x$ with $x$ = `&admin=1`, and the number of compression calls the attacker makes to compute its tag from the old one. Check your answer with a pure-Python SHA-256 whose chaining value you can set.

13. • Show that HMAC-SHA-256 with a 65-byte key $K$ gives the same tags as HMAC-SHA-256 with the 32-byte key SHA-256($K$), and check it with Python's `hmac` module. Why does this not contradict the PRF security of HMAC? Does [KMAC](/kmac/) have the same property?

14. • Compute SHAKE128("abc") with 32 and with 64 bytes of output, and BLAKE2b("abc") with 32 and with 64 bytes. In which pair is the short output a prefix of the long one, and why? A program derives an encryption key as SHAKE128($s$, 16 bytes) and a MAC key as SHAKE128($s$, 32 bytes) from one secret $s$. What goes wrong, and how does cSHAKE or a change of input fix it?

15. • Let $H$ be collision resistant. Prove that $G(x) = H(H(x))$ is collision resistant, with a tight reduction in the standard model. If $H$ is SHA-256, can an attacker who sees $G(K \| m)$ use length extension to get $G(K \| m')$ for a longer $m'$?

16. • A Merkle tree computes leaves as $H(x)$ and inner nodes as $H(\ell \| r)$, with no prefixes. Give a list of two leaves whose root equals the root of the four leaves `a`, `b`, `c`, `d`. A second tree has no leaf hashing and copies the last node when a level has an odd number of nodes, as Bitcoin did. Give two different lists of leaf values with the same root. Check both with SHA-256.

17. • A parallel [Pollard rho](/pollard-rho-collision-search/) search for a 64-bit collision runs on $m = 1024$ machines, and a point is distinguished with probability $\theta = 2^{-20}$. Using the estimate $\sqrt{\pi N/2}/m + 2.5/\theta$, how many steps does each machine run, and about how many distinguished points does the central server store?

18. • [Wagner's algorithm](/wagners-algorithm/) for $k = 2^t$ lists costs about $k \cdot 2^{n/(1+t)}$. For $n = 160$, compare the costs for $k = 2$, $4$ and $16$. For $n = 24$, four lists of $2^8$ values and a first merge on 8 bits, how many solutions does the algorithm find on average?

19. • An attacker wants to invert any one of $D$ outputs of a function on $N = 2^{80}$ points, using the Biryukov-Shamir tradeoff $T M^2 D^2 = N^2$ with $D^2 \le T$ and precomputation $N/D$. With $D = 2^{16}$ and $T = M$, find $T$, $M$ and the precomputation. Can the same tradeoff be used with $T = M$ when $D = 2^{30}$?

20. • In the quantum query model, collisions of an $n$-bit random function cost about $2^{n/3}$ queries (Brassard, Høyer and Tapp) and preimages about $2^{n/2}$ (Grover). What output length gives 128-bit security against each quantum attack, and against the classical birthday attack? How many queries does the quantum collision search make on SHA-256, and what does the hardware count of Bernstein (2009) say about it?

21. • SHA-256 allows messages of up to $2^{64} - 1$ bits. For a target message of $2^{50}$ blocks, estimate the cost of the long-message [second preimage](/second-preimage-finding/) attack $k \cdot 2^{n/2+1} + 2^{n-k+1}$. Why does the same attack give nothing against SHA-512/256 or SHA3-256?

22. ★ Let $H : \{0,1\}^m \to \{0,1\}^n$ with $m > n$. Given an adversary $A$ that, on input $H(M)$ for a uniform $M$, returns a preimage with probability $\varepsilon$, build an adversary that finds a second preimage of a uniform $M$ with probability at least $(\varepsilon - 2^{n-m})/2$. This is the bound $\mathrm{Adv}^{\mathrm{pre}} \le 2\,\mathrm{Adv}^{\mathrm{sec}} + 2^{n-m}$ of [preimage resistance](/preimage-resistance/). Why does the proof fail for $m \le n$?

23. ★ Let $H = \mathrm{MD}^f$ with length padding, where $f$ is a random compression function that the distinguisher may also query. Give a distinguisher with three queries that tells $(H, f)$ from $(R, S^R)$, with $R$ a random oracle and $S$ any simulator making $q$ queries, and bound its advantage. Explain why the same distinguisher wins only with probability about $2^{-s}$ against chop-MD, which outputs $n - s$ bits of the final chaining value. Use the [indifferentiability](/indifferentiability-framework/) entry for the definitions.

24. ★ Two Merkle-Damgård hashes are concatenated: $F(m) \,\|\, G(m)$ with $F$ = SHA-1 and $G$ = SHA-256, a 416-bit digest. Using Joux's [multicollisions](/multicollision-attack/) and treating both compression functions as ideal, estimate the cost of a collision in each of the two orders (multicollision in $F$ then birthday in $G$, and the reverse). Which order is cheaper, and how does it compare with $2^{208}$? Does the practical SHA-1 collision attack change the answer?

25. ★ The herding attack builds a diamond of $2^k$ leaves for about $2^{(n+k)/2+2}$ calls offline, and then links a prefix to a leaf for about $2^{n-k+1}$ calls online. Explain why one level of the diamond costs about $2^{(n+k)/2}$ calls. For $n = 128$, choose the integer $k$ that minimizes the larger of the two costs, and give that cost.

26. ★ Let $f(h, m) = E_m(h) \oplus h$ with $E$ an ideal cipher on $n$-bit blocks. Give a distinguisher with two queries showing that $f$, with access to $E$ and $E^{-1}$, is not indifferentiable from a random function, and bound its advantage against any simulator that makes $q$ queries. Then explain why this does not prevent prefix-free or chop-MD iterations of [Davies-Meyer](/davies-meyer-construction/) from being indifferentiable in the ideal cipher model.
