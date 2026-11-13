## What to remember

- An [RNA secondary structure](/rna-secondary-structure/) is a set of nested base pairs with at least three unpaired bases in each hairpin. Their number grows like $2.29^n$ up to a polynomial factor, yet the [Nussinov algorithm](/nussinov-algorithm/) finds the most pairs in $\Theta(n^3)$ time and $\Theta(n^2)$ space, because a pair splits the interval into two independent parts.
- In the [nearest-neighbor model](/nearest-neighbor-model/) the energy is a sum over loops, so the same split works. The [Zuker algorithm](/zuker-algorithm/) finds a minimum free energy structure and the [McCaskill algorithm](/mccaskill-algorithm/) the partition function and every pair probability, both in $\Theta(n^3 + n^2 L^2)$ time and $\Theta(n^2)$ space with interior loops of at most $L$ bases. Both are exact under the model, which is itself judged by measurement.
- [Pseudoknots](/pseudoknot/) break the split. With plain pair counts and crossings allowed the problem becomes a maximum matching and stays polynomial; restricted classes cost $O(n^4)$ to $O(n^6)$; in the nearest-neighbor pseudoknot model the general problem is [NP-complete](/pseudoknot-np-hardness/).
- The best rigid fit of two matched point sets puts centroid on centroid and maximizes $\operatorname{tr}(RH)$, with maximum $s_1 + s_2 + \operatorname{sign}(\det H)\, s_3$ over rotations. The [Kabsch algorithm](/kabsch-algorithm/) and [quaternion superposition](/quaternion-superposition/) compute it exactly in $\Theta(N)$ time.
- [RMSD](/rmsd/) is ruled by a few large errors: one atom off by 5 Å, with all others exact, gives $5/\sqrt N$. [GDT-TS](/gdt-ts/) averages the fractions of residues within 1, 2, 4 and 8 Å, and [TM-score](/tm-score/) sums $1/(1 + (d_i/d_0)^2)$ with $d_0(L) = 1.24\sqrt[3]{L - 15} - 1.8$. Their search over superpositions is heuristic, so a reported value is a lower bound.
- Folding in the [HP model](/hp-model/) is [NP-complete](/hp-folding-np-completeness/) on the square and the cubic lattice. Exhaustive search is exact but exponential; Hart and Istrail give approximation ratios $1/4$ and $3/8$.
- [Threading](/protein-threading/) is an exact $O(nm)$ dynamic program with singleton scores and NP-complete with pair terms. Deciding [side-chain packing](/side-chain-packing/) is NP-complete; it is solvable exactly in $O(n p^{w+1})$ time on interaction graphs of treewidth $w$, and [dead-end elimination](/dead-end-elimination/) prunes rotamers safely but leaves an exponential search in the worst case.
- [Fragment assembly](/fragment-assembly/), [Rosetta](/rosetta/), [molecular dynamics](/molecular-dynamics/) and [I-TASSER](/i-tasser/) are heuristics: valid chains, no bound on the gap to the optimum of their energy. [AlphaFold](/alphafold/) is a trained model; its accuracy is a benchmark result (in CASP14, a median backbone r.m.s.d.95 of 0.96 Å against 2.8 Å for the next method), and pLDDT is a predicted lDDT.

| Method | Model | What it guarantees | Time | Entry |
|---|---|---|---|---|
| Nussinov | base pairs, nested | most pairs, exact | $\Theta(n^3)$ | [Nussinov](/nussinov-algorithm/) |
| Zuker | nearest-neighbor loops, nested | minimum energy, exact | $\Theta(n^3 + n^2L^2)$ | [Zuker](/zuker-algorithm/) |
| McCaskill | nearest-neighbor loops, nested | partition function and pair probabilities, exact | $\Theta(n^3 + n^2L^2)$ | [McCaskill](/mccaskill-algorithm/) |
| Sankoff, two sequences | pairs and alignment, nested | best joint score, exact | $\Theta(m^3 n^3)$ worst | [Sankoff](/sankoff-rna-algorithm/) |
| Rivas and Eddy | one class of pseudoknots | minimum energy in the class, exact | $O(n^6)$ | [pseudoknot prediction](/rna-pseudoknot-prediction/) |
| Kabsch, quaternion | RMSD, given correspondence | optimal rigid fit, exact | $\Theta(N)$ | [Kabsch](/kabsch-algorithm/) |
| HP exhaustive search | square or cubic lattice | optimum, exact | exponential | [HP model](/hp-model/) |
| Threading, singleton | sequence-to-core scores | best threading, exact | $O(nm)$ | [threading](/protein-threading/) |
| Dead-end elimination | pairwise rotamer energy | never removes the optimum | $O(n^3 p^4)$, then search | [DEE](/dead-end-elimination/) |
| Fragment assembly | lattice or coarse score | best state visited | $O(Sn)$ | [fragment assembly](/fragment-assembly/) |
| AlphaFold | trained network | none; accuracy measured | $O(s^2 n + s n^2 + n^3)$ per cycle | [AlphaFold](/alphafold/) |

: Main methods of the chapter. $n$ and $m$ are sequence lengths, $L$ the largest interior loop, $N$ the number of atoms, $p$ the rotamers per residue, $S$ the Monte Carlo steps and $s$ the number of sequences in the alignment. "Exact" is under the stated model.

## Choosing a method

For one RNA sequence, run a Zuker and McCaskill package with the Turner 2004 parameters, and check the pair probabilities before you trust the minimum energy structure. With several related sequences, use [simultaneous alignment and folding](/simultaneous-alignment-and-folding/), or a [covariance model](/covariance-model/) when the family is known. Allow pseudoknots only with a program that names its class, and expect $O(n^4)$ time or worse.

For a protein, start with a trained predictor such as AlphaFold and read its pLDDT: regions below 50 are often disordered, and accuracy falls when the alignment has few sequences. With a close template, [comparative modeling](/comparative-modeling/) is cheap and easy to check. Molecular dynamics answers questions about motion. To compare models, report TM-score or GDT-TS with RMSD, and lDDT when domains may move.
