## History

The heap began as a sorting tool. J. W. J. Williams published Heapsort as Algorithm 232 in the *Communications of the ACM* in 1964, with the array layout and the insert and extract operations. In the same year Robert Floyd published Treesort 3, Algorithm 245, which builds the heap bottom-up in linear time. The use of the heap as a general priority queue, with decrease-key, came later and is the form most textbooks now give.

Merging came next. Clark Crane described leftist trees in his Stanford thesis of 1972, and Knuth put them in Volume 3 of *The Art of Computer Programming* in 1973. Donald Johnson used heaps with $d$ children in 1975 for shortest paths and minimum spanning trees. Jean Vuillemin introduced the binomial queue in 1978, and Mark Brown analysed and implemented it in the same year.

The 1980s brought amortized analysis to heaps. Michael Fredman and Robert Tarjan presented the Fibonacci heap in 1984 and published the full paper in 1987; it made decrease-key $O(1)$ amortized and so improved Dijkstra's and Prim's algorithms. Daniel Sleator and Tarjan gave the self-adjusting skew heap in 1986, and in the same year Fredman, Robert Sedgewick, Sleator and Tarjan gave the pairing heap, which is simpler and fast in practice. Whether the pairing heap matches the Fibonacci bounds stayed open until Fredman showed in 1999 that its decrease-key cannot be $O(1)$; its exact cost is still unknown.

Later work sought the same bounds in the worst case, or with simpler structures. Relaxed heaps (Driscoll, Gabow, Shrairman and Tarjan, 1988) made decrease-key $O(1)$ in the worst case without meld, and Gerth Stølting Brodal's queue of 1996 did it with meld as well. Brodal, George Lagogiannis and Tarjan gave strict Fibonacci heaps in 2012, with the same bounds on a pointer machine. Rank-pairing heaps (2009), thin heaps (2008) and hollow heaps (2015) aim at simplicity instead. Bernard Chazelle's soft heap of 1998, which corrupts keys on purpose, gave his minimum spanning tree algorithm, and Kaplan, Tarjan and Zwick published a simpler version in 2013.

The integer heaps have their own line. Robert Dial's bucket queue of 1969 was a shortest-path method, Randy Brown's calendar queue of 1988 was made for event simulation, and the radix heap of Ahuja, Mehlhorn, Orlin and Tarjan (1990) was again made for shortest paths.

## Further reading

- Donald E. Knuth, *The Art of Computer Programming, Volume 3: Sorting and Searching*, second edition (1998). Section 5.2.3 treats heaps, heapsort and leftist trees, with their history.
- Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest and Clifford Stein, *Introduction to Algorithms*, fourth edition (2022). Chapter 6 covers the binary heap and its priority queue operations with careful proofs; the third edition (2009) has a chapter on Fibonacci heaps.
- Robert Sedgewick and Kevin Wayne, *Algorithms*, fourth edition (2011). Section 2.4 gives the heap as code, with the indexed priority queue and the top M client.
- Robert Endre Tarjan, *Data Structures and Network Algorithms*, SIAM (1983). A short book that treats heaps, among them the leftist heap, as tools for network algorithms.
- Michael L. Fredman and Robert E. Tarjan, *Fibonacci heaps and their uses in improved network optimization algorithms*, Journal of the ACM 34(3), 1987. The paper that started the search for fast decrease-key.
- Chris Okasaki, *Purely Functional Data Structures*, Cambridge University Press (1998). Heaps without assignment; Section 3.1 is the leftist heap.
