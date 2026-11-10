## History

Sampling began in survey statistics. Neyman's paper of 1934 set out stratified sampling with the allocation that bears his name, Hansen and Hurwitz gave the estimator for sampling with probability proportional to size in 1943, and Horvitz and Thompson generalized it in 1952 to any design without replacement whose inclusion probabilities are known. Systematic selection was in use long before its theory, which William and Lillian Madow gave in the 1940s. McKay, Beckman and Conover brought the stratification idea to computer experiments in 1979 with Latin hypercube sampling.

The computer methods for drawing samples started with Fan, Muller and Rezucha, who published sequential item-by-item selection in 1962; Knuth presents it as Algorithm S. Knuth's second edition of *Seminumerical Algorithms* (1981) gave the reservoir method, Algorithm R, and credited it to Alan G. Waterman. Vitter (1985) analysed it, proved the lower bound on the number of reservoir changes, and gave the skip methods X, Y and Z. Bentley published Floyd's sampling algorithm in his Programming Pearls column in 1987, and Li (1994) reached Vitter's bound with the short Algorithm L.

Methods for non-uniform variates are as old as electronic computing. Von Neumann described rejection in 1951. Box and Muller published their transform in 1958, and Marsaglia and Bray the polar method in 1964. Walker gave the alias method in 1974 and 1977, and Vose the linear-time construction in 1991. Kinderman and Monahan introduced ratio-of-uniforms in 1977, Marsaglia and Tsang the ziggurat in 1984 and its fast 128-layer form in 2000, and Gilks and Wild adaptive rejection sampling in 1992 for Gibbs samplers. Knuth and Yao (1976) proved that an exact sampler from fair bits needs at least the entropy of the target law on average, and Devroye's book of 1986 collected the field.

Weighted keys came later. Efraimidis and Spirakis (2006) gave the keys $u^{1/w}$ and the one-pass weighted reservoir, which is the Gumbel-max trick in another form; Yellott (1977) had related that trick to Luce's choice axiom. Duffield, Lund and Thorup published priority sampling in 2007, and Szegedy proved its near-optimal variance. On the side of counting, Karp and Luby (1983), and with Madras in 1989, gave the union estimator, and Jerrum, Valiant and Vazirani (1986) proved that approximate counting and almost uniform sampling are equivalent for self-reducible problems, which made sampling a route to counting.

## Further reading

- Donald E. Knuth, *The Art of Computer Programming, Volume 2: Seminumerical Algorithms*, third edition (1997). Section 3.4.1 covers the classical variate generators, and Section 3.4.2 the sampling Algorithms S and R.
- Luc Devroye, *Non-Uniform Random Variate Generation* (1986). The reference work on inversion, rejection, ratio-of-uniforms, tables and the random bit model.
- Jeffrey S. Vitter, *Random Sampling with a Reservoir*, ACM Transactions on Mathematical Software 11(1), 1985. The lower bound and the skip methods, with the analysis in full.
- William G. Cochran, *Sampling Techniques*, third edition (1977). The survey designs of the first group, with their estimators and variances.
- Art B. Owen, *Monte Carlo Theory, Methods and Examples* (2013). Importance sampling, stratification and Latin hypercube designs from the side of estimation.
