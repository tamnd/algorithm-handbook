## History

Sorting was one of the first jobs given to stored-program computers, and some of the first programs ever written were sorts. John von Neumann wrote a merge sort for the EDVAC in 1945, as a test of what the planned machine could do. John Mauchly described insertion sort, with binary insertion, in the Moore School Lectures of 1946.

Shellsort came in 1959, from Donald Shell. Quicksort came in 1961, from C. A. R. Hoare, who published it as an algorithm in the *Communications of the ACM* and in a longer paper in *The Computer Journal* the next year. Heapsort came in 1964, from J. W. J. Williams; Robert Floyd improved its first phase in the same year. In 1959 Lester Ford and Selmer Johnson found the merge insertion method, which still makes the fewest comparisons known for most small $n$.

The theory came with the methods. The decision-tree argument for the $\lg n!$ lower bound was known by the late 1950s. Robert Sedgewick's thesis of 1975 analyzed quicksort and its variants in detail. Vaughan Pratt showed in 1971 that Shellsort with gaps of the form $2^p 3^q$ runs in $\Theta(n \log^2 n)$ time; how fast Shellsort can be with the best gaps is still open.

The sorts in today's libraries were built later. Jon Bentley and Douglas McIlroy described the quicksort of the C library in *Engineering a Sort Function* (1993). David Musser introduced introsort in 1997, and it became the sort of the C++ standard library. Tim Peters wrote Timsort for Python in 2002; Java adopted it for objects. In 2015 a team using the KeY verification system found that the invariant on the run stack of Timsort, as implemented in Java and Python, could fail on some inputs, and the implementations were fixed. Vladimir Yaroslavskiy's dual-pivot quicksort became the sort for primitive arrays in Java 7, and later analysis by Sebastian Wild and Markus Nebel explained why it runs faster than classic quicksort.

Two lines of research run through the advanced entries of the chapter. Adaptive sorting asks how fast a sort can be in terms of how much disorder its input has; Heikki Mannila set out measures of presortedness in 1985, and Vladimir Estivill-Castro and Derick Wood surveyed the field in 1992. Stable in-place sorting asks whether a sort can be stable, in place and $O(n \log n)$ at once; [block sort](/block-sort/) and its relatives, such as the method of Pok-Son Kim and Arne Kutzner (2008), show that it can.

## Further reading

- Donald E. Knuth, *The Art of Computer Programming, Volume 3: Sorting and Searching*, second edition (1998). Chapter 5 is still the deepest single treatment of sorting, with its history and hundreds of exercises.
- Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest and Clifford Stein, *Introduction to Algorithms*, fourth edition (2022). Chapters 2, 6, 7 and 8 cover insertion sort, merge sort, heapsort, quicksort and the lower bound, with careful proofs.
- Robert Sedgewick and Kevin Wayne, *Algorithms*, fourth edition (2011). Chapter 2 treats the sorts as code to be measured, with experiments.
- Jon Bentley and M. Douglas McIlroy, *Engineering a Sort Function*, Software: Practice and Experience 23(11), 1993. A short paper on how a real library sort is built and tested.
- Vladimir Estivill-Castro and Derick Wood, *A Survey of Adaptive Sorting Algorithms*, ACM Computing Surveys 24(4), 1992.
