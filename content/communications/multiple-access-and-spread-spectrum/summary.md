## What to remember

- **Orthogonal sharing leaves rate on the table.** FDMA fits $K = \lfloor (B_t - 2B_g)/B_c \rfloor$
  channels, and TDMA loses the guard time of every slot. Under an average power limit, both reach the sum
  capacity only when the shares are in proportion to the SNRs; TDMA under a peak limit is strictly inside.
- **Despreading gains against interference, not white noise.** The
  [processing gain](/processing-gain/) $G_p = W/R$ divides interference of fixed power; it does not improve
  $E_b/N_0$.
- **m-sequences are the building block.** A primitive polynomial of degree $n$ gives period $2^n - 1$
  and the two-valued autocorrelation $N$ and $-1$. Gold and Kasami families are sums of m-sequences.
- **The Welch bound limits every family.** For $K$ unit vectors in $N$ dimensions,
  $c_{\max}^2 \ge (K - N)/(N(K - 1))$, with equality only for equiangular tight frames. Gold sets are within
  a factor of about 1.6 to 2 of it; the small Kasami set is optimal among binary sets.
- **Orthogonal codes need alignment.** OVSF codes are orthogonal unless one is an ancestor of the other,
  and Zadoff-Chu sequences have zero periodic autocorrelation off the peak when $\gcd(u, N) = 1$. Delay
  breaks the first property; a frequency offset of one bin moves the Zadoff-Chu peak.
- **The matched filter is near-far limited.** Its efficiency $\max(0, 1 - \sum_j |R_{kj}| A_j/A_k)^2$
  falls to zero when the interferers are strong enough.
- **Linear detectors trade noise for interference.** The decorrelator removes all interference for a noise
  loss of $1/(R^{-1})_{kk}$ that does not depend on the powers; the MMSE detector maximizes the SINR among
  linear detectors and tends to the decorrelator as the noise vanishes. Neither minimizes the error
  probability.
- **Cancellers are cheap and fragile.** Without noise SIC is correct under a power condition, and a wrong
  decision doubles the interference. The Jacobi form of PIC converges exactly when $\mathrm{eig}(R) \subset (0, 2)$.
- **The optimum detector is NP-hard in $K$,** by a reduction from maximum cut, for general correlation
  matrices. For fixed $K$ the search over $2^K$ vectors is polynomial.
- **Joint decoding reaches the capacity region.** The corners of the Gaussian MAC region come from
  successive cancellation of Gaussian codewords, and superposition with SIC beats time sharing on the
  degraded broadcast channel. The MPA of SCMA is a heuristic on a graph with cycles.
- **Coded random access is erasure decoding.** Coded slotted ALOHA is peeling on a bipartite graph. Its
  thresholds come from density evolution for long frames; error floors of short frames are measured.

| Receiver | Needs | Time per interval, given $z$ and $R$ | Behaviour with unequal powers | What is proved |
|---|---|---|---|---|
| Matched filter | codes | $O(1)$ per user | fails when $\sum_j \lvert R_{kj}\rvert A_j \ge A_k$ | single-user optimum when $R = I$ |
| [Decorrelator](/decorrelating-detector/) | codes | $O(K^2)$ after one $O(K^3)$ inverse | unaffected; noise raised by $(R^{-1})_{kk}$ | zero interference, optimal near-far resistance |
| [MMSE detector](/mmse-multiuser-detector/) | codes, amplitudes, noise level | $O(K^2)$ after one $O(K^3)$ factor | good; tends to the decorrelator | largest SINR of linear detectors |
| [SIC](/successive-interference-cancellation/) | codes, amplitude order | $O(K^2)$ | helped by large differences | correct without noise under the power condition |
| [PIC](/parallel-interference-cancellation/) | codes, amplitudes | $O(K^2)$ per stage | can oscillate | Jacobi form converges if and only if $\mathrm{eig}(R) \subset (0, 2)$ |
| [Optimum detector](/optimum-multiuser-detector/) | codes, amplitudes | $O(2^K K^2)$ by search | best | minimum error probability of the whole vector; NP-hard in $K$ |

: Synchronous multiuser receivers for $K$ users, with $z = RAb + n$. Forming $z$ costs $O(KN)$ and $R$
costs $O(K^2N)$ for spreading factor $N$. The rates of SIC and PIC with noise are measured in the entries.

## Choosing a scheme

- **For a few users with steady traffic,** divide the channel: TDMA or FDMA, or OFDMA when the channel is
  frequency selective and the users can be given their best subcarriers.
- **Against jamming,** spread: frequency hopping for very wide bands, direct sequence when the receiver
  must also measure delay, as in GPS.
- **For many asynchronous users on one band,** use CDMA with Gold or Kasami codes, closed-loop power
  control, and a [rake receiver](/rake-receiver/) on multipath channels.
- **For a base station that knows all the codes,** add a detector: the decorrelator when the powers are
  unknown, the MMSE detector when they are known, SIC when they differ a lot.
- **For capacity,** decode jointly: SIC on the MAC, superposition coding or NOMA on the broadcast channel.
- **For many devices with short messages,** use coded slotted ALOHA with a well chosen degree distribution,
  or a scheme for [unsourced random access](/unsourced-random-access/) on the Gaussian channel.
