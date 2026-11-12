## What to remember

- A code of [minimum distance](/minimum-distance/) $d$ detects up to $d - 1$ errors, corrects up to $\lfloor (d-1)/2 \rfloor$, fills in up to $d - 1$ erasures and handles $\tau$ errors with $e$ erasures when $2\tau + e < d$.
- For a [linear code](/linear-code/), $d$ is the least weight of a nonzero codeword and the least number of dependent columns of the [parity-check matrix](/parity-check-matrix/). The [syndrome](/syndrome/) $H r^T$ depends only on the error, and [syndrome decoding](/syndrome-decoding/) is hard decision maximum likelihood on a BSC with $p < 1/2$, with a table of $q^{n-k}$ entries.
- Capacity is $1 - h(p)$ for the [BSC](/binary-symmetric-channel/), $1 - \varepsilon$ for the [BEC](/binary-erasure-channel/) and $\tfrac12 \log_2(1 + \mathrm{SNR})$ for the [AWGN channel](/additive-white-gaussian-noise-channel/). On the AWGN channel rate $R$ needs $E_b/N_0 \ge (2^{2R} - 1)/(2R)$: 0 dB at $R = 1/2$, and $-1.59$ dB as $R \to 0$.
- For all codes: [Singleton](/singleton-bound/) $|C| \le q^{n-d+1}$, [Hamming](/hamming-bound/) $|C| \le q^n / V_q(n, t)$, binary [Plotkin](/plotkin-bound/) $|C| \le 2\lfloor d/(2d - n) \rfloor$ for $2d > n$, [Elias](/elias-bound/) and the [LP bound](/delsarte-lp-bound/). For linear codes only: [Griesmer](/griesmer-bound/) $n \ge \sum_{i<k} \lceil d/q^i \rceil$. As $n \to \infty$, rate $1 - h_q(\delta)$ is reachable by [Gilbert-Varshamov](/gilbert-varshamov-bound/).
- The nontrivial perfect codes over finite fields have the parameters of the [Hamming](/hamming-code/) and [Golay](/golay-code/) codes. [Reed-Solomon codes](/reed-solomon-code/) are MDS, and decode $\nu$ errors and $\rho$ erasures when $2\nu + \rho \le n - k$ with [Berlekamp-Massey](/berlekamp-massey/), [Chien search](/chien-search/) and [Forney](/forney-algorithm/); [Guruswami-Sudan](/guruswami-sudan/) lists every codeword within $e < n - \sqrt{n(k-1)}$.
- Decoding a general linear code to the [nearest codeword](/nearest-codeword-problem/) is NP-hard (1978), and so is [computing its minimum distance](/minimum-distance-problem/) (Vardy 1997). Fast decoders need structure: algebra, a small [trellis](/trellis/) or a sparse [Tanner graph](/tanner-graph/).
- The asymptotic coding gain is $10 \log_{10}(R d)$ dB with soft decisions and $10 \log_{10}(R(t+1))$ dB with hard ones. At rate $1/2$, hard decisions move the binary-input AWGN limit from 0.19 dB to 1.77 dB.
- [Belief propagation](/belief-propagation-decoding/) is exact bitwise MAP only on a tree, and the [peeling decoder](/peeling-decoding/) stops at a stopping set even when Gaussian elimination would succeed. [Polar codes](/polar-code/) with [successive cancellation](/successive-cancellation-decoding/) reach capacity in $\Theta(N \log N)$ time.

| Code | Parameters | Guaranteed correction | Standard decoder | Decoding cost |
|---|---|---|---|---|
| [Repetition](/repetition-code/) | $[n, 1, n]$ | $\lfloor (n-1)/2 \rfloor$ errors | majority vote | $\Theta(n)$ |
| Hamming | $[2^r - 1, 2^r - 1 - r, 3]$ | 1 error | syndrome table | $\Theta(n^2)$ |
| Reed-Solomon | $[n, k, n - k + 1]_q$, $n \le q$ | $2\nu + \rho \le n - k$ | syndromes, BM, Chien, Forney | $O(n(n-k))$ |
| Binary [BCH](/bch-code/) | $[2^m - 1, \ge n - mt, \ge 2t + 1]$ | $t$ errors | same pipeline | $O(n t)$ |
| [Reed-Muller](/reed-muller-code/) $\mathrm{RM}(r, m)$ | $[2^m, \sum_{i \le r} \binom{m}{i}, 2^{m-r}]$ | $2^{m-r-1} - 1$ errors | [majority logic](/majority-logic-decoding/) | $\Theta(n k)$ |
| [Convolutional](/convolutional-code/), memory $m$ | rate $1/n$, free distance $d_{\mathrm{free}}$ | $\lfloor (d_{\mathrm{free}} - 1)/2 \rfloor$ on the terminated code | Viterbi | $\Theta(T\, 2^m n)$ |
| [Turbo](/turbo-code/) | rate $1/3$, punctured higher | — | [turbo decoding](/turbo-decoding/) | $\Theta(I N S)$ |
| [LDPC](/ldpc-code/) | sparse $H$ with $E$ ones | — | belief propagation, [min-sum](/min-sum-decoding/) | $\Theta(I E d)$, $\Theta(I E)$ |
| Polar | $N = 2^n$, $K$ good positions | — | successive cancellation | $\Theta(N \log N)$ |
| [LT](/lt-codes/) | rateless, $k$ source symbols | erasures only | peeling | $O(k \ln(k/\delta))$ XORs |

: Code families of the chapter. $T$ is the number of trellis steps, $I$ of iterations, $S$ of encoder states, $E$ of edges of the Tanner graph, and $d$ the largest check degree. A dash means that the code is judged by its error rate near capacity, not by a guarantee.

## Choosing a code

To detect errors and ask again, use a [CRC](/cyclic-redundancy-check/). For computer memory, use a SECDED code: an extended Hamming code shortened to $[72, 64, 4]$ corrects one bit and detects two in each word.

For storage and lost packets, where the positions of the losses are known, use an MDS [erasure code](/erasure-codes/) such as Reed-Solomon over $\mathrm{GF}(256)$: an $[n, k]$ code survives any $n - k$ losses. When receivers lose different and unknown fractions of a broadcast, use a [fountain code](/fountain-codes/), in practice a [Raptor code](/raptor-codes/).

For bursts, use Reed-Solomon over bytes with [interleaving](/interleaving/). For long blocks on a radio link with soft decisions, use LDPC codes, as Wi-Fi and the data channels of 5G do, or turbo codes. For short blocks, use polar codes with CRC-aided list decoding, as the 5G control channels do, or a convolutional code with the Viterbi algorithm.
