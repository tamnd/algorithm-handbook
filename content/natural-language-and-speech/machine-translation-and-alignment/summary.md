## What to remember

- IBM Model 1 scores a source sentence $f$ of $m$ words given a target $e$ of $l$ words as $p(f \mid e) = \frac{\varepsilon}{(l+1)^m} \prod_j \sum_i t(f_j \mid e_i)$. The sum over $(l+1)^m$ alignments factors, so the likelihood, the E step and the best alignment each cost $\Theta(lm)$. The log-likelihood is concave, so EM reaches the global maximum value, but the maximizer need not be unique.
- Models 2 to 5, the HMM model and fast_align reach only local optima. The HMM model keeps exact inference at $\Theta(ml^2)$ per pair; for Models 3 to 5 the best alignment is NP-hard and $p(f \mid e)$ is #P-complete, so training uses hill climbing over alignments.
- Alignment error rate is $1 - (|A \cap S| + |A \cap P|)/(|A| + |S|)$, with sure links $S \subseteq P$; it is 0 exactly when $S \subseteq A \subseteq P$. A lower AER does not reliably give better translations.
- Sentence alignment is a dynamic program over the two lists of sentences in $\Theta(IJ)$ time; Gale and Church score each bead by its prior and a normal model of the difference in length.
- Finding the best translation with free reordering is NP-hard (Knight 1999), so phrase-based stack decoding, chart decoding with cube pruning and neural beam search are all approximate. Cube pruning is exact only without a language model, where it is the lazy $k$-best algorithm.
- A log-linear model scores a candidate by $\sum_q \lambda_q h_q(e, f)$; the noisy channel is the case of two features with weights 1. MERT finds the exact best step along one direction on fixed $n$-best lists in $O(n(p + \log n))$, but the whole search is a local method.
- An inversion transduction grammar biparses in $O(m^3 l^3)$; its one-to-one orders are the separable permutations, 1, 2, 6, 22, 90, 394 for $n = 1, \ldots, 6$ against $n!$.
- BLEU is the geometric mean of clipped $n$-gram precisions for $n = 1$ to 4 times $\min(1, e^{1 - r/c})$, computed at the corpus level. BLEU, chrF, TER and COMET are judged by how well they agree with human scores, which is measured on test sets, not proved.

## The main methods side by side

| Method | Task | Cost | Exact? |
|---|---|---|---|
| Gale-Church | sentence alignment | $\Theta(IJ)$ | yes, for its cost |
| IBM Model 1 (EM) | word alignment | $\Theta(lm)$ per pair and round | global maximum value |
| HMM alignment (EM) | word alignment | $\Theta(ml^2)$ per pair and round | local optimum |
| fast_align | word alignment | $\Theta(nml)$ per round | local optimum |
| Grow-diag-final | symmetrization | $O(ml(m + l))$ | heuristic |
| Stack decoding | phrase-based search | $O(m k o \log(k o))$ | no, beam |
| Cube pruning | chart cell with a language model | $O((g + kr)\log(g + kr))$ per cell | no |
| MERT | weight tuning | $O(n(p + \log n))$ per line search | exact line, local overall |
| ITG biparsing | joint parse of a pair | $O(m^3 l^3)$ | yes |
| BLEU | evaluation | $O(N^2 L \log L)$ | a metric |

: Algorithms of the chapter with the costs given in their entries. $m$ and $l$ are sentence lengths, $n$ the number of sentence pairs (for MERT, of candidates), $k$ a beam or stack size and $o$ the number of translation options.

## Choosing a method

To build a translation system today, train an encoder-decoder transformer on the parallel data, add back-translated monolingual target text, and decode with a beam. One multilingual model can serve many language pairs, and distillation into a smaller student model, or non-autoregressive decoding, buys speed at a measured cost in quality.

Word alignment is still needed for lexicons, for extracting phrase or rule tables, and for inspecting what a model learned. fast_align is the quick choice, measured at about ten times faster than IBM Model 4 training with similar translation quality; whichever model is used, run it in both directions and merge the links with grow-diag-final. The later IBM models are started from Model 1, whose likelihood reaches the same maximum value from any start with all entries positive.

Report BLEU with sacreBLEU and its signature, since tokenization alone moves it by up to 1.8 points; add chrF for morphologically rich languages and a learned metric such as COMET, with its version, when human agreement matters. Compare scores only when the metric, the version and the test set are the same.
