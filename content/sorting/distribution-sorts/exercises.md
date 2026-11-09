1. ◦ Run [counting sort](/counting-sort/) on the keys $\langle 3, 1, 0, 3, 2, 1, 3 \rangle$ with $k = 4$. Give the array $C$ after the counting pass and after the prefix sums, and the output $B$. To which index of $B$ does the first 3 of the input go?

2. ◦ Run [LSD radix sort](/radix-sort/) in base 10 on $\langle 312, 47, 205, 81, 140, 7, 263 \rangle$. Show the array after each pass. In the second pass, which keys tie on their digit, and which earlier pass decides their order?

3. ◦ A programmer writes counting sort with *inclusive* prefix sums, so that $C[v]$ is one past the end of the block of $v$, but keeps the placing pass from left to right, with $C[v] \leftarrow C[v] - 1$ before each write. Run this version on three items $x, y, z$ with keys $1, 0, 1$. Is the output sorted? Is it stable?

4. ◦ Run [bucket sort](/bucket-sort/) with $n = 8$ buckets on $\langle 0.61, 0.07, 0.93, 0.55, 0.12, 0.58, 0.31, 0.04 \rangle$. Give the bucket sizes $n_j$, the sum $\sum_j n_j^2$, and the number of shifts that the insertion sorts make in all.

5. ◦ Run the first partition of [radix exchange sort](/radix-exchange-sort/) on the 3-bit keys $\langle 5, 2, 7, 0, 6, 3, 1 \rangle$, on the most significant bit. Show the array after the partition and the index $i$ where the part with bit 1 starts.

6. ◦ You sort $n = 2^{20}$ keys of 32 bits with LSD radix sort and digits of $r$ bits. Compute the model cost $\lceil 32/r \rceil (n + 2^r)$ for $r = 4, 8, 11, 16$ and $32$. Which $r$ is best, and why is $r = 32$ so bad?

7. ◦ Find the distinguishing prefix of each string of $\{\text{apple}, \text{apricot}, \text{banana}, \text{band}, \text{bandana}, \text{cherry}\}$. Compute $D$ and the total length $N$, as defined in [string sorting](/string-sorting/).

8. ◦ [MSD radix sort](/msd-radix-sort/) with an alphabet of $R$ characters and no cut-off sorts the two strings $\mathtt{a}^L\mathtt{b}$ and $\mathtt{a}^L\mathtt{c}$, where $\mathtt{a}^L$ is $L$ copies of a. How many tasks with two strings does it run, and how many counters does it set up in all? How many characters does insertion sort read on the same input?

9. ◦ Sort $\langle 8, 1024, 33, 5, 700, 91 \rangle$ by the method for integers of [sorting variable-length items](/sorting-variable-length-items/): group by length, then sort each group. Give the groups. How many digits does the method read, and how many would LSD radix sort read after padding every key to four digits?

10. • Show that the *first* pass of LSD radix sort may use any sort on digit 0, stable or not, and the output is still sorted, but that each later pass must be stable. Is the whole sort still stable if only the first pass is unstable?

11. • Given $n$ integers in $\{0, \ldots, k-1\}$, show how to spend $O(n + k)$ time on preprocessing so that afterwards any question "how many of the integers lie in $[a, b]$?" is answered in $O(1)$ time.

12. • Sort $n$ points $(x, y)$ with integer coordinates $0 \le x, y < n$ in lexicographic order (by $x$, then by $y$) in $O(n)$ time. In what order do the two passes go? If $n = 10^6$ and you use 8-bit digits instead of base $n$ on the keys $xn + y$, how many passes do you need?

13. • Bucket sort uses $m$ buckets for $n$ independent keys, uniform on $[0, 1)$. Show that $\mathbb{E}\big[\sum_j n_j^2\big] = n(1 - 1/m) + n^2/m$. What is the expected time with $m = \lceil \sqrt{n} \rceil$ buckets? With $m = n/10$, as in [flashsort](/flashsort/)?

14. • The keys of bucket sort are independent, with a density $f$ on $[0, 1)$ that satisfies $f(x) \le c$ for all $x$, for a constant $c$. Show that bucket sort with $n$ buckets still runs in expected $O(n)$ time, with no change to the algorithm.

15. • Radix sort sorts $n$ distinct integers from $\{0, \ldots, n^2 - 1\}$ in $O(n)$ time. Show that every [comparison sort](/comparison-sort/) still needs $\lceil \lg n! \rceil$ comparisons in the worst case on such keys. What does radix sort do that a comparison sort may not?

16. • Find an input of four one-character strings on which the permutation pass of [American flag sort](/american-flag-sort/) changes the order of two equal strings. Use two copies each of a and b, and tell the copies apart by a mark.

17. • An IEEE 754 floating-point number is stored as a sign bit, then the exponent, then the fraction. Explain why, to sort floats with a radix sort on their bit patterns as unsigned integers, you flip only the sign bit of a non-negative number but *all* bits of a negative number. Where do $-0.0$ and $+0.0$ end up?

18. • For $w$-bit keys with $w \ge \lg n$, LSD radix sort with $r$-bit digits costs $\lceil w/r \rceil (n + 2^r)$ steps in the model of the [radix sort time bound](/radix-sort-time-bound/). Show that no choice of $r$ gives less than $wn/\lg n$, and that $r = \lfloor \lg n \rfloor$ is within a constant factor of this.

19. • Sort $n$ dates between the years 1900 and 2099 in linear time with three counting sorts. In what order do you sort on day, month and year, and how many buckets does each pass use?

20. • Run the bottom-up method for strings of [sorting variable-length items](/sorting-variable-length-items/) on $\{\text{bab}, \text{a}, \text{ab}, \text{ba}, \text{b}\}$. Show the list before and after each pass, and count the characters read. Why must the strings of length exactly $j$ go to the front of the list in pass $j$?

21. ★ Let each key be $X = U^4$, where $U$ is uniform on $[0, 1)$, and the keys are independent. Show that bucket sort with $n$ buckets and insertion sort takes $\Theta(n^{3/2})$ expected time on these keys. Then give a bucket map that brings the expected time back to $\Theta(n)$.

22. ★ In bucket sort with $n$ buckets on $n$ independent uniform keys, show that for $n$ large enough, with probability at least $1 - 1/n$, no bucket holds more than $3 \ln n / \ln \ln n$ keys.

23. ★ Radix exchange sort runs on $n$ keys of $w$ bits whose bits are independent and uniform. Count one inspection for each key in each task of at least two keys. Show that the expected number of inspections is at most $n(\lceil \lg n \rceil + 2)$.

24. ★ A word of the word RAM holds $q$ fields of $k + 1$ bits each: a test bit on top and a $k$-bit number below. Words $X$ and $Y$ hold the numbers $x_0, \ldots, x_{q-1}$ and $y_0, \ldots, y_{q-1}$. Show how to compute, with a constant number of word operations, a word whose test bit in field $i$ is 1 exactly when $x_i \ge y_i$. (This is the step that lets the integer sorts of [Han](/han-integer-sort/) and others compare many keys at once.)

25. ★ Prove that the bottom-up method for strings of [sorting variable-length items](/sorting-variable-length-items/) is correct: after pass $j$, the list holds exactly the strings of length at least $j$, in the order of their suffixes that start at position $j$.
