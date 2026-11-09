## History

R. C. Bose and R. J. Nelson posed the problem of the fewest comparators in *A sorting problem* (Journal of the ACM, 1962), and gave networks of size about $n^{\lg 3}$. Kenneth Batcher found the bitonic sorter and the odd-even merge sort and published them in *Sorting networks and their applications* at the AFIPS Spring Joint Computer Conference of 1968. His networks have size $O(n \log^2 n)$ and depth $O(\log^2 n)$, and for practical sizes nothing better has been found since.

Small networks were studied by hand and by early computer searches. Milton Green found the 60-comparator network for 16 inputs around 1970. Robert Floyd and Donald Knuth proved the untangling theorem and the optimal sizes for small $n$, and David Van Voorhis proved his lower bound on size in 1972. Knuth collected all of this in Section 5.3.4 of *The Art of Computer Programming*, where the zero-one principle appears as Theorem Z.

In 1983 Miklós Ajtai, János Komlós and Endre Szemerédi built a network of depth $O(\log n)$, which settled the asymptotic question but with huge constants. Michael Paterson simplified the construction in 1990 and brought the constant below 6100, and Joel Seiferas simplified it further in 2009. Whether a network of depth $O(\log n)$ with a small constant exists is still open.

The hardness of checking a network came next. Moon Jung Chung and B. Ravikumar showed in 1989 that deciding whether a network sorts is co-NP-complete, and Ian Parberry showed that this holds even for networks only $4 \lg n + O(1)$ layers deeper than the best. Parberry also found the pairwise sorting network in 1992 and used a computer search to find the optimal depth for 9 and 10 inputs.

SAT solvers then took the searches much further. Daniel Bundala and Jakub Závodný found the optimal depth for all $n \le 16$ in 2014. Michael Codish, Luís Cruz-Filipe, Michael Frank and Peter Schneider-Kamp proved that 9 inputs need 25 comparators, and later work by Codish's group settled the depth for 17 inputs. Jannis Harder found the optimal sizes for 11 and 12 inputs in 2020.

## Further reading

- Donald E. Knuth, *The Art of Computer Programming, Volume 3: Sorting and Searching*, second edition (1998), Section 5.3.4. The standard reference: the zero-one principle, Batcher's networks, the best small networks and many exercises.
- Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest and Clifford Stein, *Introduction to Algorithms*, second edition (2001), Chapter 27. A gentle account of comparators, the zero-one principle, bitonic sorting and merging networks, with figures. The chapter was dropped from later editions.
- K. E. Batcher, *Sorting networks and their applications*, AFIPS Spring Joint Computer Conference (1968). The short original paper on bitonic and odd-even merge sorting.
- Joel Seiferas, *Sorting networks of logarithmic depth, further simplified*, Algorithmica 53 (2009). The most readable proof that depth $O(\log n)$ is possible.
- Daniel Bundala and Jakub Závodný, *Optimal sorting networks*, LATA 2014. Shows how a SAT encoding settles the optimal depth of small networks.
