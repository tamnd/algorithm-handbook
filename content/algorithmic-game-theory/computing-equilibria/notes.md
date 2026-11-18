## History

Linear programming solved zero-sum games from the start: Dantzig and von Neumann saw the connection in 1947, and the simplex method computes optimal strategies. For general two-player games, C. E. Lemke and J. T. Howson gave their complementary pivoting algorithm in 1964. It was constructive, and its parity argument showed that a nondegenerate game has an odd number of equilibria. Herbert Scarf's simplicial methods later did the same kind of path following for fixed points and equilibria with more players.

The complexity question took longer. Itzhak Gilboa and Eitan Zemel showed in 1989 that many questions about equilibria with given properties are NP-complete, while correlated equilibria are found by linear programming. Finding some equilibrium did not fit NP-hardness, because a solution always exists. Nimrod Megiddo and Christos Papadimitriou described the class of total search problems in 1991, and Papadimitriou defined PPAD in 1994, with the Nash equilibrium as a motivating problem.

The answer came in 2006. Constantinos Daskalakis, Paul Goldberg and Papadimitriou proved that finding an approximate equilibrium of a game with three or more players is PPAD-complete, and Xi Chen, Xiaotie Deng and Shang-Hua Teng extended the result to two players, with the journal versions in 2009. Kousha Etessami and Mihalis Yannakakis placed exact equilibria in the class FIXP. Rahul Savani and Bernhard von Stengel built games on which every Lemke-Howson path is exponentially long.

On the approximation side, Richard Lipton, Evangelos Markakis and Aranyak Mehta (2003) showed that small supports suffice for approximate equilibria, giving a quasi-polynomial algorithm, and Aviad Rubinstein (2016) showed that, under an exponential time hypothesis for PPAD, this is essentially the best possible for constant $\varepsilon$.

## Further reading

- Noam Nisan, Tim Roughgarden, Éva Tardos and Vijay V. Vazirani (eds.), *Algorithmic Game Theory*, Cambridge University Press, 2007. Chapter 2, by Papadimitriou, explains PPAD and the complexity of Nash equilibria; Chapter 3, by von Stengel, covers support enumeration and the Lemke-Howson algorithm with care.
- Constantinos Daskalakis, Paul W. Goldberg and Christos H. Papadimitriou, *The Complexity of Computing a Nash Equilibrium*, SIAM Journal on Computing 39(1), 2009. The PPAD-completeness proof for games with three or more players.
- Xi Chen, Xiaotie Deng and Shang-Hua Teng, *Settling the Complexity of Computing Two-Player Nash Equilibria*, Journal of the ACM 56(3), 2009. The result for two players, including approximations.
- Tim Roughgarden, *Twenty Lectures on Algorithmic Game Theory*, Cambridge University Press, 2016. Lecture notes that cover the complexity of equilibria and the learning dynamics that reach correlated and coarse correlated equilibria.
