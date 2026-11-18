## What to remember

- A [complexity class](/complexity-class/) is fixed by a model, a resource and a bound in the input length $n$. [P](/p/) is $\bigcup_k \mathsf{DTIME}(n^k)$, [NP](/np/) is the class of problems whose yes-instances have certificates checked in polynomial time, and [coNP](/co-np/) holds their complements. Whether $\mathsf{P} = \mathsf{NP}$ and whether $\mathsf{NP} = \mathsf{coNP}$ are open.
- The chain $\mathsf{L} \subseteq \mathsf{NL} \subseteq \mathsf{P} \subseteq \mathsf{NP} \subseteq \mathsf{PSPACE} \subseteq \mathsf{EXP}$ is proved. The hierarchy theorems give $\mathsf{NL} \ne \mathsf{PSPACE}$ and $\mathsf{P} \ne \mathsf{EXP}$, so some step is strict, but no single step is known to be strict.
- The [time hierarchy theorem](/time-hierarchy-theorem/) needs $f(n) \log f(n) = o(g(n))$ with $g$ time-constructible. The [space hierarchy theorem](/space-hierarchy-theorem/) needs only $f(n) = o(g(n))$ with $g(n) \ge \log n$. Almost every unconditional separation in the chapter rests on them.
- Nondeterminism costs little in space. [Savitch's theorem](/savitch-theorem/) gives $\mathsf{NSPACE}(s) \subseteq \mathsf{DSPACE}(s^2)$ for $s(n) \ge \log n$, so $\mathsf{NPSPACE} = \mathsf{PSPACE}$. The [Immerman-Szelepcsényi theorem](/immerman-szelepcsenyi-theorem/) gives $\mathsf{NL} = \mathsf{coNL}$. For time, nothing of this kind is known.
- Randomized classes differ by their error. [RP](/rp/) errs only on yes-instances, [coRP](/co-rp/) only on no-instances, [BPP](/bpp/) on both with probability at most $1/3$, and [ZPP](/zpp/) $= \mathsf{RP} \cap \mathsf{coRP}$ never errs. Repetition drives a bounded error down to $2^{-k}$ with $O(k)$ runs. [PP](/pp/) has no gap and cannot be amplified this way. $\mathsf{BPP} \subseteq \mathsf{P/poly}$ ([Adleman](/adleman-theorem/)) and $\mathsf{BPP} \subseteq \Sigma_2^p \cap \Pi_2^p$ ([Sipser-Gács](/sipser-gacs-theorem/)); whether $\mathsf{BPP} = \mathsf{P}$ is open.
- The [polynomial hierarchy](/polynomial-hierarchy/) adds alternating quantifiers to NP. It lies inside PSPACE, and by [Toda's theorem](/toda-theorem/) inside $\mathsf{P}^{\mathsf{PP}}$. If $\mathsf{NP} \subseteq \mathsf{P/poly}$, it collapses to $\Sigma_2^p$ ([Karp-Lipton](/karp-lipton-theorem/)).
- Circuit lower bounds are proved only for restricted circuits: parity is not in [AC0](/ac0/), and monotone circuits for clique need exponential size. No superpolynomial lower bound is known for general circuits computing any problem in NP.
- Interaction and randomness change what a proof can show: $\mathsf{IP} = \mathsf{PSPACE}$, $\mathsf{MIP} = \mathsf{NEXP}$ and $\mathsf{NP} = \mathsf{PCP}(O(\log n), O(1))$. These are theorems, proved without any hypothesis.
- Three barriers explain why the open questions resist: there are oracles with $\mathsf{P}^A = \mathsf{NP}^A$ and $\mathsf{P}^B \ne \mathsf{NP}^B$ ([Baker-Gill-Solovay](/baker-gill-solovay-theorem/)), natural proofs would break [pseudorandom functions](/pseudorandom-function/), and the methods behind IP = PSPACE [algebrize](/algebrization-barrier/).

## The main classes side by side

| Class | Model and bound | A complete problem | Known relations | Open question |
|---|---|---|---|---|
| [L](/logspace/) | deterministic, $O(\log n)$ space | undirected reachability, under reductions weaker than logspace | $\mathsf{L} = \mathsf{SL}$, $\mathsf{L} \subseteq \mathsf{NL}$ | $\mathsf{L} = \mathsf{P}$? |
| [NL](/nondeterministic-logspace/) | nondeterministic, $O(\log n)$ space | directed reachability | $\mathsf{NL} = \mathsf{coNL}$, $\mathsf{NL} \subseteq \mathsf{DSPACE}(\log^2 n)$ | $\mathsf{L} = \mathsf{NL}$? |
| [P](/p/) | deterministic, $n^{O(1)}$ time | circuit value (logspace reductions) | $\mathsf{P} \ne \mathsf{EXP}$ | $\mathsf{P} = \mathsf{NP}$? |
| [NP](/np/) | certificates checked in $n^{O(1)}$ time | SAT | $\mathsf{NP} \subseteq \mathsf{PSPACE}$, $\mathsf{NP} \ne \mathsf{NEXP}$ | $\mathsf{NP} = \mathsf{coNP}$? |
| [BPP](/bpp/) | coins, error $\le 1/3$, $n^{O(1)}$ time | none known | $\mathsf{BPP} \subseteq \Sigma_2^p \cap \Pi_2^p$, $\subseteq \mathsf{P/poly}$ | $\mathsf{BPP} = \mathsf{P}$? |
| [PH](/polynomial-hierarchy/) | $k$ alternating quantifiers, all $k$ | none unless it collapses | $\mathsf{PH} \subseteq \mathsf{P}^{\mathsf{PP}} \subseteq \mathsf{PSPACE}$ | infinite? |
| [PSPACE](/pspace/) | deterministic, $n^{O(1)}$ space | [QSAT](/qsat/) | $= \mathsf{NPSPACE} = \mathsf{IP}$, $\ne \mathsf{EXPSPACE}$ | $\mathsf{P} = \mathsf{PSPACE}$? |
| [EXP](/exptime/) | deterministic, $2^{n^{O(1)}}$ time | succinct circuit value | $\mathsf{P} \ne \mathsf{EXP}$ | $\mathsf{EXP} = \mathsf{NEXP}$? |

: The classes most used in the volume. "Complete" is under polynomial-time many-one reductions unless stated, and under logspace reductions for P. Every question in the last column is open.

## Using the chapter

- To place a problem, find an upper bound, such as an algorithm, a certificate or a game, and a lower bound, a reduction from a complete problem. When the two meet, the problem is complete, and that is the most the theory can say while the separations are open.
- Read every "not in P" as "not in P unless P = NP", and the same for the other open pairs. The unconditional statements are the hierarchy theorems and their consequences, the circuit bounds for AC0 and monotone circuits, and the relativization results.
- For a randomized algorithm with one-sided error, the side decides between RP and coRP. [Polynomial identity testing](/polynomial-identity-testing/) is in coRP, and no deterministic polynomial-time algorithm is known.
- PSPACE-completeness is the usual verdict for two-player games, planning and questions about regular expressions. It says more than NP-hardness: a polynomial-time algorithm would give $\mathsf{P} = \mathsf{PSPACE}$, which implies $\mathsf{P} = \mathsf{NP}$.
- If an exact algorithm runs in $n^{O(\log n)}$, the problem is in [quasi-polynomial time](/quasi-polynomial-time/). That is strong evidence that it is not NP-complete, since every NP problem would then be solvable in quasi-polynomial time.
