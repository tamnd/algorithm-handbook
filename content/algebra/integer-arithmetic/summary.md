## What to remember

- A big integer is a sign and an array of $n$ limbs, its digits in the radix $\beta = 2^w$. Addition, subtraction and comparison take $\Theta(n)$ limb operations.
- **Multiplication sets the price of everything.** Write $M(n)$ for the cost of multiplying two $n$-limb numbers. Division, square roots and $k$-th roots for fixed $k$ cost $O(M(n))$; radix conversion costs $O(M(n) \log n)$.
- **Fewer products, more additions.** [Karatsuba multiplication](/karatsuba-multiplication/) gets the middle term of a product of halves from one product, $(a_0 + a_1)(b_0 + b_1) - a_0b_0 - a_1b_1$, so $M(n) = 3M(n/2) + O(n) = \Theta(n^{\log_2 3})$. [Toom-Cook](/toom-cook-multiplication/) with $k$ pieces gives $\Theta(n^{\log_k (2k-1)})$.
- **The FFT methods** treat a product as a convolution. [Schönhage-Strassen](/schonhage-strassen-multiplication/) reaches $O(N \log N \log \log N)$ bit operations, and [Harvey and van der Hoeven](/harvey-van-der-hoeven-multiplication/) reach $O(N \log N)$. No lower bound above $\Omega(N)$ is proved.
- **Division is as fast as multiplication.** [Newton-Raphson division](/newton-raphson-division/) doubles the number of correct digits of $1/D$ at each step, so a reciprocal costs a constant number of full-size products. Below that range, [long division](/long-division/) with a normalized divisor guesses each quotient digit with an error of at most 2.
- **A divisor known in advance is a multiplier.** If $M = \lceil 2^{w+s}/d \rceil$ and $Md - 2^{w+s} \le 2^s$, then $\lfloor n/d \rfloor = \lfloor Mn / 2^{w+s} \rfloor$ for all $0 \le n < 2^w$.
- **Powers by squaring.** $x^e$ takes about $\log_2 e$ multiplications by the binary method, and an [addition chain](/addition-chain/) is a plan for fewer. The bit cost is $O(M(eN))$, about one product of the size of the answer. [Fast doubling](/fibonacci-fast-doubling/) computes $F_n$ the same way.
- **In hardware, depth is the cost.** A ripple-carry adder has depth $\Theta(n)$; lookahead and prefix adders reach $\Theta(\log n)$ with $O(n)$ to $O(n \log n)$ cells. [Carry-save addition](/carry-save-addition/) turns three numbers into two in constant depth, which is why tree multipliers have depth $\Theta(\log n)$.

## The main methods side by side

| Method | Operation | Cost | Extra space |
|---|---|---|---|
| [Schoolbook](/schoolbook-multiplication/) | $m \times n$ limbs | $\Theta(mn)$ | $\Theta(m + n)$ |
| [Karatsuba](/karatsuba-multiplication/) | $n \times n$ limbs | $\Theta(n^{\log_2 3}) \approx n^{1.585}$ | $\Theta(n)$ |
| [Toom-3](/toom-cook-multiplication/) | $n \times n$ limbs | $\Theta(n^{\log_3 5}) \approx n^{1.465}$ | $\Theta(n)$ |
| [Schönhage-Strassen](/schonhage-strassen-multiplication/) | $N \times N$ bits | $O(N \log N \log \log N)$ | $O(N)$ |
| [Harvey-van der Hoeven](/harvey-van-der-hoeven-multiplication/) | $N \times N$ bits | $O(N \log N)$ | — |
| [Long division](/long-division/) | $(m + n)$ by $n$ limbs | $\Theta(n(m + 1))$ | $\Theta(m + n)$ |
| [Burnikel-Ziegler](/burnikel-ziegler-division/) | $2n$ by $n$ limbs | $O(M(n) \log n)$ | $O(n \log n)$ |
| [Newton-Raphson division](/newton-raphson-division/) | $2n$ by $n$ limbs | $O(M(n))$ | $O(n)$ |
| [Radix conversion](/radix-conversion/), divide and conquer | $n$ limbs | $O(M(n) \log n)$ | — |

: The main software methods. Costs are in limb operations on the word RAM, except for the FFT methods, whose costs are in bit operations on a multitape Turing machine. With Karatsuba products, Burnikel-Ziegler costs about twice a multiplication.

| Adder | Depth | Size |
|---|---|---|
| [Ripple-carry](/ripple-carry-adder/) | $2n + 1$ gates | $5n$ gates |
| [Carry-select](/carry-select-adder/) | $\Theta(\sqrt n)$ | $\Theta(n)$ |
| [Carry-lookahead](/carry-lookahead-adder/), blocks of 4 | $\Theta(\log n)$ | $\Theta(n)$ |
| [Brent-Kung](/brent-kung-adder/), $n = 2^L$ | $2L - 1$ prefix levels | $2n - 2 - L$ prefix cells |
| [Sklansky](/sklansky-adder/) | $\lceil \log_2 n \rceil$ prefix levels | about $\frac{n}{2} \log_2 n$ cells, fan-out up to $n/2$ |
| [Kogge-Stone](/kogge-stone-adder/) | $\lceil \log_2 n \rceil$ prefix levels | about $n \log_2 n$ cells, fan-out 2 |

: Adders for $n$-bit words. The [carry-skip adder](/carry-skip-adder/) is left out: its depth is $\Theta(n)$, but no input makes the long path slow, and its delay is $\Theta(\sqrt n)$.

## Choosing a method

Use the big integers of your language or of GMP unless you have measured a reason not to; they switch methods at thresholds tuned for each machine. If you write your own:

- Below a few dozen limbs, the schoolbook method and long division are fastest. Add Karatsuba above that, and Toom-3 above a few hundred limbs; FFT multiplication pays only for much larger numbers.
- Divide by Newton's method only when multiplication is already subquadratic; with schoolbook products, long division is as fast and simpler.
- For a divisor fixed at compile time or used many times, precompute its reciprocal ([Granlund-Montgomery division](/granlund-montgomery-division/)).
- Never take an integer root through floating point; use [integer Newton steps](/newton-integer-root/).
- For modular powers with a public exponent, use [sliding windows](/sliding-window-exponentiation/). With a secret exponent, use a fixed window, so that the sequence of operations does not depend on the exponent.
