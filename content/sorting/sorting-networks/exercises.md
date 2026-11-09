1. ◦ Run the network $[0{:}1], [2{:}3], [0{:}2], [1{:}3], [1{:}2]$ on $\langle 4, 3, 2, 1 \rangle$. Show the four wires after each [comparator](/comparator/). Which comparators exchange their items?

2. ◦ The network $[0{:}1], [3{:}4], [2{:}4], [2{:}3], [1{:}4], [0{:}3], [0{:}2], [1{:}3], [1{:}2]$ sorts 5 items. Give its size. Split it into layers by the greedy rule of [network depth](/network-depth/), and give its depth. Is the depth the smallest possible for 5 wires?

3. ◦ The network $[0{:}1], [1{:}2], [2{:}3], [0{:}1], [1{:}2]$ on 4 wires is the bubble sort network with its last comparator removed. Find every input of zeros and ones on which it fails. Then give an input of four distinct numbers on which it fails, and its output.

4. ◦ Which of these sequences are [bitonic](/bitonic-sequence/): $\langle 2, 5, 9, 7, 3 \rangle$, $\langle 4, 1, 2, 3 \rangle$, $\langle 1, 4, 2, 5 \rangle$, $\langle 1, 1, 0, 0, 0, 1 \rangle$, $\langle 0, 1, 1, 0, 0, 1 \rangle$? For each one that is not, give a threshold whose positions do not form a cyclic interval.

5. ◦ Run the [bitonic merger](/bitonic-merger/) on 8 wires on $\langle 2, 6, 9, 7, 5, 4, 3, 1 \rangle$. Show the wires after each of its three layers. After the first layer, check that each item of the first half is at most each item of the second half.

6. ◦ Merge $\langle 2, 5, 6, 8 \rangle$ with $\langle 1, 3, 4, 7 \rangle$ by Batcher's odd-even merge, as in [odd-even merge sort](/odd-even-merge-sort/). Give the merged items of the even places, the merged items of the odd places, the sequence after you interleave them, and the result of the last layer. How many comparators of the last layer exchange their items?

7. ◦ (a) How many inputs of zeros and ones must you test to show that a network of standard comparators on 6 wires sorts? (b) How many to show that a network on 6 wires merges two sorted lists of 3 items each? (c) Give the size and the depth of bitonic sort and of odd-even merge sort on 32 wires.

8. ◦ What do the two bounds of the [depth lower bound](/sorting-network-depth-lower-bound/) give for $n = 3$ and for $n = 12$? Compare them with $d(3) = 3$ and $d(12) = 8$. Then use $s(12) = 39$ and Van Voorhis's bound from [minimum-size sorting network](/minimum-size-sorting-network/) to give a lower bound for $s(13)$.

9. • Prove that every sorting network of standard comparators on $n$ wires has a comparator $[i{:}i+1]$ for each $i$ from 0 to $n - 2$.

10. • Let $n$ be even. Give a comparator network with $3n/2 - 2$ comparators that puts the smallest item on wire 0 and the largest on wire $n - 1$. What is its depth? Explain why no network can do this with fewer comparators. (See [finding the minimum and maximum](/minimum-and-maximum-finding/).)

11. • Add the comparators $[3{:}4], [2{:}3], [1{:}2], [0{:}1]$ after the 4-wire sorting network $[0{:}1], [2{:}3], [0{:}2], [1{:}3], [1{:}2]$. Prove that the result sorts 5 items, so that $s(5) \le 9$. What is its depth, and is it optimal?

12. • Prove that there are exactly $n(n-1) + 2$ bitonic sequences of zeros and ones of length $n \ge 2$. Check the count for $n = 4$ by listing the sequences that are not bitonic.

13. • The *mirror* of a network on $n$ wires replaces each comparator $[i{:}j]$ by $[n-1-j{:}n-1-i]$. Prove that the mirror of a sorting network is a sorting network.

14. • Run a sorting network on an input of zeros and ones. Prove that output wire $n - k$ holds 1 exactly when the input has at least $k$ ones. Use this to build a monotone Boolean circuit of 32 AND and OR gates that computes the majority of 7 bits.

15. • Build [bitonic sort](/bitonic-sort/) for 8 wires as its entry gives it, and drop every comparator that touches wire 6 or 7. Show that 15 comparators remain, and find one of them that never exchanges its items, on any input. Why does it never exchange?

16. • On $2m$ wires, sort the first $m$ wires and the last $m$ wires with any sorting networks, and then add the layer $[i{:}2m-1-i]$ for $i < m$. Prove that the result puts the $m$ smallest items on the first $m$ wires, so it is a 0-[halver](/halver/). What depth does it have with Batcher's networks when $2m = 2^{k+1}$?

17. • A *single exception network* on 3 wires sorts every input of zeros and ones except one. Give a network of two comparators that fails only on $\langle 0, 1, 0 \rangle$, and one that fails only on $\langle 1, 0, 1 \rangle$. Why does this mean that a test of a 3-wire network cannot skip any of its four unsorted 0-1 inputs?

18. • A network is *primitive* if all its comparators join adjacent wires, $[i{:}i+1]$. Prove that every primitive sorting network on $n$ wires has at least $n(n-1)/2$ comparators. Which network of this chapter reaches this size with depth $n$?

19. ★ A general comparator may put the minimum on the higher wire. Suppose a network of general comparators sorts every input. Process its comparators in order; at each comparator that puts the minimum on its higher wire, turn it into a standard comparator and exchange the names of its two wires in all later comparators. Prove that the result is a standard network of the same size and depth that sorts every input.

20. ★ Prove that a primitive network on $n$ wires sorts every input if and only if it sorts the single input $\langle n, n-1, \ldots, 1 \rangle$.

21. ★ Prove Van Voorhis's bound $s(n) \ge s(n-1) + \lceil \lg n \rceil$ for $n \ge 2$. Use exercise 19.

22. ★ After the four filter layers of [Green's network](/green-filter/), show that on every 0-1 input the set of wires that hold 1 is an up-set of the cube $\{0, 1\}^4$: if wire $w$ holds 1, so does every wire whose binary digits include those of $w$. Show that every up-set occurs as an output of the filter, and count them.
