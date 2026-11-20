1. The rows are `<s>`: a 2/4, b 1/4, c 1/4; a: b 1; b: c 1/4, `</s>` 3/4; c: b 1/2, `</s>` 1/2. So $P(\text{a b}) = \tfrac12 \cdot 1 \cdot \tfrac34 = 3/8$, $P(\text{b c}) = \tfrac14 \cdot \tfrac14 \cdot \tfrac12 = 1/32$ and $P(\text{a b c}) = \tfrac12 \cdot 1 \cdot \tfrac14 \cdot \tfrac12 = 1/16$. "c a" gets 0 because the bigram "c a" was never seen.

3. The counts are a 5, b 2, r 2, c 1 and d 1, so $N = 11$, $N_1 = 2$, $N_2 = 2$, $N_5 = 1$. The chance of a new letter is $N_1/N = 2/11$, and $r^*(1) = 2 \cdot N_2/N_1 = 2$. For $r = 2$, $N_3 = 0$ gives $r^* = 0$: a letter seen twice would get no probability. This gap is what simple Good-Turing fills.

5. The dot products are $2$, $1$ and $-1$, divided by $\sqrt 4 = 2$: $(1, 0.5, -0.5)$. The softmax gives $(0.54655, 0.33150, 0.12195)$, and the output is $(0.54655 + 2 \cdot 0.12195,\; 0.33150 + 2 \cdot 0.12195) = (0.79045, 0.57540)$.

6. For $d = 4$ the two frequencies are $1$ and $10000^{-2/4} = 0.01$. Position 1 gives $(\sin 1, \cos 1, \sin 0.01, \cos 0.01) = (0.841471, 0.540302, 0.010000, 0.999950)$, and position 2 gives $(0.909297, -0.416147, 0.019999, 0.999800)$.

11. The bigram counts of counts are $n_1 = 5$ and $n_2 = 2$, so $D = 5/9$. Of the 8 bigram types, a follows 1 history, b 3, c 2 and `</s>` 2. For history c, two types are seen, so the lower-order weight is $D \cdot 2/2 = 5/9$, and $P(b \mid c) = (1 - 5/9)/2 + \tfrac59 \cdot \tfrac38 = 31/72$.

13. Each history gives $\alpha(h) = (1 - S_1)/(1 - S_2)$, where $S_1$ is the discounted mass of the words seen after $h$ and $S_2$ their unigram mass. For c, $S_1 = \tfrac14 + \tfrac14$ and $S_2 = \tfrac13 + \tfrac13$, so $\alpha = 3/2$, and $\tfrac32 \cdot \tfrac16 = \tfrac14$ for each unseen word.

16. After the first block, $m = 3$, $\ell = e^{-2} + 1$ and the output is $(e^{-2} + 2)/\ell$. At the second block the new maximum is 4: multiply the old $\ell$ and the old weighted sum by $e^{3 - 4}$ before adding $e^{2 - 4}$ and $e^{0}$.

17. Compose $(\alpha_s, \beta_s)$ then $(\alpha_t, \beta_t)$ as $(\alpha_t \alpha_s, \alpha_t \beta_s + \beta_t)$. With $h_0 = 0$, the second part of the pair for steps 1 to $t$ is $h_t$.

21. The model is tight when $\prod_i (1 - q_i) = 0$. For $q_i = 1/(i+1)$, $\prod_{j < i} j/(j+1) = 1/i$, so a sentence has $i$ tokens with chance $\frac{1}{i} \cdot \frac{1}{i+1}$, and the sum telescopes to 1. The expected length is $\sum_i 1/(i+1)$.

22. In the row of c both seen words keep $(1 - D)/2$, and the freed mass is $D \cdot 2/2 = 5/9$. Absolute discounting multiplies it by $P(a) = 2/12$; Kneser-Ney by the continuation probability $1/8$, since a follows only `<s>`.

23. Hunter's MM update is $p_i \leftarrow W_i / \sum_{j \ne i} n_{ij}/(p_i + p_j)$, where $W_i$ is the number of wins of $i$ and $n_{ij}$ the number of games between $i$ and $j$; renormalize after each sweep. At the maximum, the expected wins equal the observed wins 7, 4 and 1. If C never wins, the likelihood rises as $p_C \to 0$.

24. Put $D = C/(6N)$ in the law and set the derivative in $N$ to 0. This gives $N_{\text{opt}} = G\,(C/6)^{\beta/(\alpha + \beta)}$ with $G = (\alpha A / (\beta B))^{1/(\alpha + \beta)}$, and $D_{\text{opt}} = (C/6)/N_{\text{opt}}$.

25. Without "c b", the seen mass of row c is $S_1 = 1/4$ and the backed-off unigram mass is $1 - 1/3$, so $\alpha' = (3/4)/(2/3) = 9/8$. The new row is a $3/16$, b $3/8$, c $3/16$, `</s>` $1/4$. Then $D = \tfrac16 \sum_w p(w \mid c) \ln (p(w \mid c)/p'(w \mid c))$ over all four words.
