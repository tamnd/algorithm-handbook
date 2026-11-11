## What to remember

- A problem is named $\alpha \mid \beta \mid \gamma$, with an online entry in $\beta$: $\mathrm{online\text{-}list}$ when jobs come one by one and are placed at once, $\mathrm{online\text{-}time}$ when they appear at their release times, and $\mathrm{online\text{-}time\text{-}nclv}$ when the sizes stay hidden until the jobs end.
- **List scheduling is $(2 - \frac1m)$-competitive** for the makespan over a list, because the last job to end starts no later than the average load. No deterministic rule beats $\frac32$ for $m = 2$ or $\frac53$ for $m = 3$. For large $m$ the best known ratio is about 1.9201 and the best lower bound about 1.88.
- **The machine model sets the order of the ratio.** On uniform machines greedy is $\Theta(\log m)$ and a doubling guess of the optimum gives a constant. On unrelated machines greedy is only $m$-competitive, and the best ratio is $\Theta(\log m)$.
- **Restricted assignment costs a logarithm.** Greedy is $(\lceil \log_2 m \rceil + 1)$-competitive; an adversary forces $\lceil \log_2(m + 1) \rceil$ on every deterministic rule and $H_m > \ln m$ on every randomized one.
- **SRPT is optimal** for the total flow time on one machine with preemption. On $m$ machines it is $O(\log \min(n/m, P))$-competitive, optimal up to a constant factor. Without preemption, delayed SPT has the exact deterministic ratio 2 for the total completion time.
- **Unknown sizes are expensive**: every deterministic rule is $\Omega(n^{1/3})$ for the total flow time. RMLF is $O(\log n)$, and SETF with speed $1 + \varepsilon$ is $(1 + \frac1\varepsilon)$-competitive.
- **Stretch** is flow time divided by size. SRPT is 2-competitive for the total stretch; for the maximum stretch the online ratio lies between $\Omega(\Delta^{1/3})$ and $O(\sqrt\Delta)$.
- **Deadlines.** With preemption, EDF keeps every feasible set of deadlines on one machine, but no online rule does on two. Under overload, with value equal to size, the best deterministic ratio is 4. Online machine minimization needs $O(\log \log m)$ times the optimal number of machines.
- **Speed scaling** with power $s^\alpha$: the offline optimum runs the densest interval at its density. AVR is $2^{\alpha - 1}\alpha^\alpha$-competitive, OA exactly $\alpha^\alpha$, BKP $2(\frac{\alpha}{\alpha - 1})^\alpha e^\alpha$, and no deterministic rule beats $e^{\alpha - 1}/\alpha$.

## The results side by side

| Problem | Rules | Ratios | Lower bound |
|---|---|---|---|
| $P \mid \mathrm{online\text{-}list} \mid C_{\max}$ | [list scheduling](/list-scheduling-competitive-ratio/); Fleischer and Wahl | $2 - \frac1m$; about 1.9201 | about 1.88 |
| $Q \mid \mathrm{online\text{-}list} \mid C_{\max}$ | greedy; Berman, Charikar and Karpinski | $\Theta(\log m)$; 5.828 | about 2.438 |
| $R \mid \mathrm{online\text{-}list} \mid C_{\max}$ | greedy; Aspnes et al. | $m$; $O(\log m)$ | $\Omega(\log m)$ |
| $P \mid \mathrm{online\text{-}list}, M_j \mid C_{\max}$ | [greedy](/greedy-restricted-assignment/) | $\lceil \log_2 m \rceil + 1$ | $\lceil \log_2(m + 1) \rceil$ |
| $1 \mid \mathrm{online\text{-}time}, \mathrm{pmtn} \mid \sum F_j$ | [SRPT](/srpt/) | 1 | 1 |
| $1 \mid \mathrm{online\text{-}time} \mid \sum C_j$ | delayed SPT | 2 | 2 |
| $1 \mid \mathrm{online\text{-}time\text{-}nclv}, \mathrm{pmtn} \mid \sum F_j$ | RMLF, randomized | $O(\log n)$ | $\Omega(\log n)$ |
| maximum stretch, one machine | Bender, Chakrabarti and Muthukrishnan | $O(\sqrt\Delta)$ | $\Omega(\Delta^{1/3})$ |
| throughput, value equal to size | $D^{\mathrm{over}}$ | 4 | 4 |
| intervals in order of start, unit weights | earliest end with abort | 1 | 1 |
| machine minimization | Im, Moseley, Pruhs and Stein | $O(\log \log m)$ | a constant |
| speed scaling, energy | [AVR](/avr/); [OA](/optimal-available/); [BKP](/bkp-speed-scaling/) | $2^{\alpha-1}\alpha^\alpha$; $\alpha^\alpha$; $2(\frac{\alpha}{\alpha-1})^\alpha e^\alpha$ | $e^{\alpha - 1}/\alpha$ |

: Main online results of this chapter, for deterministic rules unless a row says otherwise. $m$ is the number of machines, and $P$ and $\Delta$ are the ratio of the largest to the smallest size.

## Choosing a rule

- To place jobs on identical machines as they come, use list scheduling. The better rules for large $m$ gain about 4 per cent.
- If jobs may run only on some machines, use greedy on the eligible machines. With speeds, use greedy where the job ends first, or a doubling guess of the optimum when $m$ is large.
- For the mean response time on one machine with known sizes, use SRPT. If long jobs must not starve, look at the maximum stretch instead.
- If sizes are unknown, use a multilevel feedback queue, the practical form of SETF and RMLF, or round robin when all jobs arrive together.
- When work may exceed capacity and deadlines are firm, do not use plain EDF; use an overload rule that drops hopeless jobs.
- For energy, use OA or qOA when $\alpha$ is near 3, and BKP when $\alpha$ is large or the peak speed matters.
