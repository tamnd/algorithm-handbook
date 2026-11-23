## What to remember

- A side channel is a function of the intermediate values of a computation plus noise. The usual model is $\ell = \varepsilon\,\mathrm{HW}(v) + N$. An attack tests the guesses of one small part of the key at a time, so AES-128 needs $16 \cdot 256$ tests instead of $2^{128}$.
- One trace is enough when the sequence of operations depends on the key; many traces and a statistic are needed when only the data does.
- In the PRESENT example with the key B and 16 noise-free traces, DPA on bit 1 gives the right guess 1.0 against 0.75 for the best wrong guess, and CPA gives correlation 1 against $|r| = 0.75$. A wrong guess correlates as $c(g \oplus k)\,\rho$ with $\rho = 1/\sqrt{1 + \sigma^2/\varepsilon^2}$, and the traces needed grow about as $28/\rho^2$.
- MIA assumes no form of the leakage: with power $(w-2)^2$ the right guess of CPA has correlation 0 and MIA still finds it. A template attack with exact templates is optimal under a uniform key.
- Masking with $t + 1$ shares and sound gadgets is secure against $t$ probes (ISW). This is a theorem in the probing model; glitches and transitions are outside it unless the scheme handles them, as a threshold implementation does with non-completeness.
- TVLA flags leakage at $|t| > 4.5$ in two independent sets. It detects leakage and never proves its absence; a masked device passes the first-order test and fails the second-order one.
- Constant-time code keeps secrets out of branches, addresses and variable-time instructions. That removes timing and cache leaks in the stated leakage model, and not power, faults or transient execution.
- Meltdown and Spectre leave secrets in the cache through work that the processor discards. Kernel page table isolation stops Meltdown at a cost on every switch into the kernel; each Spectre defense removes one condition, at some places, for some variants.
- Computing twice and comparing stops faults that hit one of the two computations, at twice the work. Rowhammer makes faults from software; PARA bounds a flip by $(1-p)^k$ in a simple model.

## The attacks side by side

| Attack | What it observes | What the attacker needs | Result in the entry's example |
|---|---|---|---|
| [Simple power analysis](/simple-power-analysis/) | operation sequence in one trace | distinguishable operations | $1011_2$ read from S M S S M S M |
| [Differential power analysis](/differential-power-analysis/) | difference of means by one predicted bit | a bit of an intermediate value | success 0.925 at 400 traces, $\sigma = 1$ |
| [Correlation power analysis](/correlation-power-analysis/) | correlation with a predicted Hamming weight | a leakage roughly linear in the model | success 0.955 at 40 traces, $\sigma = 1$ |
| [Mutual information analysis](/mutual-information-analysis/) | mutual information with the predicted value | a model that is not injective | success 0.86 at 100 traces for $(w-2)^2$ leakage; CPA 0.035 |
| [Template attack](/template-attack/) | likelihood under Gaussian templates | a profiling copy of the device | success 0.85 at 5 traces with exact templates |
| [Flush+Reload](/flush-and-reload/) | reload time of a shared line | shared memory and a flush instruction | most exponent bits of GnuPG RSA from one operation (Yarom and Falkner) |
| [Prime+Probe](/prime-and-probe/) | eviction of the attacker's lines from a set | a shared cache set | set accesses of the victim in an abstract LRU cache |
| [Differential fault analysis](/differential-fault-analysis/) | difference of a correct and a faulty output | a fault model and repeated inputs | the key cancels in $y \oplus y^*$, leaving few candidates |

: The success rates are measurements in the entries' simulated models (200 or 300 seeded runs per cell, one sample per trace, $\varepsilon = 1$); the Flush+Reload line is Yarom and Falkner's measurement on their processors. None of them ranks the attacks on a real device.

## Choosing a defense

Start from the attacker. Against one who sees time and cache use, write [constant-time code](/constant-time-programming/), check it with [constant-time verification](/constant-time-verification/), and add [RSA blinding](/rsa-blinding/) where it applies. If the attacker runs code on a speculating processor, add Spectre defenses where secrets meet attacker-controlled indices, and kernel isolation on processors open to Meltdown.

Against an attacker with the device and an oscilloscope, constant time is not enough. Use [Boolean masking](/boolean-masking/) with one share more than the order you need, [ISW gadgets](/isw-private-circuits/) or composable ones for the non-linear parts, and a [threshold implementation](/threshold-implementation/) in hardware with glitches. Evaluate with TVLA at the orders that matter, and with template attacks and [key rank estimation](/side-channel-key-rank-estimation/) for the margin. Against faults, add redundancy for the stated fault model. Against length channels, compress secrets in a separate context and pad traffic to anonymity sets.
