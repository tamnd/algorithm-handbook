## History

The mathematics of this chapter is older than computers. Jacob Bernoulli proved the first law of large numbers in his *Ars Conjectandi*, published in 1713 after his death. Abraham de Moivre found the normal approximation to the number of heads in 1733, and Laplace extended it in 1812. Bienaymé proved the inequality now named after Chebyshev in 1853; Chebyshev proved it more generally in 1867. The simpler inequality named after his student Andrey Markov had appeared earlier in Chebyshev's own work. Andrey Kolmogorov gave probability its axioms, the probability space of the first entry, in 1933.

The exponential tail bounds came from statistics. Herman Chernoff published his method in 1952, in a paper on the efficiency of statistical tests, and later credited the bound itself to Herman Rubin. Wassily Hoeffding proved his inequality for bounded variables in 1963, and Kazuoki Azuma extended it to martingales in 1967. Abraham Wald proved his equation in 1944 for sequential tests, and Joseph Doob built the theory of martingales, including the optional stopping theorem, in the 1940s and 1950s.

In computer science, averages over random inputs came first. Tony Hoare analyzed the expected number of comparisons of quicksort in 1962, and Donald Knuth made average-case analysis a central method of *The Art of Computer Programming* from 1968 on. Algorithms that make their own random choices spread in the late 1970s, with Michael Rabin's paper on probabilistic algorithms of 1976 and the primality tests of Solovay and Strassen and of Rabin. The textbooks of Rajeev Motwani and Prabhakar Raghavan (1995) and of Michael Mitzenmacher and Eli Upfal (2005) collected the tools of this chapter for computer scientists.

Two results of the last group have their own story. Paul Erdős and László Lovász proved the local lemma in 1975 as a tool for showing that objects exist, with no way to find them. Robin Moser and Gábor Tardos gave a simple resampling algorithm that finds them in 2010. Daniel Spielman and Shang-Hua Teng introduced smoothed analysis in 2001 to explain why the simplex method is fast in practice, though slow on some inputs.

## Further reading

- Michael Mitzenmacher and Eli Upfal, *Probability and Computing*, second edition (2017). The standard text for this chapter, from events to martingales, with balls and bins and the Chernoff bounds in detail.
- Rajeev Motwani and Prabhakar Raghavan, *Randomized Algorithms* (1995). Tail bounds and their use in algorithms, with many examples.
- Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest and Clifford Stein, *Introduction to Algorithms*, fourth edition (2022). Chapter 5 and Appendix C: the hiring problem, indicator variables, and the basic probability.
- William Feller, *An Introduction to Probability Theory and Its Applications*, Volume 1, third edition (1968). The classical book on discrete probability.
- Noga Alon and Joel H. Spencer, *The Probabilistic Method*, fourth edition (2016). The local lemma, martingales and concentration, with combinatorial applications.
- Devdatt P. Dubhashi and Alessandro Panconesi, *Concentration of Measure for the Analysis of Randomized Algorithms* (2009). Chernoff, Hoeffding and Azuma bounds, and what to do when the variables are dependent.
