1. ◦ The definite program below has the facts $a$ and $b$. Compute its least model by [forward chaining](/forward-chaining/) and say which rules never fire. Then run [backward chaining](/backward-chaining/) on the query $d$, trying rules in the order given and body atoms from left to right, with a table of proved atoms. List the goals in the order they are called. Which atoms of the program are never touched?

```
c ← a, b.
d ← c, e.
e ← a.
f ← g.
a.
b.
```

2. ◦ The conflict set holds three instantiations. The time tags of their matched elements, listed in the order of the rule conditions, are $I_1 = (4, 9)$, $I_2 = (9, 2, 1)$ and $I_3 = (6, 8)$. In what order does the LEX [conflict resolution strategy](/conflict-resolution-strategy/) rank them, and in what order does MEA rank them? Which one does each strategy fire if $I_1$ fired in the last cycle and is still in the conflict set?

3. ◦ For the program below, compute the [reduct](/gelfond-lifschitz-reduct/) by $M = \{a, c\}$ and its least model. Is $M$ stable? Find all [stable models](/stable-model-semantics/) by trying every subset of $\{a, b, c, d\}$.

```
a ← not b.
b ← c, not a.
c ← not d.
d ← d.
```

4. ◦ Is the program below [stratified](/stratified-logic-program/)? If so, give a stratification with as few strata as possible and compute the perfect model stratum by stratum.

```
s.
t ← s, not u.
r ← s, not t.
q ← r.
q ← q.
p ← not q.
```

5. ◦ Program $T_1$ has the rules $p \leftarrow q, \mathit{not}\ r$, $q \leftarrow \mathit{not}\ p$, $r \leftarrow s$ and the fact $s$. Program $T_2$ is $T_1$ plus $q \leftarrow p$. Which of the two is tight? For each, compare the models of the [Clark completion](/clark-completion/) with the stable models. What does $T_2$ say about the converse of [Fages' theorem](/fages-theorem/)?

6. ◦ How many answer sets does the [choice rule](/choice-rule/) $2\,\{a, b, c, d\}\,3 \leftarrow$ have on its own? How many are left after adding the constraint $\leftarrow a, b$? List them.

7. ◦ A MYCIN-style system has four rules for the hypothesis $h$: $R_1$: if $e_1$ and $e_2$ then $h$ with CF $0.8$; $R_2$: if $e_3$ then $h$ with CF $0.5$; $R_3$: if $e_4$ then $h$ with CF $-0.6$; $R_4$: if $e_5$ or $e_6$ then $h$ with CF $0.9$. The evidence has $\mathrm{CF}(e_1) = 0.9$, $\mathrm{CF}(e_2) = 0.5$, $\mathrm{CF}(e_3) = 0.6$, $\mathrm{CF}(e_4) = 1$, $\mathrm{CF}(e_5) = 0.15$ and $\mathrm{CF}(e_6) = 0.1$. Using the [certainty factor](/certainty-factors/) rules with the threshold $0.2$, compute $\mathrm{CF}(h)$ to three decimals. Check that combining $R_2$ with $R_3$ first gives the same value.

8. ◦ A device has the components $A_1, A_2, M_1, M_2$. Its minimal conflict sets are $\{M_1, M_2, A_1\}$, $\{M_1, A_2\}$ and $\{M_2, A_2\}$. List all minimal diagnoses in the sense of [consistency-based diagnosis](/consistency-based-diagnosis/). Is there a diagnosis with a single component?

9. ◦ An [ATMS](/assumption-based-truth-maintenance/) has the assumptions $A, B, C$ and the justifications $x \Leftarrow A, B$; $y \Leftarrow C$; $z \Leftarrow x$; $z \Leftarrow y$; $w \Leftarrow z, A$. Give the label of each of $x, y, z, w$. Then the nogood $\{A, C\}$ is recorded. Which labels change?

10. • Add the rule $u \leftarrow p$ to the program of exercise 4. Is the result stratified? Find its stable models, the models of its completion and its [well-founded model](/well-founded-semantics/). Explain why the completion model is not stable.

11. • Run the [alternating fixpoint](/alternating-fixpoint/) on the program below. Give each pair $(K_i, U_i)$, where $K$ underestimates the true atoms and $U$ overestimates the atoms that are not false, and state the well-founded model. Does the program have a stable model?

```
a ← not b.
b ← not c.
c ← not d.
d ← d.
e ← not e.
f ← a, not e.
g ← not f.
```

12. • For the program $p \leftarrow q$, $q \leftarrow p$, $q \leftarrow r$, $r \leftarrow \mathit{not}\ s$, $s \leftarrow \mathit{not}\ r$, list the loops, the external support of each, and the [loop formulas](/loop-formulas/). Find the models of the completion and the stable models, and name the model that the loop formula removes.

13. • Run the root step of the [smodels algorithm](/smodels-algorithm/) on the program $a \leftarrow b$, $b \leftarrow a$, $\leftarrow \mathit{not}\ a$. Which of the rules R1 to R4 fire, and what does the upper closure (ATMOST) do? How many guesses does the search make? What would a solver that uses only the completion return?

14. • Use the [splitting set theorem](/splitting-set-theorem/) with $U = \{a, b\}$ to find the stable models of the program below. Is $\{a, b, c\}$ a splitting set? Is $\{a, b, c, d\}$?

```
a ← not b.
b ← not a.
c ← a, not d.
d ← not c.
e ← c.
```

15. • Find the answer sets of the [disjunctive program](/disjunctive-logic-program/) below. For the candidate $\{a, b, d\}$, show a smaller model of its reduct.

```
a ∨ b.
c ∨ d ← a.
d ← b.
a ← d, not c.
```

16. • Find the [extensions](/default-extension/) of the default theory with $W = \{a\}$ and the defaults $a : b / b$, $b : c / c$ and $: \neg c / \neg c$. Which of $b$, $c$ and $\neg c$ follow credulously, and which skeptically?

17. • Show that the [default theory](/default-logic/) with $W = \emptyset$ and the defaults $: \neg b / a$, $: \neg c / b$ and $: \neg a / c$ has no extension. Then put $W = \{c\}$ and find all extensions.

18. • The theory $A$ has the atoms $s$ (student), $y$ (adult), $e$ (employed), $\mathit{ab}_1$ and $\mathit{ab}_2$, and the formulas $s$, $y$, $y \wedge \neg\mathit{ab}_1 \supset e$, $s \wedge \neg\mathit{ab}_2 \supset \neg e$ and $s \supset \mathit{ab}_1$. Find the minimal models of the [circumscription](/circumscription/) that minimizes $\mathit{ab}_1, \mathit{ab}_2$ (a) with $e$ varying and (b) with $e$ fixed. Does $\neg e$ follow in each case? What changes in case (a) if $s \supset \mathit{ab}_1$ is removed?

19. • In the encoding of the [Yale shooting problem](/yale-shooting-problem/), replace the single wait by $k$ waits: load from 0 to 1, wait from $t$ to $t + 1$ for $t = 1, \ldots, k$, and shoot from $k + 1$ to $k + 2$, with an abnormality atom for each fluent and step and the inertia axioms of the entry. How many minimal sets of abnormalities are there, and which are they? Which one does chronological minimization keep?

20. • The conflicts $\{a, b\}$, $\{b, c\}$, $\{c, d\}$, $\{a, d\}$ are given in this order. Build the [HS-tree](/reiter-hs-tree/) without pruning, labelling each node with the first conflict in the list that its path does not hit. How many leaves does it have, and how many distinct hitting sets do they give? Which are minimal? If the tree is built breadth-first and a node is closed when its path contains the path of a finished leaf, which leaves are closed?

21. • In the Horn theory below, the hypotheses are $\mathit{rain}$, $\mathit{sprinkler}$ and $\mathit{ice}$, and the theory also contains $\neg\mathit{cold}$. Find the minimal [abductive explanations](/abductive-reasoning/) of $\{\mathit{slippery}\}$ and of $\{\mathit{slippery}, \mathit{cloudy}\}$. Which hypotheses are relevant and which are necessary for the second observation?

```
wet ← rain.
wet ← sprinkler.
slippery ← wet.
slippery ← ice.
cold ← ice.
cloudy ← rain.
```

22. • Apply the reduction of the [NP-completeness proof](/stable-model-np-completeness/), with the atom $f$, to $\varphi = (x_1 \vee x_2 \vee x_3) \wedge (\neg x_1 \vee \neg x_2) \wedge (\neg x_2 \vee \neg x_3) \wedge (\neg x_1 \vee \neg x_3)$. How many rules does the program have? List its stable models. Is the program tight, and how many models does its completion have?

23. ★ For $n \ge 2$ let $P_n$ have the rules $a_i \leftarrow a_{i+1}$ and $a_{i+1} \leftarrow a_i$ for $1 \le i < n$, and nothing else. How many loops does $P_n$ have? Find the models of its completion and its stable models. Which loop formulas does the set of all atoms violate?

24. ★ Run [System Z](/system-z/) on $b \to f$, $p \to b$, $p \to \neg f$, $s \to p$ and $s \to f$ (birds fly, penguins are birds, penguins do not fly, super penguins are penguins, super penguins fly). Give the layers. Decide $s \mathrel{|\!\sim} f$ and $s \mathrel{|\!\sim} b$ by computing the ranks $\kappa_Z$ of the formulas involved, and explain the second answer.

25. ★ Let $P = \{a \leftarrow \mathit{not}\ b,\ b \leftarrow \mathit{not}\ a,\ a \leftarrow b\}$ and $Q = \{a\}$. Show that they have the same stable models. Are they [strongly equivalent](/strong-equivalence/)? Find the SE-models where they differ and a program $R$ such that $P \cup R$ and $Q \cup R$ have different stable models.

26. ★ Build the program of the [$\Sigma_2^p$-hardness proof](/disjunctive-asp-sigma2-completeness/) for $\exists x_1 \exists x_2\, \forall y\, ((x_1 \wedge y) \vee (x_2 \wedge \neg y))$. How many rules does it have? Find its answer sets. How many answer sets does the positive program without $w \leftarrow \mathit{not}\ w$ have, and which of them contain $w$?

27. ★ Prove that if the well-founded model of a finite normal program is two-valued, with true atoms $T$, then $T$ is the unique stable model of the program. Use the alternating fixpoint and the fact that every stable model $M$ satisfies $K \subseteq M \subseteq U$ for each pair $(K, U)$ of the iteration.
