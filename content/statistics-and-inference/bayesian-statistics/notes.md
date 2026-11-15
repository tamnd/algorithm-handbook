## History

The subject begins with Bayes's essay on inverse probability, which Richard Price sent to the Royal Society after Bayes's death and which appeared in 1763. Laplace reached the same idea on his own in a memoir of 1774. He found the posterior of a binomial proportion under a uniform prior, gave the rule of succession, and approximated the integrals by expanding the logarithm of the integrand at its maximum, the method now named after him. Bernstein in 1917 and von Mises in 1931 proved that the posterior becomes normal in large samples, and Le Cam gave the modern form of the theorem in 1953.

The foundations were rebuilt in the twentieth century. De Finetti proved his representation theorem for exchangeable events in 1931 and set out subjective probability in 1937; Hewitt and Savage extended the theorem to general spaces in 1955. Jeffreys's *Theory of Probability* of 1939 built tests on Bayes factors with positive prior mass on the null, and in 1946 he proposed the prior from the Fisher information that bears his name. Lindley described in 1957 the conflict between such tests and significance tests, Dickey gave the density ratio form of the Bayes factor in 1971, and Bernardo defined reference priors in 1979.

Robbins introduced empirical Bayes in 1956, and James and Stein showed in 1961 that shrinking three or more normal means together beats estimating each one alone. Lindley and Smith wrote linear models with normal priors in stages in 1972, the start of hierarchical modelling. Mitchell and Beauchamp proposed the spike-and-slab prior for variable selection in 1988, George and McCulloch gave a Gibbs sampler for it in 1993, and Carvalho, Polson and Scott published the horseshoe prior in 2010.

Computation decided what could be done in practice. Tierney and Kadane analysed Laplace approximations for posterior moments and marginals in 1986, and Gelfand and Smith showed in 1990 how Gibbs sampling computes posterior marginals. Meng and Wong gave bridge sampling in 1996, Skilling described nested sampling in 2004, and Rue, Martino and Chopin published the integrated nested Laplace approximation in 2009. For models without a likelihood, Tavaré and coauthors in 1997 and Pritchard and coauthors in 1999 used rejection on simulated data, Beaumont, Zhang and Balding added regression adjustment in 2002, and Beaumont, Cornuet, Marin and Robert gave the weights of ABC with a population of particles in 2009.

Checking came with computing. Rubin in 1984 proposed comparing the data with replications from the posterior predictive law, and Gelman, Meng and Stern developed posterior predictive checks in 1996. Watanabe defined WAIC in 2010, and Vehtari, Gelman and Gabry compared it with leave-one-out estimates by Pareto smoothed importance sampling in 2017. Cook, Gelman and Rubin proposed in 2006 to validate software with parameters drawn from the prior, and Talts and coauthors replaced their quantiles by ranks in 2018.

## Further reading

- Andrew Gelman, John B. Carlin, Hal S. Stern, David B. Dunson, Aki Vehtari and Donald B. Rubin, *Bayesian Data Analysis*, third edition, CRC Press, 2013. The applied reference for hierarchical models, model checking and computation.
- Christian P. Robert, *The Bayesian Choice*, second edition, Springer, 2007. Decision theory, priors and Bayes factors with full proofs.
- José M. Bernardo and Adrian F. M. Smith, *Bayesian Theory*, Wiley, 1994. Exchangeability, reference priors and the foundations.
- Robert E. Kass and Adrian E. Raftery, Bayes factors, *Journal of the American Statistical Association* 90, 1995. The standard survey of Bayes factors and how to compute them.
- Bradley Efron, *Large-Scale Inference*, Cambridge University Press, 2010. Empirical Bayes for thousands of parallel cases, with Robbins's and Tweedie's formulas.
- A. W. van der Vaart, *Asymptotic Statistics*, Cambridge University Press, 1998. Chapter 10 proves the Bernstein-von Mises theorem.
