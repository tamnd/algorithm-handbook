## History

The notation is older than computers. Paul Bachmann used the symbol $O$ in 1894, in *Die analytische Zahlentheorie*, to bound the error terms of number theory. Edmund Landau used it widely from 1909, in his *Handbuch der Lehre von der Verteilung der Primzahlen*, and added the symbol $o$; that is why the notation is often called Landau notation. G. H. Hardy and J. E. Littlewood introduced $\Omega$ in 1914, with a weaker meaning than the one used for algorithms: in their sense $f = \Omega(g)$ needs $f(n) \ge c\,g(n)$ only for infinitely many $n$.

Analysis of algorithms took the notation over in the 1960s and 1970s. In 1976 Donald Knuth published *Big Omicron and big Omega and big Theta* in SIGACT News. He proposed $\Omega$ in the sense of "at least a constant times, for all large $n$" and $\Theta$ for "the same order", and these are the meanings in every algorithms text today. Knuth's *The Art of Computer Programming* set the style of exact analysis, with harmonic numbers, sums and Stirling's formula, that the later entries of this chapter follow.

The idea that "efficient" means "polynomial time" also dates from the 1960s. Alan Cobham, in a paper at the 1964 International Congress for Logic, Methodology and Philosophy of Science (published in 1965), proposed the functions computable in polynomial time as a class that does not depend on the machine. Jack Edmonds, in *Paths, Trees, and Flowers* (1965), called an algorithm "good" when its running time has a polynomial bound. In the same year Juris Hartmanis and Richard Stearns defined complexity classes by running time on Turing machines.

Some of the mathematics is much older. James Stirling gave the formula $n! \sim \sqrt{2\pi n}\,(n/e)^n$, with the constant $\sqrt{2\pi}$, in *Methodus Differentialis* (1730); Abraham de Moivre had found the form of the formula with the constant only as a numerical series. Herbert Robbins proved the two-sided bounds on the error in 1955. The Ackermann function comes from logic: Wilhelm Ackermann defined a three-argument version in 1928, Rózsa Péter gave a two-argument one in 1935, and Raphael Robinson the form used today in 1948. Its inverse entered algorithms in 1975, when Robert Tarjan showed that union-find with union by rank and path compression costs $O(m\,\alpha(m, n))$ time for $m$ operations.

The experimental side came later. Tilde notation and the doubling hypothesis are the working tools of the textbooks of Robert Sedgewick, and Catherine McGeoch's *A Guide to Experimental Algorithmics* (2012) treats the design of experiments on algorithms as a subject of its own.

## Further reading

- Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest and Clifford Stein, *Introduction to Algorithms*, fourth edition (2022). Chapter 3 defines the notation with care, and Appendix A covers sums.
- Ronald L. Graham, Donald E. Knuth and Oren Patashnik, *Concrete Mathematics*, second edition (1994). Chapter 2 on sums, Chapter 6 on harmonic numbers and Chapter 9 on asymptotics are the best training in the calculations this chapter uses.
- Donald E. Knuth, *The Art of Computer Programming, Volume 1: Fundamental Algorithms*, third edition (1997). Section 1.2 collects the mathematical preliminaries, from logarithms and harmonic numbers to the $O$ notation, with exercises.
- Robert Sedgewick and Kevin Wayne, *Algorithms*, fourth edition (2011). Section 1.4 shows how to predict running times with tilde approximations and check them by experiment.
- Robert Sedgewick and Philippe Flajolet, *An Introduction to the Analysis of Algorithms*, second edition (2013). For exact counts and the leading constants that $\Theta$ hides.
