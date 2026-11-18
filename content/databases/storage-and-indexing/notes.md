## History

The written entries of this chapter rest on the B+ tree, which Bayer and McCreight introduced as the B-tree in 1972 and which became the standard index of relational systems in the 1970s. The cost rules for clustered and unclustered access, and the choice between an index and a scan, are older textbook practice; the counting tool behind them is Yao's formula of 1977 for the expected number of blocks that $k$ records touch. Yao's analysis of random 2-3 trees (1978) gave the fill factor of trees built by insertion, the number that bulk loading improves on, and the sorting bound of Aggarwal and Vitter (1988) gives the cost of the sort that bulk loading starts with.

Indexes for analytic scans came from systems built for decision support. Patrick O'Neil described bitmaps of the rows of a value in Model 204, at the HPTS workshop of 1987. O'Neil and Quass (1997) compared variant indexes and introduced the bit-sliced index. Chan and Ioannidis mapped the space of bitmap encodings, equality, range and multi-component in 1998 and interval in 1999, and Wu, Otoo and Shoshani gave the WAH compression code and its analysis in 2006. Valduriez (1987) proposed the join index as a stored relation of pairs of tuple surrogates, and Moerkotte (1998) proposed small materialized aggregates, the per-block minimum and maximum now known as zone maps or block range indexes.

Choosing indexes is an old problem with a hard core. Comer (1978) proved a form of optimum index selection NP-complete. Chaudhuri and Narasayya built the AutoAdmin tool for Microsoft SQL Server in 1997 and 1998: a greedy search over candidate indexes, with costs taken from the optimizer through what-if calls. The approximation guarantee for greedy rests on the theorem of Nemhauser, Wolsey and Fisher (1978) on submodular functions.

The newest written entries move the index into the workload. Idreos, Kersten and Manegold introduced database cracking in MonetDB at CIDR 2007, and Halim, Idreos, Karras and Yap (2012) made it robust against sequential workloads with random pivots. Kraska, Beutel, Chi, Dean and Polyzotis proposed learned index structures at SIGMOD 2018, and Ferragina and Vinciguerra (2020) gave the PGM-index with worst-case bounds.

## Further reading

- Raghu Ramakrishnan and Johannes Gehrke, *Database Management Systems*, third edition, McGraw-Hill (2003). Chapters 8 to 11 cover files, tree indexes and the cost rules; Chapter 25 covers bitmap and join indexes for decision support.
- Goetz Graefe, Modern B-tree techniques, *Foundations and Trends in Databases* 3(4) (2011). A survey of B-tree practice, including bulk loading and covering indexes.
- Chee-Yong Chan and Yannis E. Ioannidis, Bitmap index design and evaluation, *Proceedings of ACM SIGMOD* (1998). The design space of bitmap encodings and its costs.
- Surajit Chaudhuri and Vivek Narasayya, An efficient, cost-driven index selection tool for Microsoft SQL Server, *Proceedings of VLDB* (1997). The candidate selection and greedy search used by physical design tools.
- Stratos Idreos, Martin L. Kersten and Stefan Manegold, Database cracking, *CIDR* (2007), and Tim Kraska et al., The case for learned index structures, *SIGMOD* (2018). The two starting points of adaptive and learned indexing.
