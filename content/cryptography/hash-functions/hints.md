1. For an ideal function the costs are $2^{n/2}$ and $2^n$: MD5 $2^{64}$ and $2^{128}$, SHA-1 and RIPEMD-160 $2^{80}$ and $2^{160}$, SHA-256 $2^{128}$ and $2^{256}$. MD5 has practical collisions (Wang and Yu 2005), and SHA-1 had its first collision in 2017 after about $2^{63.1}$ computations. No collision of full RIPEMD-160 is known, and for SHA-256 the best collision attack reaches 31 of 64 steps. MD5 and SHA-1 are broken for collision resistance; MD5 preimages still cost about $2^{123.4}$.

3. The number of calls is $\lceil (L + 9)/64 \rceil$: 1, 2, 2, 3 and 16. For SHA-512 it is $\lceil (L + 17)/128 \rceil$: 1 for $L = 111$ and 2 for $L = 112$.

5. Yes for SHA-256 and MD5. SHA-224 is open to it after about $2^{32}$ guesses of the 32 hidden state bits. SHA-384 hides 128 bits of state, so not in practice. No for SHA-512/256, SHA3-256, BLAKE2b and double SHA-256.

6. The key is longer than 64 bytes, so it is hashed first: 2 calls. The inner hash reads $64 + 100$ bytes: $\lceil 109/64 \rceil + 1 = 3$ calls. The outer hash reads $64 + 32$ bytes: 2 calls. That is 7 in all. With the two key states stored, each message costs $2 + 1 = 3$ calls.

7. $2n - 1 = 1999$ hash calls, and at most $\lceil \log_2 1000 \rceil = 10$ hashes in a proof. The prefixes keep a leaf from being read as an inner node, so nobody can present the 64-byte concatenation of two child hashes as a leaf of a different list with the same root.

8. $\log_2 600{,}000 \approx 19.2$ bits. With the key states stored, each iteration is two compression calls, so a guess costs about $1.2 \times 10^6$ calls. For 1000 salted users, $10^9 \cdot 1000 \cdot 1.2 \times 10^6 = 1.2 \times 10^{18}$ calls; unsalted, one computation per guess serves all users, so $1.2 \times 10^{15}$.

11. The first repeat comes at "95303", whose digest starts with `c11eb5e6`, like that of "69235". That is 95,304 hashes, against a mean of about $1.25 \cdot 2^{16} \approx 82{,}000$ and a median of about $1.18 \cdot 2^{16} \approx 77{,}000$; a single run varies widely around them.

12. $K \| m$ has 22 bytes, so the glue is `80`, 33 zero bytes and the 8-byte length 176 = `00 00 00 00 00 00 00 b0`: 42 bytes in all. The forged message has $9 + 42 + 8 = 59$ bytes. Hashed with the key it fills one block plus 8 bytes, so the attacker loads the old tag as the chaining value and makes one compression call on $x$, its padding and the length $72 \cdot 8 = 576$.

15. If $x \ne x'$ and $G(x) = G(x')$, then either $H(x) = H(x')$, a collision of $H$, or $H(x) \ne H(x')$ and these two digests collide under $H$. Either way one collision of $H$ comes out with two extra hash calls. Extension does not work: extending the outer digest gives $H(H(K \| m) \,\|\, \text{glue} \,\|\, x)$, which is not $G$ of any message.

16. Use the two leaves $H(a) \| H(b)$ and $H(c) \| H(d)$, each 64 bytes: their leaf hashes are the two inner nodes of the first tree. For the second tree, the lists $[a, b, c]$ and $[a, b, c, c]$ give the same root. This is CVE-2012-2459.

21. $50 \cdot 2^{129} + 2^{207} \approx 2^{207}$, against $2^{256}$ generic. The attack matches one of the $2^{50}$ intermediate chaining values. SHA-512/256 has 512-bit chaining values, so a match costs about $2^{463}$, above the generic $2^{256}$; SHA3-256 would have to match a 512-bit inner part, and the sponge bound $\min(2^d, 2^{c/2}) = 2^{256}$ already holds.

22. Given $M$, run $A$ on $H(M)$ and output its answer $M'$. Call $M$ lonely if no other message has the same digest; there are at most $2^n$ lonely messages, so a uniform $M$ is lonely with probability at most $2^{n-m}$. Given the digest, $M$ is uniform in its preimage set and $A$ sees only the digest, so when the set has two or more elements and $A$ succeeds, $M' \ne M$ with probability at least $1/2$. For $m \le n$ the function may be injective, as the identity is, and then every message is lonely.

23. Pick $M$ so that $M \| \mathrm{pad}(M)$ is one block, let $M' = M \| \mathrm{pad}(M) \| X$ for a short $X$, let $B$ be the last block of $M'$ after padding, and query $y = H(M)$, $z = H(M')$ and $w = f(y, B)$. In the real world $w = z$ always. In the ideal world $S$ sees only $(y, B)$; to return $R(M')$ it must query $R$ at $M'$, so it must find $M$ from $y$, a preimage under $R$: about $q/2^n$ plus $2^{-n}$, so the advantage is close to 1. With chop-MD the distinguisher knows only $n - s$ bits of the chaining value and must guess the other $s$.

24. Multicollision in SHA-1 first: a $2^{128}$-multicollision costs $128 \cdot 2^{80} = 2^{87}$, then a birthday search over $2^{128}$ messages of 128 blocks costs $2^{135}$. The other order: a $2^{80}$-multicollision in SHA-256 costs $80 \cdot 2^{128} \approx 2^{134.3}$, then $80 \cdot 2^{80} \approx 2^{86.3}$. The second is cheaper, about $2^{134.3}$, far below $2^{208}$ and close to SHA-256 alone. Cheaper SHA-1 collisions shrink only the smaller term.

25. With $2^k$ states, try about $2^{(n-k)/2}$ blocks from each: $2^{(n+k)/2}$ values give about $2^{n+k}/2^{n+1} = 2^{k-1}$ colliding pairs, enough to pair up the states, and later levels cost less. Setting $(n+k)/2 + 2 = n - k + 1$ gives $k = (n-2)/3 = 42$ for $n = 128$, and both costs are $2^{87}$, near $2^{2n/3}$.

26. Choose $m$, ask $h = E_m^{-1}(0^n)$, then ask $f(h, m)$ and output "real" if it equals $h$. In the ideal world the simulator must return an $h$ with $F(h, m) = h$, a fixed point of a random function; each of its $q$ queries finds one with probability $2^{-n}$, so the advantage is at least $1 - (q+1)/2^n$. In the iterated constructions the simulator must stay consistent only on chains that start at the IV, and a fixed point it invents is not on such a chain.
