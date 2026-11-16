1. ◦ Write `a = (b + c) * (b - d) / e` as [three-address code](/three-address-code/), first as quadruples with new temporaries and then as triples. How many quadruples and how many triples are there, and which instruction can trap?

2. ◦ The instructions below are numbered, and `br t 5 10` jumps to 5 when `t` is not zero and to 10 otherwise. Find the leaders, the [basic blocks](/basic-block/) and the edges of the [control flow graph](/control-flow-graph/). Which edge is critical, and what does the program return for $n = 7$?

```
1  i = 0
2  s = 0
3  t = i < n
4  br t 5 10
5  u = i % 3
6  br u 8 7
7  s = s + i
8  i = i + 1
9  jump 3
10 ret s
```

3. ◦ A diamond has the edges A→B, A→C, B→D, C→D and D→E, with entry A and exit E. Give the immediate dominators, the [dominance frontier](/dominance-frontier/) of each block, the immediate [post-dominators](/post-dominance/), and the [control dependences](/control-dependence/), with a node START joined to A and to E as in the control dependence entry.

4. ◦ A flow graph has entry 1 and the edges 1→2, 2→3, 3→2, 3→4, 4→1 and 4→5. Find the back edges and their [natural loops](/natural-loop/). How do the loops nest, and is the graph [reducible](/reducible-flow-graph/)?

5. ◦ Give the [def-use chains](/def-use-chains/) of this program, count the links, and say at which uses two definitions meet.

```
B1:
  x = 1
  y = 2
  br c B2 B3
B2:
  x = 3
  jump B4
B3:
  y = x + 1
  jump B4
B4:
  z = x + y
  ret z
```

6. ◦ In a program, `main` calls `f` twice and `g` once, `f` calls `g`, and `g` calls `f` and `h`; `h` calls nothing. Draw the [call graph](/call-graph/) and the call multigraph, give the [strongly connected components](/strongly-connected-components/), and give an order that visits every callee before its callers wherever recursion allows.

7. ◦ Put `(f x + g y) * h z` into [A-normal form](/a-normal-form/), evaluating from left to right. How many `let` bindings does it have?

8. ◦ In a diamond A→B, A→C, B→D, C→D, block B runs `x = 1; y = x + a` and block C runs `x = 2; y = x * a`, and D runs `ret y`. How many phi nodes do minimal, semi-pruned and [pruned SSA](/pruned-ssa-form/) place, and where?

9. ◦ Sequence the parallel copy $(a, b, x, y, z) \leftarrow (b, a, y, z, x)$ with ordinary copies and one temporary. How many copies are needed, and why can no sequence do with fewer?

10. • Run the [Cooper-Harvey-Kennedy algorithm](/cooper-harvey-kennedy-dominance/) on the graph with entry r and the edges r→a, r→b, a→c, b→c, c→b, with a depth-first search that takes the successors in the listed order. Give the reverse postorder, the guesses after each pass and the number of passes. Find the retreating edges and compare the count with the bound $d + 2$.

11. • A flow graph has entry 1, exit 7 and the edges 1→2, 2→3, 2→4, 3→5, 4→5, 4→6, 5→2, 5→7 and 6→7. Compute the immediate dominators and the dominance frontier of every block. Where does minimal SSA put phi nodes for a variable assigned in blocks 1, 3 and 6, and for one assigned in blocks 1 and 6? Which edges are critical?

12. • For the graph of exercise 11, with START joined to block 1 and to an exit node after block 7, give the immediate post-dominators and the control dependences. Which blocks depend on more than one node, and why?

13. • The graph r→A, r→B, A→B, B→A, A→C, B→C is irreducible, and no [T1-T2](/t1-t2-reduction/) step applies to it. Split B into one copy per predecessor, each with all the out-edges of B. Show that the new graph reduces to one node, list the steps, and give its size.

14. • Build the [loop nesting forest](/loop-nesting-forest/) of the graph with entry r and the edges r→A, r→B, A→B, B→A, B→C, C→D, D→C, D→A and D→E. Give the loops with their headers and parents. Which cycles do natural loops find, and which do they miss?

15. • Sequence the parallel copy $(a, b, c, d) \leftarrow (b, c, a, a)$. The procedure of the [out-of-SSA translation](/out-of-ssa-translation/) entry emits $\lvert P \rvert + c = 5$ copies. Find a sequence of 4 copies with no temporary, and say when such a saving is possible.

16. • Apply Method I of [Sreedhar's translation](/sreedhar-cssa-translation/) to the folded swap loop of the [lost-copy and swap problems](/lost-copy-and-swap-problems/) entry, with the three phi nodes `a.2`, `b.2` and `i.2` at B2. How many copies does it add? Write the code after the names of each congruence class are merged, and check that it returns 21 for $n = 1$.

17. • Compile `let a = 2 in let b = 3 in let f = fun x -> x * a + b in f 1 + f 2` three ways: by [closure conversion](/closure-conversion/) with a flat closure, by [lambda lifting](/lambda-lifting/) and by [defunctionalization](/defunctionalization/). What does each call of `f` pass, and what is the value?

18. • Lambda lift `let p = 1 in let q = 2 in letrec f n = if n < 1 then p else g (n - 1) and g n = h n + q and h n = f n in f 3`. Give $D$, $R$ and $E$ for each function, write the global functions, and evaluate the program. What goes wrong if each function takes only $D$?

19. • Translate the pruned SSA form of the odd-sum program, as built in the [Braun construction](/braun-ssa-construction/) entry, into nested block functions as in the [correspondence of SSA and CPS](/ssa-cps-correspondence/). Which block functions have parameters, which arguments does each jump pass, and which names does B5 read from an enclosing function?

20. • In the odd-sum program, replace B4 by `u = n * 2`, `v = i * u`, `w = 100 / n`, `s = s + v`, `s = s + w` and `jump B5`. In the [sea of nodes](/sea-of-nodes/), which block does the schedule give to `u`, `v` and `w`? Why must `w` stay in B4 although its input does not change in the loop?

21. • Put this program into [SSI form](/static-single-information-form/): with a parameter `a`, block A runs `x = a - 1`, `p = x > 0` and `br p B C`; B runs `y = 100 / x`; C runs `y = 0 - x`; both jump to D, which runs `z = x + y` and `ret z`. Where do sigma and phi functions go, and how many does SSA form need for the same program?

22. ★ Prove that on a reducible graph, with the vertices in reverse postorder, every guess that the Cooper-Harvey-Kennedy algorithm makes in its first pass is final, so it stops after two passes.

23. ★ For $k \ge 1$, take the vertices r, a, $v_0, \dots, v_k$ and the edges r→a, r→$v_0$, a→$v_k$, and $v_i \to v_{i+1}$ and $v_{i+1} \to v_i$ for $0 \le i < k$. The search from r visits a before $v_0$. Show that the Cooper-Harvey-Kennedy algorithm needs exactly $k + 2$ passes and that $d = k$, so the bound $d + 2$ is reached.

24. ★ A-normalize $E_1 + (E_2 + (\dots + E_k))$ where $E_j$ is `if a_j then b_j else c_j`, by copying the context into the branches. How many branches does the result have, and how many additions? Then give a form with join points, and count again.

25. ★ Prove that splitting a critical edge u→v by a new block w changes no dominance frontier of an old block, and that w lies in no dominance frontier. Conclude that minimal SSA puts its phi nodes in the same blocks before and after the split.

26. ★ Apply Method I of Sreedhar's translation to the folded lost-copy loop of the lost-copy and swap problems entry. Then merge the copies whose two names do not interfere. How many of the copies remain, and does the result return 2 for $n = 3$?
