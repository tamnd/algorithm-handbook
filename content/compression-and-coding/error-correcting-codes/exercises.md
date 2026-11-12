1. ◦ A code has [minimum distance](/minimum-distance/) $d = 6$. How many errors can it always detect, how many can it always correct, and how many erasures can it always fill in? Can it always handle 2 errors and 1 erasure in the same word? A decoder is to correct every pattern of up to $t'$ errors and to detect every pattern of up to $s \ge t'$ errors. Which pairs $(t', s)$ can it guarantee?

2. ◦ The [repetition code](/repetition-code/) of length 5 with majority vote is used on a [binary symmetric channel](/binary-symmetric-channel/) with crossover probability $p = 0.2$. Compute the probability that a data bit is decoded wrongly. Then compute the capacity of the channel and compare it with the rate of the code.

3. ◦ The [Hamming code](/hamming-code/) $[7, 4, 3]$ is laid out with check bits in positions 1, 2 and 4 and data bits in positions 3, 5, 6 and 7, so that column $j$ of the [parity-check matrix](/parity-check-matrix/) is $j$ written in binary. The word $1101110$ is received. Compute the [syndrome](/syndrome/), correct the word, and read off the four data bits.

4. ◦ A [Reed-Solomon code](/reed-solomon-code/) $[255, 223]$ over $\mathrm{GF}(256)$ is used for bytes. Give its minimum distance, the number of byte errors it always corrects, the number of byte erasures it always fills in, and its rate. Give one combination of errors and erasures, with both counts at least 10, that it always corrects.

5. ◦ Let $n = 10$ and $d = 5$ for binary codes. Compute the [Hamming bound](/hamming-bound/) on the number of codewords, and the number of codewords that the greedy argument of the [Gilbert-Varshamov bound](/gilbert-varshamov-bound/) guarantees. Then use the linear form of the bound, $2^{n-k} > V(n - 1, d - 2)$, to find the largest $k$ for which a linear $[10, k, 5]$ code is guaranteed. The true maximum is $A(10, 5) = 12$; which of your numbers is closest?

6. ◦ Describe the [dual code](/dual-code/) of the binary repetition code of length 5: its dimension, its minimum distance and its weight distribution $A_0, \dots, A_5$.

7. ◦ A rate $1/2$ [convolutional code](/convolutional-code/) has generators $g_1 = 1 + D + D^2$ and $g_2 = 1 + D^2$, and each step outputs the bit of $g_1$ first. Encode the input $1101$ followed by two zero tail bits, starting from the zero state. Give the six output pairs and the weight of the codeword.

8. ◦ On the [AWGN channel](/additive-white-gaussian-noise-channel/) with real inputs, a code of rate $R$ needs $E_b/N_0 \ge (2^{2R} - 1)/(2R)$. Compute this limit in dB for $R = 1/3$. Uncoded BPSK needs about 9.6 dB for a bit error rate of $10^{-5}$. How many dB of gain does the limit leave room for at that error rate?

9. ◦ An [LT code](/lt-codes/) has four source bits $s_1, s_2, s_3, s_4$. The receiver gets five encoded bits: $s_2 = 1$, $s_1 \oplus s_2 = 0$, $s_2 \oplus s_3 \oplus s_4 = 1$, $s_3 \oplus s_4 = 0$ and $s_1 \oplus s_4 = 1$. Run the [peeling decoder](/peeling-decoding/) step by step and give the source bits.

10. • The Hamming code of exercise 3 is extended by an overall parity bit in position 8, which gives a SECDED code $[8, 4, 4]$. The codeword $11001100$ is sent. Decode the received words $r_1 = 11101100$ and $r_2 = 01001110$. For each, give the syndrome of the first seven bits, the overall parity, and the decision: correct a single error, or report a double error.

11. • The [Golay code](/golay-code/) $[23, 12, 7]$ is used on a BSC with $p = 0.01$ with a decoder that corrects every pattern of up to 3 errors. Check that the code is perfect, then compute the probability that a block is decoded wrongly. Compare it with the probability that at least one of 12 uncoded bits is wrong.

12. • Use the [Griesmer bound](/griesmer-bound/) to find the shortest possible binary linear code of dimension 5 and minimum distance 8. Name a code that meets it.

13. • For binary codes of length 10 and minimum distance 6, compare the [Plotkin bound](/plotkin-bound/) with the Hamming bound. Then build a code with as many words as the Plotkin bound allows, and so find $A(10, 6)$.

14. • The Reed-Solomon code of exercise 4 is used with byte [interleaving](/interleaving/) to depth 4. What is the longest burst of byte errors that is always corrected? A burst of $b$ bits can touch $\lceil (b - 1)/8 \rceil + 1$ bytes. What is the longest burst of bits that is always corrected, however it is aligned?

15. • Run the [Berlekamp-Massey algorithm](/berlekamp-massey/) over $\mathrm{GF}(2)$ on the sequence $1, 1, 0, 0, 1, 0, 1, 1$. Give the linear complexity after each bit, the final connection polynomial and the recurrence it defines. Why is the final polynomial the only one of its length that generates the sequence?

16. • A Reed-Solomon code $[6, 2]$ over $\mathrm{GF}(7)$ evaluates a message polynomial $f(x) = f_0 + f_1 x$ at the points $1, 2, \dots, 6$. The word $(1, 2, 4, 2, 1, 5)$ is received. Find $f$, the sent codeword and the error positions. You may use the [Berlekamp-Welch algorithm](/berlekamp-welch/) or a search over the pairs of points.

17. • A [polar code](/polar-code/) of length $N = 4$ is used on a [binary erasure channel](/binary-erasure-channel/) with erasure probability $0.3$. Using $z \mapsto 2z - z^2$ for the worse channel and $z \mapsto z^2$ for the better one, compute the erasure probabilities of the four synthetic channels for $u_1, \dots, u_4$. Check that they add up to $N\varepsilon$. For $K = 2$, which positions carry data, and what does the union bound give for the block error probability under [successive cancellation](/successive-cancellation-decoding/)?

18. • The code of exercise 7 is decoded with the Viterbi algorithm and hard decisions. The received pairs are $10, 01, 01, 00, 00, 11$, and the encoder ends in the zero state. Find the most likely input of four bits and the Hamming distance from the received word to its codeword.

19. • The extended Golay code $[24, 12, 8]$ is used with BPSK on the AWGN channel. Give its asymptotic coding gain with soft decisions and with hard decisions, in dB.

20. • Take the LT code of exercise 9 without the received bit $s_2 = 1$. Show that peeling cannot start, but that the four remaining equations still determine the source bits, and solve them by Gaussian elimination.

21. • A Reed-Solomon code $[255, 32]$ is decoded by a unique decoder and by [Guruswami-Sudan](/guruswami-sudan/) list decoding. How many errors does each always handle?

22. ★ Show that a binary linear code with $r$ check bits and minimum distance at least 4 has length at most $2^{r-1}$, and that this length is reached for every $r \ge 3$. What is the bound for $r = 4$ and for $r = 8$, and how does the SECDED code $[72, 64, 4]$ of computer memory fit it?

23. ★ A [concatenated code](/concatenated-codes/) uses an outer Reed-Solomon code $[15, 9, 7]$ over $\mathrm{GF}(16)$ and the inner Hamming code $[7, 4, 3]$, one inner block per outer symbol. Give the length, dimension and designed distance of the binary code. Decoding first corrects each inner block to the nearest codeword and then decodes the outer code up to its unique radius. What is the largest number of bit errors that it always corrects? Give a pattern with one more error on which it fails. How many errors does generalized minimum distance decoding guarantee?

24. ★ The [product code](/product-codes/) of the even-weight codes $[4, 3, 2]$ and $[5, 4, 2]$ is a $[20, 12, 4]$ code of $4 \times 5$ arrays. Find the number of codewords of weight 4 and describe them.

25. ★ Compare the asymptotic bounds on the rate of binary codes at relative distance $\delta = 0.1$: Gilbert-Varshamov, Hamming, Plotkin $1 - 2\delta$, and the [Elias bound](/elias-bound/) $1 - h(J(\delta))$ with $J(\delta) = (1 - \sqrt{1 - 2\delta})/2$. From these four numbers alone, what interval must the best achievable rate lie in?

26. ★ A bit passes through a BSC with $p = 0.1$, and the result then passes through an erasure channel with erasure probability $0.2$. Find the [capacity](/channel-capacity/) of the combined channel, and show why it is the product of a factor for each stage.
