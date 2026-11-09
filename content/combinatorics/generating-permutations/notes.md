## History

Listing permutations is older than computers. Knuth traces the lexicographic successor rule, the method of [next permutation](/next-permutation/), to the Indian mathematician Nārāyaṇa Paṇḍita in the fourteenth century. English change ringers of the seventeenth century rang the bells of a tower in the order now called plain changes, in which two bells adjacent in the order of ringing swap places at each change. Hugo Steinhaus later posed the same order in a book of mathematical problems.

The computer methods came in the early 1960s. H. F. Trotter published plain changes as Algorithm 115, "Perm", in the *Communications of the ACM* in 1962, and Selmer M. Johnson published the same order in *Mathematics of Computation* in 1963; the order now carries the names of all three. In 1963 B. R. Heap described a method that makes one exchange of any two positions per step, in "Permutations by interchanges" in *The Computer Journal*. In 1973 Gideon Ehrlich gave loopless versions of plain changes, with a constant bound on the time of each step.

Robert Sedgewick's survey "Permutation generation methods" (1977) put the methods side by side. He studied the exchange methods in detail, found that they beat the lexicographic methods for listing all permutations, and recommended Heap's method as the fastest simple one. Knuth's Section 7.2.1.2, in Volume 4A of *The Art of Computer Programming*, gathers the methods as Algorithm L for lexicographic order, Algorithm P for plain changes and Algorithm E for Ehrlich's swaps, with their history. The lexicographic rule became the function `next_permutation` of the C++ standard library.

Ranking turns a permutation into a number. In lexicographic order the rank is the Lehmer code read in the factorial number system, which gives a simple quadratic method and an $O(n \log n)$ method with a counting tree. Kreher and Stinson (1999) gave rank, unrank and successor functions for both lexicographic and Trotter-Johnson order. Wendy Myrvold and Frank Ruskey (2001) ranked and unranked in $O(n)$ time by giving up lexicographic order, and Martin Mareš and Milan Straka (2007) reached $O(n)$ arithmetic operations for lexicographic order itself.

Multisets and restricted classes came later. James Korsh and Paul LaFollette (2004) gave a loopless generator for multiset permutations, and Aaron Williams (2009) gave one that uses a constant number of variables and moves by prefix shifts. Involutions appear in Knuth's volume on sorting: Section 5.1.4 of Volume 3 counts them and relates them to tableaux through the Robinson-Schensted correspondence, and Flajolet and Sedgewick's *Analytic Combinatorics* (2009) derives their exponential generating function $e^{z + z^2/2}$.

## Further reading

- Donald E. Knuth, *The Art of Computer Programming, Volume 4A: Combinatorial Algorithms, Part 1* (2011). Section 7.2.1.2 covers every generator of this chapter, with exact operation counts, history and many exercises.
- Robert Sedgewick, *Permutation Generation Methods*, ACM Computing Surveys 9(2), 1977. The survey that compared the methods as programs and timed them.
- Donald L. Kreher and Douglas R. Stinson, *Combinatorial Algorithms: Generation, Enumeration, and Search* (1999). Chapter 2 gives successor, rank and unrank functions for lexicographic and Trotter-Johnson order, written as code.
- Carla Savage, *A Survey of Combinatorial Gray Codes*, SIAM Review 39(4), 1997. The minimal-change orders of permutations in the wider setting of Gray codes, with the Cayley graph view.
- Richard P. Stanley, *Enumerative Combinatorics, Volume 1*, second edition (2012). Section 1.3 treats cycles, the standard representation and the fundamental bijection.
