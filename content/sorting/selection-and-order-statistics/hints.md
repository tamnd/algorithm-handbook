1. Sorted, the array is $\langle 3, 5, 8, 9, 11, 12, 14, 17 \rangle$, so $a_{(1)} = 3$, $a_{(4)} = 9$ and $a_{(8)} = 17$. The lower median is $a_{(4)} = 9$ and the upper median is $a_{(5)} = 11$. The quartiles are $a_{(2)} = 5$, $a_{(4)} = 9$ and $a_{(6)} = 12$. The rule of R and NumPy puts the median at position $(n - 1)/2 + 1 = 4.5$ and interpolates: $9 + (11 - 9)/2 = 10$.

3. The rounds give $6, 3, 9, 2$, then $3, 2$, then $2$: seven comparisons. The winner 2 beat 8, 9 and 3, and two more comparisons among them give the second smallest, 3. The total is $9 = 8 + \lceil \lg 8 \rceil - 2$.

4. The first pivot is 5, and the array becomes $\langle 1, 4, 2, 5, 7, 9, 8, 6 \rangle$ after 7 comparisons, with 5 at rank 4. The search goes left to $\langle 1, 4, 2 \rangle$; the pivot 2 gives $\langle 1, 2, 4 \rangle$ after 2 comparisons, with 2 at rank 2. The search goes right to the single item 4, which is the answer. Nine comparisons in all.

5. The group medians are 14, 28 and 17, so $x = 17$. Three items in each of the groups with medians 14 and 17 are at most 17, and three in each of the groups with medians 17 and 28 are at least 17: six on each side. In fact 17 has rank 7. The median has rank 8, so the search goes to the eight larger items and takes the smallest of them, 19.

6. The bound $n - 1 + \min(k - 1, n - k)$ gives 12 for the median and 9 for the second smallest. The tournament makes $9 + \lceil \lg 9 \rceil - 2 = 11$ comparisons, and 11 is the exact answer: the lower bound for rank 2 is not tight.

8. The high digits are $3, 7, 3, 3, 10, 3, 7, 0$, with counts 1 for digit 0, 4 for digit 3, 2 for digit 7 and 1 for digit 10. Digit 0 holds rank 1 and digit 3 holds ranks 2 to 5, so the search enters bucket 3 and looks for its third item. The low digits there are $10, 1, 12, 5$, and the third smallest is 10, so the answer is $3 \cdot 16 + 10 = 58$.

10. If the pivot has rank $j$, the search goes on with $j - 1$ items, so $C(n) = n - 1 + \frac{1}{n} \sum_{j=0}^{n-1} C(j)$. Multiply the equation for $n$ by $n$, subtract the equation for $n - 1$ multiplied by $n - 1$, and simplify to get $C(n) = C(n - 1) + 2 - 2/n$, so $C(n) = 2n - 2H_n$, about $1985.0$ for $n = 1000$.

11. Half the groups have medians at most the pivot, and each of them gives $(g + 1)/2$ items. The larger side has at most $n(3g - 1)/(4g)$ items, so the fractions sum to $(3g + 3)/(4g)$, which is less than 1 exactly when $g > 3$. For $g = 3$ the sum is 1, and $T(n) = T(n/3) + T(2n/3) + \Theta(n)$ is $\Theta(n \log n)$.

15. There are 6 entries at most 9 and 7 at most 10, so the seventh smallest is 10. Each step of the walk moves up or right, so it visits at most $m + n - 1$ cells.

17. In each coordinate the total weight is 8, and the weights in sorted order add up to $2, 3, 6, 8$, so the weighted median is the third value in each: $p = (6, 5)$. The sum is $2 \cdot 7 + 1 \cdot 5 + 3 \cdot 0 + 2 \cdot 7 = 33$. The Manhattan distance is a sum of a term in $x$ and a term in $y$, and each term can be minimized alone.

21. Compare $a : b$ and $c : d$, and name them so that $a < b$ and $c < d$. Compare $a : c$; if $a < c$, then $a$ is below $b$, $c$ and $d$, so it is below the median, and the median of all five is the second smallest of $b, c, d, e$. Compare $b : e$, then compare the smaller items of the two pairs. The smaller of these is the least of the four; drop it, and compare its partner with the smaller item of the other pair. The smaller of these two is the median: six comparisons in all.

22. Every item but the smallest must lose a comparison, which is $n - 1$ comparisons. An adversary that lets the item with the larger "weight" win, with weights that merge on each comparison, forces the smallest to meet at least $\lceil \lg n \rceil$ items, and all but one of those must lose a second time.

23. The copies of such a value fill a run of more than $n/q$ ranks in sorted order, and no run that long fits between two of the ranks $\lceil jn/q \rceil$. Select the $q$ ranks by multiple selection, then count the copies of each candidate with one pass and a binary search among the sorted candidates. For $n = 12$ and $q = 4$ the ranks are 3, 6, 9 and 12.

24. Keep two values $lo < hi$ with the answer known to lie strictly between them. In one pass, count the items in $(lo, hi)$ and choose one of them at random by reservoir sampling; in a second pass, find its rank. Then either it is the answer or it becomes the new $lo$ or $hi$, as in quickselect, and $O(\log n)$ rounds suffice on average.

25. Find the median $m$ and split the items around it in $O(n)$ time. Compare the weight of the items below $m$, and of those up to $m$, with the target $pW$; either $m$ is the answer, or the search continues in one half with the target reduced by the weight left behind. The time is $T(n) \le T(\lceil n/2 \rceil) + O(n) = O(n)$.
