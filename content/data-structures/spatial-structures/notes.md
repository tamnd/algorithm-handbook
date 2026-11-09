## History

The oldest ideas in the chapter are mathematical. Giuseppe Peano described a continuous curve that fills a square in 1890, and David Hilbert gave his simpler curve a year later, both in *Mathematische Annalen*. Their use as orders on data came much later: G. M. Morton proposed interleaving the bits of coordinates in an IBM report of 1966, for a geographic file, and Orenstein and Merrett built search structures on this order in 1984.

The trees for points came in the 1970s. Raphael Finkel and Jon Bentley introduced the quad tree for records with two keys in 1974, and Bentley the k-d tree in 1975. Two years later, Friedman, Bentley and Finkel gave nearest neighbor search in logarithmic expected time, Lee and Wong proved the worst-case bound for range queries, and Bentley, Stanat and Williams analyzed the cell method of the uniform grid. In image processing, Klinger cut pictures into quadrants in the early 1970s, Hunter and Steiglitz analyzed region quadtrees in 1979, and Gargantini stored them as sorted lists of codes in 1982. Graphics brought the BSP tree, from Fuchs, Kedem and Naylor in 1980, and the octree of Meagher.

Databases needed structures on disk. Robinson's k-d-B tree of 1981 put the k-d tree into pages, and the grid file of Nievergelt, Hinterberger and Sevcik in 1984 promised two disk accesses per lookup. In the same year Antonin Guttman introduced the R-tree, with its three splits. The R+-tree followed in 1987, the R*-tree of Beckmann, Kriegel, Schneider and Seeger in 1990, the Hilbert packing and Hilbert R-tree of Kamel and Faloutsos in 1993 and 1994, and STR in 1997. Hanan Samet gathered the quadtree family in his survey of 1984 and in his books, and Gaede and Günther surveyed the access methods in 1998.

Two later lines changed the picture. For many dimensions, the SS-tree and the X-tree of 1996 and the SR-tree of 1997 tried to save the R-tree, until the VA-file paper of 1998 showed that in very high dimensions a scan of compressed vectors can beat them all. On the theory side, Arge, de Berg, Haverkort and Yi gave the priority R-tree in 2004, the first R-tree with an optimal worst-case window query. Practice moved to the globe: geohash appeared in 2008, Eric Veach's S2 library at Google was opened around 2011, and Uber's H3 grid uses hexagons on an icosahedron.

## Further reading

- Hanan Samet, *Foundations of Multidimensional and Metric Data Structures*, Morgan Kaufmann, 2006. The reference for the whole chapter, with every quadtree, grid and R-tree variant and its history.
- Volker Gaede and Oliver Günther, *Multidimensional access methods*, ACM Computing Surveys 30(2), 1998. A survey of the point and spatial access methods for databases, with a clear classification.
- Mark de Berg, Otfried Cheong, Marc van Kreveld and Mark Overmars, *Computational Geometry, Algorithms and Applications*, third edition, Springer, 2008. Chapter 5 proves the range query bound of the k-d tree, and a later chapter uses quadtrees for mesh generation.
- Christer Ericson, *Real-Time Collision Detection*, Morgan Kaufmann, 2005. Grids, hashing, octrees, BSP trees and sweep and prune, as used in games.
- Michael Bader, *Space-Filling Curves, An Introduction with Applications in Scientific Computing*, Springer, 2013. The Hilbert, Peano and Morton curves, their computation and their locality.
