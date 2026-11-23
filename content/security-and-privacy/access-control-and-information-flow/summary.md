## What to remember

- The [access control matrix](/access-control-matrix/) is the state: $\mathrm{allow}(s, o, r) \iff r \in A[s, o]$. A list stores a column and checks in $O(s)$ time; a [capability list](/capability-list/) stores a row, checks and delegates in $O(1)$, and revokes $k$ derived capabilities in $O(k)$. Roles, attributes and relations compute cells of the same matrix.
- In [Bell-LaPadula](/bell-lapadula-model/), read needs $f_s(s) \succeq f_o(o)$ and $f_c(s) \succeq f_o(o)$, append needs $f_o(o) \succeq f_c(s)$, and write needs $f_s(s) \succeq f_o(o)$ and $f_o(o) = f_c(s)$. The [basic security theorem](/basic-security-theorem/) proves that these state properties hold in every reachable state when each transition keeps them. It is a theorem about the model's definition of a secure state, not about covert channels, and System Z shows how weak that definition is when levels can change.
- [HRU](/harrison-ruzzo-ullman-model/) safety is [undecidable](/hru-safety-undecidability/) in general, decidable for mono-operational commands (NP-complete with the commands in the input), and PSPACE-complete without creates. [Take-Grant](/take-grant-model/) decides $\mathit{can\_share}$ in $O(n + m)$ time.
- Checking that no $k - 1$ users together hold a permission set $P$ is coNP-complete, and deciding whether $k$ roles reproduce a user-permission matrix is NP-complete. Role mining tools are heuristics whose quality is measured.
- A monitor that sees one run and may only stop it enforces only [safety properties](/safety-property/), and a computable one only some of them. [Noninterference](/noninterference/) is a 2-safety [hyperproperty](/hyperproperty/), so no such monitor enforces it exactly.
- The [security type system](/security-type-system/) runs in linear time, and every typable program is TINI; it rejects secure programs such as $l := h - h$. [NSU](/no-sensitive-upgrade/) and [faceted execution](/faceted-execution/) give TINI at run time, [secure multi-execution](/secure-multi-execution/) gives TSNI at the price of one run per level.
- Min-entropy leakage is $\mathcal L(\pi, C) = \log_2 \frac{\sum_y \max_x \pi(x) C[x, y]}{\max_x \pi(x)}$ bits, for an attacker who knows $\pi$ and $C$ and makes one guess. Over all priors it is at most $\log_2 \sum_y \max_x C[x, y]$, reached at the uniform prior, and $\log_2$ of the number of outputs for a deterministic program. This bound also bounds every g-leakage and the Shannon capacity, but only for the observables in $C$.
- [Covert channels](/covert-channel/) can be reduced and audited, not removed in general: [confinement](/confinement-problem/) is undecidable, and the [shared resource matrix](/shared-resource-matrix/) gives candidates, not channels.

## Methods side by side

| Method | Decides | Guarantee | Cost |
|---|---|---|---|
| [RBAC](/role-based-access-control/) check | one access through roles | exactly $UA \circ RH^* \circ PA$ | $O(a + e)$ |
| [Take-Grant](/take-grant-model/) | whether a right can reach a vertex | exact characterization | $O(n + m)$ |
| [Security automaton](/security-automaton/) | each prefix of one run | exactly the safety properties | one step per action |
| [Type system](/security-type-system/) | the program text | TINI; rejects some secure programs | $\Theta(n)$ |
| [NSU](/no-sensitive-upgrade/) | one run | TINI; stops some secure runs | $O(t n)$ |
| [Multi-execution](/secure-multi-execution/) | $k$ runs | TSNI; precise for TSNI programs | about $k$ runs |
| [Faceted execution](/faceted-execution/) | one run that splits | TINI; no stops | $O((a + b) n)$ |
| [Min-capacity](/min-entropy-leakage-bound/) | the channel matrix | worst leakage over priors | $O(\lvert\mathcal X\rvert\,\lvert\mathcal Y\rvert)$ |
| [Shared resource matrix](/shared-resource-matrix/) | a design table | candidates only | $O(m n^2)$ |

: Methods of the chapter, with the symbols of each entry: $a$ and $e$ roles and hierarchy edges below the active roles; $n$ vertices or program size; $m$ edges or primitives; $t$, $a$, $b$ steps of a run; $k$ levels.

## Choosing a method

For single accesses, store the matrix in the form that makes the common operation cheap: lists to review who can reach an object, capabilities when rights are passed on and revoked as a tree. Use roles when many users share a job, and check separation of duty constraints on each assignment and each new hierarchy edge. To prove that no right can leak, choose the model first: arbitrary HRU commands give no algorithm, Take-Grant gives a linear test.

For flows inside a program, use the type system when the code is known in advance. When it arrives at run time, use NSU if a stop is acceptable, faceted execution if not, and secure multi-execution if the termination channel matters. State intended releases as declassification policies and measure them with a leakage that fits the attacker. For a whole system, list the shared state and bound each remaining channel in bits per second.
