## History

Jean-Charles de Borda read a paper on elections to the French Academy of Sciences in 1770, and his memoir appeared in 1784 in the Academy's volume for 1781. He showed that plurality voting can elect a candidate whom most voters rank last and proposed points by position. The Marquis de Condorcet, who edited the volume, objected that the rule can reject a candidate who wins every head-to-head majority, and in his essay of 1785 he described the majority cycles that now carry his name. The two ideas, scoring by position and respecting pairwise majorities, still divide voting rules.

John Kemeny proposed in 1959, in "Mathematics without numbers", to measure the distance between two rankings by the pairs on which they disagree and to take as consensus the ranking with the least total distance to the given ones. H. P. Young and A. Levenglick proved in 1978 that Kemeny's rule is the only one that is neutral, consistent and Condorcet. The rule is also the maximum likelihood estimate of the central ranking in the Mallows model.

Computation came later. John Bartholdi, Craig Tovey and Michael Trick showed in 1989 that it is NP-hard to tell who wins a Kemeny election, and Edith Hemaspaandra, Holger Spakowski and Jörg Vogel placed the winner problem exactly in $\Theta_2^p$ in 2005. Cynthia Dwork, Ravi Kumar, Moni Naor and D. Sivakumar brought rank aggregation to web metasearch in 2001, proved NP-hardness for four voters, and used the footrule to get a factor 2. Nir Ailon, Moses Charikar and Alantha Newman analysed KwikSort, Claire Kenyon-Mathieu and Warren Schudy gave a PTAS in 2007, and Don Coppersmith, Lisa Fleischer and Atri Rudra proved the factor 5 for the Borda order.

In information retrieval, Javed Aslam and Mark Montague adapted the Borda count as Borda-fuse in 2001 to merge the result lists of search systems.

## Further reading

- Felix Brandt, Vincent Conitzer, Ulle Endriss, Jérôme Lang and Ariel D. Procaccia (eds.), *Handbook of Computational Social Choice*, Cambridge University Press, 2016. The standard survey of voting rules, their axioms and their computational complexity.
- Cynthia Dwork, Ravi Kumar, Moni Naor and D. Sivakumar, *Rank Aggregation Methods for the Web*, Proceedings of the 10th International World Wide Web Conference, 2001. Kemeny aggregation, the footrule and local Kemenization for metasearch.
- Nir Ailon, Moses Charikar and Alantha Newman, *Aggregating Inconsistent Information: Ranking and Clustering*, Journal of the ACM 55(5), 2008. KwikSort and its analysis.
- H. P. Young and A. Levenglick, *A Consistent Extension of Condorcet's Election Principle*, SIAM Journal on Applied Mathematics 35(2), 1978. The axiomatic characterization of Kemeny's rule.
