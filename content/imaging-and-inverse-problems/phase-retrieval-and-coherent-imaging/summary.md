## What to remember

- [Phase retrieval](/phase-retrieval/) asks for a signal $x$ of length $n$ from the magnitude $|X(e^{i\omega})|$ of its Fourier transform. The square of the magnitude is the Fourier transform of the autocorrelation $r$, so two signals have the same magnitude exactly when they have the same autocorrelation.
- $M \ge 2n - 1$ equally spaced samples of the magnitude determine $r$ by an inverse DFT, and no method can get more out of them. With fewer samples $r$ is aliased: $[1, 5, 6]$ and $[1, 6, 5]$ agree at $M = 3$ and differ at $M = 5$.
- Three ambiguities are always there: a shift, a conjugate reversal and a constant of modulus 1. For a real signal they reduce to sign and reversal.
- In one dimension the nontrivial ambiguities come from the zeros of the z-transform. Moving a zero from $a$ to $1/\bar a$ keeps the magnitude, so a signal can have up to $2^{n-2}$ different solutions, and almost every signal has that many. $[1, 5, 6]$ and $[2, 7, 3]$ share the autocorrelation $[6, 35, 62, 35, 6]$. A zero on the unit circle gives nothing new.
- In one dimension spectral factorization lists every solution, by finding the roots of a polynomial of degree $2n - 2$. The minimum-phase solution, with all zeros inside the unit circle, is the one a filter designer wants.
- In two or more dimensions the magnitude determines almost every image up to the trivial ambiguities. That is a statement about the solutions, not about the cost of computing one.
- The iterations alternate between the measured magnitude and what is known about the object. The error of Fienup's error reduction, the one-magnitude form of Gerchberg-Saxton, never increases, but the iteration can stop at a point that is not a solution. Hybrid input-output often does better and has no proof. PhaseLift and Wirtinger flow recover $x$ with high probability, but only for random measurements.

## The methods

| method | data | what is proved |
|---|---|---|
| spectral factorization | 1D magnitude, $M \ge 2n - 1$ | finds all solutions; cost of one root finding of degree $2n - 2$, then $2^{n-2}$ choices |
| Gerchberg-Saxton (1972) | magnitudes in two planes | alternating projections; no global guarantee |
| error reduction (Fienup 1982) | magnitude and a support or sign constraint | error does not increase; often stalls |
| hybrid input-output (Fienup 1982) | magnitude and support | nothing; good behaviour is observed |
| Griffin-Lim (1984) | STFT magnitude | distance does not increase |
| PhaseLift | random generalized measurements | exact recovery with high probability, by a semidefinite program |
| Wirtinger flow | random generalized measurements | exact recovery with high probability, by gradient descent from a spectral start |

## Checking a reconstruction

When you test a phase retrieval method on a known signal, compare the result with the truth only up to the trivial ambiguities: align shifts, try the conjugate reversal, and remove the best global phase before you measure the error. In one dimension a result that fits the data and differs from the truth may be another exact solution, not a failure; check whether its zeros are flips of the true ones. Report how many random starts were run and how many reached a given data error, since iterations started differently can end in different places.
