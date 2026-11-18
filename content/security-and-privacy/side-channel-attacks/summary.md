## What to remember

- A timing attack treats the device as a function $T(c) = f(c, d) + \text{noise}$ of the input $c$ and the secret $d$, and inverts $f$ in $d$, piece by piece. The algorithm can be correct and the implementation still leak.
- Left-to-right square and multiply costs $1 + d_i$ multiplications for bit $d_i$. The total, $k + \mathrm{wt}(d)$ for a $k$-bit exponent, gives the Hamming weight; the list of per-bit costs gives the whole exponent. For $d = 157 = 10011101_2$ the list is $2, 1, 1, 2, 2, 2, 1, 2$.
- Kocher's attack needs only a step whose cost the attacker can predict from the input and a guess of the next bit. A right guess splits the inputs into two sets with different mean times; a wrong guess gives equal means.
- Noise averages away: over $k$ repeats of one query the standard error falls as $1/\sqrt{k}$, so a small but stable difference is enough.
- The extra reduction of Montgomery multiplication happens for some operands and not others. On the entry's toy key the private operation does 183 Montgomery multiplications, of which 21 or 36 need the extra reduction for two chosen ciphertexts, the same every time.
- [RSA blinding](/rsa-blinding/) runs the exponentiation on $c\, r^e \bmod N$ for a fresh random $r$, so a repeated query is not a repeated measurement.
- A constant operation count is necessary, not sufficient. Branches, memory addresses, early exits and data-dependent instructions all leak, and a compiler can undo careful source code. Constant-time code removes the timing channel only for the leakage model it was written against; check the binary.

## Leaks and fixes

| leak | what the attacker sees | what it gives | fix |
|---|---|---|---|
| square and multiply, total time | $k + \mathrm{wt}(d)$ | the Hamming weight of $d$ | Montgomery ladder |
| square and multiply, per-step cost | $1 + d_i$ for each bit | every bit of $d$ | Montgomery ladder |
| Montgomery extra reduction | a count that depends on $c$ | bits of a prime factor, by Brumley and Boneh | blinding |
| table lookup at a secret index | which cache lines were used | the index, as for AES tables and exponent windows | no secret addresses |
| early-exit comparison or error path | how far the check got | the correct prefix, or a padding oracle | one uniform error path |
| loop over the bits of a nonce | the bit length of the nonce | the key, through a lattice attack (Minerva, TPM-Fail) | fixed loop length |

: The leaks of the [timing attack](/timing-attack/) entry. The Montgomery ladder does one squaring and one multiplication for every bit, so its per-step cost is the constant 2.

## Checking an implementation

Write the code with no branch, loop bound or memory address that depends on a secret, and with arithmetic by masks instead of `if`. Blind RSA inputs even when the code is believed to be constant time, because blinding also covers leaks you did not think of. Then measure the compiled binary on two classes of inputs and test whether the distributions of its running times differ; a count of operations in the source is not enough evidence.
