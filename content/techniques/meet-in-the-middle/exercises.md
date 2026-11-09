1. ◦ Run the [Horowitz-Sahni algorithm](/horowitz-sahni-algorithm/) on the items $(3, 34, 4, 12, 5, 2)$ with target $t = 9$. Split them into the first three and the last three, write both sorted lists of sums, and scan with one pointer at the start of the first list and one at the end of the second. List the pair sums you meet and give the subset found.

2. ◦ A subset sum instance has $n = 40$ items. How many subsets does exhaustive search try? How long is each sorted list in the [Horowitz-Sahni algorithm](/horowitz-sahni-algorithm/), and how long is each of the four lists in the [Schroeppel-Shamir algorithm](/schroeppel-shamir-algorithm/)?

3. ◦ A cipher has 64-bit keys and 64-bit blocks and is used twice with two independent keys. Treat each wrong key pair as a random map, so it matches a given known pair with probability $2^{-64}$. About how many wrong key pairs survive one, two and three known plaintext-ciphertext pairs? How many pairs should the [meet-in-the-middle attack](/meet-in-the-middle-attack/) collect, and about how many cipher calls and table entries does it use?

4. ◦ The [Schroeppel-Shamir algorithm](/schroeppel-shamir-algorithm/) splits the items into four quarters A, B, C, D. Explain why it sorts the sums of B and D but never needs the sums of A or C in sorted order.

5. ◦ A search tree has branching factor $b = 10$, and the goal lies at depth $d = 8$. About how many nodes does a search from the start alone generate? About how many does [bidirectional search](/bidirectional-search/) generate if it grows two trees of depth 4 that meet in the middle?

6. ◦ Repeat Exercise 1 with target $t = 30$. How many pair sums does the scan look at before it stops, and what does it return?

7. • Change the scan of Exercise 1 so that it counts the subsets with sum $t$ instead of stopping at the first one. Equal sums in a list need care. Run it on the items $(1, 2, 3, 4, 5, 6)$ with $t = 9$, split as $(1, 2, 3)$ and $(4, 5, 6)$, and list the subsets it counts.

8. • Change the [Horowitz-Sahni algorithm](/horowitz-sahni-algorithm/) to return the largest subset sum that does not exceed $t$, still in $O(2^{n/2})$ time after sorting. What does it return for the items of Exercise 1 with $t = 30$?

9. • Solve $3^x \equiv 7 \pmod{17}$ with [baby-step giant-step](/baby-step-giant-step/) and $m = 4$. Write the table of baby steps $3^j$ for $0 \le j < 4$, the giant-step factor $3^{-4} \bmod 17$, and the giant steps until one hits the table.

10. • In the [meet-in-the-middle attack](/meet-in-the-middle-attack/) on a cipher with 56-bit keys, the table can hold only $2^{40}$ entries. The attacker splits the first key space into blocks that fit, builds the table for one block at a time and runs the whole second key space against each table. How many passes are there, and about how many cipher calls in all?

11. • Given $n$ positive integers, we want two disjoint nonempty subsets with the same sum. Restate this as a search for a nonzero vector $c \in \{-1, 0, 1\}^n$ with $\sum c_i a_i = 0$, and give a meet-in-the-middle algorithm for it. What is its running time, and which match must it ignore?

12. • Four lists $A$, $B$, $C$, $D$ each hold $N$ integers. Give an $O(N^2 \log N)$ algorithm that decides whether $a + b + c + d = t$ for some $a \in A$, $b \in B$, $c \in C$, $d \in D$. How much memory does it use?

13. • A [representation](/representation-technique/) can also use $-1$ entries. Let $e \in \{0, 1\}^n$ have weight $w$, with $w$ even. Count the ways to write $e = x + y$ where $x$ and $y$ lie in $\{-1, 0, 1\}^n$ and each has exactly $w/2 + 1$ entries equal to 1 and exactly one entry equal to $-1$. Evaluate the count for $n = 40$ and $w = 20$ and compare it with the count for plain 0-1 halves of weight $w/2$.

14. • Triple encryption with three independent $k$-bit keys computes $C = E_{k_3}(E_{k_2}(E_{k_1}(P)))$. Adapt the [meet-in-the-middle attack](/meet-in-the-middle-attack/) to it. How many cipher calls and table entries does it use, and what does that give for DES with $k = 56$?

15. ★ Change the [Horowitz-Sahni algorithm](/horowitz-sahni-algorithm/) so that it decides whether some subset of exactly $w$ items has sum $t$. Keep the running time within $O(n 2^{n/2})$.

16. ★ A 0-1 knapsack has six items, given as (weight, value): $(3, 4)$, $(4, 5)$, $(2, 3)$ in the first half and $(5, 8)$, $(1, 1)$, $(6, 7)$ in the second, with capacity $W = 10$. Solve it by meet in the middle: list the (weight, value) pairs of each half, remove the dominated pairs from the second list, and find the best combination. Which items are taken, and what is the value?

17. ★ Run the heap method of the [Schroeppel-Shamir algorithm](/schroeppel-shamir-algorithm/) on four lists $A$, $B$, $C$, $D$ of $N$ numbers each, to decide whether $a + b + c + d = t$. Show that it uses $O(N^2 \log N)$ time and $O(N)$ memory.

18. ★ Solve the four-list problem of Exercise 12 in a different way. Fix a modulus $M$ and, for each residue $r$ in $[0, M)$, build only the pairs $a + b$ with $a + b \equiv r \pmod M$ and the pairs $c + d$ with $c + d \equiv t - r \pmod M$, then join them by a hash table. Assume the values are spread evenly over the residues. What are the expected time and memory as functions of $N$ and $M$, and which $M$ gives $O(N^2)$ time with $O(N)$ memory?
