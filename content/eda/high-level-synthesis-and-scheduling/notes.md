## History

Scheduling with limits on resources is older than chip design. The forward and backward passes of the critical path method, published by Kelley and Walker in 1959, are the ASAP and ALAP schedules of high-level synthesis. Hu gave his exact scheduler for in-trees on identical processors in 1961, and Ullman showed in 1975 that scheduling unit-time tasks on a given number of processors is NP-complete. Hartmanis and Stearns built the theory of partitions with the substitution property in the early 1960s and collected it in their 1966 book, the base of every later method of FSM decomposition.

High-level synthesis as a field took shape in the 1980s. Tseng and Siewiorek published their clique partitioning heuristic for the Facet system in 1986, Kurdahi and Parker used the left-edge algorithm for registers in the REAL program in 1987, and Paulin and Knight gave force-directed scheduling in 1989. Huang, Chen, Lin and Hsu bound registers by weighted bipartite matching in 1990, and in 1991 Hwang, Lee and Hsu wrote scheduling as a 0-1 integer program in ALPS, while Camposano gave path-based scheduling for branching code. The textbooks of Gajski, Dutt, Wu and Lin in 1992 and De Micheli in 1994 brought the subject into one model.

State encoding grew alongside. De Micheli, Brayton and Sangiovanni-Vincentelli introduced symbolic minimization and face constraints in KISS in 1985, Devadas, Ma, Newton and Sangiovanni-Vincentelli built MUSTANG for multi-level logic in 1988, and Villa and Sangiovanni-Vincentelli gave NOVA in 1990. Devadas and Newton turned decomposition into factorization in 1989.

Signal processing brought its own models. Kahn defined his process networks in 1974, and Lee and Messerschmitt introduced synchronous dataflow and its static scheduling in 1987. Renfors and Neuvo proved the iteration bound of recursive filters in 1981, and Parhi and Messerschmitt reached it by unfolding in 1991. At the system level, Gupta and De Micheli with Vulcan and Ernst, Henkel and Benner with COSYMA split tasks between hardware and software in 1993, and Carloni, McMillan and Sangiovanni-Vincentelli gave the theory of latency-insensitive design in 2001.

Later tools synthesize C and C++ directly. Cong and Zhang wrote timing, chaining and latency as one system of difference constraints in the xPilot system at UCLA, presented at DAC 2006, and the LegUp system of the University of Toronto schedules the same way. Zhang and Liu extended it to loop pipelining in 2013, building on the modulo scheduling bounds of Rau from 1994, and Canis, Brown and Anderson added backtracking for recurrences in LegUp in 2014.

## Further reading

- Giovanni De Micheli, *Synthesis and Optimization of Digital Circuits*, McGraw-Hill, 1994. The standard text on scheduling, binding and state encoding, with the sequencing graph and the compatibility graphs used throughout this chapter.
- Daniel D. Gajski, Nikil D. Dutt, Allen C.-H. Wu and Steve Y.-L. Lin, *High-Level Synthesis: Introduction to Chip and System Design*, Kluwer, 1992. The book that set out the finite state machine with datapath and the steps of the synthesis flow.
- Keshab K. Parhi, *VLSI Digital Signal Processing Systems: Design and Implementation*, Wiley, 1999. Iteration bound, retiming, folding and unfolding for filters, with many worked examples.
- Jason Cong and Zhiru Zhang, "An efficient and versatile scheduling algorithm based on SDC formulation", *Proceedings of the 43rd Design Automation Conference*, 2006. A short paper that shows how far difference constraints reach in scheduling.
- Juris Hartmanis and Richard E. Stearns, *Algebraic Structure Theory of Sequential Machines*, Prentice-Hall, 1966. Partition pairs, the substitution property and the decomposition of machines, in full.
