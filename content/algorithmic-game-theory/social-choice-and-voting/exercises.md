1. ◦ Eleven voters rank four candidates: two vote $d \succ a \succ c \succ b$, four vote $a \succ c \succ b \succ d$ and five vote $c \succ d \succ b \succ a$. Compute the six pairwise margins. Is there a [Condorcet winner](/condorcet-winner/)? Find the [Smith set](/smith-set/).

2. ◦ For the profile of Exercise 1, find the winner under [plurality](/plurality-voting/), under the [Borda count](/borda-count/) with $4, 3, 2, 1$ points, and under [instant-runoff voting](/instant-runoff-voting/).

3. ◦ For the profile of Exercise 1, find the [Copeland](/copeland-method/) scores (wins minus losses) and run [ranked pairs](/ranked-pairs/). Which pair is skipped, and what ranking results?

4. ◦ Nine voters rank three candidates: four vote $a \succ b \succ c$, three vote $c \succ b \succ a$ and two vote $b \succ c \succ a$. Under plurality with ties broken in favour of $a$, show that the two voters of the last group can together change the winner to one they prefer, but neither can do so alone.

5. ◦ Six parties win $4700$, $1600$, $1580$, $1200$, $610$ and $310$ votes, and $10$ seats are to be filled. Compute the quotas and the seats under the [D'Hondt method](/dhondt-method/), the [Sainte-Lague method](/sainte-lague-method/) and [Hamilton's method](/hamilton-method/).

6. ◦ Four states have populations $40$, $40$, $15$ and $5$ thousand. Apportion $8$ seats and then $9$ seats by Hamilton's method. Which paradox do you see?

7. ◦ Each voter in a jury is right with probability $2/3$, independently. Compute the probability that the majority is right for $n = 3$ and $n = 5$, as the [Condorcet jury theorem](/condorcet-jury-theorem/) describes.

8. ◦ Twelve voters cast [approval ballots](/approval-voting/): five approve $\{a, b, c\}$, one approves $\{a, b\}$, one approves $\{a\}$, three approve $\{d, e\}$, one approves $\{d\}$ and one approves $\{f\}$. A committee of $k = 3$ is to be chosen. Which committee has the most approvals? Does it satisfy [justified representation](/justified-representation/)?

9. ◦ Each rule below is for two candidates. Say which conditions of [May's theorem](/may-theorem/) it fails. (a) Candidate $a$ wins unless at least two thirds of the voters prefer $b$. (b) The winner is the majority choice of all voters except voter 1, and ties among them are ties.

10. ◦ On the axis $1 \lhd 2 \lhd 3 \lhd 4 \lhd 5$, which of the rankings $32451$, $31245$, $43521$ and $25431$ are [single-peaked](/single-peaked-preferences/)? For each one that is not, name the prefix that is not an interval.

11. • Compute the [Dodgson](/dodgson-rule/) score of each candidate in the profile of Exercise 1. Who wins?

12. • Run the [Schulze method](/schulze-method/) on the profile of Exercise 1, with margins as link strengths. Give the table of strongest paths and the winner.

13. • Find the [Kemeny ranking](/kemeny-rank-aggregation/) of the profile of Exercise 1 and its total Kendall tau distance to the ballots. Then find every ranking that minimizes the number of reversed majorities, as the [Slater rule](/slater-rule/) does. Is the Kemeny ranking among them?

14. • Show that the Borda count, used as a [social welfare function](/social-welfare-function/), fails independence of irrelevant alternatives. Use the four-voter profiles $P$: $a \succ b \succ c$ twice, $b \succ c \succ a$, $c \succ b \succ a$, and $Q$: $a \succ c \succ b$ twice, $b \succ c \succ a$, $c \succ b \succ a$, with $2, 1, 0$ points.

15. • Three voters rank four candidates with Borda points $4, 3, 2, 1$. Two vote $a \succ b \succ c \succ d$ and one votes $b \succ c \succ d \succ a$. Show that one of the first two voters can make $a$ the unique winner by reporting a false ranking. Which strategy does the false ranking use, and what does the [Gibbard-Satterthwaite theorem](/gibbard-satterthwaite-theorem/) say about such examples?

16. • Run the [Huntington-Hill method](/huntington-hill-method/) on the six parties of Exercise 5. Compare the result with Sainte-Lague: which party gains a seat and which loses one, and why?

17. • Parties win $600$, $300$, $200$ and $100$ votes, and $8$ seats are filled by D'Hondt. Show that the largest party gets more than its upper quota.

18. • Prove that Hamilton's method always stays within quota, and that every divisor method is house monotone. Why does this not contradict Exercise 6?

19. • Five voters rank the candidates $u, v, w, x, z$: $x \succ w \succ z \succ u \succ v$, $w \succ x \succ z \succ u \succ v$, $z \succ u \succ w \succ v \succ x$, $v \succ u \succ z \succ w \succ x$ and $u \succ z \succ v \succ w \succ x$. Find an axis on which the profile is single-peaked, as [single-peaked recognition](/single-peaked-recognition/) does. Use the [median voter theorem](/median-voter-theorem/) to name the Condorcet winner. Then show that adding the ballot $w \succ u \succ x \succ z \succ v$ makes the profile single-peaked on no axis.

20. • Run [Phragmen's sequential method](/phragmen-sequential-method/) on the profile of Exercise 8, with ties broken alphabetically. Give the time of each candidate in each round and the committee. Does it satisfy justified representation?

21. • For the profile of Exercise 8, find the committee of size 3 chosen by [proportional approval voting](/proportional-approval-voting/), and the committee chosen by sequential PAV. Give the PAV score of each.

22. • Show that a committee $W$ satisfies justified representation if and only if no candidate is approved by at least $n/k$ voters who approve no member of $W$. Turn this into an algorithm that checks JR in time linear in the total size of the ballots.

23. ★ Prove that if a Condorcet winner exists, every Kemeny ranking puts it first.

24. ★ With Borda points $m, m - 1, \dots, 1$, show that the Borda score of a candidate $x$ is $n + \sum_{y \ne x} N(x, y)$, where $N(x, y)$ is the number of voters who prefer $x$ to $y$. Deduce that the Borda count never elects a Condorcet loser.

25. ★ Prove that the D'Hondt method always gives each party at least its lower quota $\lfloor h p_i / P \rfloor$, when no ties occur.

26. ★ On single-peaked preferences over a line, show that the median of the reported peaks and a fixed set of phantom points, as in the [generalized median voter rule](/generalized-median-voter-rule/), is strategyproof.

27. ★ Prove that if the number of voters is odd and every voter's ranking is single-peaked on the same axis, the majority relation is transitive.
