## History

The storage layer took its form in the relational systems of the 1970s. Slotted pages, heap files and record ids of the form (page, slot) were standard by the time Gray and Reuter wrote them down in 1993. Stonebraker (1981) explained why a database should manage its own buffer pool, and Effelsberg and Haerder (1984) surveyed its design. Chou and DeWitt (1985) proposed DBMIN, with locality sets sized by the reference pattern of each file; O'Neil, O'Neil and Weikum (1993) gave LRU-K. Gray and Putzolu stated the five-minute rule in 1987, and Gray and Graefe (1997) and Graefe (2007) redid the arithmetic for later prices and for flash.

Copeland and Khoshafian proposed the decomposition storage model in 1985; MonetDB and C-Store built column stores on it a decade and more later. Ailamaki, DeWitt, Hill and Skounakis introduced PAX in 2001. Goldstein, Ramakrishnan and Shaft (1998) compressed blocks by frame of reference, and Abadi, Madden and Ferreira (2006) and Abadi, Myers, DeWitt and Madden (2007) showed how a column store runs on compressed data and when to build rows late. Abadi, Boncz, Harizopoulos, Idreos and Madden surveyed these designs in 2013.

The tree entries rest on the B-tree of Bayer and McCreight (1972). Bayer and Unterauer (1977) gave the prefix B-tree. Yao's formula of 1977 counts the blocks that $k$ records touch, and his analysis of random 2-3 trees (1978) gave the fill factor that bulk loading improves on. Hellerstein, Naughton and Pfeffer (1995) generalized the search tree as the GiST, and Levandoski, Lomet and Sengupta (2013) built the latch-free Bw-tree on the B-link tree of Lehman and Yao (1981).

Indexes for analytic scans came from systems for decision support. O'Neil described bitmaps in Model 204 in 1987, and O'Neil and Quass (1997) introduced the bit-sliced index. Chan and Ioannidis mapped bitmap encodings in 1998 and 1999, and Wu, Otoo and Shoshani gave WAH in 2002, with its analysis in 2006. Valduriez (1987) proposed the join index, and Moerkotte (1998) proposed the per-block minimum and maximum now called zone maps.

Comer (1978) proved a form of index selection NP-complete. Chaudhuri and Narasayya built AutoAdmin for Microsoft SQL Server in 1997 and added what-if calls in 1998; the guarantee for greedy rests on Nemhauser, Wolsey and Fisher (1978). Idreos, Kersten and Manegold introduced database cracking in 2007 and Graefe and Kuno adaptive merging in 2010. Kraska, Beutel, Chi, Dean and Polyzotis proposed learned indexes in 2018; Ferragina and Vinciguerra (2020) gave the PGM-index with worst-case bounds, and Ding and coauthors (2020) gave ALEX.

## Further reading

- Raghu Ramakrishnan and Johannes Gehrke, *Database Management Systems*, third edition, McGraw-Hill (2003). Chapters 8 to 11 cover files, tree indexes and the cost rules; Chapter 25 covers bitmap and join indexes.
- Jim Gray and Andreas Reuter, *Transaction Processing: Concepts and Techniques*, Morgan Kaufmann (1993). Pages, files, record ids and the buffer manager as built in practice.
- Goetz Graefe, Modern B-tree techniques, *Foundations and Trends in Databases* 3(4) (2011). A survey of B-tree practice, including prefix truncation, bulk loading and covering indexes.
- Daniel Abadi, Peter Boncz, Stavros Harizopoulos, Stratos Idreos and Samuel Madden, The design and implementation of modern column-oriented database systems, *Foundations and Trends in Databases* 5(3) (2013). Layouts, compression and late materialization.
- Chee-Yong Chan and Yannis E. Ioannidis, Bitmap index design and evaluation, *Proceedings of ACM SIGMOD* (1998). The design space of bitmap encodings.
- Stratos Idreos, Martin L. Kersten and Stefan Manegold, Database cracking, *CIDR* (2007), and Tim Kraska et al., The case for learned index structures, *SIGMOD* (2018). The two starting points of adaptive and learned indexing.
