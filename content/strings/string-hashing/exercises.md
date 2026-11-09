1. ◦ With the codes $\texttt{a} = 1$, $\texttt{b} = 2$, $\texttt{c} = 3$, $\texttt{d} = 4$, the base $r = 10$ and $p = 101$, compute the [polynomial hash](/polynomial-rolling-hash/) of $\texttt{abc}$. Then slide the window one step along $\texttt{abcd}$ with the update rule, and check the result against the hash of $\texttt{bcd}$ computed directly.

2. ◦ With the codes $\texttt{a} = 1$ and $\texttt{b} = 2$ and a prime $p$, for which bases $r$ do $\texttt{ab}$ and $\texttt{ba}$ have the same hash? Compare with the [collision bound](/polynomial-hash-collision-bound/).

3. ◦ For $T = \texttt{banana}$ with the codes $\texttt{a} = 1$, $\texttt{b} = 2$, $\texttt{n} = 3$ and the base 10, with $p$ large enough that no reduction happens, write the prefix hashes $H[0..6]$. Use them to answer the [substring equality query](/substring-equality-queries/) $T[1..3] = T[3..5]$.

4. ◦ The 32-bit [FNV-1a](/fnv-hash/) hash starts from $\mathtt{0x811c9dc5}$ and uses the prime $16777619$. Compute the hash of the one-byte string $\texttt{a}$ ($\mathtt{0x61}$).

5. ◦ Show that $t^2 + t + 1$ is irreducible over the field of two elements, and compute the [Rabin fingerprint](/rabin-fingerprint/) of the bit string $1101$ with this polynomial.

6. ◦ Run [Rabin-Karp](/rabin-karp/) for the pattern $\texttt{aba}$ in the text $\texttt{abbabaab}$, with the codes $\texttt{a} = 1$, $\texttt{b} = 2$, the base $r = 3$ and $p = 7$. List the hash of every window, the occurrences and the [spurious hits](/spurious-hit/).

7. ◦ Rabin-Karp with verification searches for $a^m$ in $a^n$. Explain why it takes $\Theta(nm)$ time for every choice of $p$ and $r$. What does the Monte Carlo variant, which skips the verification, risk on this input?

8. • With the codes $\texttt{a} = 1$, $\texttt{b} = 2$ and $p = 13$, find every base for which $\texttt{abab}$ and $\texttt{baba}$ collide, by factoring their difference polynomial. Is the bound $(n-1)/p$ reached?

9. • A program stores the hashes of $N = 2 \cdot 10^5$ different strings, with a random base modulo $p = 10^9 + 7$, and assumes that all hashes differ. Estimate the expected number of colliding pairs. How large must $p$ be for the expectation to be below $0.01$?

10. • With $p = 101$ and the base 10, the hash of a string of decimal digits is the number it spells modulo 101. Show that every four-digit string of the form $xyxy$ has hash 0. Generalize: for which strings of length $2k$ does the same happen whenever $r^k \equiv -1 \pmod p$? This is a simple [anti-hash test](/anti-hash-tests/).

11. • Using prefix hashes, show how to decide in $O(1)$ time whether a substring $s[i..j]$ has period $d$, and whether it is a square, a string of the form $x\,x$.

12. • Find the [longest repeated substring](/longest-repeated-substring/) of a string of length $n$ in $O(n \log n)$ expected time with hashing. Why may you binary search on the length?

13. • Show how to compare two substrings of a fixed text in lexicographic order in $O(\log n)$ time with prefix hashes, and use it to sort all suffixes in $O(n \log^2 n)$ time. Bound the probability that the result is wrong.

14. • Extend Rabin-Karp to two dimensions: find all occurrences of an $m \times m$ pattern in an $n \times n$ text in $O(n^2)$ expected time, for $m \le n$.

15. • Find the [minimal rotation](/minimal-rotation/) of a string of length $n$ in $O(n \log n)$ time with hashing. Which string do you build first?

16. • In Karp and Rabin's original fingerprint, an $n$-bit string is read as a number $x$ and reduced modulo a prime $q$ drawn at random from the primes up to $M$. Show that a nonzero integer below $2^n$ has fewer than $n$ distinct prime factors, and deduce a bound on the probability that $x \ne y$ but $x \equiv y \pmod q$.

17. • For $p = 2^{61} - 1$ and any fixed base, show that two binary strings of length 62 with the same hash must exist. Why does this not contradict the collision bound?

18. ★ Give an algorithm that finds all positions where a pattern of length $m$ occurs in a text of length $n$ with at most $k$ mismatches, in $O(nk \log m)$ time with prefix hashes.

19. ★ Decide whether a string of length $n$ contains a square, a substring of the form $x\,x$ with $x$ nonempty, in $O(n \log^2 n)$ time with hashing. Use divide and conquer on the position of the square.

20. ★ Keep a string under three operations, each in $O(\log n)$ expected time: change one symbol, reverse a substring, and test whether a substring is a palindrome. Use a balanced tree whose nodes store hashes.

21. ★ Given $k$ strings of total length $N$, find all pairs of strings of the same length that differ in exactly one position. Use $O(N)$ hash values, and say how the pairs are read off.
