## What to remember

- **Majorities can cycle.** With three or more candidates the [majority relation](/condorcet-paradox/) need not be transitive, so a [Condorcet winner](/condorcet-winner/), a candidate who beats every rival head to head, may not exist. When one exists, a Condorcet consistent rule elects it. [Plurality](/plurality-voting/), the [Borda count](/borda-count/) and [instant-runoff voting](/instant-runoff-voting/) are not Condorcet consistent, and on the same ballots they can elect different candidates.
- **Two candidates are easy.** By [May's theorem](/may-theorem/), simple majority is the only rule for two candidates that is decisive, anonymous, neutral and positively responsive.
- **Arrow's theorem.** With at least 3 alternatives and an unrestricted domain, every [social welfare function](/social-welfare-function/) that satisfies Pareto and independence of irrelevant alternatives is a dictatorship.
- **Gibbard-Satterthwaite.** A deterministic voting rule whose range has at least 3 candidates, defined on all strict rankings, is strategyproof only if it is a dictatorship. For some rules, such as STV, finding a manipulation is NP-hard, but only in the worst case; see the [manipulation problem](/voting-manipulation-problem/).
- **Pairwise rules.** The [Smith set](/smith-set/) is the smallest set of candidates that beats everyone outside it. [Copeland](/copeland-method/), [ranked pairs](/ranked-pairs/) and [Schulze](/schulze-method/) elect from it, so they are Condorcet consistent, and ranked pairs and Schulze are computed in $O(nm^2 + m^3)$ time for $n$ voters and $m$ candidates.
- **Consensus rankings are hard.** The [Kemeny ranking](/kemeny-rank-aggregation/) minimizes the total [Kendall tau distance](/kendall-tau-distance/) to the ballots. Finding it is NP-hard already for four ballots, and deciding a Kemeny winner, like a [Dodgson winner](/dodgson-rule/), is complete for $\Theta_2^p$. [KwikSort](/kwiksort-rank-aggregation/) is an expected 2-approximation, and $11/7$ when the best input ranking is also tried.
- **Single-peaked preferences tame majorities.** If preferences are [single-peaked](/single-peaked-preferences/) on an axis and the number of voters is odd, the median peak is the Condorcet winner. The axis is found in $O(mn)$ time, and the [generalized median rules](/generalized-median-voter-rule/) are exactly the anonymous strategyproof rules that use only the peaks.
- **Apportionment.** [Hamilton's method](/hamilton-method/) stays within quota but shows the [Alabama paradox](/alabama-paradox/). Divisor methods are house and population monotone but can leave quota. By the [Balinski-Young theorem](/balinski-young-theorem/), with five or more states no method both stays within quota and is population monotone.
- **Proportional committees.** [Justified representation](/justified-representation/) and its strengthenings PJR and EJR say that large cohesive groups of voters get representatives. [PAV](/proportional-approval-voting/) satisfies EJR but is NP-hard to compute. [Phragmen's method](/phragmen-sequential-method/) is polynomial and satisfies PJR but not EJR. The [method of equal shares](/method-of-equal-shares/) is polynomial and satisfies EJR.

## The single-winner rules side by side

| Rule | Ballot | Condorcet consistent | Time |
|---|---|---|---|
| [Plurality](/plurality-voting/) | top choice | no | $O(n + m)$ |
| [Approval](/approval-voting/) | set of candidates | no | $O(n + m + L)$ |
| [Borda](/borda-count/) | ranking | no | $O(nm + m \log m)$ |
| [Instant-runoff](/instant-runoff-voting/) | ranking | no | $O(L + m^2)$ |
| [Copeland](/copeland-method/) | ranking | yes | $O(nm^2)$ |
| [Ranked pairs](/ranked-pairs/) | ranking | yes | $O(nm^2 + m^3)$ |
| [Schulze](/schulze-method/) | ranking | yes | $O(nm^2 + m^3)$ |
| [Kemeny](/kemeny-rank-aggregation/) | ranking | yes | $O(2^m m^2 + m^2 n)$; NP-hard |
| [Slater](/slater-rule/) | ranking | yes | $O(nm^2 + 2^m m)$; NP-hard |
| [Dodgson](/dodgson-rule/) | ranking | yes | $O(m^3 n (n/2 + 2)^{m-1})$; winner $\Theta_2^p$-complete |

: Single-winner rules for $n$ voters and $m$ candidates; $L$ is the total length of the ballots. The exponential times are those of the exact algorithms in the entries. Instant-runoff voting is also not monotone, and neither is Dodgson's rule.

## Choosing a rule

- If a Condorcet winner should win whenever there is one, use ranked pairs or Schulze. Both are monotone, polynomial and pick from the Smith set.
- If the ballots must be simple, plurality and approval voting are counted in one pass. Approval ballots let a voter support several similar candidates.
- If you need a full consensus ranking, the Kemeny ranking is the principled choice. Solve it exactly for a few candidates and use KwikSort or another approximation for many.
- If preferences lie on a line, as with a budget or a position on one issue, use the median of the peaks: it is strategyproof.
- For seats in a parliament, pick a divisor method. Sainte-Lague favours neither large nor small parties on average, while D'Hondt favours large parties.
- For a committee from approval ballots, use the method of equal shares or Phragmen's method when proportionality matters, and PAV when you can afford to solve it exactly.
