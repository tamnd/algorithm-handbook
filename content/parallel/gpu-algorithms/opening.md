Add two arrays of $10^8$ floats on an NVIDIA A100. Each output costs one addition and 12 bytes of traffic: two loads and one store of 4 bytes. That is $1/12$ FLOP per byte. The 40 GB part moves 1555 GB/s from its memory and does 19.5 TFLOP/s in FP32, so the addition can run at most at $1555/12 \approx 129.6$ GFLOP/s, about 0.66% of the peak, and the kernel takes at least 0.77 ms. If the arrays start on the host, the copies matter more than the kernel. Over a bus at an assumed 25 GB/s, moving the three arrays takes 48 ms, more than sixty times the kernel's own time.

That small sum shows what the chapter is about. A GPU has thousands of lanes that run in lock step, and it is fast only when they all do useful work on data that arrives in time. The cost of a GPU algorithm is rarely its operation count. It is the number of bytes it moves through each level of memory, the number of warps that do nothing, and the number of times the whole grid must stop and start again. The entries count each of these with small models and check the counts on real numbers from vendor documents.

## What the chapter covers

The chapter is in eight groups, read in order.

1. **The SIMT machine.** The [SIMT model](/simt-model/): warps of 32 lanes that issue one instruction at a time, with cost counted in issued warp instructions. [Warp divergence](/warp-divergence/) is what a branch costs, and the [CUDA programming model](/cuda-programming-model/) with its [blocks and grids](/thread-block-and-grid/) is how a program names the threads.
2. **Memory.** The [GPU memory hierarchy](/gpu-memory-hierarchy/) from registers to global memory, and its two rules: [memory coalescing](/memory-coalescing/) for global memory and [bank conflicts](/shared-memory-bank-conflicts/) for shared memory.
3. **Performance models.** [Arithmetic intensity](/arithmetic-intensity/) and the [roofline model](/roofline-model/), $P(I) = \min(\pi, I\beta)$, which tell a memory-bound kernel from a compute-bound one.
4. **Keeping the SMs busy.** [Occupancy](/occupancy/) counts the resident warps, [latency hiding](/latency-hiding/) says how many are enough, and [warp-level primitives](/warp-level-primitives/) share values between lanes in registers.
5. **Host, streams and launches.** The cost of [host-device transfers](/host-device-data-transfer/), the overlap that [CUDA streams](/cuda-streams/) give, and the fixed [cost of each launch](/kernel-launch-overhead/).
6. **Tiled kernels.** [Shared-memory tiling](/shared-memory-tiling/) for matrix multiplication, [stencils](/stencil-computation/), [wavefront parallelism](/wavefront-parallelism/) for dynamic programming tables, and [tensor cores](/tensor-cores/).
7. **Layout and passes over memory.** The [ELLPACK format](/ellpack-format/) for sparse matrices, [kernel fusion](/kernel-fusion/), and the [decoupled look-back scan](/decoupled-look-back-scan/), a prefix sum in one pass.
8. **Advanced control of blocks and warps.** [Cooperative groups](/cooperative-groups/), [persistent threads](/persistent-threads/), [dynamic parallelism](/dynamic-parallelism/), [warp-aggregated atomics](/warp-aggregated-atomics/) and [warp specialization](/warp-specialization/).

## A first reading

For a first reading, take these twelve entries in order: the SIMT model, warp divergence, the CUDA programming model, thread blocks and grids, the GPU memory hierarchy, memory coalescing, shared-memory bank conflicts, arithmetic intensity, the roofline model, occupancy, host-device data transfer and shared-memory tiling. Together they give the machine, its memory, the two performance models and the one technique that every fast dense kernel uses.

Then read latency hiding, kernel fusion and the decoupled look-back scan, which put the models to work. The other entries of groups 5 to 7 can be read when a problem calls for them. Group 8 and tensor cores are advanced. They assume the earlier groups, and they matter mostly to people who write libraries or tune kernels for one generation of hardware.

## Before you start

The chapter uses the [work-span model](/work-span-model/) and [Brent's theorem](/brent-theorem/) from Chapter 20.1, and [data parallelism](/data-parallelism/), [all-prefix-sums](/all-prefix-sums/), [parallel reduction](/parallel-reduce/) and the [Blelloch scan](/blelloch-scan/) from Chapter 20.2. From other volumes it assumes the [memory hierarchy](/memory-hierarchy/) of an ordinary computer, [naive matrix multiplication](/naive-matrix-multiplication/), [sparse matrices](/sparse-matrix/) in the [compressed sparse row](/compressed-sparse-row/) format, [floating-point arithmetic](/floating-point-arithmetic/) and [fetch-and-add](/fetch-and-add/).

The code is CUDA C++, but the ideas carry over to other GPUs: AMD calls a warp a wavefront, of 64 or 32 lanes, and OpenCL calls a block a work-group. Hardware numbers change with every generation. Where an entry gives one, it names the GPU and the document it comes from, and the exercises give their numbers as part of the question. Learn the formulas, and look up the numbers for the GPU you have.
