## What to remember

- $f(n) = O(g(n))$ means $f(n) \le c\,g(n)$ for one constant $c > 0$ and all $n \ge n_0$. $\Omega$ is the same with $\ge$, and $\Theta$ is both. $o$ and $\omega$ require the inequality for *every* constant $c > 0$, so $f = o(g)$ exactly when $f(n)/g(n) \to 0$. The equals sign in $f = O(g)$ is one way only.
- A bound is a statement about a function, and the function must be named: worst-case or best-case time, or space, in a stated [model of computation](/random-access-machine/), as a function of a stated [input size](/input-size/). "Insertion sort is $O(n^2)$" is a claim about its worst-case time; its best-case time is $\Theta(n)$.
- A sum of a fixed number of terms has the order of its largest term. The arithmetic series $\sum_{i=1}^{n} i = n(n+1)/2$ gives $\Theta(n^2)$ for two nested loops. A geometric series with a constant ratio $r \ne 1$ is within a constant factor of its largest term, so $1 + 2 + 4 + \cdots + n = \Theta(n)$.
- The [harmonic number](/harmonic-series/) satisfies $\ln(n+1) \le H_n \le 1 + \ln n$, and [Stirling's approximation](/stirling-approximation/) $n! \sim \sqrt{2\pi n}\,(n/e)^n$ gives $\lg n! = n \lg n - n \lg e + O(\log n)$. So $\lg n! = \Theta(n \log n)$.
- The common growth rates form a ladder in which each function is $o$ of the next: $1 \prec \lg \lg n \prec \lg n \prec \lg^2 n \prec \sqrt n \prec n \prec n \lg n \prec n^2 \prec n^3 \prec 2^n \prec n! \prec n^n$. The base of a logarithm does not matter inside $O$; the base of an exponential does.
- [Polynomial time](/polynomial-time/), $O(n^k)$ for a constant $k$ with $n$ the length of the input in bits, is the formal meaning of "efficient". Trial division up to $\sqrt N$ is polynomial in $N$ but exponential in the length of $N$.
- $f \sim g$ means $f(n)/g(n) \to 1$. [Tilde notation](/tilde-notation/) keeps the leading constant and is the right tool for predictions: if $T(n) \sim a n^b$, then $T(2n)/T(n) \to 2^b$, which is the [doubling hypothesis](/doubling-hypothesis/).
- The [iterated logarithm](/iterated-logarithm/) $\lg^* n$ is at most 5 for every $n \le 2^{65536}$, and the [inverse Ackermann function](/inverse-ackermann-function/) $\alpha(n)$ is at most 4 for every $n \le 2^{2048}$. Both tend to infinity.

## The ladder in numbers

| Growth | Example | $T(2n)$ | Largest $n$ in $10^9$ steps |
|---|---|---|---|
| $1$ | read one array cell | $T(n)$ | any |
| $\lg n$ | [binary search](/binary-search/) | $T(n) + a$ | any |
| $n$ | maximum of an array | $2\,T(n)$ | $10^9$ |
| $n \lg n$ | [merge sort](/merge-sort/) | $2\,T(n)(1 + 1/\lg n)$ | 39620077 |
| $n^2$ | [insertion sort](/insertion-sort/), reversed input | $4\,T(n)$ | 31622 |
| $n^3$ | naive matrix product | $8\,T(n)$ | 1000 |
| $2^n$ | all subsets | $2^n\,T(n)$ | 29 |
| $n!$ | all orders | more than $n^n\,T(n)$ | 12 |

: The common growth rates, from [common growth rates](/common-growth-rates/). The third column assumes $T(n) = a f(n)$ exactly. The last column is the largest $n$ with $f(n) \le 10^9$, about one second at $10^9$ simple steps a second. A machine 1000 times faster multiplies the $n^2$ entry by about 31.6 but adds only about 10 to the $2^n$ entry.

## Using the notation well

- Say which case and which measure a bound is about. A worst-case bound of $O(n^2)$ is not a claim that the program is slow on every input, and a best-case bound says almost nothing about a program you will run on data you do not control.
- Prefer $\Theta$ when you know it. $O(n^3)$ is true of an algorithm that runs in $\Theta(n)$, and it misleads.
- Use $\sim$, not $\Theta$, when you want to compare two programs of the same order or predict a running time: $\Theta$ hides exactly the constant that decides the comparison.
- Check the input size before you call an algorithm polynomial. A number $N$ has about $\lg N$ bits, not $N$.
- When a bound has two parameters, such as $O(V + E)$ for a graph, say which values they can take together; [multivariate asymptotic notation](/multivariate-asymptotic-notation/) explains why this matters.
- Time the program. A measured ratio $T(2n)/T(n)$ far from the predicted $2^b$ is a sign of a bug in the program or in the analysis.
