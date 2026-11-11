## What to remember

- A parallel computation has two costs. The **work** $T_1$ is the number of unit strands of its [computation DAG](/computation-dag/), and the **span** $T_\infty$ is the number of strands on its longest path. For a sequence the costs add; across a fork the work adds and the span takes the maximum.
- Every schedule on $p$ processors obeys the [work law](/work-law/) $T_p \ge T_1/p$ and the [span law](/span-law/) $T_p \ge T_\infty$. So the speedup $T_1/T_p$ is at most $p$, and at most the [parallelism](/parallelism/) $T_1/T_\infty$.
- A [greedy scheduler](/greedy-scheduling/) achieves $T_p \le (T_1 - T_\infty)/p + T_\infty$, which is within a factor $2 - 1/p$ of the best schedule. This is [Brent's theorem](/brent-theorem/) in its modern form. When the [slackness](/parallel-slackness/) $T_1/(pT_\infty)$ is at least 10, the speedup is at least 91 per cent of $p$.
- [Work stealing](/work-stealing/) gets the same bound in expectation, $\mathrm{E}[T_p] = T_1/p + O(T_\infty)$, with one deque per processor and no central queue. Its space is at most $p S_1$.
- [Work efficiency](/work-efficiency/) comes first. An algorithm whose work is $\lg n$ times the best sequential time needs more than $\lg n$ processors just to break even. The [Hillis–Steele scan](/hillis-steele-scan/) has span $\lg n$ but work $\Theta(n \log n)$; the [Blelloch scan](/blelloch-scan/) has span $2\lg n$ and work $2(n-1)$, and is the one to use.
- [Amdahl's law](/amdahls-law/) bounds the speedup of a fixed problem with parallel fraction $f$ by $1/((1-f) + f/p) < 1/(1-f)$. [Gustafson's law](/gustafsons-law/) gives the scaled speedup $p - (p-1)s$ when the problem grows with $p$ and the serial fraction $s$ of the parallel run stays fixed. Both are the span law and the work law applied to a two-phase program.
- The [PRAM](/pram-model/) variants form a chain, EREW, CREW, then CRCW under the common, arbitrary and priority rules, and the gaps are real. The OR of $n$ bits takes one step on a common CRCW PRAM and $\Theta(\log n)$ steps on a CREW PRAM.
- A [determinacy race](/determinacy-race/) is two logically parallel accesses to one location, at least one of them a write. A lock removes a data race but not a determinacy race; the SP-bags algorithm finds one, if any exists, in a single serial run.

## The measures side by side

| Measure | Definition | Bound | Good value |
|---|---|---|---|
| [Parallelism](/parallelism/) | $T_1/T_\infty$ | none | much more than $p$ |
| [Speedup](/speedup/) | $T_1/T_p$ | $\le \min(p, T_1/T_\infty)$ | close to $p$ |
| [Parallel efficiency](/parallel-efficiency/) | $T_1/(pT_p)$ | $\le 1$ | close to 1 |
| [Slackness](/parallel-slackness/) | $T_1/(pT_\infty)$ | none | at least 10 |
| Absolute speedup | $T_{\mathrm{seq}}/T_p$ | $\le pT_{\mathrm{seq}}/T_1$ | close to $p$ |
| [Amdahl bound](/amdahls-law/) | $1/((1-f) + f/p)$ | $< 1/(1-f)$ | — |
| [Scaled speedup](/gustafsons-law/) | $p - (p-1)s$ | $\le p$ | close to $p$ |

: The measures of the chapter. $T_{\mathrm{seq}}$ is the time of the best sequential algorithm, $f$ is the parallel fraction of a one-processor run, and $s$ is the serial fraction of a $p$-processor run. Absolute speedup is the only one of them that a work-inefficient algorithm cannot make look good.

## Using the measures

To analyse a new parallel algorithm, write recurrences for its work and span from the code, solve them, and compare the work with the best sequential time before anything else. If the work is too large, no number of processors will help much. If the work is right, divide it by the span: the parallelism tells you how many processors the algorithm can keep busy, and dividing by ten gives a safe number to use.

Report speedup against the best sequential program, not against the parallel program on one processor. Say whether a scaling experiment fixed the problem size or the work per processor, since a strong-scaling curve and a weak-scaling curve of the same code look very different.

When a later chapter says an algorithm "runs in $O(\log n)$ time on an EREW PRAM with $n/\log n$ processors", read it as work $O(n)$ and span $O(\log n)$. The work-time principle of the [PRAM model](/pram-model/) turns one statement into the other.
