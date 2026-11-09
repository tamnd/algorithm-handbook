## History

Recurrences are much older than algorithms. Leonardo of Pisa posed the rabbit problem whose answer is the Fibonacci sequence in his *Liber Abaci* of 1202. Abraham de Moivre solved linear recurrences with constant coefficients in the 1720s by the method now called generating functions, and the closed form $F_n = (\varphi^n - \psi^n)/\sqrt5$ was known to him and to Daniel Bernoulli; Jacques Binet published it in 1843, and it carries his name. Giovanni Domenico Cassini found the identity $F_{n-1}F_{n+1} - F_n^2 = (-1)^n$ in 1680. Gabriel Lamé used the Fibonacci numbers in 1844 to bound the number of steps of the Euclidean algorithm, one of the first analyses of an algorithm.

The divide-and-conquer recurrence came with the algorithms that produce it: merge sort in the 1940s, Karatsuba's multiplication in 1962 and Strassen's matrix product in 1969. Jon Bentley, Dorothea Haken and James Saxe published a general method for solving such recurrences in 1980 in *SIGACT News*, and the textbook of Cormen, Leiserson and Rivest (1990) gave it the form of the master theorem with three cases that is taught today. The fourth edition of that book (2022) states the second case with a factor $\lg^k n$ and introduced the name watershed function.

The master theorem does not cover subproblems of different sizes. Mohamad Akra and Louay Bazzi solved that case in a paper published in 1998, and Tom Leighton's notes of 1996 gave a short inductive proof of a slightly more general form. Salvador Roura's paper of 2001 in the *Journal of the ACM* gave master theorems with exact leading constants, among them the continuous master theorem for recurrences that sum over all smaller sizes, as in quicksort. The smoothness rule, which justifies solving for powers of 2 only, is stated in this form in the textbook of Gilles Brassard and Paul Bratley.

## Further reading

- Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest and Clifford Stein, *Introduction to Algorithms*, fourth edition (2022). Chapter 4 covers the substitution and recursion-tree methods, the master theorem with its proof, and Akra-Bazzi recurrences.
- Ronald L. Graham, Donald E. Knuth and Oren Patashnik, *Concrete Mathematics*, second edition (1994). Chapter 1 on recurrent problems, Chapter 2 on summation factors and Chapter 6 on Fibonacci numbers, with many exercises.
- Robert Sedgewick and Philippe Flajolet, *An Introduction to the Analysis of Algorithms*, second edition (2013). Chapter 2 treats recurrences, including the exact solution of divide-and-conquer recurrences on binary numbers.
- Gilles Brassard and Paul Bratley, *Fundamentals of Algorithmics* (1996). Chapters 3 and 4 state the smoothness rule and solve recurrences by the characteristic equation.
- Salvador Roura, "Improved master theorems for divide-and-conquer recurrences", *Journal of the ACM* 48(2) (2001). The master theorems with exact constants, with the analyses of quicksort, quickselect and quadtrees as examples.
