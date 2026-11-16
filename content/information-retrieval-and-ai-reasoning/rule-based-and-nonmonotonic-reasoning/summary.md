## What to remember

- **Horn rules are cheap.** The least model of a propositional definite program is computed by [forward chaining](/forward-chaining/) in time linear in its size. With variables, the cost is polynomial in the facts for a fixed program, and exponential when the program is part of the input.
- **The reduct defines stable models.** $M$ is stable when $M = \mathrm{lm}(P^M)$, where $P^M$ drops every rule with a $\mathit{not}\ c$ such that $c \in M$ and strips the other negative literals. A program can have no stable model ($p \leftarrow \mathit{not}\ p$) or many, and existence is NP-complete.
- **Completion is weaker.** Every stable model is a model of the completion. The converse holds for tight programs ([Fages' theorem](/fages-theorem/)); for any finite program it holds once a [loop formula](/loop-formulas/) is added for every loop, and there can be exponentially many loops.
- **Stratified programs are easy.** With no cycle through negation, the program has a unique perfect model, computed stratum by stratum, and it is also the unique stable model and the well-founded model.
- **The well-founded model is a polynomial core.** The [alternating fixpoint](/alternating-fixpoint/) computes it in $O(n \cdot s)$ time. It may leave atoms undefined, and every stable model agrees with its true and false atoms.
- **Disjunction and defaults cost one more level.** Existence of an answer set of a disjunctive program, and of an extension of a default theory, is $\Sigma_2^p$-complete; the inner test is a coNP minimality or consistency check.
- **Specificity from ranks.** System Z ranks rules by tolerance and gives the rational closure with at most $r(r+1)/2$ SAT calls for the ranking and $O(\log r)$ per query.
- **Diagnoses are hitting sets.** The minimal diagnoses of a system are the minimal hitting sets of its minimal conflict sets (Reiter 1987).
- **Measured, not proved.** Rete and TREAT beat a full rematch on measured programs, not in the worst case, and Rete's tokens can grow as $n^m$. Certainty factors are not probabilities: outside conditional independence they can contradict them.

| Method | Problem | Cost | What you get |
|---|---|---|---|
| Forward chaining | least model of definite rules | linear, propositional | all consequences |
| [Rete](/rete-algorithm/) | keep the conflict set after each change | $O(r\, m\, a\, n^m)$ time, $O(r\, m\, n^m)$ space | exact conflict set, measured speedup |
| [TREAT](/treat-algorithm/) | the same | $O(r\, m\, a\, n^{m-1})$ per insert, $O(r\, m\, n + k)$ space | exact conflict set, little memory |
| Alternating fixpoint | well-founded model | $O(n \cdot s)$ | three-valued model, may be partial |
| [SLG resolution](/slg-resolution/) | well-founded queries, top down | $O(s^3)$ | answers with delays for undefined atoms |
| [Smodels](/smodels-algorithm/) | stable models | $O(2^n n^3 s)$ | all stable models, no learning |
| [Conflict-driven solving](/conflict-driven-answer-set-solving/) | stable models | exponential worst case | learned nogoods, loop nogoods on demand |
| [System Z](/system-z/) | rational closure queries | $O(r^2)$ SAT calls | ranks that respect specificity |
| [HS-DAG](/reiter-hs-tree/) | minimal hitting sets of conflicts | at most one oracle call per node, $\Theta(k u)$ space | all minimal diagnoses |
| [ATMS](/assumption-based-truth-maintenance/) | labels of all contexts | exponential labels | minimal environments of each node |

: Main methods of the chapter. $n$: atoms or facts; $s$: size of the program; $r$: rules; $m$: conditions per rule; $a$: arity; $k$: size of the conflict set for TREAT and number of nodes for the HS-DAG; $u$: components; see each entry for the exact parameters.

## Choosing a method

For rules without negation, use forward chaining when all consequences are wanted and backward chaining when one goal is asked; add Rete when the facts change a little at a time and memory is plentiful, and TREAT when deletions are common or memory is short. For rules with negation, first test for stratification: if the program is stratified, evaluate it stratum by stratum and stop. If not, and one cautious answer per query is enough, compute the well-founded model in polynomial time. For all solutions of a search problem, write it in [answer set programming](/answer-set-programming/) and use a conflict-driven solver; on tight programs the completion alone is enough. Use disjunctive heads only for problems that really sit at $\Sigma_2^p$. For defaults written as logic, prefer normal defaults, which always have an extension, and use System Z or rational closure when specificity should decide conflicts. For a faulty device with a model of correct behavior, use consistency-based diagnosis with the HS-DAG.
