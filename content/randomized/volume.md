A randomized algorithm flips coins as it runs. Randomized quicksort picks its pivots at random and sorts every input in $O(n \log n)$ expected time. A hash table draws its hash function at random, so that no fixed set of keys is bad for it. A primality test picks random bases and declares a 300-digit number prime, with an error probability that falls by a constant factor with every base it tries. A Markov chain wanders over the colourings of a graph and, after enough steps, returns one that is nearly uniform among them. In each case the coins belong to the algorithm and not to the input, and the analysis takes the probability over the coins.

This volume is about randomness as a subject in its own right. It starts with the most direct uses of coins, drawing samples and shuffling, then turns to random hash functions, to the two ways a randomized algorithm can be wrong or slow, and to Markov chains that sample what cannot be sampled directly. It ends by asking how much of the randomness can be removed.

## Why randomness gets a volume of its own

Randomness turns up in almost every other volume, as a tool for one problem at a time. Here the tool is the object of study, and the same few ideas carry across chapters:

- **Exact laws from simple coins.** [Reservoir sampling](/reservoir-sampling/) keeps a uniform sample of a stream, and the [Fisher-Yates shuffle](/fisher-yates-shuffle/) makes each of the $n!$ orders equally likely. Each is a short loop whose probabilities must be exactly right, and the proofs count runs.
- **Random keys.** Give each item a random number and keep the smallest. The idea gives uniform and weighted samples, [shuffles by sorting](/permute-by-sorting/), and estimates of similarity.
- **Small families instead of full randomness.** A [pairwise independent](/pairwise-independence/) hash function costs a few random numbers, yet it gives the same expected costs as a truly random one for a chained table.
- **Two kinds of error.** A [Las Vegas algorithm](/las-vegas-algorithm/) is always right and sometimes slow; a [Monte Carlo algorithm](/monte-carlo-algorithm/) is always fast and sometimes wrong. Repetition drives the error down exponentially, as in [Freivalds' algorithm](/freivalds-algorithm/).
- **Sampling by walking.** [Metropolis-Hastings](/metropolis-hastings/) and [Gibbs sampling](/gibbs-sampling/) build a Markov chain whose stationary law is the target, and the [mixing time](/mixing-time/) says how long to run it.
- **Removing the coins.** The [method of conditional expectations](/method-of-conditional-expectations/) fixes coins one at a time, [k-wise independence](/k-wise-independence/) shrinks the sample space, and [pseudorandom generators](/pseudorandom-generator/) stretch a short seed.

## How this volume relates to the others

Several earlier volumes hold material that this one builds on or overlaps, and they are worth naming plainly.

- **Volume 1, probabilistic analysis**, supplies the tools: [expected value](/expected-value/), [linearity of expectation](/linearity-of-expectation/), [Markov's](/markov-inequality/) and [Chebyshev's](/chebyshev-inequality/) inequalities, the [Chernoff bound](/chernoff-bound/), [martingales](/martingale/) and the [coupon collector](/coupon-collector-problem/). This volume uses them throughout and does not prove them again.
- **Volume 2, randomization techniques**, defines the [randomized algorithm](/randomized-algorithm/) and [expected running time](/expected-running-time/), and treats randomization as a design technique beside divide and conquer and greedy choice, with [backwards analysis](/backwards-analysis/), [randomized incremental construction](/randomized-incremental-construction/) and the [probabilistic method](/probabilistic-method/). This volume goes deeper into the kinds of error, the families of random objects and their derandomization.
- **Volume 3, hashing and probabilistic structures**, builds the tables, the [universal hash family](/universal-hash-family/), cuckoo hashing, Bloom filters and sketches. Chapter 17.3 studies the hash families themselves as random objects.
- **Volume 12, random number generation and quadrature**, explains where uniform numbers come from: [pseudorandom number generators](/pseudorandom-number-generator/), [unbiased bounded integers](/uniform-random-integer-generation/) and quasi-random sequences. Its [Monte Carlo integration](/monte-carlo-integration/) is the estimator that importance sampling and Markov chains refine here. This volume assumes a source of uniform numbers and starts from there.
- **Volume 10, primality**, gives the [Miller-Rabin](/miller-rabin/) and [Solovay-Strassen](/solovay-strassen/) tests as number theory. Chapter 17.4 has its own entries for the same tests, read as one-sided Monte Carlo algorithms.
- **Volume 14, counting algorithms**, gives [FPRAS](/fpras/) and the [Karp-Luby algorithm](/karp-luby-algorithm/) for DNF counting. Chapter 17.1 has the general Karp-Luby union estimator, and Chapter 17.5 the Markov chains that make approximate counting possible.

## The chapters

**Chapter 17.1, Sampling**, chooses random subsets and random numbers. It covers survey designs, uniform subsets by scans, Floyd's method and reservoirs, sampling by weight with the alias method and random keys, the generation of variates by inversion and rejection, and estimation by importance sampling.

**Chapter 17.2, Shuffling**, makes uniform random permutations. It starts with the Fisher-Yates shuffle and the ways a shuffle goes wrong, then shuffles by sorting and merging, random cyclic permutations, and the question of how many riffle shuffles mix a deck of cards.

**Chapter 17.3, Random hashing**, is the short chapter. It defines pairwise and $k$-wise independent families, builds them over a prime field or from one machine multiplication, and proves the expected chain lengths, the min-wise property and the load threshold of cuckoo hashing.

**Chapter 17.4, Monte Carlo and Las Vegas**, separates the two kinds of randomized algorithm, shows how to amplify success and convert one kind into the other, and gives the classical examples: primality tests, Freivalds' check of a matrix product, polynomial identity testing with the Schwartz-Zippel lemma, and random choices in combinatorial problems.

**Chapter 17.5, Markov chain Monte Carlo**, is the largest. It covers Markov chains and their limits, distances to stationarity, Metropolis-Hastings and Gibbs sampling, the reading of the output, bounds on mixing times, spin systems and exact sampling by coupling from the past, gradient-based samplers such as Hamiltonian Monte Carlo, and samplers for hard targets.

**Chapter 17.6, Derandomization**, removes or saves random bits. It covers the method of conditional expectations, small sample spaces of $k$-wise independent bits, walks on expanders, pseudorandom generators, the trade between hardness and randomness, and extractors for weak random sources.

## How to read this volume

If this is your first course, read these entries in this order. From Chapter 17.1: [uniform random subset](/uniform-random-subset/), [reservoir sampling](/reservoir-sampling/), [inverse transform sampling](/inverse-transform-sampling/), [rejection sampling](/rejection-sampling/) and the [alias method](/alias-method/). From Chapter 17.2: the [Fisher-Yates shuffle](/fisher-yates-shuffle/) and the [naive shuffle](/naive-shuffle/). From Chapter 17.3: [pairwise independence](/pairwise-independence/) and the [expected chain length](/universal-hashing-expected-chain-length/). From Chapter 17.4: [Las Vegas](/las-vegas-algorithm/) and [Monte Carlo](/monte-carlo-algorithm/) algorithms, [error amplification](/error-amplification/), [Freivalds' algorithm](/freivalds-algorithm/), the [Miller-Rabin test](/miller-rabin-primality-test/) and the [Schwartz-Zippel lemma](/schwartz-zippel-lemma/). From Chapter 17.5: [Markov chains](/markov-chain/), [Metropolis-Hastings](/metropolis-hastings/) and the [mixing time](/mixing-time/). From Chapter 17.6: the [method of conditional expectations](/method-of-conditional-expectations/). Do the exercises marked ◦ and • at the end of these chapters. That is a complete first unit on randomized algorithms.

If you already know the basics, start with the opening page of each chapter. It names the groups in the chapter and the order to read them. Beyond the first course, the chapters can be read in any order. The entries marked *Advanced* and *Research* are the place to go deeper; much of Chapters 17.5 and 17.6 is at that level.

Each entry stands on its own. Its facts box lists what it needs, with the number of the entry where each prerequisite is explained. Entries in other volumes are cited by number too.

## What you need first

You should be able to read a short program and follow a proof by induction. From Volume 1 you need discrete probability: random variables, expectation and its linearity, variance, and the inequalities of Markov and Chebyshev; the later chapters also use the Chernoff bound. For Chapters 17.5 and 17.6 some linear algebra helps, mainly eigenvalues of symmetric matrices. Volume 2's [randomized algorithm](/randomized-algorithm/) entry is a good first page if the idea of an algorithm that flips coins is new.

## The exercises

Each chapter ends with exercises in three bands. Exercises marked ◦ check that you read the entries closely; you should be able to do them in a few minutes. Exercises marked • ask you to use an idea in a new place; each takes some thought, and some need a short program. Exercises marked ★ are harder; some are results from research papers. Hints for many exercises are in the appendix *Hints to the exercises* at the end of the volume.
