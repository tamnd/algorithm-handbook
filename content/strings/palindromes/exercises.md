1. ◦ Which of the DNA strings $\texttt{GGATCC}$, $\texttt{AAGCTT}$, $\texttt{ACGCGT}$ and $\texttt{GATTAC}$ are [reverse-complement palindromes](/reverse-complement-palindrome/)? Explain why no such string has odd length.

2. ◦ How many [palindromes](/palindrome/) of length $n$ are there over an alphabet of $\sigma$ symbols? Give the numbers for binary strings of length 6 and of length 7.

3. ◦ The string $s = \texttt{abacabad}$ has $2 \cdot 8 + 1 = 17$ centers: one before each symbol, one at each symbol, and one at the end. Write down the length of the longest palindrome at each center, as [Manacher's algorithm](/manacher/) computes it, and read off the [longest palindromic substring](/longest-palindromic-substring/).

4. ◦ For $s = \texttt{abcbab}$, count the palindromic substrings by occurrence and as distinct strings, as in [counting palindromic substrings](/count-palindromic-substrings/).

5. ◦ Find the [shortest palindrome](/shortest-palindrome/) that can be made from $\texttt{abacd}$ by adding symbols in front of it. Which value of the prefix function of $\texttt{abacd\#dcaba}$ gives the answer?

6. ◦ Compute the [palindromic closure](/palindromic-closure/) of $\texttt{aabcb}$ and of $\texttt{abc}$.

7. ◦ List all [palindromic partitions](/palindrome-partitioning/) of $\texttt{aaba}$. What is its palindromic length?

8. • Use the 17 values of exercise 3 to decide whether $s[1..5]$, $s[2..5]$ and $s[4..6]$ are palindromes, with 0-based indices. State the test for a general $s[i..j]$ as one comparison with one entry of the array, as in [palindrome substring queries](/palindrome-substring-queries/).

9. • Find the [palindrome edit distance](/palindrome-edit-distance/) of $\texttt{character}$ when only deletions are allowed, and when only substitutions are allowed.

10. • For the string $a^n$, find the number of palindromic occurrences, the number of distinct nonempty palindromes, and the number of palindromic partitions. Which of the three reaches the largest value possible for a string of length $n$?

11. • Build the [palindromic tree](/palindromic-tree/) of $\texttt{abaab}$. List its nodes, the parent and edge label of each, and its suffix links. Is $\texttt{abaab}$ a [rich string](/rich-string/)?

12. • Let $\mathrm{PL}(s)$ be the [palindromic length](/minimum-palindrome-partition/) of $s$. Prove that $|\mathrm{PL}(s\,c) - \mathrm{PL}(s)| \le 1$ for every string $s$ and symbol $c$.

13. • Estimate the expected number of palindromic occurrences in a random string of length $n$ over $\sigma$ symbols, each symbol drawn uniformly and independently. What is it for binary strings and for DNA?

14. • Symbols arrive one at a time. After each one you must say whether the string read so far is a palindrome, in $O(1)$ time per symbol. Show how to do it with two polynomial hashes, and give their update rules.

15. • Show how to compute, for every end position $j$, the length of the longest palindrome that ends at $j$, from the output of Manacher's algorithm in $O(n)$ total time. Give the answers for $\texttt{abacabad}$.

16. • A palindrome of length $L$ can be tested by hashing in $O(1)$ time, so binary search on $L$ suggests an $O(n \log n)$ algorithm for the longest palindromic substring. Why must the search be done separately for odd and even lengths? Give a string on which a single binary search over all lengths fails.

17. • How many strings of length $n \ge 2$ over $\{a, b, c\}$ have no palindromic substring of length at least 2? Generalize to $\sigma$ symbols.

18. ★ Call a string an even-palindrome product if it is a concatenation of nonempty palindromes of even length. Prove that the greedy method, which repeatedly removes the shortest nonempty even palindromic prefix, decides correctly whether a string is an even-palindrome product.

19. ★ Give an $O(nk)$ algorithm that finds the longest substring of $s$ that becomes a palindrome after at most $k$ substitutions, using [longest common extension queries](/longest-common-extension-query/) on $s$ and $s^R$.

20. ★ Compute, for every position $p$ of $s$, the number of palindromic occurrences $s[i..j]$ with $i \le p \le j$, in $O(n)$ total time. Check your method on $\texttt{abcbab}$.

21. ★ Prove that $s$ is a concatenation $u\,v$ of two palindromes, either of which may be empty, if and only if $s^R$ is a rotation of $s$. Derive a linear-time test.
