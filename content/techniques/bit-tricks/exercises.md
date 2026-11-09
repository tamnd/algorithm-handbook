1. ◦ Write the 8-bit [two's complement](/twos-complement/) patterns of $-1$, $-37$ and $-128$. Then give the value of the pattern $10110100_2$ read as an unsigned and as a signed 8-bit word.

2. ◦ The 5-bit field $v = 10110_2$ holds a signed number. Give its value, and [sign-extend](/sign-extension/) it to 8 bits with the formula $(v \oplus m) - m$, $m = 2^4$. Write the result in binary.

3. ◦ For the 8-bit word $x = 01011000_2$, compute $x \wedge (-x)$, $x \wedge (x - 1)$, $\operatorname{ctz}(x)$, $\lfloor \lg x \rfloor$, $\operatorname{clz}(x)$ and $\nu(x)$.

4. ◦ Byte-swap the 32-bit word `0x0A0B0C0D`, as in [endianness conversion](/endianness-conversion/). Then [reverse the bits](/bit-reversal/) of the byte `0xD2` and give the result in hexadecimal.

5. ◦ Run [Kernighan's bit count](/kernighan-popcount/) on $x = 11100110_2$. List the value of $x$ after each round and give the count.

6. ◦ Compute the [next power of two](/next-power-of-two/) of $x = 37$ and of $x = 200$ on 8-bit words by smearing: set $y = x - 1$, apply $y \gets y \vee (y \gg s)$ for $s = 1, 2, 4$, and return $y + 1$ modulo $2^8$. Show $y$ after each step. Which of the two results is wrong, and why?

7. ◦ In the array $\langle 3, 8, 3, 5, 10, 8 \rangle$ every value occurs twice except two. Find them with XOR: compute the XOR $t$ of all elements, isolate its lowest set bit, split the array by that bit and XOR each part. Give $t$ and the two values.

8. ◦ A thousand values below 1000 are [bit-packed](/bit-packing/) into 64-bit words with $b = 10$ bits each, value $i$ starting at bit $10i$ of the array. How many words does the array use? Which indices among $0, \ldots, 31$ have a field that crosses a word boundary, and how many among $0, \ldots, 999$?

9. ◦ The [Morton code](/morton-encoding/) of a point $(x, y)$ puts bit $i$ of $x$ at bit $2i$ and bit $i$ of $y$ at bit $2i + 1$. Compute the code of $(5, 3)$ with 3-bit coordinates, and find the point whose code is $45$.

10. ◦ Run [SOS DP](/sos-dp/) for $n = 3$ on $f = \langle 2, 7, 1, 8, 2, 8, 1, 8 \rangle$, indexed by the masks $0, \ldots, 7$. Give the array after each of the three passes.

11. ◦ Start [Gosper's hack](/gospers-hack/) at $x = 00111_2$ and list the 3-element subsets of $\{0, \ldots, 4\}$ that it produces, in order, as 5-bit words. What does one more call return after the last of them?

12. • Prove that $x \oplus (x - 1)$, for a nonzero unsigned word $x$, has 1-bits exactly at the lowest set bit of $x$ and below it, so that $\operatorname{ctz}(x) = \nu(x \oplus (x - 1)) - 1$. What does this formula return for $x = 0$ on 32-bit words, and how does that compare with the formula $\nu(\overline{x} \wedge (x - 1))$ of the [trailing zero count](/trailing-zero-count/)?

13. • Show that after $y \gets x$ and $y \gets y \oplus (y \gg s)$ for $s = 1, 2, 4$, bit $i$ of the 8-bit word $y$ is the parity of bits $i, i + 1, \ldots, 7$ of $x$. Compute $y$ for $x = 10110100_2$, and explain why the same steps convert a Gray code word to binary.

14. • Write a branch-free function that returns $\operatorname{sgn}(x) \in \{-1, 0, 1\}$ for a signed 32-bit $x$, using one arithmetic right shift of $x$ and one logical right shift of $-x$, both by 31. Check it on $x = 0$, $x = 5$, $x = -5$ and $x = -2^{31}$, where $-x$ overflows.

15. • The add-and-subtract swap runs $x \gets x + y$, $y \gets x - y$, $x \gets x - y$. Prove that it swaps any two unsigned $w$-bit words, although $x + y$ may wrap around modulo $2^w$. What does it leave when $x$ and $y$ are the same memory cell? Why should it not be used on signed integers in C?

16. • In a [Fenwick tree](/fenwick-tree/) of size 16, list the indices visited from $i = 13$ by the query step $i \gets i - (i \wedge -i)$ down to 0, and by the update step $i \gets i + (i \wedge -i)$ while $i \le 16$. Prove that the query walk from any $i \ge 1$ takes exactly $\nu(i)$ steps.

17. • Count the pairs $i < j$ with $a_i \wedge a_j = 0$ in $a = \langle 1, 2, 3, 4, 6 \rangle$ on 3-bit masks, by building $c[s]$, the number of elements equal to $s$, running SOS DP on $c$, and adding up $F[\overline{a_i}]$ over all $i$. Give $F$ and the count, and say what changes when the array may contain 0.

18. • Prove that running the passes of SOS DP with subtraction in place of addition, $F[m] \gets F[m] - F[m \oplus 2^i]$ for every $m$ with bit $i$ set, inverts the transform. Use it to recover $f$ from the submask sums $F = \langle 1, 3, 4, 10, 5, 12, 13, 30 \rangle$ on 3-bit masks.

19. • With 8-bit lanes and the masks $L = $ `0x7F7F` and $H = $ `0x8080`, prove that $((x \wedge L) + (y \wedge L)) \oplus ((x \oplus y) \wedge H)$ adds the two 16-bit words lane by lane modulo $2^8$, with no carry between lanes. Compute it and the plain sum modulo $2^{16}$ for $x = $ `0x80FF`, $y = $ `0x8001`.

20. • Write the binary search for the [floor of $\lg x$](/floor-log2/) on 32-bit words with five tests, for shifts of 16, 8, 4, 2 and 1. Trace it on $x = $ `0x00000B00` and give the answer.

21. • A [bit vector](/bit-set/) over 16 items is stored in two 8-bit words, item $i$ in bit $i \bmod 8$ of word $\lfloor i / 8 \rfloor$, with $W_0 = 10110100_2$ and $W_1 = 01101111_2$. Write $\operatorname{rank}(i)$, the number of members smaller than $i$, as a sum of population counts with one mask, and compute $\operatorname{rank}(13)$.

22. • A [Roaring bitmap](/roaring-bitmap/) holds the values 70000, 5, 131071 and 65536. Give the key and the low 16 bits of each, and the containers that result. Then choose the cheapest of an array, a bitmap and a run container, in bytes, for each of three chunks: the 9000 values $1000, \ldots, 9999$; the 32768 even values $0, 2, \ldots, 65534$; and the 3000 values $0, 20, 40, \ldots, 59980$.

23. • Combine smearing with the [de Bruijn bit scan](/de-bruijn-bit-scan/) to compute $\lfloor \lg x \rfloor$: smear $x$ to $y$, isolate the top bit as $y - (y \gg 1)$, and look it up with $D = $ `0x1D` and its table on 8-bit words. Trace it on $x = 45$.

24. ★ Prove that $\nu(x) = x - \sum_{k \ge 1} \lfloor x / 2^k \rfloor$ for every integer $x \ge 0$. Explain how the first line of the [SWAR population count](/swar-popcount/), $x - ((x \gg 1) \wedge M_1)$, applies this identity to each 2-bit field.

25. ★ The OR-convolution of $f$ and $g$ on masks of $n$ bits is $h[m] = \sum_{a \vee b = m} f[a] g[b]$. Prove that the submask sums satisfy $F_h[m] = F_f[m] \cdot F_g[m]$, and derive an $O(n 2^n)$ algorithm from SOS DP and its inverse. Compute $h$ for $n = 2$, $f = \langle 1, 2, 0, 1 \rangle$, $g = \langle 0, 1, 1, 1 \rangle$.

26. ★ Gosper's hack lists the $k$-subsets of $\{0, \ldots, n - 1\}$ in [colexicographic order](/colexicographic-order/). Prove that the subset $\{c_1 < c_2 < \cdots < c_k\}$ has position $\sum_{i=1}^{k} \binom{c_i}{i}$ in that list, counting from 0, and use it to find the position of $10110_2$ among the 3-subsets of $\{0, \ldots, 4\}$.

27. ★ Let $\operatorname{less}(a, b)$ be the test $a < b \wedge a < (a \oplus b)$ on unsigned words. Prove that it holds exactly when the highest 1-bit of $a$ is below the highest 1-bit of $b$. Use it to compare two points in Z-order with the layout of Exercise 9, without computing their Morton codes.

28. ★ The de Bruijn bit scan on 8-bit words works with a constant $D$ when the top 3 bits of $(2^k D) \bmod 2^8$ differ for $k = 0, \ldots, 7$. The entry uses constants that begin with $\lg w$ zeros. Find every 8-bit $D$ for which the scan works, and characterize them: prove that $D$ works exactly when its top $\lg w - 1$ bits are 0 and its bits, read cyclically, form a de Bruijn sequence. How many constants work for $w = 16$?
