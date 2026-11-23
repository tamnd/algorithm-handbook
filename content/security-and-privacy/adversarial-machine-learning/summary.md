## What to remember

- **State the threat model first:** the goal, the knowledge (white box, scores, labels only) and the capability (a test input in $B_p(x, \epsilon) \cap [0,1]^d$, or a fraction of the training data).
- **Linear models have closed forms.** For $f(x) = w \cdot x + b$ the smallest change that reaches the boundary has size $\rho_2 = |f(x)|/\lVert w \rVert_2$ in $\ell_2$ and $\rho_\infty = |f(x)|/\lVert w \rVert_1$ in $\ell_\infty$, ignoring the box $[0,1]^d$, which can only make it larger. One FGSM step of size $\epsilon$ changes the logit by $\epsilon \lVert w \rVert_1$.
- **Attacks bound robust accuracy from above, certificates from below.** A failed PGD run proves nothing. Athalye, Carlini and Wagner (2018) found that 7 of 9 defenses of ICLR 2018 relied on obfuscated gradients, and circumvented 6 completely and 1 partly.
- **Verification is NP-complete; bounds are sound and incomplete.** Reluplex decides the problem exactly, at a cost exponential in the number of unstable ReLUs in the worst case. Interval bounds cost about two forward passes, linear bounds about $n$ times more, and a negative bound says nothing.
- **Randomized smoothing certifies the smoothed classifier $g$**, not the base classifier, with radius $R = \frac{\sigma}{2}\big(\Phi^{-1}(p_A) - \Phi^{-1}(p_B)\big)$. CERTIFY uses $R = \sigma \Phi^{-1}(\underline{p_A})$ with a Clopper-Pearson lower bound, and the claim holds with probability at least $1 - \alpha$. An $\ell_2$ radius $R$ gives only $R/\sqrt d$ in $\ell_\infty$.
- **Poisoning defenses are narrow.** A partition-and-vote model is certified against $r$ changed training points when the vote gap exceeds $2r$. Krum needs $n > 2f + 2$ and bounds how far its output can be from the honest updates; it does not find the Byzantine clients. No backdoor defense is proved against every trigger.
- **Privacy attacks are measured; DP bounds them.** The membership advantage is $\mathrm{TPR} - \mathrm{FPR}$, and against $\epsilon$-DP training every attacker has advantage at most $e^\epsilon - 1$. Report the TPR at a low FPR, as the likelihood ratio attack does.
- **Exact unlearning is retraining.** The model after a deletion must have the distribution of a model trained without the record. SISA lowers the cost to one shard from one checkpoint; approximate unlearning only bounds the difference.
- **A watermark is a hypothesis test.** The green list detector computes $z = (|s|_G - \gamma T)/\sqrt{T\gamma(1-\gamma)}$ and flags $z > z^*$; the false positive rate is bounded for text that does not depend on the key, and $z$ grows like $\sqrt T$.

| Method | Kind | Knowledge or access | Guarantee | Cost |
|---|---|---|---|---|
| FGSM | attack, $\ell_\infty$ | white box | none; exact for a linear model | one gradient |
| PGD | attack, $\ell_\infty$ or $\ell_2$ | white box | none; a local search | $T$ gradients |
| Boundary attack | attack | labels only | stays adversarial | at most $2T$ queries |
| IBP | certificate | the weights | sound, incomplete | about two forward passes |
| Linear bounds (CROWN) | certificate | the weights | sound, incomplete | $O(K n N + K n d)$ |
| Reluplex | verifier | the weights | sound and complete | $O(2^R s)$ worst case |
| Randomized smoothing | certificate for $g$ | queries of $f$ | holds with probability $1 - \alpha$ | $n_0 + n$ noisy queries |
| Krum | aggregation | the updates | needs $n > 2f + 2$ | $O(n^2(d + \log n))$ |
| SISA | exact unlearning | the data | equals retraining | delete $O(EdnR/S)$ |

: The main methods of the chapter. $T$ is the number of steps, $K$ the layers, $n$ the width, $N$ the weights, $R$ the ReLUs (for Reluplex) or the slices (for SISA), and $s$ the cost of one simplex run.

## Choosing and evaluating a defense

Write the threat model down first. For evasion, measure robust accuracy with PGD with random restarts and with an attack adapted to the defense, and report the budget and the steps; attack non-differentiable or random steps with BPDA and EOT, on fresh random draws. For a proof, use interval or linear bounds on networks trained for them, an exact verifier on small networks, and randomized smoothing for large models under an $\ell_2$ threat.

Against poisoning, control the provenance of the data first; spectral filters and Krum help only within their assumptions. For privacy, train with differential privacy when a bound is needed, and audit with membership tests at a low false positive rate. Fix the SISA partition before training if deletions are expected. In systems built on language models, treat retrieved text as untrusted data and keep the model's permissions small.
