## What to remember

- The capacity of $y = Hx + w$ with power $P$ is the maximum of $\log_2\det(I + HQH^H/N_0)$ over
  $\mathrm{tr}\,Q \le P$. With the channel known at the transmitter, SVD precoding and water-filling over the
  singular values reach it. With i.i.d. Rayleigh fading known only at the receiver, equal power is optimal and
  $C = \min(N_t, N_r)\log_2\rho + O(1)$. In the Kronecker model, correlation never helps at high SNR.
- The Alamouti code is the only complex orthogonal design with rate one, and it exists for two transmit
  antennas. It has full diversity $2N_r$ and a linear ML decoder. Complex orthogonal designs for more
  antennas have rate below one, at most $3/4$ when the entries are $0$, $\pm s_k$ and $\pm s_k^*$.
- A space-time code has diversity $N_r$ times the smallest rank of a codeword difference, and its coding gain
  is set by the determinants. The diversity-multiplexing tradeoff $d^*(r)$, linear between the points
  $(k, (N_t-k)(N_r-k))$, is a high-SNR statement about exponents. The golden code reaches it on $2 \times 2$
  because its determinants do not vanish.
- ML detection is a closest vector search over $M^n$ vectors and NP-hard in general. Sphere decoding is
  exact ML, and its expected cost grows exponentially in $n$ at every fixed SNR. Zero forcing and MMSE are
  linear and suboptimal, with diversity $m - n + 1$ in i.i.d. Rayleigh fading. V-BLAST orders the streams to
  maximize the smallest SNR, but its hard cancellation propagates errors.
- With MMSE nulling, Gaussian codes and correct cancellation, successive detection reaches
  $\log_2\det(I + (E_s/N_0)H^HH)$, the capacity with equal power.
- Maximum ratio transmission is the best single beam, with SNR $P\|h\|^2/N_0$. Zero-forcing precoding gives
  each user diversity $M - K + 1$ and a sum rate that grows as $K\log_2\rho$. Dirty paper coding reaches the
  capacity region of the Gaussian MIMO broadcast channel. Weighted MMSE never lowers the weighted sum rate,
  but it stops at a stationary point.
- In massive MIMO with i.i.d. Rayleigh fading, $G^HG/M \to \mathrm{diag}(\beta_k)$: channel hardening and
  favorable propagation. With matched filtering and pilots reused between cells, the SINR tends to
  $\beta_{jjk}^2/\sum_{l\ne j}\beta_{jlk}^2$ instead of growing with $M$. This cap belongs to the
  uncorrelated model with single-cell processing; multicell MMSE on correlated channels removes it.

| Detector | Exact ML | Diversity, i.i.d. Rayleigh | Time per vector and channel |
|---|---|---|---|
| Exhaustive ML | yes | $m$ | $O(M^n nm)$ |
| Zero forcing | no | $m - n + 1$ | $O(n^2m + n^3 + nM)$ |
| MMSE | no | $m - n + 1$ in the standard analysis, more at low rates | $O(n^2m + n^3 + nM)$ |
| V-BLAST | no | first stream at least $m - n + 1$ | $O(n^3m + n^4 + nM)$ |
| K-best | only for $K \ge M^{n-1}$ | that of ZF-SIC for $K = 1$ | $O(n^2m + n^3 + n^2K + nKM\log(KM))$ |
| List sphere decoder | yes, for $L = 1$ | $m$ | $O(n^2m + n^3 + M^n(n + \log M + L))$ worst case |
| Lattice reduction with ZF or SIC | no | $m$ for lattice decoding, without the box | $O((S+1)n^2m + n^3 + nM)$ |
| AMP | no | no guarantee for small channels | $O(T(nm + nM))$ |

: The detectors of the chapter for $n$ streams, $m \ge n$ receive antennas and $M$ points per symbol. $K$,
$L$, $S$ and $T$ are the list size, the list length, the reduction steps and the iterations.

## Choosing a method

Without channel knowledge at the transmitter and with one or two receive antennas, the Alamouti code is the
simple choice for two antennas. When the rate matters more, send independent streams. MMSE is the standard linear receiver, MMSE V-BLAST adds
ordering and cancellation at a modest cost, and a K-best search or a sphere decoder gets near ML for small
$n$ and moderate $M$. A channel decoder needs soft values, which the list sphere decoder gives.

With channel knowledge at the transmitter and one user, use SVD precoding with water-filling, or a codebook
when the channel can only be fed back in a few bits. For several single-antenna users, regularized zero
forcing is the usual linear choice, close to zero forcing at high SNR and to maximum ratio transmission at
low SNR. Use block diagonalization when the users have several antennas, and weighted MMSE when the users
have different weights or the target is a weighted sum rate.

With many more antennas than users, maximum ratio processing and zero forcing are close to optimal in the
i.i.d. model. The design effort moves to pilot reuse, power control, the number of radio chains and the fronthaul.
