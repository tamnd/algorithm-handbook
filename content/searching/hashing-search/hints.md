2. No: 10 and 22 both go to 2, and 37 and 45 both go to 1. The smallest $m$ is 10, with slots 0, 2, 7 and 5. Yes: $(x \bmod 10) \bmod 4$ maps $S$ to 0, 2, 3 and 1.

3. $10 \cdot 9 \cdot 8 \cdot 7 \cdot 6 / 10^5 = 0.3024$, and $5!/5^5 = 0.0384$. The function takes about $1.443 \times 10^9$ bits, about 180 megabytes, against 8 gigabytes for the keys.

4. $\alpha = 3$, so an unsuccessful search examines 3 keys on average, with standard deviation $\sqrt{3(1 - 1/1000)} \approx 1.73$. A successful search examines $1 + 2999/2000 \approx 2.50$ keys.

5. Uniform hashing: $1/(1 - 0.8) = 5$ probes, and $1.25 \ln 5 \approx 2.01$. Linear probing: $\frac{1}{2}(1 + 25) = 13$ probes, and $\frac{1}{2}(1 + 5) = 3$.

6. The slots 0 to 10 hold $-, 23, 34, 3, 15, 26, -, -, -, 9, 20$. The insertions make $1, 1, 2, 2, 1, 1, 2$ probes. An unsuccessful search costs $1, 6, 5, 4, 3, 2, 1, 1, 1, 3, 2$ probes from the home slots 0 to 10, so $29/11 \approx 2.64$ on average. Slots 1 to 5 form one run, although the keys in it have only the homes 1, 3 and 4.

10. The union bound gives $m (e/t)^t$ at $\alpha = 1$. This is about $7.5 \times 10^{-6}$ at $t = 15$ and $4.8 \times 10^{-7}$ at $t = 16$, so $t = 16$.

12. The $i$-th key was inserted at load $(i - 1)/m$, so the average successful cost is $\frac{1}{n} \sum_{i < n} U(i/m)$, a Riemann sum for the integral. For linear probing, $\frac{1}{\alpha} \int_0^\alpha \frac{1}{2}\left(1 + \frac{1}{(1 - t)^2}\right) dt = \frac{1}{2}\left(1 + \frac{1}{1 - \alpha}\right)$.

13. They collide for $a = 1, 2, 9, 10$, so for 4 of the 10 functions: probability $0.4 > 1/4$, and the family is not universal. No pair does worse, so the family is $\varepsilon$-universal with $\varepsilon = 0.4$, and the lemma bounds the expected chain of an unsuccessful search by $0.4\,n$.

14. A key at slot $j$ with home $h$ may move into the hole at $i$ when $h$ is not in the cyclic range $(i, j]$, that is, when the hole lies on its probe path. Here 34 moves to slot 1 and the hole moves to slot 2; then 3, 15 and 26 all have homes after the hole and stay, and the scan stops at the empty slot 6. The result is $-, 34, -, 3, 15, 26, -, -, -, 9, 20$.

15. Slots 0, 1, 4 and 2, since $i^2 \bmod 7$ takes only the values 0, 1, 2 and 4. Insert 0, 1, 2 and 4; then 7 finds all four slots full while 3, 5 and 6 are free. In general $i^2 \equiv j^2 \pmod m$ when $j \equiv -i$, so $i$ and $m - i$ give the same slot.

16. Bucket 0 takes $d = 0$, slots 0, 3 and 4. Bucket 1 takes $d = 5$, slots 5 and 1. Bucket 2 takes $d = 2$, slot 2. Two keys with the same $f$ land in the same slot for every $d$; the real method uses $(f_1(x) + d_0 + d_1 f_2(x)) \bmod m$, or draws new hash functions.

17. Every bucket that holds the two keys beginning $0^{10}1$ must be named by at least 11 bits, so $d = 11$ and the directory has 2048 pointers for 3 keys. Its size depends on how close the hash values are, not only on $n$.

19. Let the hash of $s_1 \ldots s_w$ be $\bigoplus_i \mathrm{rot}^{w - i}(T[s_i])$. Then the next window has hash $\mathrm{rot}(h) \oplus \mathrm{rot}^{w}(T[s_1]) \oplus T[s_{w+1}]$. With $b$-bit words, $\mathrm{rot}^b$ is the identity, so when $w > b$, two positions $b$ apart get the same rotation and swapping their characters does not change the hash.

20. Take keys $(a, x)$, $(a, y)$, $(b, x)$ and $(b, y)$: each word appears twice in the XOR. For three distinct keys, some key has a character at some position that neither other key has there; its table word appears only in that key's hash, so that hash is uniform given the other two. Two distinct keys differ at some position $j$, and the two words of position $j$ make their pair of hashes uniform.

21. Claim: slot $j$ is occupied if and only if, for some $k \ge 1$, at least $k$ keys have their home in the $k$ slots ending at $j$. If $j$ is empty, every key with its home in such a window stops before $j$, inside the $k - 1$ slots before it, so there are at most $k - 1$ such keys. If $j$ is full, take the run that contains it, starting after an empty slot; every key in the run up to $j$ has its home there, so the window from the start of the run to $j$ holds at least as many homes as slots. The condition does not mention the order.

22. Count pairs of a set and an assignment, $\binom{u}{n} n!$ of them. A fixed function $h$ fits a pair only if $S$ takes one key from each class $h^{-1}(j)$, so it fits at most $\prod_j |h^{-1}(j)| \le (u/n)^n$ pairs. The program needs at least $\lg$ of the ratio, which tends to $\lg n^n = n \lg n$ as $u$ grows.
