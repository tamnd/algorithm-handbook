1. ◦ A [decision tree](/decision-tree-model/) sorts every input of 4 distinct keys. How many leaves must it have at least, and what is the least height it can have?

2. ◦ In the [external memory model](/external-memory-model/) take $N = 10^9$ items, a memory of $M = 10^6$ items and blocks of $B = 100$ items. (a) How many block transfers does one scan of the data take? (b) How many sorted runs of size $M$ does the first pass of a multiway merge sort produce, and how many merge passes follow if each merge reads $M/B - 1$ runs at once? (c) About how many transfers does a binary search in a sorted array of $N$ items take, and how many does a search in a B-tree with nodes of one block take?

3. ◦ An array of $2^{20}$ items of 8 bytes each is read once, and the [memory hierarchy](/memory-hierarchy/) moves data in lines of 64 bytes. The cache starts empty and is much smaller than the array. About how many cache misses does a sequential scan cause, and about how many does a scan in a random order cause?

4. ◦ In the [lambda calculus](/lambda-calculus/), reduce $(\lambda x.\,x\,x)(\lambda y.\,y)$ to normal form. Then let $\Omega = (\lambda x.\,x\,x)(\lambda x.\,x\,x)$ and consider $(\lambda x.\,y)\,\Omega$. Does it have a normal form, and does every order of reduction reach it?

5. ◦ A one-dimensional [cellular automaton](/cellular-automaton/) runs Rule 110 on an infinite row of 0s with a single 1. Write the rows after one, two and three steps, giving only the part between the leftmost and the rightmost 1.

6. ◦ A [nondeterministic Turing machine](/nondeterministic-turing-machine/) has at most two choices in each step and halts within $t$ steps on every branch. At most how many computation paths does it have? How much time does a deterministic machine need if it tries the paths one after another, each from the start?

7. ◦ A [probabilistic Turing machine](/probabilistic-turing-machine/) for a language in RP accepts each string not in the language with probability 0 and each string in it with probability at least $1/2$. (a) How many independent runs, accepting if any run accepts, bring the error below $10^{-9}$? (b) A machine with two-sided error answers wrongly with probability $1/3$ on every input. What is the error of the majority answer of three independent runs?

8. ◦ A [word RAM](/word-ram/) has words of $w = 32$ bits. What is the largest input size $n$ the model allows, and why does the model require $w \ge \lg n$?

9. ◦ A program adds $n$ integers, each between 1 and $n$, into one total. What is its running time under the [unit-cost model](/unit-cost-model/), and what is a bound under the [logarithmic-cost model](/logarithmic-cost-model/)?

10. ◦ Build a [Boolean circuit](/boolean-circuit/) with AND and OR gates of fan-in 2 that outputs the majority of three bits $a$, $b$, $c$, using 4 gates. What is its depth?

11. • A program computes $3^n$ by starting from 1 and multiplying by 3 $n$ times. How many bits does the result have? What is the running time under the unit-cost model and under the logarithmic-cost model, if multiplying $x$ by 3 costs $\Theta(\lg x)$?

12. • A [register machine](/register-machine/) has the instructions `INC r`, `DEC r` (which leaves 0 at 0), `JZ r j` (jump to line $j$ if register $r$ is 0) and `JMP j`. Write programs that (a) add $R_1$ to $R_2$, leaving the sum in $R_2$, and (b) put $\lfloor R_1/2 \rfloor$ into $R_2$, starting from $R_2 = 0$. How many steps does each take when $R_1 = x$, and why is this exponential in the length of the input?

13. • A one-tape [Turing machine](/turing-machine/) adds 1 to a binary number of $n$ bits written with the least significant bit in the leftmost cell, with the head on that cell at the start. Describe the machine and give its worst-case number of steps. What goes wrong if the number is written with the most significant bit first and every bit is 1?

14. • With Church numerals $c_n = \lambda f\,x.\,f^n\,x$ and $\mathrm{ADD} = \lambda m\,n\,f\,x.\,m\,f\,(n\,f\,x)$, reduce $\mathrm{ADD}\;c_2\;c_1$ to $c_3$, showing each beta step.

15. • Element distinctness on $n$ real numbers needs $\Omega(n \log n)$ steps in the algebraic decision tree model. Show how to decide element distinctness in $O(n)$ time on a word RAM when the inputs are integers in $[0, n^2)$, and say which step of your algorithm has no counterpart in a decision tree.

16. • On a word RAM with $w = 64$, compute the number of 1 bits in a word with $O(\log w)$ word operations, using shifts, masks, additions and ANDs. Give the masks for the first two rounds.

17. • For a word $x \ne 0$ in two's complement, show that $x \mathbin{\&} (-x)$ is the lowest 1 bit of $x$ alone and $x \mathbin{\&} (x - 1)$ is $x$ with that bit cleared. How many times does the loop `while x ≠ 0: x ← x & (x − 1)` run?

18. • A [pointer machine](/pointer-machine/) holds $n$ records, each with at most $k$ pointer fields, and the machine starts at one fixed record. Prove that some record cannot be reached in fewer than $\log_k n - 1$ steps, so that finding a given record needs $\Omega(\log n)$ steps in the worst case. A RAM can reach any of $n$ cells in one step; what feature of the RAM does the pointer machine lack?

19. • With the numbers of Exercise 2, count the block transfers of external merge sort when each merge pass merges only two runs, and compare with the multiway merge. Count a pass as reading and writing all $N$ items.

20. • Permuting $N$ items to given positions in external memory can be done by moving the items one at a time, with about $N$ transfers, or by sorting them by target position. For which values of $N$, $M$ and $B$ is sorting cheaper? Is it cheaper for the numbers of Exercise 2?

21. • Draw a [branching program](/branching-program/) of width 2 that computes the parity of $n$ bits, and count its nodes. Then show that every Boolean function of $n$ variables has a branching program with at most $2^n - 1$ inner nodes.

22. ★ Prove that a Turing machine whose head moves right in every step, and which accepts or rejects when it reaches the first blank, recognizes exactly the regular languages.

23. ★ Rule 90 sets each cell to the XOR of its two neighbours. Start it from a single 1 at position 0. Prove that after $t$ steps the cell at position $i$ holds $\binom{t}{(t+i)/2} \bmod 2$ when $|i| \le t$ and $t + i$ is even, and 0 otherwise. How many cells are 1 after $t = 2^k$ steps?

24. ★ Show that $\mathrm{MULT} = \lambda m\,n\,f.\,m\,(n\,f)$ satisfies $\mathrm{MULT}\;c_m\;c_n \to^* c_{mn}$ for Church numerals.

25. ★ ZPP is the class of languages with a probabilistic algorithm that never errs and runs in expected polynomial time. Prove that $\mathrm{ZPP} = \mathrm{RP} \cap \mathrm{coRP}$.

26. ★ Let $H$ be the set of strings $1^k$ such that the $k$-th Turing machine halts on empty input. Show that $H$ is undecidable but has Boolean circuits of polynomial size, one for each input length, so that $H \in \mathrm{P/poly}$.
