1. ◦ A test bend of a strip with $t = 1.5$ mm through 90 degrees on a tool with inside radius $R = 2$ mm leaves flat flanges of $a = 30$ mm and $b = 20$ mm from a blank of $53.9$ mm. Find the bend allowance and the [K-factor](/k-factor/). Then find the K-factor that DIN 6935 gives for this ratio $r/s$, and the blank it predicts.

2. ◦ A drawing shows a bend with an included angle of 135 degrees, in sheet with $t = 1$ mm, $R = 1$ mm and $K = 0.4$, with outer dimensions $A = 40$ mm and $B = 20$ mm to the mold point. Find the bend angle $\theta$, the [bend allowance](/bend-allowance/), the outside setback, the bend deduction and the blank. What blank results if someone reads 135 degrees as the bend angle?

3. ◦ Show that a cube of side $a$, a sphere of diameter $a$ and a cylinder of diameter $a$ and height $a$, each cooling on its whole surface, have the same modulus. What does [Chvorinov's rule](/chvorinov-rule/) say about their freezing times?

4. ◦ A steel bar of $40 \times 40 \times 400$ mm is cast in a mold with $B = 2$ min/cm$^2$ and $n = 2$. Find its modulus with all faces cooling and its freezing time. What does the long-bar modulus $a/4$ give?

5. ◦ A tool follows [Taylor's law](/taylor-tool-life-equation/) with $n = 0.25$ and $C = 400$ m/min. Find the tool life at 200 m/min and the speed that gives a tool life of 60 min. For a tool with $n = 0.2$, by what percentage must the speed fall to double the tool life?

6. ◦ A tool has $n = 0.2$, the tool change takes $t_c = 3$ min, an edge costs $C_t = 8$ dollars, and the machine costs $C_o = 2$ dollars per minute. Find the tool life of least cost and the tool life of least time. Why must the first be the larger?

7. ◦ A turning tool with nose radius $r = 0.4$ mm must leave a peak-to-valley height of at most $4\ \mu$m. Find the largest feed by the approximation $f^2/(8r)$ and by the exact height of the arc, as in [cutting parameter optimization](/cutting-parameter-optimization/).

8. ◦ In a [3-2-1 layout](/three-two-one-locating-principle/) the two secondary locators are 80 mm apart, and one of them stands out of its plane by $0.02$ mm. By what angle does the part turn, and how far does a point 300 mm from the axis of that turn move?

9. ◦ A sheet metal part has 12 bends. Compare the number of bend orders with the number of sets of done bends that a [bend sequence](/bend-sequence-planning/) search must visit. Why is the set enough as a state?

10. ◦ A closed cubical box with all six faces is folded from one flat blank, as in [flat pattern development](/flat-pattern-development/). What graph is its face graph? How many of its 12 edges can be bends, and how many must be cut?

11. • A tray has a base of outer size $100 \times 60$ mm and four walls of outer height 20 mm, with open corners, in sheet with $t = 1$ mm, $R = 1$ mm and $K = 0.4$, all bends of 90 degrees. Find the bend allowance and bend deduction, the size of the blank, the flat sizes of the base and the walls, and the size of the squares cut away at the four corners when each bend zone is kept whole.

12. • Sheet with $t = 2$ mm and $Y/E = 0.0025$ is bent to 90 degrees on a tool whose neutral radius is 100 mm. Use the elastic-perfectly plastic model of [springback compensation](/springback-compensation/) to find $x$, the radius and the angle after release. What is the largest tool radius that leaves any permanent bend in this sheet?

13. • Use the cost model and the tool of the Taylor entry ($n = 0.25$, $C = 397$ m/min, $t_c = 2$ min, $C_t = 5$ dollars, $C_o = 1$ dollar per min, $K = 301.6$ m). The machine cannot cut faster than 160 m/min. Show that the best speed is then 160 m/min, and give the cost per part and the tool life there.

14. • Two test cubes of 50 mm and 100 mm freeze in 3.0 min and 11.0 min in the same mold. Fit $n$ and $B$ in Chvorinov's rule, with the modulus in cm. Predict the freezing time of a 150 mm cube, and compare it with the prediction from the small cube alone with $n = 2$.

15. • Size a cylindrical top riser with $H = D$ for a steel plate of $250 \times 250 \times 40$ mm by the [modulus method](/riser-design-modulus-method/). Start with all faces of the plate cooling, then leave the contact face out and iterate. Then check the volume with shrinkage $\beta = 0.03$ and riser efficiency $\varepsilon = 0.15$, and give the neck modulus by the proportion $1 : 1.1 : 1.2$.

16. • A wide plate 20 mm thick and a long square bar of $20 \times 20$ mm are cast of the same metal in the same mold. Give for each the largest distance from metal to mold, which a [hot spot](/casting-hot-spot-detection/) search ranks by, and the modulus. What ratio of freezing times does Chvorinov's rule with $n = 2$ give, and what does this say about the distance proxy?

17. • Five features have these sets of access directions: $f_1$: $\{+z\}$, $f_2$: $\{+z, +x\}$, $f_3$: $\{+x, -y\}$, $f_4$: $\{-y\}$, $f_5$: $\{+z, -y\}$. Find the fewest setups for [setup planning](/setup-planning/). Then a tight tolerance between $f_2$ and $f_3$ requires them in one setup. How many setups are needed now?

18. • Give a setup planning instance, with features and their access directions among the six axis directions, on which [greedy set cover](/greedy-set-cover/) uses 3 setups and 2 suffice.

19. • Eight operations form three chains of 3, 3 and 2 operations, with no precedence between chains. How many orders respect the precedence? How many states does the dynamic program over downsets of [operation sequencing](/operation-sequencing/) have? Compare both with $8!$.

20. • In [cutting sequence planning](/cutting-sequence-planning/) with a fixed order of contours, show by an example with two contours that taking at each step the pierce point nearest to the head can be worse than the best choice. How does a shortest path find the best choice?

21. • A unit square $[0,1]^2$ has four frictionless contacts: at $(\tfrac14, 0)$ pushing in $+y$, at $(1, \tfrac14)$ pushing in $-x$, at $(\tfrac34, 1)$ pushing in $-y$, and at $(0, \tfrac34)$ pushing in $+x$. Show with the planar test of the [modular fixture](/modular-fixture-design/) entry that they do not give form closure, and find a motion that frees the part. Then move the last contact to $(0, \tfrac18)$ and show that the four contacts give form closure.

22. • A long thin strip cavity of length $L$ fills along its length from its gates, and the flow length of a point is its distance to the nearest gate. Where should one gate go? Where should two gates go, and what is the longest flow then? Run the greedy 2-approximation of [gate location](/gate-location-optimization/) by [k-center](/gonzalez-k-center/) from one end, and compare.

23. • Find the [parting lines](/parting-line-generation/) of the unit cube $[0,1]^3$ for $d = (1, 1, 1)$, and for $d = (1, 1, 0)$ with vertical faces sent to the lower side and then to the upper side. For each, give the number of loops and of edges, and say whether a loop is planar.

24. ★ Use the matrix-tree theorem to show that the face graph of the cube has 384 spanning trees, so a closed cubical box has 384 choices of 7 cut edges. Show that the cut edges always form a spanning tree of the graph of the cube's vertices and edges. Under the 48 symmetries of the cube the 384 trees fall into 11 classes, the 11 nets of the cube. Check this count by Burnside's lemma or by a program.

25. ★ In the model of [A* bend sequencing](/a-star-bend-sequencing/), call a tool forced for the bends left $R$ if it is the only tool that fits some bend of $R$, and let $F(R)$ be the set of forced tools. Let $\psi'(u) = \lvert F(R) \setminus \{\tau\} \rvert$ when the last tool $\tau$ is a tool, and $\max(\lvert F(R) \rvert - 1, 0)$ at the start. Show that $\textit{change} \cdot \psi'$ is consistent, and that $\textit{flip} \cdot \varphi + \textit{change} \cdot \max(\psi, \psi')$ is consistent too.

26. ★ In the model of the [Brost-Goldberg algorithm](/modular-fixture-design/), show that turning a fixture by 90 degrees about a lattice point gives a fixture. Show that if the part has no rotational symmetry of order 2 or 4, the four turns of a fixture are four different fixtures after the move that puts the first locator at the origin. What does this say about the 56 fixtures of the triangle in the entry's example?

27. ★ A steel cube casting of side 120 mm is to be fed by a cylindrical top riser with $H = D$ standing with its whole base on the top face. With the contact face left out of the casting's cooling area, show that no such riser meets $M_r \ge 1.2\, M_c$. Does a riser with $H = 2D$ fit? What can the designer do instead?

28. ★ The extended Taylor law $V T^n f^a = C'$ with $0 < a < 1$ adds the feed $f$, at a fixed depth. For one turning pass with the cost model of the Taylor entry, show that the tool life of least cost at a fixed feed is Gilbert's $T_{\text{cost}}$ and does not depend on $f$. Then show that at this tool life the cost per part falls as $f$ grows, so without other limits the cheapest feed is the largest one allowed, for example by the finish of exercise 7.
