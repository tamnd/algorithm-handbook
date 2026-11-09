1. $h(\texttt{abc}) = 123 \bmod 101 = 22$. The update gives $(22 - 1 \cdot 100) \cdot 10 + 4 = -776 \equiv 32 \pmod{101}$, and $h(\texttt{bcd}) = 234 \bmod 101 = 32$.

2. $h(\texttt{ab}) - h(\texttt{ba}) = (r + 2) - (2r + 1) = 1 - r$, so only $r = 1$. The bound $(n-1)/p = 1/p$ allows exactly one base.

3. $H = 0, 2, 21, 213, 2131, 21313, 213131$. Both substrings $\texttt{ana}$ get $H[4] - H[1] \cdot 10^3 = 131$ and $H[6] - H[3] \cdot 10^3 = 131$, so the answer is yes.

4. $\mathtt{0x811c9dc5} \oplus \mathtt{0x61} = \mathtt{0x811c9da4}$; multiplied by 16777619 modulo $2^{32}$ it gives $\mathtt{0xe40c292c}$.

5. A polynomial of degree 2 over the two-element field is irreducible exactly when it has no root, and $t^2 + t + 1$ is 1 at both 0 and 1. Since $t^2 \equiv t + 1$, also $t^3 \equiv 1$, so $t^3 + t^2 + 1 \equiv 1 + (t + 1) + 1 = t + 1$: the fingerprint is $11$.

6. The windows $\texttt{abb}, \texttt{bba}, \texttt{bab}, \texttt{aba}, \texttt{baa}, \texttt{aab}$ have hashes $3, 4, 2, 2, 1, 0$, and $h(\texttt{aba}) = 2$. The occurrence is at position 3; the window $\texttt{bab}$ at position 2 is a spurious hit, since $h(\texttt{bab}) - h(\texttt{aba}) = r^2 - r + 1 = 7 \equiv 0 \pmod 7$.

7. Every one of the $n - m + 1$ windows is a real occurrence, so every window is verified at cost $m$, whatever the hash. The Monte Carlo variant runs in $O(n + m)$ time and is right here, since it has no false matches to make; its risk on other inputs is a false occurrence, with probability at most $(n - m + 1)(m - 1)/p$.

8. $h(\texttt{abab}) - h(\texttt{baba}) = -t^3 + t^2 - t + 1 = -(t - 1)(t^2 + 1)$. Modulo 13 the roots are $1$ and the square roots of $-1$, which are $5$ and $8$. So 3 of the 13 bases collide, exactly the bound $3/13$.

9. There are $\binom{N}{2} \approx 2 \cdot 10^{10}$ pairs, each colliding with probability at most about $1/p$, so about 20 collisions are expected. For less than $0.01$ you need $p \ge 2 \cdot 10^{12}$; the prime $2^{61} - 1$ gives about $10^{-8}$.

10. $xyxy = 100 \cdot \overline{xy} + \overline{xy} = 101 \cdot \overline{xy}$, since $10^2 \equiv -1$. In general, every square $u\,u$ with $|u| = k$ has hash $h(u)(r^k + 1) \equiv 0$, so all such squares collide with each other.

11. $s[i..j]$ has period $d$ exactly when $s[i..j-d] = s[i+d..j]$, one substring comparison. It is a square exactly when its length $2k$ is even and its two halves $s[i..i+k-1]$ and $s[i+k..j]$ are equal.

12. If a substring of length $L$ occurs twice, so do its prefixes of length $L - 1$, so the answer "some length-$L$ substring repeats" is monotone. For a given $L$, put the hashes of all $n - L + 1$ windows in a hash table and look for a repeat, in $O(n)$ expected time; binary search adds a factor $\log n$.

13. Find the longest common prefix by binary search on its length, comparing hashes, then compare the next symbol. Sorting makes $O(n \log n)$ comparisons with $O(\log n)$ hash tests each. Each test errs with probability at most $(n-1)/p$, so the union bound gives an error of $O(n^2 \log^2 n / p)$.

14. Hash each length-$m$ window of each row with a rolling hash, giving an $n \times (n - m + 1)$ array of numbers. Then run a rolling hash with a second base down each column of that array, over windows of $m$ rows, and compare with the hash of the pattern computed the same way. Each step is $O(1)$.

15. Build $s\,s$ and its prefix hashes. Keep the best start so far, and compare it with each other start by the $O(\log n)$ comparison of exercise 13 on rotations of length $n$. There are $n - 1$ comparisons.

16. Each prime factor is at least 2, so $k$ distinct factors give a product of at least $2^k$; with $|x - y| < 2^n$ this forces $k < n$. A wrong yes needs $q$ to divide $x - y$, so its probability is below $n/\pi(M)$, where $\pi(M)$ is the number of primes up to $M$.

17. There are $2^{62}$ strings and fewer than $2^{61}$ hash values, so two strings share a value. The bound is for a fixed pair over a random base. For each base some pair collides, but different bases need different pairs, and a pair chosen before the base still collides with probability at most $61/p$.

18. At each alignment, find the first mismatch by a longest-common-extension query, done by binary search on prefix hashes of the text and the pattern in $O(\log m)$ time. Skip it and repeat. At most $k + 1$ queries decide the alignment, so the total is $O(nk \log m)$, with the usual error bound per query.

19. Split the string at its middle. A square that crosses the middle has its first half or its second half covering the middle; for each half-length $\ell$ and each side, two extension queries from the middle, one forward and one backward, decide whether such a square exists. That is $O(n)$ queries of $O(\log n)$ time each per level of the recursion, and there are $O(\log n)$ levels.

20. Use an implicit treap or splay tree keyed by position. Each node stores the hash of its subtree read forward and read backward, its size, and a lazy reversal flag. A reversal splits off the range, sets the flag, which swaps the two hashes, and joins the parts. A substring is a palindrome when its two hashes agree.

21. For each string $x$ and each position $i$, compute the hash of $x$ with position $i$ replaced by a symbol that occurs nowhere, from prefix and suffix hashes in $O(1)$ time. Group the triples (length, $i$, hash) in a hash table. Two different strings in one group differ exactly at position $i$, after a check that rules out collisions.
