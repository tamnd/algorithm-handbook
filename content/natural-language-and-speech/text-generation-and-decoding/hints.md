1. The outputs are a`</s>` 0.165, aa`</s>` 0.22, ab`</s>` 0.165, b`</s>` 0.315, ba`</s>` 0.09 and bb`</s>` 0.045. Greedy takes a (0.55) and then a (0.4), and returns aa`</s>` with 0.22. The mode is b`</s>` with 0.315. A beam of width 2 keeps a and b after step 1, and b`</s>` is the best finished output it sees, so it finds the mode. Per token, b`</s>` scores $\ln 0.315 / 2 = -0.578$ and aa`</s>` scores $\ln 0.22 / 3 = -0.505$, so dividing by the length picks aa`</s>`.

3. Top-k keeps $0.35, 0.20, 0.15$, of mass 0.70, and renormalizes them to $(0.5, 0.2857, 0.2143)$. Nucleus adds tokens in order until the mass reaches 0.8: $0.35, 0.55, 0.70, 0.82$, so it keeps four tokens of mass 0.82, renormalized to $(0.4268, 0.2439, 0.1829, 0.1463)$.

4. Unigrams: the (twice), cat, on and mat match, so ROUGE-1 recall is $5/6$. Bigrams: the cat, on the and the mat match among five, so ROUGE-2 recall is $3/5$. The longest common subsequence is "the cat on the mat", of length 5, so ROUGE-L recall, precision and F are all $5/6$, since both texts have six words.

7. $\alpha = \min(0.5, 0.4) + \min(0.3, 0.4) + \min(0.2, 0.2) = 0.9$. The residual $\max(0, p - q) = (0.1, 0, 0)$ normalizes to all mass on a. A step yields $(1 - 0.9^4)/(1 - 0.9) = 3.439$ tokens on average.

9. The significant words are at positions 0, 3, 8, 9 and 15, with 2, 4, 0 and 5 words between neighbours. With $g = 3$ the clusters are {0, 3}, {8, 9} and {15}, scoring $4/4$, $4/2$ and $1$, so the score is 2. With $g = 4$ they are {0, 3, 8, 9}, of length 10, and {15}: the score is $16/10 = 1.6$. With $g = 5$ one cluster covers all 16 words: $25/16 = 1.5625$. A larger gap limit merges clusters and can lower the score.

10. With self-loops the degrees are 4, 2, 3 and 3. For $d = 0$ the walk on an undirected graph has stationary vector proportional to the degrees, $(1/3, 1/6, 1/4, 1/4)$. For $d = 0.15$ the linear system gives $(911/2811, 520/2811, 230/937, 230/937) \approx (0.3241, 0.1850, 0.2455, 0.2455)$. Damping moves mass toward the uniform vector but keeps the ranking 1, then 3 and 4, then 2.

11. The expected utility is $0.4 \cdot 1 + 0.35 \cdot 0.2 + 0.25 \cdot 0.3 = 0.545$ for A, $0.655$ for B and $0.4 \cdot 0.3 + 0.35 \cdot 0.9 + 0.25 = 0.685$ for C. MBR chooses C, the least probable candidate, because it is close to B and the two together hold 0.6 of the mass.

17. The mask lets both a and b start a string of the language, and after the first token only one continuation is allowed. So masked sampling gives aa with 0.9 and bb with 0.1. The model gives aa $0.9 \cdot 0.05 = 0.045$ and bb $0.1 \cdot 0.9 = 0.09$, so conditioned on the language the law is aa $1/3$, bb $2/3$. The mask reverses the order of the two strings.

18. $H = 1.7279$ nats. The surprisals closest to $H$ are those of the tokens of probability 0.20 (distance 0.119), 0.15 (0.169) and 0.12 (0.392), and then 0.35 (0.678). With $\tau = 0.4$ the kept set is the three middle tokens, of mass 0.47, without the most probable token. With $\tau = 0.5$ the token of probability 0.35 joins, mass 0.82. Nucleus sampling at $p = 0.4$ keeps the two most probable tokens, of mass 0.55.

20. Token a is drafted with probability 0.2 and always accepted, and every rejection (probability $1 - \alpha = 0.3$) draws from the residual, which is all on a: $0.2 + 0.3 = 0.5$. Token b is drafted with 0.3 and always accepted: 0.3. Token c is drafted with 0.5 and accepted with $0.2/0.5$: 0.2. The speed up $(1 - 0.7^{\gamma + 1})/(0.3(1 + 0.1\gamma))$ is 1.546, 1.825, 1.949, 1.981 and 1.961 for $\gamma = 1$ to 5, so the best is $\gamma = 4$, about 1.98.

21. The pair scores are 1.2 for 1–2 and 1–3, 1.3 for 1–4, 1.5 for 2–3 and 0.9 for 2–4 and 3–4, so the best pair is 2–3. MMR first takes sentence 1, the most relevant. It then scores $0.5 \cdot 0.8 - 0.5 \cdot 0.6 = 0.1$ for 2 and 3 and $0.5 \cdot 0.3 - 0 = 0.15$ for 4, and takes 4. Its summary scores 1.3: the greedy first choice locks out the best pair.

22. Colour brown rules out the black dog; size large rules out the two small objects; collar red rules out the large brown cat. Type is then added for the noun, so the algorithm returns four properties, "the large brown dog with the red collar". No two properties rule out all four distractors, but dog, brown and large do, so the shortest description has three.

23. Let $\pi_t$ be the probability that token $t$ is wrong. Then $\pi_1 = \varepsilon$ and $\pi_{t+1} = \varepsilon + (\beta - \varepsilon)\pi_t$. Summing gives 1.888 for $\beta = 0.5$ and $\sum_{t=1}^{50} (1 - 0.98^t) = 18.84$ for $\beta = 1$, against $50 \cdot 0.02 = 1$ under teacher forcing. A model that recovers stays near its long-run error rate $\varepsilon/(\varepsilon + 1 - \beta) = 1/26$; one that never recovers pays for every error until the end.

24. Compute the probability of a win exactly by summing over the counts of the four answers. It is 0.89 at $m = 40$, 0.8983 at $m = 42$ and 0.9022 at $m = 43$, and it rises with $m$ in this range, so the answer is $m = 43$.
