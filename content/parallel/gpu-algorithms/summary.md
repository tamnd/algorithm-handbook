## What to remember

- A GPU issues one instruction for a **warp** of 32 lanes. A kernel costs its issued warp instructions $I$; its work is its lane instructions $L$, and the SIMT efficiency is $L/(32I)$. A divergent branch issues both paths, and a loop runs as often as its longest lane.
- A warp load from global memory costs one transaction per 32-byte sector it touches. For 4-byte words at stride $s$ words this is $\min(32, \lfloor 31 \cdot 4s/32 \rfloor + 1)$ sectors, so stride 1 needs 4 and stride 8 or more needs 32. Shared memory has 32 banks, and stride $s$ gives a conflict of degree $\gcd(s, 32)$. Padding rows of 32 words to 33 removes the conflicts of a column read.
- The **roofline** bounds the rate of a kernel by $P(I) = \min(\pi, I\beta)$, with intensity $I$ in FLOP per byte. Below the ridge point $\pi/\beta$ a kernel is limited by memory. The ridge point of the A100 40 GB in FP32 is about 12.54.
- **Occupancy** is the number of resident warps per SM over the maximum. The resident blocks are the minimum of five limits: blocks, threads, warps, registers and shared memory. High occupancy is not a goal in itself. By Little's law the GPU needs bandwidth times latency bytes in flight, from many warps or from fewer warps with more independent loads each.
- **Tiling** a matrix product with $T \times T$ shared tiles cuts the global loads from $2n^3$ to $2n^3/T$ and raises the intensity to $T/4$ FLOP per byte. Stencils reuse a tile with a halo, at $1 + 4r/T$ loads per output for a 2D star of radius $r$.
- Copies and launches have fixed costs. A copy of $s$ bytes takes $L + s/\beta$, so copies well below $L\beta$ bytes waste most of the link. A chain of $k$ kernels pays $k$ launch costs; streams, CUDA Graphs and fusion hide or remove them.
- For a bandwidth-bound kernel, count passes over memory. Fusing $k$ elementwise kernels cuts $2kn$ words to $2n$. The decoupled look-back scan moves about $2n$ items, against $3n + 4t - 1$ for reduce-then-scan over $t$ tiles.
- The only grid-wide barrier of a plain launch is the end of the kernel. A barrier inside a kernel is safe only when all blocks are resident at once, which a cooperative launch checks.

| Technique | What it saves | Key count | Price |
|---|---|---|---|
| Coalescing | global memory sectors | 4 sectors per warp load of 32 floats | a layout such as structure of arrays |
| Bank-conflict padding | shared memory replays | degree $\gcd(w, 32)$ for row width $w$ | 32 words for a $32 \times 33$ tile |
| Shared-memory tiling | global loads | $2n^3/T$ loads, $I = T/4$ | shared memory, two barriers per phase |
| Kernel fusion | round trips through memory | $2kn \to 2n$ words for $k$ elementwise kernels | registers, and so occupancy |
| Streams | idle copy engines | $H + K + D \to \max(H, K, D)$ as chunks grow | pinned memory, a cost $\lambda$ per operation |
| CUDA Graphs | per-launch overhead | break even after $C/(k\delta)$ launches | instantiation cost $C$ |
| Decoupled look-back | a pass over the input | about $2n$ items instead of about $3n$ | atomics, forward progress of resident blocks |
| Warp-aggregated atomics | contended atomics | up to 32 atomics become one | a vote and a shuffle per warp |
| Warp specialization | exposed load time | $L + C + (T - 1)\max(L, C)$ per block | shared memory for $k \ge 2$ buffers |

: The main techniques of the chapter, what each saves and what it costs, with counts from the entries.

## Choosing a method

Start with the roofline: compare the intensity of the kernel with the ridge point of the GPU to learn which resource to work on. Below the ridge, make every access coalesced, keep reused data in shared memory or registers, and remove passes over memory by fusion or single-pass methods. Above it, use register tiling and, where the precision allows, tensor cores.

Raise the occupancy only when the kernel has too few bytes in flight, and sort data-dependent work by size to cut divergence. For a long chain of small kernels, try a CUDA Graph, fusion or a persistent kernel. If the data starts on the host, the bus may cost more than the kernel: overlap copies with work in streams, or keep the data on the device.

Use the advanced techniques last. A grid barrier, dynamic parallelism and warp specialization each fix one problem, but they tie the code to one generation of hardware.
