## What to remember

- In a rectified pair a point at depth $Z$ has disparity $d = fb/Z$. A disparity error $\delta d$ gives a depth error of about $Z^2|\delta d|/(fb)$, so depth error grows with the square of depth, and a search range of $D$ disparities sees no nearer than $fb/(D-1)$.
- Most two-view methods fill a $W \times H \times D$ cost volume and then choose one disparity per pixel. A local method sums costs over a window and takes the minimum in $\Theta(WHD)$ time; the window size trades noise against blurred edges.
- The census transform keeps only the order of the intensities around a pixel. Its Hamming cost does not change under any strictly increasing change of brightness, such as a gain difference between the cameras.
- Scanline dynamic programming finds the exact minimum of its cost along one row, but the rows do not agree with each other. Semi-global matching sums 8 or 16 such path costs per pixel with penalties $P_1$ for a one-step change and $P_2$ for a jump. It is fast and accurate in practice but has no bound for the 2D energy.
- Only regular binary energies can be represented by a cut. A pair term is regular when $E(0,0) + E(1,1) \le E(0,1) + E(1,0)$, and for terms of up to three variables regularity is also sufficient, so one s-t minimum cut gives the exact minimum.
- For several labels, alpha-expansion with a metric pair term reaches a local minimum within $2c$ of the optimum, where $c$ is the ratio of the largest to the smallest nonzero pair cost; $c = 1$ for Potts. Alpha-beta swap needs only a semimetric but has no constant bound. ICM stops at a single-site local minimum that depends on the visiting order. Potts minimization with three or more labels is NP-hard.
- Photometric stereo is exact for a Lambertian surface under three or more known, non-coplanar lights: $I = \rho\, s^{\top} n$ is linear in $g = \rho n$. Shape from shading with one image is ill-posed without boundary data.
- With many views, plane sweep tests $D$ depth planes in $\Theta(DNWH)$ time, TSDF fusion averages truncated signed distances in each voxel, and space carving reaches the photo hull, the largest shape consistent with all images.
- NeRF and 3D Gaussian splatting fit a scene to posed images by gradient descent. They are judged by benchmark measurements, not by guarantees.

| Method | Time | Optimality |
|---|---|---|
| Block matching | $\Theta(WHD)$ | exact winner per pixel for its window cost |
| Scanline dynamic programming | $\Theta(WHD)$ | exact per row for its cost |
| Semi-global matching | $\Theta(WHDR)$, space $\Theta(WHD)$ | no bound for the 2D energy |
| PatchMatch stereo | $\Theta(TWHs\log D)$ | no bound, measured |
| Iterated conditional modes | $O(kL(n + m))$ | single-site local minimum |
| Alpha-beta swap | $O(kL^2(F + n + m))$ | local minimum, no constant bound |
| Alpha-expansion | $O(kL(F + n + m))$ | within $2c$ of the optimum |
| QPBO | $O(F + n + m)$ | partial labeling, part of an optimum |
| Plane sweep stereo | $\Theta(DNWH)$ | best plane per pixel |
| TSDF fusion | $\Theta(Nn^3)$ | weighted average per voxel |
| Voxel coloring | $\Theta(NWHn)$ | photo-consistent, needs a camera condition |
| Space carving | $O(NWHn^4)$ | the photo hull |
| Photometric stereo | $\Theta(NWH)$ | exact under the Lambertian model |

: Main methods. Images are $W \times H$ with $D$ disparities or planes; $R$ is the number of SGM paths; $T$ and $s$ are the iterations and window size of PatchMatch; $k$ cycles, $L$ labels, $n$ sites, $m$ pair terms and max-flow cost $F$ for the energies; $N$ images and $n$ voxels per side for the volume methods.

## Choosing a method

For a calibrated two-camera rig, rectify first. Census costs with semi-global matching, then subpixel refinement and a left-right check, are the usual baseline; SGM has been built in hardware for real time use. Block matching is simpler and suits scenes with texture everywhere. Use PatchMatch stereo when large slanted surfaces matter more than speed.

For a clear objective, write a Potts or truncated linear energy and run alpha-expansion; QPBO handles moves that are not regular. ICM is only a quick polish.

For many photographs of one object, sweep planes or run PMVS, then fuse the depth maps; for a moving depth camera, use TSDF fusion. Silhouettes alone give only the visual hull, which misses concavities. When the light can be controlled, structured light or photometric stereo gives denser depth than passive matching. For new views rather than a measured surface, use NeRF or Gaussian splatting; splatting renders in real time.
