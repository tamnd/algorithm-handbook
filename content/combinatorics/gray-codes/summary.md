## What to remember

- **The reflected code.** The [binary reflected Gray code](/binary-reflected-gray-code/) is $\Gamma_0 = \varepsilon$ and $\Gamma_{n+1} = 0\Gamma_n,\ 1\Gamma_n^R$. Its string of rank $k$ is $g(k) = k \oplus \lfloor k/2 \rfloor$, and it is cyclic: the last string is $10\cdots0$, one bit from the first.
- **The ruler.** Step $k$ of $\Gamma_n$ changes bit $\rho(k)$, the number of trailing zeros of $k$. The [ruler sequence](/ruler-sequence/) satisfies $R_{n+1} = R_n, n, R_n$, and around the cycle bit $j$ changes $2^{n-1-j}$ times for $j \le n-2$ and the top bit twice.
- **The inverse.** The rank of a code word is its prefix exclusive or, $b_j = a_j \oplus a_{j+1} \oplus \cdots \oplus a_{n-1}$. [Gray to binary conversion](/gray-to-binary-conversion/) takes $\Theta(n)$ steps bit by bit and $\lceil \lg w \rceil$ shift-and-xor rounds on a word, and $b_0$ is the parity of the whole word.
- **Cycles and parity.** Each step changes the weight by 1, so the two ends of a binary Gray code differ in an odd number of bits. A [cyclic Gray code](/cyclic-gray-code/) is a Hamiltonian cycle of the $n$-cube $Q_n$, which exists for every $n \ge 2$ by the [hypercube Hamiltonian cycle](/hypercube-hamiltonian-cycle/) theorem. $Q_n$ has 1, 6, 1344 and 906,545,760 such cycles for $n = 2, 3, 4, 5$.
- **Balance.** In a [balanced Gray code](/balanced-gray-code/) every transition count $c_j$ is even and $|c_j - 2^n/n| < 2$. Balanced codes exist for every $n$ (Bhat and Savage, 1996).
- **Focus pointers.** [Loopless Gray code generation](/loopless-gray-code-generation/) keeps pointers $f_0, \ldots, f_n$ and makes each step with $j \leftarrow f_0$, $f_0 \leftarrow 0$, $f_j \leftarrow f_{j+1}$, $f_{j+1} \leftarrow j+1$ and a flip of bit $j$: $O(1)$ time in the worst case, with no word operations.
- **Larger alphabets.** In the reflected [k-ary Gray code](/k-ary-gray-code/) each step moves one digit by $\pm 1$. Under that rule a cyclic code exists for even $k$ and $n \ge 2$, and never for odd $k$. The modular code, digit $j$ equal to $(b_j - b_{j+1}) \bmod k$, is cyclic for every $k$ if a digit may wrap from $k-1$ to 0.
- **Combinations.** The rules for a step, from weak to strong, are a transposition, a homogeneous move $10^p \leftrightarrow 0^p1$, a near-perfect move $01 \leftrightarrow 10$ or $001 \leftrightarrow 100$, and an adjacent move $01 \leftrightarrow 10$. The [revolving door order](/revolving-door-ordering/) meets the first, the [Eades-McKay order](/eades-mckay-algorithm/) the second, and [Chase's sequence](/chase-sequence/) the third. The adjacent rule can be met only when $k \le 1$, $n - k \le 1$, or $k$ and $n - k$ are both odd.

## The methods side by side

| Method | Objects | Change per step | Amortized time per step | Worst step | Extra space |
|---|---|---|---|---|---|
| [Reflection](/binary-reflected-gray-code/), whole list | $\{0,1\}^n$ | one bit | $\Theta(1)$ | $\Theta(1)$ per append | $\Theta(2^n)$ |
| Parity rule (Knuth's Algorithm G) | $\{0,1\}^n$ | one bit | $O(1)$ | $O(n)$ | $O(n)$ |
| [Focus pointers](/loopless-gray-code-generation/) | $\{0,1\}^n$ | one bit | $\Theta(1)$ | $O(1)$ | $\Theta(n)$ |
| [Binary to Gray](/binary-to-gray-conversion/) for each rank | $\{0,1\}^n$, random access | the whole word | $\Theta(1)$ | $\Theta(1)$ | $\Theta(1)$ |
| [Reflected k-ary code](/k-ary-gray-code/) with focus pointers | mixed radix strings | one digit by $\pm 1$ | $\Theta(1)$ | $O(1)$ | $\Theta(n)$ |
| [Revolving door](/revolving-door-ordering/), recursive | $k$-subsets | one element out, one in | $\Theta(1)$ | $\Theta(n)$ | $\Theta(n)$ |
| [Chase's sequence](/chase-sequence/) | $k$-subsets | a 1 moves one or two places | $\Theta(1)$ | $\Theta(n)$ | $\Theta(n)$ |
| [Eades-McKay](/eades-mckay-algorithm/) | $k$-subsets | a 1 moves across 0s only | $\Theta(1)$ | $\Theta(n)$ | $\Theta(n)$ |

: Generators of Gray codes, with times on the word RAM in the visit model, where the visit itself is free. Each generator also spends $\Theta(n)$ time to start, so the generators of $k$-subsets take $\Theta(n + N)$ in total for $N = \binom{n}{k}$.

## Choosing a method

- When $n$ fits in a word, keep a counter $k$ and flip bit $\rho(k)$ with a [trailing zero count](/trailing-zero-count/), or use the parity rule. Both are short and CAT.
- When each step must take bounded time, or $n$ is larger than a word, use the focus pointers.
- When you need the string of a given rank, or the rank of a given string, use $g(k) = k \oplus \lfloor k/2 \rfloor$ and the prefix exclusive or.
- When each bit drives a physical part and wear matters, use a balanced code and accept that its rank function is not simple.
- When the digits run over more than two values, use the reflected k-ary code if a digit may change only by $\pm 1$, and the modular code if the list must close into a ring for odd $k$.
- For $k$-subsets, use the revolving door order when any swap is cheap, since it has a closed rank formula and a loopless form in [Ehrlich's loopless combination generation](/ehrlich-loopless-combinations/). Use Chase's sequence when the moved 1 must stay within two places; it is then also homogeneous. The Eades-McKay order is only homogeneous, but it runs from $0^s1^t$ to $1^t0^s$ and comes from a three-part recursion that is easy to check.
