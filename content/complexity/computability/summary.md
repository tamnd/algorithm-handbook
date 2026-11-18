## What to remember

- A language is [decidable](/decidable-language/) when one machine halts on every input with the right answer, and [computably enumerable](/recursively-enumerable-language/) (c.e.) when a machine accepts exactly its words and may run forever on the others. A language is decidable exactly when it and its complement are both c.e.
- The [Church-Turing thesis](/church-turing-thesis/) is a thesis, not a theorem: it says that every mechanical method can be simulated by a [Turing machine](/turing-machine/). The equivalence of Turing machines, the lambda calculus and the [partial recursive functions](/partial-recursive-function/) is a theorem, and it is the main evidence for the thesis.
- There are countably many machines and uncountably many languages, so most languages are undecidable. The [diagonalization argument](/diagonalization-argument/) gives explicit ones, and the [halting problem](/halting-problem/) $K$ is c.e. but not decidable, so its complement is not c.e.
- A many-one reduction $A \le_m B$ is a total computable map with $x \in A \iff f(x) \in B$. It carries decidability and c.e.-ness from $B$ down to $A$, and undecidability from $A$ up to $B$. A Turing reduction $A \le_T B$ uses $B$ as an oracle and preserves only decidability: $\overline{K} \le_T K$ but $\overline{K} \not\le_m K$.
- [Rice's theorem](/rice-theorem/): every property of the language $L(M)$ that holds for some c.e. languages and fails for others is undecidable. Properties of the code itself, such as the number of states, or of a bounded run, are outside the theorem and are often decidable.
- Undecidable problems arise in mathematics: the [Post correspondence problem](/post-correspondence-problem/), validity in first-order logic ([Church's theorem](/church-theorem/)), integer solutions of polynomial equations ([Hilbert's tenth problem](/hilberts-tenth-problem/)), the [Wang tiling problem](/wang-tiling-problem/) and the [word problem for groups](/word-problem-for-groups/).
- The [busy beaver function](/busy-beaver-function/) $\Sigma(n)$ grows faster than every computable function. Its known values stop at $n = 5$, where $S(5) = 47{,}176{,}870$ and $\Sigma(5) = 4098$. [Kolmogorov complexity](/kolmogorov-complexity/) and [Chaitin's constant](/chaitins-constant/) are uncomputable as well, and the first $n$ bits of $\Omega$ decide halting for all programs of length at most $n$.
- The [s-m-n theorem](/s-m-n-theorem/) turns constructions on functions into total computable maps on indices, and [Kleene's recursion theorem](/kleene-recursion-theorem/) gives every total computable $f$ an $n$ with $\varphi_n = \varphi_{f(n)}$.
- [Post's theorem](/posts-theorem/): a set is $\Sigma_{n+1}$ exactly when it is c.e. relative to $\emptyset^{(n)}$, and $\Delta_{n+1}$ exactly when it is computable from $\emptyset^{(n)}$. Each quantifier costs one [jump](/turing-jump/). Between $\mathbf{0}$ and $\mathbf{0}'$ there are c.e. degrees that are neither, by the solution of [Post's problem](/post-problem/).

## Where the standard problems sit

| Problem | Decidable | c.e. | Complement c.e. | Level |
|---|---|---|---|---|
| [Acceptance](/acceptance-problem/) $A_{\mathrm{TM}}$, halting $K$ | no | yes | no | $\Sigma_1$ |
| Emptiness $\{ e : W_e = \emptyset \}$ | no | no | yes | $\Pi_1$ |
| Post correspondence problem | no | yes | no | $\Sigma_1$ |
| Validity of first-order sentences | no | yes | no | $\Sigma_1$ |
| Diophantine equations with an integer solution | no | yes | no | $\Sigma_1$ |
| Wang tile sets that tile the plane | no | no | yes | $\Pi_1$ |
| Totality $\{ e : \varphi_e \text{ total} \}$ | no | no | no | $\Pi_2$ |
| Finiteness $\{ e : W_e \text{ finite} \}$ | no | no | no | $\Sigma_2$ |
| Cofiniteness $\{ e : W_e \text{ cofinite} \}$ | no | no | no | $\Sigma_3$ |

: Status of standard problems. The last column gives the level of the quantifier form; for $K$ and totality the entries also prove completeness for the level. All entries are unconditional theorems.

## Using the chapter

To show that a problem is undecidable, look for a many-one reduction from a problem already known to be undecidable. For questions about the language of a machine, Rice's theorem does the work at once; check first that the property depends only on the language and is nontrivial. For questions about words, strings or grammars, start from the Post correspondence problem. For questions about arithmetic, the MRDP theorem behind Hilbert's tenth problem turns every c.e. set into a Diophantine one.

To show that a problem is not c.e., reduce the complement of the halting problem to it, or show that its complement is c.e. and the problem is undecidable. To place a problem exactly, write its definition with as few alternating quantifiers as you can, which gives an upper bound in the arithmetical hierarchy, and then reduce a complete set of that level to it. Keep the reduction type in view: a Turing reduction shows only that the problem is undecidable, not that it is not c.e.
