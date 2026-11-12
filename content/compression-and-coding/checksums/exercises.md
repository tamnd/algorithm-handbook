1. ◦ The ASCII string "ABC" is the three bytes 0x41, 0x42, 0x43. Compute its even [parity bit](/parity-bit/), its XOR [longitudinal redundancy check](/longitudinal-redundancy-check/), the sum of its bytes modulo 256, and the Modbus LRC, which is the two's complement of that sum.

2. ◦ Compute by hand the CRC of the data bits 110101 with the generator $G = x^3 + x + 1$ (bits 1011), with no initial value and no final XOR: append three zeros and divide 110101000 by 1011 over GF(2). Give the remainder and the codeword, and check that the codeword leaves remainder 0.

3. ◦ Using [GF(2) polynomial arithmetic](/gf2-polynomial-arithmetic/), compute the carry-less product of 0x0F with itself and compare it with the integer product $15 \cdot 15$. Then compute $(x^4 + x + 1)^2$. What rule for squares over GF(2) do the two results show?

4. ◦ Compute the [Internet checksum](/internet-checksum/) of the three 16-bit words 0x8001, 0xF203, 0x1234: give the ones' complement sum and the checksum. Then a little-endian machine reads the same six bytes as the words 0x0180, 0x03F2, 0x3412. What sum does it get, and how is it related to the first?

5. ◦ Compute the [Fletcher-16](/fletcher-checksum/) checksum $B \cdot 256 + A$ (both sums modulo 255) and the [Adler-32](/adler-32/) checksum of the two-byte messages "ab" and "ba". In each checksum, which of the two sums tells the messages apart?

6. ◦ Find the check digit of the ISBN-10 0-201-89683-?, the check digit of the ISBN-13 978-0-201-89683-?, and the [Luhn](/luhn-algorithm/) check digit of the payload 12345. Use the rules of [check digit computation](/check-digit-computation/).

7. ◦ A clerk computes $4567 \cdot 238 = 1089646$. Does [casting out nines](/casting-out-nines/) catch the mistake? Does the check by elevens? The correct product is 1086946; what kind of error did the clerk make?

8. ◦ Compute the [Verhoeff](/verhoeff-algorithm/) check digit and the [Damm](/damm-algorithm/) check digit of the payload 12345, and then of 012345, using the tables in the two entries. Which algorithm gives the same digit for both?

9. ◦ An 8-bit CRC generator is listed in Koopman's notation as 0x9B. Write its full polynomial in hexadecimal and as a sum of powers of $x$, and give its normal and its reversed notation, as defined in the entry on the [generator polynomial](/crc-generator-polynomial/).

10. • A header has the Internet checksum HC = 0x1A2B, and one of its 16-bit fields changes from 0x0000 to 0x1234. Compute the new checksum with the rule of RFC 1624 from [incremental checksum update](/incremental-checksum-update/). Check your answer by recomputing the checksum of the three-word header 0x4500, 0x0000, 0xA0D4 before and after the change.

11. • Compute the entries $T[1]$, $T[2]$, $T[\text{0x80}]$ and $T[\text{0xFF}]$ of the byte table of CRC-8/SMBUS (poly 0x07, not reflected), where $T[v] = v \cdot x^8 \bmod G$ as in the [table-driven CRC](/table-driven-crc/). Show that $T[a \oplus b] = T[a] \oplus T[b]$, and use it to get $T[\text{0x81}]$ without a division.

12. • For $G_1 = x^4 + x + 1$ and $G_2 = x^4 + x^3 + x^2 + x + 1$, find the period $e$, the least $e > 0$ with $G \mid x^e + 1$. For each, what is the longest codeword in which every two-bit error is caught, and which two-bit error is missed in a codeword one bit longer? Does either generator catch every error of odd weight?

13. • Eight data bytes are written as an $8 \times 8$ array of bits. Each row gets a parity bit, the column parities form an LRC byte, and one corner bit makes the parity row even, giving a $9 \times 9$ array in which every row and column has even weight. Show that every error of weight 1, 2 or 3 is detected, and count the undetected errors of weight 4.

14. • The single-parity-check code of length $n$ has $\binom{n}{i}$ codewords of each even weight $i$. Show that its [undetected error probability](/undetected-error-probability/) is $P_{ud}(p) = \tfrac{1}{2}\bigl(1 + (1 - 2p)^n\bigr) - (1 - p)^n$. Evaluate it for $n = 8$ at $p = 0.01$ and at $p = 1/2$, and prove that the code is proper for every $n$.

15. • Adler-32 can serve as a [rolling checksum](/rolling-checksum/). For a window of $L$ bytes, derive the update of $s_1$ and $s_2$ modulo 65521 when the byte $x_{\text{out}}$ leaves on the left and $x_{\text{in}}$ enters on the right. How does it differ from the rsync update, and why? Check it on the string "checksums" with $L = 4$, moving from the window "chec" to "heck".

16. • For an Adler-32 checksum of $n$ bytes, give upper bounds on $s_1$ and $s_2$ before any reduction. What is the smallest $n$ for which $s_1$ can reach 65521? For $n = 4$, how many of the 32 bits of the checksum can ever be 1? Check your bounds with the message of four 0xFF bytes.

17. • Count the irreducible polynomials of degree 8 over GF(2), the primitive polynomials of degree 8, and the 8-bit CRC generators of the form $(x + 1)\,p(x)$ with $p$ primitive of degree 7. Which kind of generator gives distance 3 at the longest lengths, and which gives distance 4?

18. • Compute the CRC-32 (ISO-HDLC, as in zlib) of the message "abc" followed by its own CRC written as four bytes, low byte first. Do the same for the empty message. Explain why both give the same value, and how that value is related to the residue 0xDEBB20E3 listed in the catalogue for this CRC.

19. • The ISBN-13 978-0-201-89683-1 is valid. Swap the adjacent digits 8 and 3 near its end to get 978-0-201-89638-1. Is the result valid? Is the ISBN-10 0-201-89638-4, with the same swap, valid? Explain both answers from the weights.

20. • How much memory do the tables of slicing-by-16 for CRC-32 take, and the tables of slicing-by-8 for CRC-64? For a 2051-byte message, how many dependent table steps does the byte-wise CRC take, how many does [slicing-by-8](/slicing-by-8/) take, counting one per 8-byte block and one per leftover byte, and how many does slicing-by-16 take?

21. • rsync compares every window of a new file of $2^{30}$ bytes with $2^{14}$ blocks of the old file by a 32-bit weak checksum, and computes the strong hash only when the weak checksum matches. If the weak checksum behaved like a uniform random 32-bit value, about how many windows would match by chance? Give one property of the sums $a$ and $b$ that makes real data produce more chance matches.

22. • Prove that a leading zero never changes the Damm check digit. Then compute the Verhoeff check digits of 7, 07 and 007, and explain from the permutation $\sigma$ why they differ.

23. ★ The generator of CRC-16/ARC is 0x18005, that is $x^{16} + x^{15} + x^2 + 1$. Show that it equals $(x + 1)(x^{15} + x + 1)$. Given that $x^{15} + x + 1$ is primitive, prove that the CRC has Hamming distance at least 4 for every data length up to 32,751 bits and distance 2 at 32,752 bits, and give a two-bit error it misses at that length. Why is the distance never 3?

24. ★ Find the four bytes that must follow "abc" so that the CRC-32 (ISO-HDLC) of the seven bytes is 0xCBF43926, the check value of "123456789". Prove that for every message and every target there is exactly one such four-byte suffix.

25. ★ Let $c_1$ = CRC-32(A) and $c_2$ = CRC-32(B), where B has $\ell$ bytes, with init and xorout 0xFFFFFFFF. Show that CRC-32(A followed by B) $= (c_1 \cdot x^{8\ell} \bmod G) \oplus c_2$, where the product acts on the register as a polynomial, and explain why the init and the xorout cancel. Show how to get $x^{8\ell} \bmod G$ with $O(\log \ell)$ products, and check the formula on A = "hello " and B = "world".

26. ★ Take the generator $x^8 + 1$ and codewords of 16 bits. Show that the codewords are the byte strings of the form $(m, m)$, and derive $P_{ud}(p) = \bigl((1 - p)^2 + p^2\bigr)^8 - (1 - p)^{16}$. Find $P_{ud}(1/2)$, and show that the code is improper by locating the maximum of $P_{ud}$ on $[0, 1/2]$ numerically.

27. ★ Prove that the Internet checksum detects every burst error of at most 15 bits, aligned or not. Then show that, when the data are not all zero before or after the error, a burst of exactly 16 bits is missed if and only if it turns 16 adjacent 0 bits into 1 bits or 16 adjacent 1 bits into 0 bits, and give an example where those 16 bits are not one aligned word.
