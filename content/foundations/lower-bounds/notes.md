## History

The first exact lower bounds were about tournaments. Lewis Carroll complained in 1883 that a knockout tennis tournament may give the second prize to a player who lost early to the winner. J. Schreier gave in 1932 a method that finds the second best with $n + \lceil \lg n \rceil - 2$ games, with an incomplete argument that no method does better, and S. S. Kislitsyn completed the proof in 1964. Ira Pohl proved the bound $\lceil 3n/2 \rceil - 2$ for the maximum and minimum in 1972. Knuth's third volume, first published in 1973, collected these results together with the information-theoretic bound for sorting and the analysis of merge insertion by Lester Ford and Selmer Johnson (1959).

Bounds that count arithmetic operations began with Alexander Ostrowski, who asked in 1954 whether Horner's rule is optimal and proved it for small degrees; Victor Pan proved the multiplication bound for every degree in 1966. Jacques Morgenstern proved in 1973 that the fast Fourier transform is optimal up to a constant factor among linear algorithms with bounded constants. For problems with yes-or-no answers, David Dobkin and Richard Lipton counted the connected components of the yes set for linear decision trees in 1979; J. Michael Steele and Andrew Yao extended the count to algebraic decision trees in 1982, and Michael Ben-Or to algebraic computation trees in 1983.

Andrew Yao contributed two of the methods of the last groups. In 1977 he observed that the minimax theorem of von Neumann turns a lower bound on a random input into a lower bound for randomized algorithms. In 1981, in the paper "Should tables be sorted?", he introduced the cell-probe model. Michael Fredman and Michael Saks proved the first strong cell-probe bounds, for partial sums and union-find, in 1989. Memory traffic got its own lower bounds with the red-blue pebble game of Jia-Wei Hong and H. T. Kung in 1981 and with the external memory model of Alok Aggarwal and Jeffrey Vitter in 1988.

## Further reading

- Donald E. Knuth, *The Art of Computer Programming*, Volume 3, *Sorting and Searching*, second edition (1998). Section 5.3 on minimum-comparison sorting and selection, with the history of the tournament problems.
- Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest and Clifford Stein, *Introduction to Algorithms*, fourth edition (2022). Section 8.1 for the sorting bound and Section 9.1 for the maximum and minimum.
- Peter Bürgisser, Michael Clausen and M. Amin Shokrollahi, *Algebraic Complexity Theory* (1997). Lower bounds for arithmetic: Horner's rule, the FFT and algebraic computation trees.
- Ming Li and Paul Vitányi, *An Introduction to Kolmogorov Complexity and Its Applications*, fourth edition (2019). The incompressibility method, with many lower bounds proved by it.
- Mihai Pătraşcu, *Lower Bound Techniques for Data Structures*, PhD thesis, MIT (2008). The modern methods of cell-probe lower bounds.
