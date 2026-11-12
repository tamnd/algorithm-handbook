1. The three bytes have $2 + 2 + 3 = 7$ one bits, so the even parity bit is 1. The XOR is 0x40, the sum is 0xC6, and the Modbus LRC is $256 - 198 = 58$ = 0x3A.

2. The long division leaves the remainder 111, so the codeword is 110101111. Dividing it by 1011 leaves 000.

4. $\text{0x8001} + \text{0xF203} = \text{0x17204}$, which folds to 0x7205; adding 0x1234 gives the sum 0x8439 and the checksum 0x7BC6. The little-endian machine gets 0x3984, the first sum with its bytes swapped, and its checksum 0xC67B is the swap of 0x7BC6. Swapping bytes multiplies by 256 modulo 65535, so the two results always agree after a swap.

6. ISBN-10: the weighted sum $10 \cdot 0 + 9 \cdot 2 + 8 \cdot 0 + 7 \cdot 1 + 6 \cdot 8 + 5 \cdot 9 + 4 \cdot 6 + 3 \cdot 8 + 2 \cdot 3 = 172 \equiv 7 \pmod{11}$, so the check digit is 4. ISBN-13: the check digit is 1. Luhn: doubling 5, 3 and 1 gives $1 + 4 + 6 + 2 + 2 = 15$, so the check digit is 5.

7. Nines: $4 \cdot 4 = 16 \to 7$, and the digits of 1089646 add to 34, also $\to 7$, so the check passes. Elevens: $2 \cdot 7 = 14 \equiv 3$, but $1089646 \equiv 8 \pmod{11}$, so the check fails. The clerk swapped the neighboring digits 6 and 9, which changes the number by a multiple of 9.

8. Verhoeff gives 1 for 12345 and 4 for 012345. Damm gives 9 for both, because the walk starts in row 0 and $Q[0][0] = 0$.

10. $\sim HC = \text{0xE5D4}$ and $\sim m = \text{0xFFFF}$; their ones' complement sum is 0xE5D4, and adding $m' = \text{0x1234}$ gives 0xF808. The new checksum is 0x07F7. Recomputing: the old words add to 0xE5D4, checksum 0x1A2B; the new ones add to 0xF808, checksum 0x07F7.

13. A weight-1, 2 or 3 pattern leaves some row or some column with an odd number of errors. A weight-4 pattern is missed exactly when every row and every column it touches holds two of its bits, so its bits are the corners of a rectangle. There are $\binom{9}{2}^2 = 1296$ of them.

14. Sum $\binom{n}{i} p^i (1-p)^{n-i}$ over the even $i$ with $(a + b)^n + (b - a)^n$ and drop $i = 0$. For $n = 8$, $P_{ud}(0.01) \approx 2.64 \times 10^{-3}$ and $P_{ud}(1/2) = 127/256$. The derivative is $n\bigl((1-p)^{n-1} - (1-2p)^{n-1}\bigr) \ge 0$ on $[0, 1/2]$.

16. $s_1 \le 1 + 255n$ and $s_2 \le n + 255\, n(n+1)/2$. Since $1 + 255 \cdot 256 = 65281 < 65521$, $s_1$ first can reach 65521 at $n = 257$. For $n = 4$, $s_1 \le 1021$ uses 10 bits and $s_2 \le 2554$ uses 12, so only 22 of the 32 bits can be 1; four 0xFF bytes give 0x09FA03FD.

18. Both give 0x2144DF1C, which is the residue 0xDEBB20E3 XOR 0xFFFFFFFF. If the register after the message is $R$, the appended bytes are $R \oplus \text{0xFFFFFFFF}$, so they clear the message out of the register and leave a state that does not depend on the message.

23. A two-bit error $x^i(x^j + 1)$ is missed exactly when $x^{15} + x + 1$ divides $x^j + 1$, that is when $32767 \mid j$. So the first missed pair is $x^{32767} + 1$, in a codeword of 32,768 bits, which holds 32,752 data bits. A factor $x + 1$ makes every codeword have even weight, so no codeword has weight 1 or 3.

24. The suffix is the bytes e8 4c e9 c7. In the register, four bytes $s$ processed from the state $R$ give $(R \oplus s) \cdot x^{32} \bmod G$, in the bit order of the register. Multiplication by $x^{32}$ is invertible modulo $G$ because $G(0) = 1$, so the map from $s$ to the CRC is a bijection of 32-bit values.

25. Write the register before the final XOR. Processing B from a state $S$ gives $S \cdot x^{8\ell} \oplus \beta$ modulo $G$, with $\beta$ fixed by B. Apply this once with $S = c_1 \oplus F$ and once with $S = F$, where $F$ = 0xFFFFFFFF, and XOR the results: everything cancels except $c_1 \cdot x^{8\ell}$. Square $x^8$ repeatedly and multiply the powers chosen by the bits of $\ell$, as zlib's crc32_combine does. Here $c_1$ = 0xED81F9F6, $c_2$ = 0x3A771143, and the result is 0x0D4A1185, the CRC-32 of "hello world".

26. $m(x)(x^8 + 1)$ with $\deg m < 8$ is the byte $m$ written twice. There are $\binom{8}{w}$ codewords of weight $2w$, and the binomial theorem gives the formula. $P_{ud}(1/2) = 2^{-8} - 2^{-16} = 255/65536$. The maximum is about 0.0209 near $p \approx 0.136$, about 5.3 times $2^{-8}$.

27. Since $2^{16} \equiv 1 \pmod{65535}$, the ones' complement sum is the whole message read as one number modulo 65535. A burst starting at bit $s$ changes that number by $2^s \delta$ with $0 < |\delta| < 2^{b}$, and $2$ is invertible modulo 65535, so the error is missed only if $65535 \mid \delta$. For $b \le 15$ that is impossible; for $b = 16$ it forces $|\delta| = 2^{16} - 1$, all 16 bits flipped the same way. Example: the words 0x1200, 0x0034 changed to 0x12FF, 0xFF34.
