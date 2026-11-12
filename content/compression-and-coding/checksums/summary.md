## What to remember

- A check of $r$ bits takes $2^r$ values, so on long messages it misses some errors; under random errors a good one misses about $2^{-r}$. The methods differ in which small errors they are sure to catch.
- The [parity bit](/parity-bit/) catches every odd number of bit errors and no even number. The XOR [LRC](/longitudinal-redundancy-check/) misses an error exactly when every bit column has an even number of errors, so it catches every burst of at most 8 bits.
- An [additive checksum](/additive-checksum/) modulo $2^k$ misses an error exactly when the changes add to $0 \bmod 2^k$, and never sees word order. The [Internet checksum](/internet-checksum/) takes the sum modulo $2^{16} - 1$ in [ones' complement](/ones-complement-arithmetic/). It does not depend on byte order, catches every burst of at most 15 bits, and RFC 1624 patches it in $O(1)$ by $HC' = \sim(\sim HC + \sim m + m')$.
- [Fletcher](/fletcher-checksum/) adds a second sum of the running sums, which weights each word by its distance from the end; modulo 255 it confuses 0x00 with 0xFF. [Adler-32](/adler-32/) works modulo the prime 65521 and catches every error confined to two bytes less than 65521 apart, but on $n$ bytes $s_1 \le 1 + 255n$, so short messages waste most of its 32 bits.
- A [CRC](/cyclic-redundancy-check/) with generator $G$ of degree $r$ and $G(0) = 1$ misses an error $E$ exactly when $G \mid E$. So it [catches](/crc-error-detection-guarantees/) every burst of length at most $r$, every two-bit error closer than the period of $G$, and every odd number of errors when $(x + 1) \mid G$. It misses a fraction $2^{-(r-1)}$ of the bursts of length $r + 1$ and $2^{-r}$ of longer ones.
- A CRC is fixed by width, poly, init, refin, refout and xorout, and checked on "123456789". A [primitive](/crc-generator-polynomial/) $G$ gives Hamming distance 3 up to $2^r - 1 - r$ data bits, and $(x + 1)$ times a primitive polynomial gives distance 4 up to $2^{r-1} - 1 - r$.
- The [undetected error probability](/undetected-error-probability/) is $P_{ud}(p) = \sum_i A_i p^i (1-p)^{n-i}$, with $P_{ud}(1/2) = (2^k - 1)/2^n$. An improper code, such as $x^8 + 1$ at 64 bits, goes far above $2^{-r}$ at moderate $p$.
- Fast CRCs trade memory for parallel work: one 256-entry [table](/table-driven-crc/) (1 KiB for CRC-32), eight tables for [slicing-by-8](/slicing-by-8/) (8 KiB), or carry-less multiplies that [fold](/clmul-crc-folding/) four 128-bit blocks at once.
- No weighted sum modulo 10 catches every single error and every adjacent swap. [Luhn](/luhn-algorithm/) misses only the swap of 09 and 90; [Verhoeff](/verhoeff-algorithm/) and [Damm](/damm-algorithm/) miss none.

| Method | Bits | Always caught | Typical miss | Check of "123456789" |
|---|---|---|---|---|
| Parity | 1 | odd weight | two bit errors | 1 (even) |
| LRC (XOR) | 8 | bursts $\le 8$, odd weight | two errors in one column | 0x31 |
| Sum mod 256 | 8 | one-byte errors | swapped bytes | 0xDD |
| Internet checksum | 16 | bursts $\le 15$ | reordered words | — |
| Fletcher-16 | 16 | bursts $\le 7$ | a byte 0x00 to 0xFF | — |
| Adler-32 | 32 | two bytes $< 65521$ apart | short messages | — |
| CRC-8/SMBUS | 8 | bursts $\le 8$, odd weight | two errors $127k$ apart | 0xF4 |
| CRC-32/ISO-HDLC | 32 | bursts $\le 32$; HD 4 to 91,607 bits | — | 0xCBF43926 |
| CRC-32C | 32 | bursts $\le 32$; HD 6 to 5,243 bits | — | 0xE3069283 |

: Checksums of the chapter. The check values are those of the entries and of Greg Cook's catalogue; Hamming distances are Koopman's, in data bits.

## Choosing a method

When a standard names the check, use exactly its parameters and test against its check value: a CRC with one wrong parameter looks fine and agrees with nobody. For a new protocol or format, use CRC-32C, which has an instruction on x86 (SSE4.2) and ARMv8. Use the Internet checksum or Fletcher only where required or where routers patch the check in place, and Adler-32 only inside zlib. For a CRC on messages of known length, compare the Hamming distance profiles of the generators at that length.

For numbers that people type, use Verhoeff or Damm in a new scheme, and Luhn, ISBN or IBAN where a standard requires them. Fix the number of digits for Verhoeff, since a leading zero changes its check digit.

None of these methods resists an attacker. Use a MAC such as [HMAC](/hmac/) when the data may be changed on purpose.
