1. The Kraft sums are (a) $9/8$, (b) $1$, (c) $17/16$ and (d) $13/16$. So (b) and (d) are lengths of prefix codes, and only (b) is complete.

2. It is not a prefix code, since 0 is a prefix of 01, but it is uniquely decodable: the reversed codewords 0, 10 and 11 form a prefix code, so the string can be decoded from the right. The string 01111 decodes as 0, 11, 11. A 0 followed by an even run of ones starts with the codeword 0, and one followed by an odd run starts with 01, so the decoder had to read all four remaining bits. The delay has no bound.

3. $H = 1.875$ bits. The Huffman lengths are 1, 2, 3, 4, 4, so the mean length is also 1.875: every probability is a power of $1/2$.

5. Gamma: 00000100101 (11 bits). Delta: the gamma code of the bit length 6, which is 00110, then 00101, so 0011000101 (10 bits). Rice: 110 11. Fibonacci: $20 = 13 + 5 + 2$, so the digits for 1, 2, 3, 5, 8, 13 are 010101, and the codeword is 0101011.

6. There are $2^{16} - 1 = 65535$ strings of length at most 15, counting the empty one, so at most 65535 inputs, a fraction of about 0.062.

7. The all-zero sequence has probability $0.9^{100} \approx 2.7 \times 10^{-5}$ and the other $0.1^{10}\,0.9^{90} \approx 7.6 \times 10^{-15}$, so the all-zero sequence is far more likely. But $-\tfrac{1}{100}\log_2 0.9^{100} \approx 0.152$, which is not within 0.1 of $H = h(0.1) \approx 0.469$, so it is not typical.

10. Huffman makes a chain with lengths 1, 2, 3, 4, 5, 5 and cost 45. With $L = 4$ the best cost is 46, for instance with lengths 1, 2, 4, 4, 4, 4; with $L = 3$ it is 47, with lengths 2, 2, 3, 3, 3, 3. Check each candidate with the Kraft sum.

12. The rule $\theta^m + \theta^{m+1} \le 1$ first holds at $m = 7$: $0.9^6 \cdot 1.9 \approx 1.009$ and $0.9^7 \cdot 1.9 \approx 0.909$. For $x = 20$, $q = 2$ and $r = 6$. With $k = 2$ and $u = 1$, the remainder takes three bits as $r + u = 7$. The codeword is 110 111.

14. The interval is $[27/64, 36/64)$, of width $9/64$. No string of three bits works, but 0111 names $[7/16, 8/16)$, which lies inside. The bound $\lceil \log_2(1/P) \rceil + 1 = 4$ is met exactly.

19. Coding a gives $\lfloor 16/12 \rfloor \cdot 16 + 0 + 4 = 20$, and coding b then gives $5 \cdot 16 + 12 + 0 = 92$. The decoder sees slot $92 \bmod 16 = 12$ and outputs b first, then a: the order is reversed. The state grew by $\log_2(92/16) \approx 2.52$ bits, against an ideal $\log_2(16/12) + \log_2(16/4) \approx 2.42$ bits.

21. For the first part, cut the source at $N$ and lump the tail into one symbol of probability $\theta^N$. The two least likely symbols are the tail and $x = N - 1$, of probability $(1 - \theta)\theta^{N-1}$, as long as $\theta^N \le (1-\theta)\theta^{N-2}$, which is $\theta + \theta^2 \le 1$. Their merge is the tail of the source cut at $N - 1$, so Huffman's algorithm builds unary step by step; let $N$ grow. For the second part, unary has mean length $1/(1-\theta)$ and the Golomb code with $m = 2$ has $(2 - \theta^2)/(1 - \theta^2)$; the difference is $(\theta^2 + \theta - 1)/(1 - \theta^2)$.

22. Follow the path from the deep leaf $v_0$ up to the root $v_d$. The sibling of $v_i$ weighs at least $w(v_{i-1})$: either it was in the queue when $v_{i-1}$ was merged, or it was made later, and the sums that Huffman's algorithm makes never decrease. So $w(v_{i+1}) \ge w(v_i) + w(v_{i-1})$, which gives Fibonacci growth. The weights 1, 1, 1, 2, 3, 5, … show that the bound is tight. A codeword of 16 bits needs $W \ge F_{18} = 2584$.

23. The best one-to-one map sends the inputs to the $2^n$ shortest strings: one of length 0, two of length 1, and so on up to $2^{n-1}$ of length $n - 1$, and one of length $n$. Sum the lengths. For prefix codes, the Kraft inequality and the source coding bound give a mean of at least $H = n$.

24. Multiply the predictions. Whatever the order, the numerators for the zeros are $\tfrac12, \tfrac32, \ldots, a - \tfrac12$, those for the ones are $\tfrac12, \ldots, b - \tfrac12$, and the denominators are $1, 2, \ldots, a + b$. For 00011 the probability is $3/256$. The best memoryless model gives $(3/5)^3 (2/5)^2 = 108/3125$, so the regret is about 1.56 bits, below the bound $\tfrac12 \log_2 5 + 1 \approx 2.16$.

25. Write $|s|\,H_0(s)$ as the least value of $\sum_i \log_2(1/q(s_i))$ over all distributions $q$. Then $n H_1(s) = \sum_w \min_{q_w} \sum \log_2(1/q_w(\cdot))$ over the symbols after $w$, which is at most the same sum with one $q$ for all $w$, the frequencies of $s$, and that sum leaves out only the first symbol. For 01010101, $H_0 = 1$ and $H_1 = 0$.
