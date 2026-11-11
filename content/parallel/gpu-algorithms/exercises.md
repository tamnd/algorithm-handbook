1. ◦ Use the counts of the vector add kernel in the [SIMT model](/simt-model/) for $n = 100$ items and blocks of $T = 64$ threads. Find the issued warp instructions $I$, the lane instructions $L$ and the SIMT efficiency. In a block of 96 threads, which warp holds thread 70, and which lane is it?

2. ◦ In one warp, lane $\ell$ runs a loop $(\ell \bmod 4) + 1$ times, and the loop body has 3 instructions. By the rule of [warp divergence](/warp-divergence/), how many body instructions does the warp issue, how many lane instructions does it run, and what is the efficiency of the loop?

3. ◦ By the rule of [memory coalescing](/memory-coalescing/), how many 32-byte sectors does one warp load touch, and what is its efficiency, when lane $\ell$ reads (a) the 4-byte word $3\ell$ of an aligned array, (b) the 8-byte word $\ell$, (c) the 8-byte word $2\ell$?

4. ◦ A block keeps a tile `float t[32][w]` in shared memory, and a warp reads one column of it, one row per lane. Give the conflict degree for $w = 24$, $40$, $41$ and $34$. Use [shared memory bank conflicts](/shared-memory-bank-conflicts/).

5. ◦ A kernel gives one thread to each pixel of a $1000 \times 1000$ image, with blocks of $32 \times 8$ threads and the usual rounding up of the [grid](/thread-block-and-grid/). Give the grid dimensions, the number of blocks, the number of threads launched and the number of threads that fail the bounds test.

6. ◦ SAXPY computes $y_i \gets a x_i + y_i$ on 4-byte floats. Give its arithmetic intensity. A GPU has a peak of $\pi = 20$ TFLOP/s and a bandwidth of $\beta = 1$ TB/s. Give its ridge point, the rate that the [roofline model](/roofline-model/) allows for SAXPY, and that rate as a fraction of the peak.

7. ◦ A host link has latency $L = 8$ µs and bandwidth $\beta = 20$ GB/s in the model of [host-device data transfer](/host-device-data-transfer/). How long does a copy of $10^6$ bytes take? What is the half-bandwidth size? What effective bandwidth does a copy of 16 000 bytes see?

8. ◦ Compute the [occupancy](/occupancy/) on compute capability 8.0 of a kernel with blocks of 128 threads and 64 registers per thread and no shared memory. Which limit binds? Then let each block also use 48 KB of shared memory.

9. ◦ In a full warp, the lanes $\ell$ with $\ell \bmod 5 = 0$ have a true predicate. Write the result of `__ballot_sync(0xffffffff, p)` in hexadecimal and give its population count. Which output slot does lane 15 get from the rank formula of [warp-level primitives](/warp-level-primitives/)?

10. • A job launches $k = 200$ kernels in a row. Each has a body of $\tau = 6$ µs and an overhead of $o = 4$ µs that nothing hides. Give the time of the job and the efficiency $\eta$ in the model of [kernel launch overhead](/kernel-launch-overhead/). How long must a body be for $\eta \ge 0.9$? Next, the same steps are put in a CUDA Graph of $k = 20$ kernels that costs $C = 500$ µs to instantiate and saves $\delta = 1.5$ µs per kernel. From which launch of the graph on is the graph ahead?

11. • Records of four floats $x, y, z, w$ are stored as an array of structures, and lane $\ell$ of a warp needs record $\ell$. Count the sectors and give the efficiency when the kernel (a) reads only the field $x$, (b) reads $x$ from a structure of arrays instead, (c) reads the whole record as one 16-byte `float4`. Why does the formula $T(s)$ of [memory coalescing](/memory-coalescing/) still apply in case (c)?

12. • On the GPU of the SAXPY exercise ($\pi = 20$ TFLOP/s, $\beta = 1$ TB/s), [tiled matrix multiplication](/shared-memory-tiling/) with $T \times T$ tiles has intensity close to $T/4$ for large $n$. What tile edge does it need to reach the ridge point? Explain why a kernel with one thread per output cannot have it, and give block and register tile sizes that can.

13. • An $8$-row sparse matrix has row lengths $3, 1, 4, 1, 5, 9, 2, 6$. Find $K$, the number of slots and the fraction of padding of its [ELLPACK](/ellpack-format/) form. Then split it as HYB with $K = 3$: how many ELL slots are filled, how many are padding, and how many entries go to COO? With 4-byte values and indices, compare the bytes of ELL, of HYB and of CSR.

14. • A dynamic programming table of $6 \times 4$ cells is filled by [wavefront parallelism](/wavefront-parallelism/) on $p = 2$ threads with a barrier per anti-diagonal. List the widths $w_d$, compute $T_2$ exactly and compare it with the bound $nm/p + n + m - 1$. What fraction of the thread steps does useful work?

15. • A 2D star [stencil](/stencil-computation/) of radius $r = 2$ runs on $16 \times 16$ tiles. Give the global loads per output with no reuse, with a star halo and with a box halo. Which of the two halos is easier to load with the threads of one block, and why does the star halo still win on loads?

16. • Three elementwise kernels run in a row over $n = 2.5 \cdot 10^8$ floats, each reading one array and writing one, at a bandwidth of 1 TB/s. Give the memory time before and after [kernel fusion](/kernel-fusion/). Now let the third kernel be a sum of the array instead. Give both times again.

17. • A GPU has 100 SMs of at most 64 warps each, a memory bandwidth of 1.5 TB/s and a memory latency of 600 ns. By Little's law, how many bytes must be in flight on each SM? Count in coalesced warp loads of 128 bytes. Can one load in flight per thread hide the latency? How many warps per SM are needed with 2 and with 4 independent loads per thread? See [latency hiding](/latency-hiding/).

18. • Round $0.3$ to FP16 and to BF16 and give the relative errors. Compare them with the unit roundoffs of [tensor cores](/tensor-cores/). Then a product of two $600 \times 600$ FP16 matrices runs as $16 \times 16 \times 16$ warp operations, with each dimension padded to a multiple of 16. How many warp operations does it take, and what fraction of their multiply-adds is useful?

19. • A scan runs over $n = 2^{30}$ items of 4 bytes, in tiles of $b = 4096$ items. Count the bytes that the [decoupled look-back scan](/decoupled-look-back-scan/) moves, ignoring the descriptors, and the bytes of reduce-then-scan, counted exactly as $3n + 4t - 1$ items. At an assumed 2 TB/s, give both times.

20. • A grid has $w = 100$ full warps, and each lane takes part in an atomic increment with probability $q$, independently. Give the expected numbers of atomics with and without [warp-aggregated atomics](/warp-aggregated-atomics/) for $q = 0.25$ and for $q = 1/32$, and the factor saved in each case.

21. • A block works on $T = 10$ tiles. Loading a tile takes $L = 5$ µs and computing on it takes $C = 3$ µs. Give the time when one group of warps loads and then computes each tile, and the time with [warp specialization](/warp-specialization/) and two buffers. What does the specialized time become if the compute gets three times faster? If the load drops to 3 µs instead?

22. • Prove that after `__shfl_xor_sync` steps with masks 16, 8, 4, 2 and 1, each adding the value received, every lane of a warp holds the sum of all 32 inputs. Which sum does lane $\ell$ hold if the loop stops after the masks 16 and 8? Use [warp-level primitives](/warp-level-primitives/).

23. ★ In the pipeline model of [CUDA streams](/cuda-streams/), let $S = H + K + D$ and $M = \max(H, K, D)$. Show that $T(m) = M + (S - M)/m + (m + 2)\lambda$, and that the real $m$ that minimizes it is $\sqrt{(S - M)/\lambda}$. For $H = 6$, $K = 3$, $D = 3$ ms and $\lambda = 0.1$ ms, find the best integer $m$, its time, and the time with $\lambda = 0$ at the same $m$.

24. ★ In temporal blocking of a [stencil](/stencil-computation/), the loads per output per sweep are $f(s) = (T + 2rs)^2/(sT^2)$. Show that $f$ is smallest at $s = T/(2r)$ and that the minimum is $8r/T$. Then take $T = 64$ and $r = 2$, and let the block keep one array of $(T + 2rs)^2$ floats in 48 KB of shared memory. Find the best $s$ allowed and its $f(s)$.

25. ★ Let $x$ be $0.1$ rounded to FP16. Give $x$ exactly. Add $x$ to itself $10\,000$ times in an FP16 accumulator with round to nearest, and show that the sum stops growing at 256. Then show that an FP32 accumulator gives exactly $10\,000x$, and give that value. Relate both results to what [tensor cores](/tensor-cores/) do with the accumulator.

26. ★ In the [decoupled look-back scan](/decoupled-look-back-scan/), tiles are numbered by an atomic counter and at most $p$ blocks are resident at once. Prove that the look-back of each tile reads at most $p$ descriptors, not counting failed polls. Then let the tile index be `blockIdx.x` with $p = 2$, and give a dispatch order of blocks that deadlocks.

27. ★ Take the GPU of the Little's law exercise: 100 SMs, 1.5 TB/s, 600 ns, coalesced warp loads of 128 bytes. Its SMs follow the [occupancy](/occupancy/) rules of compute capability 8.0. A kernel uses blocks of 128 threads and no shared memory. Each thread keeps $j$ independent loads in flight. For $j = 2$ and $j = 4$, find the largest number of registers per thread that still keeps enough warps resident to hide the latency. Explain why the kernel with $j = 4$ can be the faster one.
