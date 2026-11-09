1. The final table holds 19, –, 13, 35, –, 27, –, 40, 51, 62, 8 in slots 0 to 10. The inserts take 1, 1, 1, 2, 3, 3, 2 and 4 probes, so a successful search averages $17/8 = 2.125$. The unsuccessful searches from homes 0 to 10 take 2, 1, 3, 2, 1, 2, 1, 6, 5, 4, 3 probes, which is $30/11 \approx 2.73$ on average.

3. All five keys have $h_1 = 3$. Key 14 goes to slot 3 in one probe; 25, 36, 3 and 47 have $h_2 = 5, 2, 4, 6$ and go to slots 8, 5, 7 and 9 in two probes each, so 9 probes in all. Linear probing would put them in slots 3 to 7 with $1 + 2 + 3 + 4 + 5 = 15$ probes.

4. The squares modulo 8 are only 0, 1 and 4, so the insert sees slots 0, 1 and 4 and nothing else. Fill those three slots and leave the other five empty.

6. The values are 9, 3, 13, 7 and 1.

10. The probability of no collision among $n$ keys is $\prod_{i=1}^{n-1} (1 - i/m)$. It first drops to $1/2$ or below at $n = 302$, where the probability of a collision is about $0.5007$. The estimate $\sqrt{2m \ln 2}$ is about $301.4$.

12. Three keys with the same $h_1$ and the same $h_2$ are three keys that leave the same remainder modulo 49, such as 5, 54 and 103. They have only two cells between them.

14. The doublings happen before the 5th, 9th, 17th, ..., 513th insert. That is 8 doublings, which move $4 + 8 + \cdots + 512 = 1020$ keys, and $m$ ends at 2048.

16. With step $s$ the sequence visits $12/\gcd(s, 12)$ slots before it repeats.

19. The low four bits of all three hash values are 0000, so any depth up to 4 leaves three keys in one bucket.

20. After four splits the level becomes 1 and $p$ returns to 0. A key whose value modulo 8 is less than $p$ uses its value modulo 16.

24. Assume $n < m$, so some slot stays empty. Show that slot $j$ ends up occupied exactly when, for some $t \ge 0$, at least $t + 1$ keys have their home in the $t + 1$ slots $j - t, \ldots, j$ (taken modulo $m$). This condition mentions only the homes, not the order. For one direction, look at the run of occupied slots that contains $j$: none of its keys can have passed the empty slot before it.

25. Robin Hood stops at the first empty slot, just as linear probing does, so exercise 24 applies. Cut the circle at a slot that stays empty. Then the displacement of a key is its slot minus its home, and the total is the sum of the occupied slots minus the sum of the homes.

26. Compute $\frac{1}{\alpha} \int_0^\alpha \frac12 \bigl(1 + (1-x)^{-2}\bigr)\, dx$. The integral of $(1-x)^{-2}$ from 0 to $\alpha$ is $\alpha/(1-\alpha)$.

27. One direction is the pigeonhole principle. For the other, a connected graph with no more edges than vertices is a tree or has exactly one cycle. Point each edge at one of its ends so that no vertex receives two edges: around the cycle in one direction, and on the trees away from the cycle or from a chosen root.

28. The first probe is $h_1$ and the second is $h_1 + h_2 \bmod 16$, so the first two probes give back the pair.
