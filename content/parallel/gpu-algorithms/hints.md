1. The grid has 2 blocks of 2 warps, and all 4 warps have an active lane, so $I = 2 \cdot 2 \cdot 2 + 4 \cdot 4 = 24$ and $L = 2 \cdot 2 \cdot 64 + 4 \cdot 100 = 656$. The efficiency is $656/768 \approx 0.85$. Thread 70 is lane 6 of warp 2.

2. The warp runs $\max_\ell t_\ell = 4$ trips, so it issues $12$ body instructions. The trip counts sum to $8 \cdot (1 + 2 + 3 + 4) = 80$, so it runs $240$ lane instructions, and the efficiency is $80/128 = 62.5\%$.

3. (a) $\lfloor 31 \cdot 12/32 \rfloor + 1 = 12$ sectors, efficiency $1/3$. (b) $8$ sectors, efficiency $100\%$. (c) $16$ sectors for 256 useful bytes out of 512, efficiency $50\%$.

4. The column read has stride $w$, so the degree is $\gcd(w, 32)$: 8, 8, 1 and 2.

5. The grid is $32 \times 125$ blocks, 4000 in all, with $1\,024\,000$ threads, of which $24\,000$ fail the test. All of them are in the last column of blocks, where only $1000 - 31 \cdot 32 = 8$ of the 32 columns of threads are inside the image.

6. Each item does 2 FLOP and moves 12 bytes, so $I = 1/6$. The ridge is $20$ FLOP per byte, and the roofline allows $10^{12}/6 \approx 167$ GFLOP/s, about $0.83\%$ of the peak.

7. $8 + 50 = 58$ µs. The half-bandwidth size is $L\beta = 160\,000$ bytes. A copy of 16 000 bytes takes $8.8$ µs, which is about $1.82$ GB/s, $9\%$ of $\beta$.

8. A warp takes $\rho = 2048$ registers, so $W_R = 4 \lfloor 16384/2048 \rfloor = 32$ and the registers allow 8 blocks, against 16 for threads and warps and 32 block slots. The occupancy is $32/64 = 50\%$, limited by registers. With 48 KB per block, shared memory allows $\lfloor 164/48 \rfloor = 3$ blocks, 12 warps, $18.75\%$.

9. The true lanes are $0, 5, 10, \ldots, 30$, so the ballot is `0x42108421` with 7 bits set. Lane 15 counts the set bits below bit 15, lanes 0, 5 and 10, so it takes slot 3.

10. $T = 200 \cdot 10 = 2000$ µs and $\eta = 0.6$. $\tau/(\tau + o) \ge 0.9$ gives $\tau \ge 9o = 36$ µs. One launch of the graph saves $k\delta = 30$ µs, and $\lceil 500/30 \rceil = 17$, so the graph is ahead from its 17th launch.

11. (a) Stride 4 words: 16 sectors, $25\%$. (b) 4 sectors, $100\%$. (c) 16 sectors, all 512 bytes useful, $100\%$. The formula needs the word size to divide 32 and the array to be aligned, and both hold for 16-byte words.

12. $T/4 \ge 20$ gives $T \ge 80$. One thread per output would need blocks of $6400$ threads, but a block holds at most 1024, so $T \le 32$ and $I \le 8$. With $r \times r$ register tiles inside $T \times T$ thread blocks the loads fall to $2n^3/(Tr)$ and the intensity approaches $Tr/4$. So $Tr \ge 80$ is enough, for example $T = 16$ and $r = 5$.

13. $K = 9$, $72$ slots for $31$ nonzeros, so $41$ padding slots, about $57\%$. With $K = 3$ the ELL part has 24 slots, 19 filled and 5 padding, and COO holds the other 12 entries. ELL needs 576 bytes, HYB $24 \cdot 8 + 12 \cdot 12 = 336$ and CSR $31 \cdot 8 + 9 \cdot 4 = 284$.

14. The widths are $1, 2, 3, 4, 4, 4, 3, 2, 1$, which sum to 24. Then $T_2 = 1 + 1 + 2 + 2 + 2 + 2 + 2 + 1 + 1 = 14$, against the bound 21, and the threads do useful work in $24/28 \approx 86\%$ of their steps.

17. $1.5 \cdot 10^{12} \cdot 600 \cdot 10^{-9} = 900$ KB, or 9000 bytes per SM, which is 71 warp loads. With one load per thread that needs 71 warps, more than 64, so no. With 2 loads per thread, 36 warps; with 4, 18 warps.

18. FP16 gives $1229/4096 = 0.300048828125$, a relative error of about $1.6 \cdot 10^{-4}$, below $2^{-11} \approx 4.9 \cdot 10^{-4}$. BF16 gives $154/512 = 0.30078125$, about $2.6 \cdot 10^{-3}$, below $2^{-8} \approx 3.9 \cdot 10^{-3}$. Padding to 608 gives $38^3 = 54\,872$ warp operations, of which $(600/608)^3 \approx 96\%$ of the work is useful.

19. $t = 2^{18}$. The single pass moves $2n$ items, $8\,589\,934\,592$ bytes, in about $4.29$ ms. Reduce-then-scan moves $(3n + 4t - 1) \cdot 4 = 12\,889\,096\,188$ bytes, in about $6.44$ ms.

20. For $q = 0.25$: $E[a] = 100(1 - 0.75^{32}) \approx 99.99$ and $E[k] = 800$, a factor of about 8. For $q = 1/32$: $E[a] = 100(1 - (31/32)^{32}) \approx 63.8$ and $E[k] = 100$, a factor of about $1.57$.

22. Use induction. After the steps with masks $16, 8, \ldots, 2^i$, lane $\ell$ holds the sum over all $j$ that agree with $\ell$ in bits $0$ to $i - 1$. Before the first step this holds with $i = 5$. The step with mask $2^{i-1}$ adds the sum held by lane $\ell \oplus 2^{i-1}$, which covers the $j$ that agree with $\ell$ in bits $0$ to $i - 2$ and differ from it in bit $i - 1$. After the masks 16 and 8, lane $\ell$ holds $\sum_{j \equiv \ell \ (\mathrm{mod}\ 8)} x_j$, a sum of 4 inputs.

23. Put $\max(H/m, K/m, D/m) = M/m$ into the formula of the entry and collect the terms. The part that depends on $m$ is $(S - M)/m + m\lambda$. Here $S - M = 6$, so the real minimum is at $\sqrt{60} \approx 7.75$. Then $T(7) \approx 7.757$, $T(8) = 7.75$ and $T(9) \approx 7.767$ ms, so $m = 8$. With $\lambda = 0$, $T(8) = 6.75$ ms.

24. Minimize $g(s) = (T + 2rs)^2/s$. Setting $g'(s) = 0$ gives $4rs = T + 2rs$, so $s = T/(2r)$ and $f = (2T)^2/((T/2r) T^2) = 8r/T$. Here the minimum $s = 16$ would need $128^2$ floats, 64 KB. The memory holds 12 288 floats, so $64 + 4s \le 110$ and $s \le 11$. Since $f$ falls for $s < 16$, the best is $s = 11$, with $f = 11\,664/45\,056 \approx 0.259$, against $0.25$ without the limit.

25. $x = 819/8192 = 0.0999755859375$. Below 256 the spacing of FP16 is at most $0.125$, so half a spacing is at most $0.0625 < x$, and each add raises the sum by more than $0.0625$. It reaches 256 within 4096 adds. At 256 the spacing is $0.25$, and $x$ is less than half of it, so $256 + x$ rounds back to 256. In FP32, each partial sum is $k \cdot 819 \cdot 2^{-13}$ with $k \cdot 819 < 2^{23}$, so it is exact, and the result is $999.755859375$. The only error is the rounding of $0.1$ to FP16.

26. For $g < p$ there are only $g$ tiles to read. For $g \ge p$: when tile $g$ is taken, at most $p - 1$ other blocks are resident, and each block holds one tile, so one of the tiles $g - p, \ldots, g - 1$ belongs to a block that has already exited. A block exits only after it publishes its inclusive prefix, so the look-back stops there at the latest. For the deadlock, let blocks 1 and 2 become resident before block 0. Block 1 waits for tile 0. Block 2 passes tile 1, which shows its aggregate, and then also waits for tile 0. Both slots stay full, so block 0 never starts.

27. You need 36 warps for $j = 2$, so 9 blocks of 4 warps. That needs $W_R \ge 36$, and $\rho = 1792$ works but $2048$ does not, so $r \le 56$. For $j = 4$ you need 18 warps, which is 5 blocks or 20 warps. That needs $\lfloor 16384/\rho \rfloor \ge 5$, so $\rho \le 3072$ and $r \le 96$. The extra registers can hold more outputs per thread and reused values, which is the case of Volkov's measurements.
