1. ◦ Align the reference "please call stella ask her to bring" with the hypothesis "please call stellar ask to bring these" and give $S$, $D$, $I$ and the [word error rate](/word-error-rate/). A second sentence has reference "yes" and hypothesis "no". Give the WER of the two sentences as a corpus, and the mean of their sentence WERs.

2. ◦ In a [GMM-HMM](/gmm-hmm-acoustic-model/) a state has self-loop probability 0.8 and frames 10 ms apart. What is the mean time spent in the state? What is the probability that it lasts exactly one frame, and that it lasts 10 frames or more?

3. ◦ A [forced alignment](/forced-alignment/) uses a word model of 3 states, left to right, each with a self-loop and no skips. The path must start in state 1 and end in state 3 after $T = 6$ frames. How many state paths are there?

4. ◦ A language has 45 phones. How many [triphones](/triphone-model/) are there? With 3 states each, 16 Gaussians per state and diagonal covariances in 39 dimensions (a mean, a variance per dimension and one weight per Gaussian), how many parameters would an untied model have? How many after tying to 4000 states?

5. ◦ [MLLR](/maximum-likelihood-linear-regression/) adapts the means with $\hat\mu = A\mu + b$. How many parameters does one transform have for 13-dimensional features, and for 39?

6. ◦ In [wav2vec 2.0](/wav2vec-2/) each frame starts a masked span with probability $p$ independently, and a span covers $M$ frames from its start. Away from the edges, what fraction of the frames is masked? Evaluate it for $p = 0.065$ with $M = 5$ and $M = 10$.

7. ◦ The [x-vector](/x-vector/) statistics pooling layer receives three frame vectors $(0, 1)$, $(2, 1)$ and $(4, 4)$. Give the pooled vector of means and standard deviations (divide by the number of frames).

8. ◦ Target scores are $N(d', 1)$ and nontarget scores $N(0, 1)$. Give the [equal error rate](/equal-error-rate/) for $d' = 1$ and $d' = 3$.

9. ◦ For one utterance the only hypotheses have joint scores $p(O \mid W)P(W)$ equal to 0.5 for the correct transcript and 0.3 and 0.2 for two others. Give the [MMI](/maximum-mutual-information-training/) objective. What is it if the score of the correct transcript doubles?

10. • [MAP adaptation](/map-speaker-adaptation/) of a mean uses $\hat\mu = (\tau\mu_0 + \sum_t \gamma_t o_t)/(\tau + \sum_t \gamma_t)$ with $\tau = 16$ and prior mean 0. Give $\hat\mu$ after 4 frames and after 64 frames, all fully assigned to the Gaussian, with sample mean 2.

11. • Run [dynamic time warping](/dynamic-time-warping/) on $x = (1, 3, 4, 9)$ and $y = (1, 4, 9, 9)$ with local cost $|x_i - y_j|$ and the steps $(1, 0)$, $(0, 1)$ and $(1, 1)$, from $(1, 1)$ to $(4, 4)$. Give the cost and a best path. What is the cost of the diagonal path?

12. • Count the warping paths with those three steps from $(1, 1)$ to $(5, 5)$. How many stay in the [Sakoe-Chiba band](/sakoe-chiba-band/) $|i - j| \le 1$? How many paths are there from $(1, 1)$ to $(7, 7)$ without a band?

13. • Count the [CTC](/connectionist-temporal-classification/) paths of length $T = 4$ over $\{a, b, \text{blank}\}$ that collapse to "ab", and those that collapse to "aa". How many paths of length 3 collapse to "a"?

14. • An [RNN transducer](/rnn-transducer/) has $T = 2$ frames and one output label, $U = 1$. At the lattice nodes the label probabilities are $y(1, 0) = 0.6$ and $y(2, 0) = 0.3$, and the blank probabilities are $\varnothing(1, 0) = 0.4$, $\varnothing(1, 1) = 0.5$, $\varnothing(2, 0) = 0.7$, $\varnothing(2, 1) = 0.9$. List the alignments and give the probability of the label.

15. • [PLDA](/plda-scoring/) in one dimension has between-speaker variance 1 and within-speaker variance 1, with mean 0. Compute the log-likelihood ratio of the same-speaker hypothesis for the pairs $(1, 1)$, $(1, -1)$, $(0, 0)$ and $(2, 2)$. Does the score depend only on $|x_1 - x_2|$?

16. • An [i-vector](/i-vector/) extractor has two components with one-dimensional features, identity covariances and total variability matrix $T = (1, 1)^\top$, one row per component. The zeroth-order statistics are $N = (2, 2)$ and the centred first-order statistics $\tilde F = (1, 3)$. Compute the precision $L$, the i-vector $\hat w$ and its posterior variance.

17. • A [confusion network](/confusion-network/) has the slots {the 0.9, a 0.1}, {cat 0.5, cap 0.3, $\varepsilon$ 0.2} and {sat 0.6, $\varepsilon$ 0.4}. Give the consensus hypothesis and its expected number of word errors against the network.

18. • In [Viterbi training](/viterbi-training/) the best path of one utterance through a 3-state model is 1, 1, 1, 2, 2, 3, 3, 3, 3. Give the re-estimated transitions out of states 1 and 2.

19. • A [decision tree](/phonetic-decision-tree-state-tying/) node pools the one-dimensional frames $A = (0, 1, 0, 1)$ and $B = (4, 5, 4, 5)$, each set modelled by a maximum likelihood Gaussian. A question splits $A$ from $B$. Compute the gain in log-likelihood.

20. • In [joint CTC-attention](/joint-ctc-attention/) decoding the score is $\lambda \log p_{\text{ctc}} + (1 - \lambda)\log p_{\text{att}}$. Hypothesis A has $\log p_{\text{ctc}} = -2.0$ and $\log p_{\text{att}} = -1.0$; hypothesis B has $-5.0$ and $-0.5$. Which wins at $\lambda = 0.3$, and at which $\lambda$ do they tie?

21. ★ Targets score 0.9, 0.7, 0.6 and 0.2; nontargets score 0.8, 0.5, 0.4, 0.3 and 0.1; a trial is accepted when its score is at least the threshold. Give the EER by the nearest-point convention (the threshold where $|P_{\text{miss}} - P_{\text{fa}}|$ is least, and the mean of the two rates there). Then give the EER of the ROC convex hull.

22. ★ A [word lattice](/word-lattice/) has the arcs $0 \to 1$ labelled $a$ with weight 0.6 and $b$ with 0.4, $1 \to 2$ labelled $c$ with 0.6 and $d$ with 0.4, and $0 \to 2$ labelled $e$ with 0.4; state 2 is final. Compute the total weight $Z$, the posterior of every arc and the best path. Does choosing the arc of highest posterior at each step give the best path?

23. ★ Take CTC with $T = 2$ frames, the same outputs each frame (blank 0.4, $a$ 0.35, $b$ 0.25), and no other labels. Give the probability of every labeling. What does greedy best-path decoding return, and what is the most likely labeling?

24. ★ [Push the weights](/weight-pushing/) in the tropical semiring of the automaton with arcs $0 \to 1$ cost 1, $0 \to 2$ cost 4, $1 \to 3$ cost 5, $2 \to 3$ cost 1, $1 \to 2$ cost 1, initial state 0 and final state 3. Give the shortest distance to the final state from every state, the new arc weights and the initial weight.

25. ★ A tropical weighted acceptor has the arcs $0 \xrightarrow{a/1} 1$, $0 \xrightarrow{a/2} 2$, a loop $b/3$ at state 1, a loop $b/3$ at state 2, $1 \xrightarrow{c/0} 3$ and $2 \xrightarrow{d/0} 3$, with state 3 final. Follow [weighted determinization](/weighted-determinization/) on the inputs $a b^k$. Does it terminate? What changes if the loop at state 2 costs 4?
