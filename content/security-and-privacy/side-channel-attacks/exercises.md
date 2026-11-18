In these exercises left-to-right square and multiply starts from the value 1, squares once for every bit of the exponent from the top bit down, and multiplies by the base after the squaring when the bit is 1, as in the [timing attack](/timing-attack/) entry.

1. ◦ Write the list of per-bit costs, in multiplications, of square and multiply for the exponent $d = 89$. What are the total, the number of squarings and the number of multiplications by the base?

2. ◦ A stopwatch shows that square and multiply with a 20-bit secret exponent (top bit 1) did 31 multiplications in all. (a) What is the Hamming weight of the exponent? (b) How many 20-bit exponents are consistent with this reading, and how many bits of the key has the reading given away, compared with the $2^{19}$ exponents possible before?

3. ◦ The Montgomery ladder does one squaring and one multiplication for every bit. For an 8-bit exponent, what is its list of per-bit costs? Square and multiply on a random 8-bit exponent, with the top bit 1 and the other seven bits fair coin flips, does how many multiplications on average? How much slower is the ladder, as a ratio?

4. ◦ An ECDSA implementation runs its scalar multiplication loop once for each bit of the nonce, and the nonces are uniform in $[0, 2^{256})$. An attacker keeps the signatures whose nonce is below $2^{252}$. What fraction of the signatures is that, and about how many signatures must the attacker collect to keep 100?

5. • A server checks a 16-byte MAC tag with a byte comparison that returns at the first byte that differs, and the attacker can tell from the time how many bytes matched. Describe how to forge the tag for a chosen message byte by byte, and give the largest number of tags the attacker must try. Compare with guessing the whole tag.

6. • Take [Montgomery multiplication](/montgomery-multiplication/) with $n = 13$ and $R = 16$, so that $\mathrm{Mont}(a, b) = a b R^{-1} \bmod 13$, computed as $t = ab$, $m = (t \bmod R)\, n' \bmod R$ with $n' = -n^{-1} \bmod R$, $u = (t + mn)/R$, and an extra reduction $u \leftarrow u - n$ when $u \ge n$. (a) Find $n'$. (b) Compute $\mathrm{Mont}(7, 11)$ and $\mathrm{Mont}(3, 4)$, and say for each whether the extra reduction happens. (c) Write a short program to count the pairs $0 \le a, b \le 12$ for which it happens.

7. • A fixed-window exponentiation reads the exponent in windows of 2 bits from the top. For each window $w$ it squares twice and then, if $w \ne 0$, multiplies by the table entry $c^w$. (a) Give the per-window costs and the table indices read for $d = 157 = 10011101_2$ and for $d = 135 = 10000111_2$. (b) What does an attacker learn from the costs alone, and what from the addresses of the table reads?

8. • Each timing measurement has noise with standard deviation 400 cycles, and the attacker wants to see a difference of 20 cycles between the mean times of two sets of inputs. With $k$ independent measurements in each set, the standard error of the difference of the two means is $400 \sqrt{2/k}$. How large must $k$ be for the standard error to be at most a third of the difference?

9. • Write a branch-free select that returns $x$ when the bit $b$ is 1 and $y$ when $b$ is 0, using only negation, AND and XOR on 4-bit words. Check it on $x = 1010_2$ and $y = 0110_2$ for both values of $b$. Why is a select written this way still not enough to call the compiled code constant time?

10. ★ RSA blinding computes $(c\, r^e)^d \bmod N$ for a random $r$ and then multiplies by $r^{-1}$. Assume $r$ is uniform over the units modulo $N$ and $\gcd(e, \varphi(N)) = 1$. Prove that for every unit $c$ the blinded input $c\, r^e \bmod N$ is uniform over the units, and conclude that the distribution of the number of extra reductions is the same for every chosen $c$.

11. ★ In Kocher's attack the bits of $d$ are recovered from the top, and each test uses the bits found so far to simulate the device. Suppose one bit is guessed wrong and the attack goes on. What do the tests of the following bits show, and how can the attacker use this to find and correct the error?
