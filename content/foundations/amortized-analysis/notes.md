## History

Arguments that charge the cost of an expensive step to earlier cheap ones were used long before they had a name. The analyses of union-find in the 1970s, by John Hopcroft and Jeffrey Ullman and then by Robert Tarjan, bound the total cost of a sequence of operations rather than each one. Jon Bentley and James Saxe's logarithmic method of 1980, which makes static structures dynamic with a binary-counter scheme, has the same form.

The name and the methods were fixed in 1985. Tarjan's paper *Amortized computational complexity*, in the *SIAM Journal on Algebraic and Discrete Methods*, defined the amortized cost of an operation and described the two ways of proving amortized bounds that this chapter calls the accounting method (the banker's view, with credits on objects) and the potential method (the physicist's view, with one function of the whole state). In the same year Daniel Sleator and Tarjan published two analyses that show the strength of the potential method: the list-update paper in the *Communications of the ACM*, which proved that move-to-front is within a factor of 2 of any fixed order, and the paper on splay trees in the *Journal of the ACM*. Michael Fredman and Tarjan's Fibonacci heaps, presented in 1984 and published in 1987, made amortized bounds central to the design of graph algorithms.

The questions of when amortized bounds are not enough came next. Mark Overmars, in *The Design of Dynamic Data Structures* (1983), developed global rebuilding, which spreads the cost of rebuilding a structure over the operations that precede the rebuild and so gives worst-case bounds. Chris Okasaki, in *Purely Functional Data Structures* (1998), showed how amortization fails when old versions of a structure can be used again, and how lazy evaluation repairs it in functional languages.

## Further reading

- Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest and Clifford Stein, *Introduction to Algorithms*, fourth edition (2022). Chapter 16 presents the three methods with the stack, the counter and dynamic tables.
- Robert E. Tarjan, "Amortized computational complexity", *SIAM Journal on Algebraic and Discrete Methods* 6(2) (1985). The paper that named the subject; short and readable.
- Daniel D. Sleator and Robert E. Tarjan, "Amortized efficiency of list update and paging rules", *Communications of the ACM* 28(2) (1985). The move-to-front analysis, a model of the potential method.
- Chris Okasaki, *Purely Functional Data Structures* (1998). Amortization with and without persistence, and the banker's and physicist's methods in a functional setting.
- Mark H. Overmars, *The Design of Dynamic Data Structures*, Lecture Notes in Computer Science 156 (1983). Global rebuilding and the transformation of static structures into dynamic ones.
