1. The relevant documents are at ranks 2, 3 and 7. So $P@1 = 0$, $P@3 = 2/3$, $P@5 = 2/5$ and $P@10 = 3/10$. With $R = 4$, the R-precision is $P@4 = 2/4 = 1/2$. Recall at 10 is $3/4$, since k is never retrieved.

2. $\mathrm{AP} = (1/2 + 2/3 + 3/7 + 0)/4 = 67/168 \approx 0.3988$. The unretrieved document k adds 0 but still counts in $R = 4$.

3. The points are (recall $1/4$, precision $1/2$) at rank 2, ($1/2$, $2/3$) at rank 3 and ($3/4$, $3/7$) at rank 7, and recall 1 is never reached. The levels 0 to 0.5 get $2/3$, the levels 0.6 and 0.7 get $3/7$, and the levels 0.8 to 1 get 0. The mean is $(6 \cdot 2/3 + 2 \cdot 3/7)/11 = 34/77 \approx 0.4416$.

5. b and g satisfy with probability $3/4$, c with $1/4$. The user reaches rank 2 for sure, rank 3 with probability $1/4$ and rank 7 with probability $(1/4)(3/4)$. So $\mathrm{ERR} = (3/4)/2 + (1/4)(1/4)/3 + (1/4)(3/4)(3/4)/7 = 3/8 + 1/48 + 9/448 = 559/1344 \approx 0.4159$, and ERR at 3 is $3/8 + 1/48 = 19/48 \approx 0.3958$.

8. In the paper form, b and c each have one judged nonrelevant document above them (a) and get $1 - 1/4$; g has two (a and e) and gets $1 - 2/4$; k is not retrieved and gets 0. So bpref $= (3/4 + 3/4 + 1/2)/4 = 1/2$. With $N = 3$, trec_eval divides by $\min(3, 4) = 3$ and gets $(2/3 + 2/3 + 1/3)/4 = 5/12$. The unjudged d and f play no part.

11. The relevant x lands at rank 2, 3 or 4, each in two of the six orders, and y is always at rank 5. So $\mathrm{AP} = (1/r_x + 2/5)/2$: id ascending puts x at rank 4 and gives $13/40$, reverse lexical puts it at rank 2 and gives $9/20$, and the tie-aware mean is $(9/20 + 11/30 + 13/40)/3 = 137/360 \approx 0.3806$.

14. The pool is $\{a, x, b\}$, so only a and b are known relevant and $R = 2$. On the pool, AP is $5/6$ for A, 1 for B and $(1/4 + 2/5)/2 = 13/40$ for C. On the full judgments it is $17/30 \approx 0.567$ for A, $13/20 = 0.65$ for B and $193/240 \approx 0.804$ for C. The order B, A, C becomes C, B, A: the pool never judged c and d, which C ranks 1 and 3.

16. P@3: $C = 1, 1, 0$, $W = 1/3$ each, EU $= 2/3$, ED $= 3$. RBP: $W = 1/2, 1/4, 1/8$, EU $= 1/2 + 1/8 = 5/8$, ED $= 2$. RR: $C(1) = 0$, so $W(1) = 1$, EU $= 1$, ED $= 1$. AP: $\sum_{j \ge i} g_j/j$ is $4/3$ for $i = 1$ and $1/3$ for $i = 2, 3$, so $C = 1/4, 1, 0$, the unnormalized weights are $1, 1/4, 1/4$, ED $= 3/2$, $W = 2/3, 1/6, 1/6$ and EU $= 5/6$, the AP $(1 + 2/3)/2$.

19. With $g_{\max} = 3$, grade 3 satisfies with probability $7/8$ and grade 2 with $3/8$. ERR is $7/8$ for X and $3/8 + (5/8)(3/8)/2 + (5/8)^2(3/8)/3 = 277/512 \approx 0.541$ for Y. nDCG at 3 with gain $g$ is 0.5701 for X and 0.8100 for Y; with gain $2^g - 1$ it is 0.6735 for X and 0.6151 for Y. ERR and the exponential gain prefer X, the linear gain prefers Y. Under the cascade, the first document already stops most users, so later documents add little.

21. The nonzero coefficients are $c_{aa} = 1/2$, $c_{ab} = 1/6$, $c_{bb} = 1/6$, $c_{ac} = -1/6$ and $c_{cc} = -2/3$, so $D$ starts in $[-5/6, 5/6]$. The scores are $1/3$ for a, $1/6$ for b and $5/12$ for c, which comes from $(1 - p)w^N_c = (1/2)(2/3 + 1/6)$. c is not relevant, so its pairs drop out and $D \in [0, 5/6]$. Then a scores $1/3$ against $1/6$ for b; a is relevant, $D \in [1/2, 5/6]$, and the algorithm returns A after two judgments. b is never judged.

22. Greedy takes A, the only document with four new nuggets, and then B or C, each with one new nugget: $4 + 1/\log_2 3 \approx 4.6309$. The ranking B, C covers all six nuggets and has $3 + 3/\log_2 3 \approx 4.8928$, the best of the six ordered pairs. Its alpha-nDCG at 2 is $1.0565 > 1$. With $\alpha = 1$, the cumulated gain at depth $j$ counts distinct nuggets, so the ideal at depth $j$ solves maximum coverage with $j$ sets, and greedy fails here although rank 1 has no tie.

23. AP is $(1/2 + 2/3)/2 = 7/12$. For the sample $\{a, b\}$, b at rank 2 has a judged nonrelevant document above it and gets $1/2$. For $\{a, c\}$, c at rank 3 gets $1/3$. For $\{b, c\}$, b at rank 2 has nothing judged above, so the rate is $1/2$ and $\hat P_2 = 3/4$; c at rank 3 gets $1/3 + 2/3 = 1$; infAP is $7/8$. The mean is $41/72 \approx 0.5694$, so the bias is $-1/72$.

24. At position 1, A gives a the share $1/(1 + 1/8 + 1/27) = 216/251$ and B gives it $27/251$, so $q_1 = 8/9$. At position 2, b and c are left: $f_1 = (1/8)/(1/8 + 1/27) = 27/35$ and $f_2 = 1/(1 + 1/27) = 27/28$, so $q_2 = 4/9$. At position 3 both rankings must draw c, so $q_3 = 1/2$. Clicks on positions 1 and 2 give $(8/9)(4/9) - (1/9)(5/9) = 1/3$. A click on position 2 alone gives $4/9 - 5/9 = -1/9$.
