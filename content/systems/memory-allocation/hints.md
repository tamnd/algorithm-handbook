1. $T = 32$ and $L = 12$, so the fragmentation is $1 - 12/32 = 0.625$. A request of $n$ words needs $n + 2 \le 12$, so malloc(10) is the largest that succeeds; malloc(11) fails with 32 free words.

5. The block of 5 words is at 0 (8 words), the block of 3 at 8 (4 words), the block of 9 at 16 (16 words); the only free block is $(12, 4)$. Freeing the block at 0 adds $(0, 8)$, since its buddy at 8 is split. Freeing the block at 8 merges it with its buddy at $8 \oplus 4 = 12$ into $(8, 8)$, then with $(0, 8)$ into $(0, 16)$; the buddy at 16 is in use, so the free list is $(0, 16)$ alone.

8. $A = 1$, $B = 3$, $C = 1$, $M = 3$ and $e = 1$, and $2 \cdot 3 = 2 \cdot 1 + 3 + 1$. For $N = 600$ and $p = 0.9$, between 270 and 271 free blocks, about $270/870 \approx 0.31$ of all blocks, and about $pk/(pk + 2) = 1.8/3.8 \approx 0.47$ of the memory.

10. First fit uses $(0, 4)$, $(28, 12)$ and all of $(48, 16)$ with 1, 3 and 4 probes, ending with $(4, 8), (16, 8), (40, 4)$. Best fit uses $(16, 4)$, all of $(0, 12)$ and all of $(28, 16)$ with 4, 1 and 3 probes, ending with $(20, 4), (48, 16)$. Worst fit splits $(28, 16)$ and then $(48, 16)$, and fails on malloc(12) with 36 free words in blocks of 12, 8, 12 and 4.

12. A block of 1000 words is in class $(9, 15)$, sizes 992 to 1023. MAPPING-SEARCH adds $2^{9-4} - 1 = 31$ and maps 1031 to class $(10, 0)$, sizes 1024 to 1087, so the request is rounded to 1024 and a free block of up to 1023 words is not seen.

13. The worst requests are one more than a Fibonacci size, $S_k + 1$, with waste $(S_{k-1} - 1)/S_{k+1}$. Up to 100 the worst is 90, which gets 144 and wastes $54/144 = 0.375$. Since $S_{k-1}/S_{k+1} \le 2/5$, with equality only at $2/5$ itself, the share stays below $2/5$, and it tends to $1/\varphi^2 \approx 0.382$.

16. If the three blocks of 1 word lie in $[0, 4)$, one word $f$ there is free; free a block that is not next to $f$. The two free words below 4 are then apart, so a block of 2 words must reach address 4. Offline, put the item that will be freed next to the word that stays free.

17. LOAD is 4, at time 3. First fit puts A, B and C at 0, 1 and 2, and D, which meets B and C, at 3, so it uses 5 words. Offsets B $= 0$, C $= 1$, A $= 2$ and D $= 2$ use 4 words, since A ends before D starts.

19. With $a_i = 256$ both conditions read $u_i < 192$. The invariant allows $a_i \le \max(u_i + KS, u_i/(1 - f))$, which is 214 for $u_i = 150$ and 94 for $u_i = 30$: at most 3 superblocks and 1 superblock.

21. With immediate merging, the free blocks depend only on the allocated set, and an aligned group of $2^k$ words with no used word lies inside one free block of order at least $k$. So a failure needs a used word in each of the $2^{m-k}$ aligned groups, and at most $2^m - 2^{m-k}$ words are free. Allocate $2^m$ blocks of one word and free all but the first of each group.

22. A block of 1 word placed at $q$ has every word below $q$ in use, so $q \le 3$. A block of 2 words placed at $p$ finds word $p - 1$ used and no two adjacent free words below it; with at most 2 live words this forces $p \le 4$.

23. The only state of at most 2 live words in $[0, 5)$ with no two adjacent free words has blocks of one word at 1 and 3 and nothing else. Place blocks of 1 word at the first free word in the order 2, 0, 4, 1, 3, and blocks of 2 words at any free pair. A block of 1 word goes to 1 or 3 only when 0, 2 and 4 are in use, so 1 and 3 can never hold blocks of 1 word at the same time.

24. Allocate 8 blocks of 1 word (0 to 7), free those at 0, 2, 4 and 6, allocate 2 blocks of 2 words (8 and 10), free the blocks at 1, 5 and 8. The live words 3, 7, 10 and 11 leave no free run of 4 below 12, so the block of 4 words goes to 12.

25. Allocate two objects of 32 bytes (one full superblock), one of 8 bytes and one of 16 bytes (a new superblock each): $u = 88$ and $a = 192$, which already breaks the invariant. Free one object of 32 bytes: $u = 56$. Moving the superblocks with 8, then 16, then 32 bytes in use leaves $(48, 128)$, then $(32, 64)$, both still past the threshold, and finally $(0, 0)$.
