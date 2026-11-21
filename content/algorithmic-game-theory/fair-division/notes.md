## History

Fair division became a mathematical problem with Hugo Steinhaus, who asked how to divide a cake among $n$
people so that each gets at least $1/n$. In "The problem of fair division" (1948) he gave an answer that he
credited to Stefan Banach and Bronisław Knaster: the method now called the last diminisher.
Dubins and Spanier gave the moving knife version in "How to cut a cake fairly" (1961), and Even and Paz
showed in 1984 that halving the group at a median mark needs only $O(n \log n)$ queries. The query model
is named after Robertson and Webb, whose book on cake cutting appeared in 1998, and Edmonds and Pruhs
proved in 2006 that Even-Paz is optimal.

Envy-freeness was introduced by Foley in 1967 as a criterion for economic allocations. For three agents,
Selfridge found a discrete envy-free protocol around 1960, and Conway found it independently; it was not
published by either of them and appears in the book of Brams and Taylor. Stromquist gave his moving knife
procedure for connected pieces in 1980 and proved in 2008 that no finite protocol can do the same. Brams
and Taylor published the first finite envy-free protocol for any number of agents in 1995, and Aziz and
Mackenzie gave the first bounded one, for four agents at STOC 2016 and for any number at FOCS 2016. Su
brought Sperner's lemma to rent division in "Rental harmony" (1999).

The study of indivisible goods grew with computer science. Lipton, Markakis, Mossel and Saberi showed in
2004 that envy-cycle elimination gives allocations in which envy is bounded by one good. Budish introduced
the maximin share in 2011, and Kurokawa, Procaccia and Wang showed that it cannot always be guaranteed,
while a $2/3$ fraction can; later work pushed the fraction past $3/4$. Caragiannis, Kurokawa, Moulin,
Procaccia, Shah and Wang showed at EC 2016 that maximum Nash welfare is EF1 and Pareto optimal, and they
defined the stronger notion EFX. Barman, Krishnamurthy and Vaish gave a pseudo-polynomial algorithm for EF1
and Pareto optimality at EC 2018. Chaudhury, Garg and Mehlhorn proved that EFX allocations exist for three
additive agents (EC 2020); the case of four agents remains open.

The topological side has an older root. Hobby and Rice proved in 1965 the theorem that gives consensus
halving, Goldberg and West the necklace theorem for two thieves in 1985, and Alon the case of any number of
thieves in 1987. Simmons and Su turned consensus halving into an algorithm in 2003, and Filos-Ratsikas and
Goldberg showed that the approximate problem is PPA-complete (STOC 2018), and that necklace splitting for
two thieves is too (STOC 2019).

## Further reading

- Steven J. Brams and Alan D. Taylor, *Fair Division: From Cake-Cutting to Dispute Resolution* (1996). The
  standard account of the classical protocols, including Selfridge-Conway and adjusted winner.
- Jack Robertson and William Webb, *Cake-Cutting Algorithms: Be Fair If You Can* (1998). Sets out the query
  model and proves the classical bounds in it.
- Felix Brandt, Vincent Conitzer, Ulle Endriss, Jérôme Lang and Ariel D. Procaccia (eds.), *Handbook of
  Computational Social Choice* (2016). Its chapters on cake cutting and on indivisible goods survey the
  algorithmic results up to that time.
- Francis Edward Su, "Rental harmony: Sperner's lemma in fair division", *American Mathematical Monthly*
  106 (1999). A readable introduction to the topological methods, with rent, cake and chores.
- Jeff Edmonds and Kirk Pruhs, "Cake cutting really is not a piece of cake", *ACM Transactions on
  Algorithms* 7 (2011). The lower bound for proportional division, with the adversary in full.
