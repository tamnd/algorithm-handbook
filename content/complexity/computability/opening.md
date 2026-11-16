Before asking how fast a problem can be solved, you can ask whether it can be solved at all. Computability theory answers that question, and for many natural problems the answer is no. No algorithm decides, for every program and input, whether the program halts. No algorithm decides whether a Diophantine equation has an integer solution. These are theorems, proved without any hypothesis, and they hold for every model of computation equivalent to the Turing machine.

The subject matters in practice because undecidability spreads by reduction. Any nontrivial property of what a program computes is undecidable, by Rice's theorem. So a compiler cannot decide exactly which pointers may alias, and a type checker for some rich type systems cannot infer every type. Tools in these areas must give up exactness, completeness or termination, and the theory explains why.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Models and the thesis.** Computable and partial recursive functions, primitive recursive functions, Turing completeness, the Church-Turing thesis, Gödel numbering and the universal Turing machine.
2. **Decidable and undecidable sets.** Decidable and recursively enumerable languages, countability and the diagonalization argument, the halting and acceptance problems, many-one reducibility and Rice's theorem.
3. **Undecidable problems.** Post's correspondence problem, Hilbert's tenth problem, the Wang tiling problem, the word problem for groups, and the Entscheidungsproblem with Church's theorem.
4. **Logic.** Gödel's incompleteness theorems, Kleene's recursion theorem and the s-m-n theorem.
5. **Degrees of unsolvability.** Oracle Turing machines, Turing degrees, the Turing jump, the arithmetical hierarchy, Post's theorem and Post's problem.
6. **Beyond computable.** Uncomputable functions, the busy beaver function, computable real numbers, Kolmogorov complexity and Chaitin's constant.

## What to read meanwhile

Volume 1 has the models. Read the [Turing machine](/turing-machine/), the [lambda calculus](/lambda-calculus/), equivalent to it in power, and the [register machine](/register-machine/), which is Turing-complete with only two counters. The [Ackermann function](/ackermann-function/) in Volume 1 is computable but not primitive recursive, and the [incompressibility method](/incompressibility-method/) in Volume 1 uses Kolmogorov complexity to prove lower bounds.

Undecidability proofs are written in several volumes. Volume 9 proves [ambiguity of context-free grammars](/cfg-ambiguity-undecidable/), [equivalence of context-free grammars](/cfg-equivalence-undecidable/) and the [word problem for string rewriting](/undecidability-of-word-problem/) undecidable. Volume 16 reduces Post's correspondence problem to [higher-order unification](/higher-order-unification-undecidability/), and in Volume 16 the [Tarski decidability theorem](/tarski-decidability-theorem/) shows a theory that is decidable. In Volume 34, [may-alias analysis](/may-alias-undecidability/) and [type inference for System F](/system-f-inference-undecidability/) are shown undecidable.
