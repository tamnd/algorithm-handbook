## History

The forest of parent pointers is older than its analysis. Bernard Galler and Michael Fischer described it in 1964, for the variables that a program declares to share memory, and Knuth gives it as Algorithm E in Section 2.3.3 of *The Art of Computer Programming*. Linking by size or rank and path compression were in use by the early 1970s; path compression is usually credited to Douglas McIlroy and Robert Morris.

The bound took a decade to settle. Fischer proved $O(m \log \log n)$ for linking by size with compression in 1972. John Hopcroft and Jeffrey Ullman improved it to $O(m \lg^* n)$ in 1973, in a paper on several set merging algorithms. In 1975 Robert Tarjan proved the bound $O(m\,\alpha(m, n))$ and showed that it is tight for this algorithm; the title of his paper, *Efficiency of a Good But Not Linear Set Union Algorithm*, states the result. In 1979 he showed that a large class of pointer-machine algorithms needs this much time, and with Jan van Leeuwen in 1984 he analysed the other rules, path halving and splitting among them.

The question of other models came next. Norbert Blum gave in 1986 a structure in which each single operation costs $O(\log n / \log\log n)$, and showed that this is the best possible for separable pointer algorithms. In 1989 Michael Fredman and Michael Saks proved, in the cell-probe model, that every structure needs $\Omega(\alpha(m, n))$ amortized time per operation, whatever it stores. Their chronogram method became a standard tool for lower bounds on dynamic structures. Harold Gabow and Tarjan showed in 1985 that the special case with the union tree known in advance takes linear time on a word RAM.

Later work made the proofs shorter and the variants wider. Raimund Seidel and Micha Sharir gave a top-down proof of the bound in 2005, and CLRS teaches a potential proof of the $O(m\,\alpha(n))$ form. Heikki Mannila and Esko Ukkonen studied union-find with backtracking in 1986, and Ashish Goel, Sanjeev Khanna, Daniel Larkin and Tarjan showed in 2014 that linking by random index matches union by rank in expectation.

## Further reading

- Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest and Clifford Stein, *Introduction to Algorithms*, fourth edition (2022). Chapter 19 gives the linked-list and forest forms and the full potential proof of the $O(m\,\alpha(n))$ bound.
- Robert Sedgewick and Kevin Wayne, *Algorithms*, fourth edition (2011). Section 1.5 builds quick-find, quick-union and weighted quick-union step by step, with traces and a table of costs.
- Robert Endre Tarjan, *Data Structures and Network Algorithms*, SIAM (1983). Chapter 2 treats disjoint sets with the rules and the analysis in a few pages.
- Robert E. Tarjan and Jan van Leeuwen, *Worst-case analysis of set union algorithms*, Journal of the ACM 31(2), 1984. The bounds for every combination of linking and compaction rules.
- Raimund Seidel and Micha Sharir, *Top-down analysis of path compression*, SIAM Journal on Computing 34(3), 2005. A short top-down proof of the inverse Ackermann bound.
