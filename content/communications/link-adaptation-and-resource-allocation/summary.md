## What to remember

- **Link adaptation is a threshold lookup.** Each scheme has an SNR threshold for the target block error
  rate, and the transmitter picks the fastest scheme whose threshold the report meets, in $O(\log J)$. An
  optimistic report is costly: in the entry's example, 3 dB too high cuts the throughput from 1.98 to 0.55.
- **The SNR gap is a design rule.** $b = \log_2(1 + \mathrm{SNR}/\Gamma)$ with
  $\Gamma = (Q^{-1}(P_e/N_e))^2/3$, about 9 dB for uncoded QAM at $10^{-6}$. Each 3.01 dB of gap or margin
  costs one bit per symbol. It is an approximation, within 0.25 dB for uncoded square QAM, not a theorem.
- **Combining attempts raises the SNR or the rate.** Chase combining adds the LLRs, which is maximal ratio
  combining and needs $\log_2(1 + \sum_i\gamma_i) \ge R$. Incremental redundancy needs only
  $\sum_i\log_2(1 + \gamma_i) \ge R$, so it never needs more rounds.
- **The outer loop fixes the error rate exactly.** With
  $\Delta_{\mathrm{down}} = \Delta_{\mathrm{up}}\beta_T/(1 - \beta_T)$, the NACK fraction tends to $\beta_T$
  whenever the offset stays bounded, whatever the bias of the reports.
- **Water-filling is optimal with transmitter channel knowledge.** The powers are $(\mu - \nu_i)^+$ for
  noise levels $\nu_i$, and the level $\mu$ comes from a sort. Truncated inversion gives a constant rate in the
  states above a cutoff; full inversion has zero rate on a Rayleigh channel.
- **Integer bit loading is solved by greedy rules.** The cost of each next bit doubles, so adding the
  cheapest bit (Hughes-Hartogs) or swapping bits until no swap helps (Levin-Campello) is optimal, and every
  prefix of the greedy sequence is optimal too. Chow-Cioffi-Bingham is faster and only close to optimal.
- **Many users turn fading into gain.** The best of $K$ Rayleigh users has mean SNR $H_K\bar\gamma$, and
  the capacity grows like $\log\log K$. Max-rate scheduling collects it at the cost of fairness; for the sum
  rate over subcarriers, each subcarrier goes to its best user and the power is water-filled.
- **Power control converges when the targets are feasible.** Foschini-Miljanic converges to the least
  power solution from any start exactly when $\rho(F) < 1$. Yates's three axioms give the same result for
  any standard interference function, synchronously or asynchronously.
- **Max-min SINR is a Perron-Frobenius problem.** With a total power limit the best common SINR is
  $1/\rho(A)$, found by bisection or by a power iteration. Weighted sum rate is NP-hard with interference;
  WMMSE reaches stationary points.
- **Energy detection has an SNR wall.** With noise uncertainty $\rho$ in linear terms, no number of samples
  detects signals below $\rho - 1/\rho$. Cyclostationary detection avoids the wall at the cost of more
  samples and of knowing the cycle frequency.

| Problem | Solved by | Time | Optimality |
|---|---|---|---|
| Sum rate, parallel channels | [water-filling](/water-filling-power-allocation/) | $O(N\log N)$ | optimal (concave problem) |
| Integer bits, least power or most bits | [Hughes-Hartogs](/hughes-hartogs-algorithm/), [Levin-Campello](/levin-campello-algorithm/) | $O(N + B\log N)$ | optimal for doubling costs |
| Integer bits, fixed target, common margin | [Chow-Cioffi-Bingham](/chow-cioffi-bingham-algorithm/) | $O(N(K + F))$ | heuristic; 0.64 dB short in the entry's example |
| Constant rate over fading | [truncated inversion](/truncated-channel-inversion/) | $O(K\log K)$ over states | optimal cutoff for this policy |
| Bits per joule | [Dinkelbach](/energy-efficient-power-allocation/) | a few concave subproblems | optimal for concave rate and affine power |
| SINR targets | [Foschini-Miljanic](/foschini-miljanic-power-control/) | $O(K^2)$ per round | least power, if feasible |
| Max-min SINR | [Perron-Frobenius and bisection](/max-min-sinr-power-control/) | $O(K^3L)$ | optimal |
| Sum rate, OFDMA, no rate targets | [best user and water-filling](/ofdma-resource-allocation/) | $O(KN + N\log N)$ | optimal |
| Weighted sum rate with interference | [WMMSE, GP rounds](/weighted-sum-rate-maximization/) | per iteration | stationary point; NP-hard in general |

: The allocation problems of the chapter. $N$ subcarriers, $B$ bits, $K$ users or states, $L$ bisection
steps, and $K$ and $F$ in the Chow-Cioffi-Bingham row are its margin rounds and fix-up steps.

## Choosing a method

- **For one link,** use a threshold table with an outer loop and hybrid ARQ with incremental redundancy.
- **For a multicarrier link,** water-fill when bits may be fractional, and use Levin-Campello from the
  previous loading when the channel changes a little; Chow-Cioffi-Bingham when time is short.
- **For a delay-sensitive constant rate,** use truncated channel inversion with the optimal cutoff.
- **For a cell with many users,** use max-rate scheduling only if fairness does not matter; otherwise
  [proportional-fair scheduling](/proportional-fair-scheduling/) keeps most of the multiuser diversity.
- **For links that interfere,** use Foschini-Miljanic for fixed targets, max-min SINR for fairness, and
  WMMSE from several starts for the weighted sum rate.
- **For opportunistic use of a band,** use an energy detector when the noise level is well known, and
  cyclostationary detection when it is not.
