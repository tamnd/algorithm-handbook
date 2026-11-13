1. ◦ Take positions $1, \ldots, 12$ of an RNA and assume that every pair listed below joins two letters that can pair. Write each set in dot-bracket notation and say whether it is an [RNA secondary structure](/rna-secondary-structure/) with at least three unpaired bases in every hairpin: (a) $\{(1, 11), (2, 10), (4, 8)\}$; (b) $\{(1, 11), (2, 10), (3, 6)\}$; (c) $\{(1, 7), (4, 11)\}$.

2. ◦ The numbers $S_3(n)$ of secondary structures of a chain of $n$ bases, when any two bases may pair and hairpins have at least three unpaired bases, start $1, 1, 1, 1, 1, 2, 4, 8, 16, 32, 65$ for $n = 0, \ldots, 10$. Use the recurrence in the entry to find $S_3(11)$ and $S_3(12)$.

3. ◦ A structure on 24 positions has the pairs $a = (1, 12)$, $b = (3, 18)$, $c = (14, 24)$, $d = (11, 21)$ and $e = (5, 10)$. Draw the crossing graph of these [pseudoknotted](/pseudoknot/) pairs. What is the least number of bracket kinds needed to write the structure, and what is the largest nested subset? Write the structure with that least number of kinds.

4. ◦ A model of a 100-residue protein is placed on the native by one fixed superposition. After it, 90 residues are 0.8 Å from their native positions and 10 residues are 10 Å away. Compute the [RMSD](/rmsd/) of this superposition, the [TM-score](/tm-score/) sum at it, and the fractions of [GDT-TS](/gdt-ts/) at it. What do these numbers tell you about the true TM-score and GDT-TS, which maximize over superpositions?

5. ◦ Compute $d_0$ of the TM-score for a target of $L = 200$ residues. What does a residue at distance $d_0$ contribute to the sum, one at $2 d_0$, and one at 3 Å?

6. ◦ Two centered point sets of $N = 4$ points have $G_A + G_B = 30$ (the sums of squared norms), and their correlation matrix $H$ has singular values $5, 3, 1$ and $\det H < 0$. Using [optimal superposition](/optimal-superposition/), find the smallest RMSD over rotations, and the smallest over rotations and reflections together.

7. ◦ A short RNA has two structures that matter: the open chain, with free energy 0, and one hairpin with $\Delta G = -1.2$ kcal/mol. At 37 °C ($T = 310.15$ K, $R = 1.987 \times 10^{-3}$ kcal/(mol K)), what is the probability of the hairpin in the Boltzmann distribution?

8. ◦ A residue-by-residue prediction of secondary structure reads CCHHHHHHCCEEECCC, and the DSSP states reduced to three classes read CHHHHHHCCEEEEECC. Compute $Q_3$ as defined in [protein secondary structure prediction](/protein-secondary-structure-prediction/), the fraction of each true state that is predicted correctly, and the $Q_3$ of the rule that predicts the most common true state everywhere.

9. ◦ With the formula of the [dihedral angle](/dihedral-angle/) entry, compute the angle of $p_0 = (1, 0, 0)$, $p_1 = (0, 0, 0)$, $p_2 = (0, 1, 0)$ and $p_3 = (1, 1, 1)$. Then give the angle when $p_3 = (1, 1, 0)$ and when $p_3 = (-1, 1, 0)$.

10. • In the square-lattice [HP model](/hp-model/), number the residues from 0. Show without search that HPHPHPHPH has optimum 0, although the bound $2 \min(|\text{EV}|, |\text{OD}|) + 2$ of the entry allows 2 contacts. For HPPHHPPHHPPH, compute the bound and then find the optimum by exhaustive search over self-avoiding walks.

11. • Run the [Nussinov algorithm](/nussinov-algorithm/) with pairs AU, GC and GU and at least three unpaired bases in a hairpin on AGGCAAAGCUAAAGU. What is the most pairs, and how many different structures reach it? Use the unambiguous recurrence to count them.

12. • Turn the Nussinov recurrence into a recurrence that counts all structures instead of maximizing. Use it to find the number of structures of GGGGAAAACCCC, and prove that $\mathrm{G}^k \mathrm{A}^u \mathrm{C}^k$ with $u \ge 3$ has $\binom{2k}{k}$ structures.

13. • The Nussinov algorithm folds GCAAAGCAAAGC into `((...)(...))`, its only structure with three pairs. Compute the energy of this structure in the toy integer model of the [Zuker algorithm](/zuker-algorithm/) entry (hairpin $3 + u$, stack $-(w + w')$, multiloop $a + bk + cu$ with $a = 3$, $b = 1$, $c = 0$). Then find the minimum free energy and all the structures that reach it.

14. • In the same toy model, take GGAAACC and weight a structure of energy $E$ by $2^{-E}$, as in the example of the [McCaskill algorithm](/mccaskill-algorithm/). List the six structures with their energies, compute $Z$, the probabilities of the pairs $(1, 7)$ and $(2, 6)$, and the centroid structure, the set of pairs with probability above $1/2$.

15. • Find the largest number of nested pairs of GGAAUUAACCAAAAAA (pairs AU, GC, GU, hairpins of at least three bases), and the largest number of pairs when crossings are allowed. Write a structure that reaches the second number with two bracket kinds.

16. • In the plane, show that after both sets are centered, the rotation angle that minimizes the RMSD is $\theta = \operatorname{atan2}\big(\sum_i x_i \times y_i,\ \sum_i x_i \cdot y_i\big)$, where $\times$ is the scalar cross product. Apply it to $x = (1, 0), (-1, 0), (0, 1), (0, -1)$ and $y = (0, 2), (0, -2), (-1, 0), (1, 0)$, and give the RMSD before and after the rotation.

17. • Prove that if all points of one structure lie in a plane, the best rotation gives the same RMSD as the best rotation or reflection, so the sign correction of the [Kabsch algorithm](/kabsch-algorithm/) never changes the RMSD.

18. • Add a free energy $\varepsilon$ to every structure that contains the pair $(i, j)$, and let $Z(\varepsilon)$ be the new partition function. Prove that the probability of the pair is $p_{ij} = -RT\, \partial \ln Z / \partial \varepsilon$ at $\varepsilon = 0$.

19. • Give an algorithm that decides whether a set of $p$ base pairs can be written in dot-bracket notation with two bracket kinds, and state its running time. Apply it to the pairs of Exercise 3 without $d$.

20. ★ A pair $(i, j)$ of a structure is stacked if $(i + 1, j - 1)$ is also a pair. Give an $O(n^3)$ dynamic program that finds a nested structure with the most stacked pairs, and prove it correct.

21. ★ Let $p_{ij}$ be the pair probabilities of a Boltzmann ensemble of nested structures. Prove that the pairs with $p_{ij} > 1/2$ form a valid secondary structure, and that this centroid structure maximizes the expected number of correct pairs minus the expected number of wrong pairs over all structures.

22. ★ Prove that with $\theta = 0$, when any two bases may pair, the secondary structures of length $n$ are counted by the Motzkin numbers: give a bijection with lattice paths of $n$ steps up, down or level that start and end at height 0 and never go below it.

23. ★ Show that when the allowed pairs are AU, GC and GU, the graph whose vertices are the positions of a sequence and whose edges are the allowed pairs with $j - i > 3$ is bipartite. Conclude that the largest number of pairs with crossings allowed can be found by [Hopcroft-Karp](/hopcroft-karp/) in $O(n^{5/2})$ time.

24. ★ In [side-chain packing](/side-chain-packing/), suppose the interaction graph is a tree on $n$ residues with $p$ rotamers each. Give a dynamic program that finds the minimum energy assignment in $O(n p^2)$ time and prove it correct.
