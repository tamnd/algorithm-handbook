2. $Y_1$ is the larger of two values and has distribution $v^4$, so $\beta(v) = \int_0^v y \cdot 4y^3\,dy / v^4 = 4v/5$. The highest value has distribution $v^6$ and mean $6/7$, so the revenue is $24/35$. The second-highest value has distribution $3v^4 - 2v^6$, and its mean $1 - 3/5 + 2/7$ is also $24/35$.

3. $F(v) = (v-1)/2$ and $f = 1/2$, so $\varphi(v) = 2v - 3$ and the reserve is $3/2$. Posting $3/2$ sells with probability $3/4$ and earns $9/8$. On $[2, 3]$ the formula is again $\varphi(v) = 2v - 3$, which is at least 1 on the whole support, so the seller never excludes a value: the reserve is $2$, the lowest value.

4. The virtual values are $-1$, $2$ and $4$. They increase, so the distribution is regular. The prices $1$, $3$ and $4$ earn $1$, $3/2$ and $1$, so the best price is $3$.

5. Accept $\{b, c\}$, $\{a\}$ and $\{d\}$, for 14. The next best allocations are the bid on all four items (12) and $\{a, b\}$ with $\{c, d\}$ (11).

7. In the first market $k = 3$ and $p_0 = (3 + 7)/2 = 5$, which lies in $[s_{(3)}, b_{(3)}] = [5, 6]$: three trades at price 5, and the auctioneer keeps nothing. In the second market $k = 3$ but $p_0 = (5 + 8)/2 = 6.5 > 6$, so the third pair is dropped. The buyers with values 9 and 8 pay 6, the sellers with costs 2 and 4 receive 5, and the auctioneer keeps 2.

8. The virtual values are $2v - 1$ and $2v - 2$. For $(0.8, 1.1)$ they are $0.6$ and $0.2$: bidder 1 wins and pays $0.6$, the value at which its virtual value falls to $0.2$. For $(0.4, 1.5)$ they are $-0.2$ and $1$: bidder 2 wins and pays $1$, where its virtual value reaches 0. For $(0.3, 0.8)$ both are $-0.4$, so the item is not sold.

11. Both auctions give the same interim allocation: a bidder wins with probability $0$, $5/8$ and $7/8$ at values $1$, $3$ and $4$. The payment that stops a type-4 bidder from reporting 3 is $4 \cdot 7/8 - (4 - 3) \cdot 5/8 = 23/8$. The second-price auction charges it only $22/8$ in expectation, because it pays 3 when it beats a bid of 3. With discrete values the allocation alone does not fix the payments, and the threshold price of a discrete type is not the next bid.

14. Truthful bids accept $10$, $7$ and $6$, and the highest losing bid is $5$. A gets two units and utility $5 + 2 = 7$. If A bids only $10$, the accepted bids are $10$, $6$ and $5$, the price falls to $1$, and A gets $9$. This is demand reduction.

16. The winner has the largest error and pays $V + e_{(2)}$, where $e_{(2)}$ is the second-largest error. Its mean is $-1 + 2(n-1)/(n+1) = (n-3)/(n+1)$, so the expected profit is $-(n-3)/(n+1)$. The winner gains $1/3$ with two bidders, breaks even with three, and loses for every $n \ge 4$.

17. The revenue curve is $R(q) = q(1 - q)$, which is concave, so the relaxation puts $q_i = 1/3$ and has value $2/3$. Each price is $2/3$, and the sale happens unless all three values fall below it: revenue $\frac{2}{3}(1 - (2/3)^3) = 38/81 \approx 0.469$. The ratio $19/27$ equals the guarantee exactly. Myerson's auction earns $17/32 \approx 0.531$.

19. The scores $v/\sqrt{|S|}$ are about $5.66$, $5$, $4$, $3.54$ and $3$, so the order is A, B, C, D, E. A, C and D win, for welfare 17, which is optimal. A pays $5\sqrt{2} \approx 7.07$, since below that B comes first and takes item 2. C pays 0, since the only bid it meets is B, which loses anyway. D pays $3\sqrt{2} \approx 4.24$, the value at which E would come first.

22. Let $B$ be the highest bid of the others. In every outcome, $(v_1/2) \cdot [B < v_1/2] \ge v_1/2 - B$. So bidder 1's equilibrium utility is at least $v_1/2 - \mathbb{E}[B]$, and $\mathbb{E}[B]$ is at most the expected revenue. The welfare is the sum of the utilities plus the revenue, and the utilities are nonnegative.

23. The optimal revenue is $\mathbb{E}[\max(2Y - 1, 0)]$ for the highest value $Y$, which has density $n y^{n-1}$; integrate from $1/2$ to $1$. A Vickrey auction with $n + 1$ bidders earns $n/(n+2)$. The difference is $2/((n+1)(n+2))$, and this is at least $1/((n+1)2^n)$ because $2^{n+1} \ge n + 2$.

24. Take values $1$, $1 - \delta$ and $0$. Bidding truthfully, the top bidder gets slot 1 and utility $\alpha_1 \delta$. Bidding between $0$ and $1 - \delta$, it gets slot 2 at price $0$ and utility $\alpha_2$. This is better when $\delta < \alpha_2/\alpha_1$.

25. For a fixed $s$, the buyer gets the good exactly when its bid is at least $s$, so its payment is the threshold $s$. In the same way the seller sells exactly when its bid is at most $b$, and it receives $b$. Each trade needs $b - s$ from outside. When $b$ and $s$ are drawn independently from overlapping intervals, the Myerson-Satterthwaite theorem says that no efficient and interim individually rational mechanism avoids an expected deficit, even if truthfulness is weakened to Bayesian incentive compatibility.

26. Add a new vertex $i'$ for each item $i$. A bid on $\{i, j\}$ becomes an edge $ij$, and a bid on $\{i\}$ becomes an edge $ii'$, weighted by the bid; keep the best bid when two name the same set. Sets of disjoint bids are then exactly the matchings, and a maximum weight matching in a general graph takes polynomial time.
