1. $10^{-2.5} \approx 0.00316$. For 0.002, $-10 \log_{10} 0.002 = 26.99$, so Q27.

3. SEQ holds the soft clip, matches and insertion: $5 + 20 + 2 + 10 + 15 = 52$ bases. The reference span counts M and D: $20 + 10 + 3 + 15 = 48$, so the last position is $100 + 48 - 1 = 147$.

4. With $e = 0.01$: $L(AA) = 0.99^4 \cdot 0.01/3 \approx 3.20 \times 10^{-3}$, $L(AG) = 0.49667^5 \approx 3.02 \times 10^{-2}$ and $L(GG) = (0.01/3)^4 \cdot 0.99 \approx 1.22 \times 10^{-10}$. PL is 10, 0 and 84, so AG is the most likely genotype.

7. Deleting `TG` at 7 to 8 gives `ACTGTGC`, and so does deleting it at 5 to 6 or 3 to 4. A further step left would delete `CT`, which gives a different sequence. With the anchor base at position 2 the normalized form is POS 2, REF `CTG`, ALT `C`.

8. $1 - \sum_{i=0}^{3} \binom{40}{i} 0.1^i\, 0.9^{40-i} = 0.5769$.

12. The cutoff is 490. The flagged fraction is $\Phi((D - 90)/30)$: 0.5 for $D = 90$, 0.8413 for 120 and 0.9772 for 150. With 10 pairs and $p = 1/2$, $P(\ge 2) = 1 - 11/1024 = 1013/1024 \approx 0.9893$.

13. The first four fragments fit `0110` or `1001` except `010-`, which is one site off from `011-`, so the cost is 1. The fragments `011-` and `010-` agree at sites 1 and 2 and differ at site 3, so they can be put neither on the same haplotype nor on opposite ones without a correction.

17. The posterior error is $p_2/(p_1 + p_2) = 1/(1 + 10^{\Delta/10})$. Then $10 \log_{10}(1 + 10^{\Delta/10}) - \Delta = 10 \log_{10}(1 + 10^{-\Delta/10})$, which lies in $(0, 10 \log_{10} 2]$ for $\Delta \ge 0$.

19. The excursion uses two switches and $L - 1$ stays, where the straight path uses $L + 1$ stays. The transition terms differ by $2 \log((1 - \varepsilon)/\varepsilon)$, and $L$ cancels. For $\varepsilon = 10^{-3}$ the threshold is $2 \ln 999 \approx 13.81$.

20. The power $P(\mathrm{Bin}(n, 0.15) \ge 4)$ is 0.9487 at $n = 49$ and 0.9540 at $n = 50$, so the depth is 50. The false call rate is $P(\mathrm{Bin}(50, 0.001) \ge 4) \approx 2.2 \times 10^{-7}$ per site.

21. With $\lambda$ reads per key, the expected fraction flagged is $1 - (1 - e^{-\lambda})/\lambda$. Single-end: $\lambda = 0.1613$ and about 7.6 percent. Pairs: $\lambda = 8.06 \times 10^{-4}$ and about 0.04 percent, which is why pairs are marked on both ends.

22. Any choice of "same" or "opposite" for each adjacent pair of sites comes from one haplotype pair, built from left to right, so the pairs do not interact. For each pair, take the relation supported by more weight. Here the costs are 1, 1 and 0, so the optimum is 2, reached by `0011` and `1100`.
