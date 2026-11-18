## What to remember

- Give each variable a level, low (public) or high (secret). States $s$ and $t$ are low-equivalent, $s =_L t$, when they agree on every low variable. A program $P$ is noninterfering (termination-insensitive) when $s_1 =_L s_2$ and both runs stop imply $[\![P]\!](s_1) =_L [\![P]\!](s_2)$.
- The termination-sensitive form also asks that the runs from $s_1$ and $s_2$ either both stop or both run forever. $\mathbf{while}\ h > 0\ \mathbf{do}\ \mathbf{skip}$ satisfies the first form and fails the second.
- Noninterference is a 2-safety property: a violation is a pair of runs from low-equivalent states with outputs that are not low-equivalent. It is not a trace property, so no set of single runs defines it. Clarkson and Schneider call such properties hyperproperties.
- It is undecidable: $Q;\ l := h$ is noninterfering exactly when $Q$ does not stop. Its complement is recursively enumerable, because a leak can be found by trying pairs of inputs.
- The definition is semantic: $l := h;\ l := 0$ and $l := h - h$ are noninterfering. A checker that is decidable and sound must therefore reject some noninterfering programs.
- Two kinds of flow must be stopped: explicit flows that copy a secret, and implicit flows through a branch on a secret. [Taint analysis](/taint-analysis/) catches only the first.
- The definition looks at final states only. Time, power and intermediate outputs are outside it; a [timing attack](/timing-attack/) can read a secret from a noninterfering program.

## How the checks compare

| method | $l := h;\ l := 0$ | $l := h - h$ | $\mathbf{if}\ h > 0\ \mathbf{then}\ l := 1$ | sound for noninterference |
|---|---|---|---|---|
| Volpano-Irvine-Smith type system | rejects | rejects | rejects | yes |
| flow-sensitive analysis | accepts | rejects | rejects | yes |
| taint analysis | accepts if flow-sensitive | rejects | accepts | no |
| [self-composition](/self-composition/) with a complete verifier | accepts | accepts | rejects | yes |

: How four checks treat three programs, with $l$ low and $h$ high. The first two programs are noninterfering and the third leaks. Self-composition is exact, but the verifier it calls cannot decide every case.

## Choosing a check

Use a security type system when you design the language or can annotate the program: it is fast, compositional and sound, and its rejections are the price. Use a flow-sensitive analysis when variables are reused for values at different levels. Use self-composition with a program verifier when a program that the type system rejects must be shown safe, and expect to supply invariants. Treat taint analysis as a bug finder for explicit flows, not as a proof. For cryptographic code, add the running time to the outputs and check constant-time execution as well.
