1. "stella" becomes "stellar" (a substitution), "her" is deleted and "these" is inserted, so $S = D = I = 1$ and the WER is $3/7 \approx 0.43$. The second sentence has one substitution in one word, WER 1. As a corpus the WER is $4/8 = 0.5$; the mean of the sentence WERs is $5/7 \approx 0.71$. Short sentences weigh too much in the mean.

2. The duration is geometric: $P(d) = 0.8^{d-1} \cdot 0.2$, with mean $1/0.2 = 5$ frames, or 50 ms. $P(d = 1) = 0.2$ and $P(d \ge 10) = 0.8^9 \approx 0.134$.

4. $45^3 = 91125$ triphones and $273375$ states. Each Gaussian has $39 + 39 + 1 = 79$ parameters, so the untied model has $273375 \times 16 \times 79 = 345{,}546{,}000$; with 4000 tied states it has $5{,}056{,}000$.

6. A frame is masked unless none of the $M$ frames ending at it starts a span, so the fraction is $1 - (1 - p)^M$: about 0.285 for $M = 5$ and 0.489 for $M = 10$. Overlapping spans make it less than $pM$.

8. The threshold $d'/2$ makes the two error rates equal, so EER $= \Phi(-d'/2)$: $\Phi(-0.5) \approx 0.309$ and $\Phi(-1.5) \approx 0.067$.

11. Fill the table row by row with $D(i, j) = |x_i - y_j| + \min$ of the three predecessors. The cost is 1, for example by $(1,1), (2,2), (3,2), (4,3), (4,4)$, where the only cost is $|3 - 4|$. The diagonal costs $0 + 1 + 5 + 0 = 6$.

13. Write the label sequence with blanks between and around, and count the ways to spread $T$ frames over it. For "aa" the blank between the two $a$'s is required, which leaves fewer paths: the counts are 15, 5 and 6.

14. There are $\binom{T + U - 1}{U} = 2$ alignments: emit the label at frame 1, or at frame 2. Each alignment ends with a blank at $(2, 1)$. Multiply the probabilities along each and add: $0.6 \cdot 0.5 \cdot 0.9 + 0.4 \cdot 0.3 \cdot 0.9$.

15. Under "same" the pair is Gaussian with covariance $\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$; under "different" it is $2I$. The ratio is $\tfrac12 \ln\tfrac43 - \tfrac13(x_1^2 - x_1x_2 + x_2^2) + \tfrac14(x_1^2 + x_2^2)$. The pairs $(0, 0)$ and $(2, 2)$ have the same distance but different scores, 0.144 and 0.811.

19. The maximized log-likelihood of $n$ frames with variance $\sigma^2$ is $-\tfrac{n}{2}(\ln 2\pi\sigma^2 + 1)$. The pooled variance is 4.25 and each child's is 0.25, so the gain is $4\ln(4.25/0.25) = 4\ln 17 \approx 11.33$.

21. Sweep the threshold over the scores and list the points $(P_{\text{fa}}, P_{\text{miss}})$. The nearest point is at threshold 0.6. For the hull, keep the lower convex hull of the points and intersect it with the line $P_{\text{miss}} = P_{\text{fa}}$; the segment that crosses it joins $(1/5, 1/4)$ and $(4/5, 0)$.

22. The forward weight of state 1 is 0.6 + 0.4 and the backward weight of state 1 is 0.6 + 0.4, so $Z = 1 \cdot 1 + 0.4$. The posterior of an arc is forward times weight times backward over $Z$. Compare the best path $e$ with the arcs of highest posterior from state 0 and from state 1.

23. Enumerate the nine paths and collapse each. The single most likely path is blank-blank, with 0.16, but "a" collects three paths: $0.35^2 + 2 \cdot 0.35 \cdot 0.4 = 0.4025$.

25. Track the subset reached by $a b^k$ as pairs (state, residual weight). With equal loops the residuals stay $(0, 1)$ for every $k$, so the subsets repeat and the construction stops; the two states are twins. With loops 3 and 4 the residual of state 2 is $1 + k$, so every $k$ gives a new subset and determinization does not terminate.
