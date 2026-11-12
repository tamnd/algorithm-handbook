1. ◦ Which of these lists of codeword lengths can belong to a binary [prefix code](/prefix-code/), and which of those codes are complete, with no room for another codeword? (a) 1, 2, 3, 3, 3. (b) 2, 2, 2, 3, 3. (c) 1, 3, 3, 3, 3, 4. (d) 2, 2, 3, 3, 4.

2. ◦ Is the code $\{0, 01, 11\}$ a prefix code? Is it [uniquely decodable](/uniquely-decodable-code/)? Decode the string 01111 by hand, and say how many bits past the end of the first codeword you had to read before you knew where it ended.

3. ◦ A source has the probabilities $1/2, 1/4, 1/8, 1/16, 1/16$. Compute its [entropy](/shannon-entropy/), build a [Huffman code](/huffman-coding/) for it, and compute the mean codeword length.

4. ◦ The symbols A, B, C and D have the codeword lengths 2, 1, 3 and 3. Write down the [canonical Huffman code](/canonical-huffman-code/) for these lengths, with shorter codes first and ties broken by symbol order.

5. ◦ Write the [Elias gamma](/elias-gamma-coding/) and [Elias delta](/elias-delta-coding/) codewords of 37, the [Rice code](/rice-coding/) of 11 with $k = 2$, and the [Fibonacci code](/fibonacci-coding/) of 20. Unary is written as ones ended by a zero.

6. ◦ A compressor maps the 20-bit strings one to one into bit strings of any length. At most how many of the $2^{20}$ inputs can have an output of 15 bits or fewer? What fraction of the inputs is that, to two significant digits?

7. ◦ A coin shows 1 with probability 0.1, and you flip it 100 times. Which is more likely: the sequence of 100 zeros, or one given sequence with exactly ten ones? Is the all-zero sequence in the typical set $A_\varepsilon^{(100)}$ of the [asymptotic equipartition property](/asymptotic-equipartition-property/) with $\varepsilon = 0.1$?

8. ◦ Let $X$ be a fair bit and $Y = X \oplus Z$, where $Z$ is 1 with probability 0.11, independent of $X$. Give the [Slepian-Wolf](/slepian-wolf-theorem/) region for coding $X$ and $Y$ apart, its two corner points, and the least sum rate, to two decimal places.

9. • A memoryless source emits 0 with probability 0.9 and 1 with probability 0.1. Build a Huffman code for blocks of two symbols and compute its rate in bits per source symbol. Compare it with the rate of coding one symbol at a time and with the entropy.

10. • Symbols have the weights 8, 5, 3, 2, 1, 1. Find the cost $\sum_i w_i \ell_i$ of a Huffman code and its longest codeword. Then find the least cost of a [length-limited code](/length-limited-prefix-code/) with $L = 4$, and with $L = 3$.

11. • A source has two symbols with probabilities $1 - 2^{-10}$ and $2^{-10}$. Give the codeword lengths $\lceil \log_2(1/p) \rceil$ of the Shannon code and those of the Huffman code, and both mean lengths. How long can a single Shannon codeword be compared with the Huffman codeword of the same symbol, as the probabilities vary?

12. • A geometric source has $P(x) = (1 - \theta)\theta^x$ for $x \ge 0$ with $\theta = 0.9$. Find the parameter $m$ of the optimal [Golomb code](/golomb-coding/) and write the codeword of 20.

13. • A geometric source has mean 20, so $\theta = 20/21$. Compute the expected length of the Rice code for $k = 2, 3, 4, 5$, find the best $k$, and compare it with the best Golomb code and with the entropy of the source. A short program helps.

14. • Code the message aab with [arithmetic coding](/arithmetic-coding/) and the fixed model $p(\mathrm a) = 3/4$, $p(\mathrm b) = 1/4$, where a takes the lower part of each interval. Give the final interval and the shortest bit string $c$ such that every number that starts with $c$ lies in the interval.

15. • A binary [Markov chain](/markov-chain/) never has two ones in a row: after a 0 the next symbol is 0 or 1 with probability 1/2 each, and after a 1 it is always 0. Find its stationary distribution and its [entropy rate](/entropy-rate/). Why is the rate smaller than the entropy of the stationary distribution?

16. • Build the [Tunstall code](/tunstall-coding/) with four words for a memoryless source with $p(\mathrm a) = 0.7$ and $p(\mathrm b) = 0.3$. Compute the expected number of source symbols per word and the rate in bits per source symbol, and compare the rate with the entropy.

17. • Build the [Shannon-Fano-Elias code](/shannon-fano-elias-coding/) for the probabilities $1/4, 1/2, 1/4$ in that order. Give the three codewords, the mean length, the entropy and the Kraft sum.

18. • The weights 1, 3, 3, 1 must keep their order, as in an [optimal alphabetic code](/optimal-alphabetic-code/). Find the least cost of an alphabetic code and the cost of a Huffman code for the same weights.

19. • An [rANS](/rans-coding/) coder has $M = 16$, $f(\mathrm a) = 12$, $c(\mathrm a) = 0$, $f(\mathrm b) = 4$ and $c(\mathrm b) = 12$, with the step $x \mapsto \lfloor x/f \rfloor M + c + (x \bmod f)$ and no renormalization. Start from $x = 16$, code a and then b, and give the final state. Decode it and say in which order the symbols come out. How many bits did the state grow, and what is the ideal cost of the two symbols?

20. • Code letters cost 1 and 2 units of time, like the dot and the dash of a telegraph. Find a prefix code of least mean cost for three equally likely symbols, and compare that cost with the lower bound $H / \log_2 c$ of [unequal letter cost coding](/unequal-letter-cost-coding/), where $c$ is the root of $c^{-1} + c^{-2} = 1$.

21. ★ Show that [unary coding](/unary-coding/) is an optimal prefix code for the geometric law $P(x) = (1 - \theta)\theta^x$ if $\theta + \theta^2 \le 1$, and that the Golomb code with $m = 2$ is strictly better if $\theta + \theta^2 > 1$.

22. ★ The weights of a Huffman code are positive integers with total $W$, and some codeword has length $d$. Show that $W \ge F_{d+2}$, where $F_1 = F_2 = 1$ are the Fibonacci numbers, and that the bound is tight. A DEFLATE block limits codewords to 15 bits. At least how many symbols, counted with repeats, must a block hold before its Huffman code can need a longer codeword?

23. ★ A compressor maps the $2^n$ strings of $n$ bits one to one into bit strings. Show that its mean output length, over inputs drawn uniformly, is at least $n - 2 + (n+2)/2^n$, and that a compressor whose outputs form a prefix code has mean output length at least $n$.

24. ★ The KT estimator of [adaptive modeling](/adaptive-modeling/) predicts the next bit to be 0 with probability $(a + \tfrac12)/(a + b + 1)$ after $a$ zeros and $b$ ones. Show that the probability it gives a whole sequence depends only on $a$ and $b$, and equals $\Gamma(a + \tfrac12)\,\Gamma(b + \tfrac12) / (\pi \, (a+b)!)$. Compute it for 00011, and compute the regret against the best memoryless model for that sequence.

25. ★ The empirical entropy $H_1(s)$ of a string $s$ of length $n$ is $\frac1n \sum_w |s_w| H_0(s_w)$, where $s_w$ is the string of symbols that follow the occurrences of the symbol $w$ in $s$. Show that $H_1(s) \le H_0(s)$ for every string $s$. Compute $H_0$ and $H_1$ for 01010101.
