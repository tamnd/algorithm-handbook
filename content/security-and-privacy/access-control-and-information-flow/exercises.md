1. ◦ An [access control matrix](/access-control-matrix/) has subjects ann, ben and cy, objects $f$, $g$ and $h$, and the nonempty cells $A[\text{ann}, f] = \{\text{own}, r, w\}$, $A[\text{ann}, g] = \{r\}$, $A[\text{ben}, g] = \{\text{own}, r\}$, $A[\text{ben}, h] = \{w\}$, $A[\text{cy}, f] = \{r\}$ and $A[\text{cy}, h] = \{\text{own}, r, w\}$. Write the [access control list](/access-control-list/) of $f$ and the [capability list](/capability-list/) of cy. How many entries do all the access control lists hold together, and how many do all the capability lists hold?

2. ◦ In [RBAC](/role-based-access-control/), the roles are staff, dev and lead, with lead $\ge$ dev $\ge$ staff. $PA$ gives staff the permission wiki, dev the permission repo and lead the permission deploy. $UA$ assigns ann to lead and ben to dev. List the permissions of each user in the flattened relation $UA \circ RH^* \circ PA$.

3. ◦ The levels are $U < C < S < TS$. Compare the labels $a = (S, \{\text{NATO}, \text{Crypto}\})$, $b = (TS, \{\text{NATO}\})$ and $c = (C, \{\text{Crypto}\})$ under the dominance order of [mandatory access control](/mandatory-access-control/): which pairs are comparable? Give $a \sqcup b$ and $a \sqcap b$.

4. ◦ In the [Bell-LaPadula model](/bell-lapadula-model/), a subject has maximum level $f_s = (S, \{\text{NATO}, \text{Crypto}\})$ and current level $f_c = (C, \{\text{NATO}\})$. For each object $o_1 = (U, \emptyset)$, $o_2 = (C, \{\text{NATO}\})$, $o_3 = (S, \{\text{NATO}\})$, $o_4 = (TS, \{\text{NATO}\})$ and $o_5 = (C, \{\text{Crypto}\})$, say whether the simple security property and the \*-property allow read, append and write.

5. ◦ Use the order of the [Biba](/biba-integrity-model/) entry, system $\sqsubseteq$ user $\sqsubseteq$ web, with system the most trusted. Under the low-water mark policy for subjects, a process at level system observes a user file. Which of a system file, a user file and a web file may it then modify?

6. ◦ In the [Chinese Wall model](/chinese-wall-model/), the conflict classes are banks $\{A, B, C\}$, oil $\{X, Y\}$ and insurance $\{P, Q\}$. A consultant has read unsanitized objects of $A$ and of $X$. Which of these requests are allowed: read $B$, read $A$, read $Y$, read $P$, read a sanitized object of $B$, write an object of $A$?

7. ◦ Three [HRU](/harrison-ruzzo-ullman-model/) commands: CREATE$(s, o)$ creates object $o$ and enters own into $(s, o)$; GRANT$(s, s', o)$ enters $r$ into $(s', o)$ if own is in $(s, o)$; REVOKE$(s, s', o)$ deletes $r$ from $(s', o)$ if own is in $(s, o)$. Which commands are mono-operational, which are monotonic, and which are monoconditional? For the system with only GRANT and REVOKE, and for the system with only CREATE and GRANT, say whether the entries give a decision procedure for safety.

8. ◦ Give the number of states of the smallest deterministic [security automaton](/security-automaton/) for each policy over the actions send, log and other: (a) no two sends without a log between them; (b) over open, read and close for one file, reads happen only while the file is open, and the file is opened at most once.

9. ◦ With $l$ low and $h$ high, which of these programs does the [security type system](/security-type-system/) of Volpano, Irvine and Smith accept: (a) $h := l + h$; (b) $\mathbf{if}\ l > 0\ \mathbf{then}\ h := 1\ \mathbf{else}\ h := 0$; (c) $\mathbf{if}\ h > 0\ \mathbf{then}\ l := 0\ \mathbf{else}\ \mathbf{skip}$; (d) $\mathbf{while}\ h > 0\ \mathbf{do}\ h := h - 1$; (e) $l := h \cdot 0$? Which of the rejected ones are noninterfering?

10. ◦ Run [secure multi-execution](/secure-multi-execution/) with two levels, $l$ low and $h$ high, default value 0, on $l := l + h;\ h := l$ from the store $(l, h) = (2, 5)$. Give the final store of each copy, the output of SME, and the output of the plain run.

11. ◦ The secret $h$ is uniform on $\{0, 1, \dots, 9\}$ and the program outputs $h \bmod 4$. Give its [min-entropy leakage](/min-entropy-leakage/) and its Shannon leakage, to three decimals.

12. • A capability $c_1$ of alice with rights $\{r, w\}$ is delegated as $c_2 = \{r, w\}$ to bob and $c_3 = \{r\}$ to carol. Bob delegates $c_4 = \{r\}$ to dave and $c_5 = \{w\}$ to erin, and dave delegates $c_6 = \{r\}$ to frank. Which capabilities does REVOKE$(c_4)$ remove? Which does a later REVOKE$(c_2)$ remove? May carol delegate a capability with $\{w\}$?

13. • A task needs the permissions $P = \{p_1, \dots, p_5\}$. The users hold $u_1 : \{p_1, p_2\}$, $u_2 : \{p_2, p_3, p_4\}$, $u_3 : \{p_4, p_5\}$, $u_4 : \{p_1, p_5\}$ and $u_5 : \{p_3\}$. The [separation of duty](/separation-of-duty/) policy says that fewer than $k$ users must never hold $P$ together. For which $k$ does the state satisfy the policy? Name the sets of users that break it for the smallest $k$ that fails.

14. • Find the Boolean rank of the user-permission matrix $u_1 : \{p_1, p_2\}$, $u_2 : \{p_2, p_3\}$, $u_3 : \{p_3, p_4\}$, $u_4 : \{p_4, p_1\}$, the answer to the [role mining problem](/role-mining-problem/). Which lower bound of the entry proves it, and which does not?

15. • A [Chinese Wall](/chinese-wall-model/) policy has three conflict classes with 3, 5 and 2 company datasets. The security automaton for the read rule keeps the set of datasets read so far. How many states can it reach? What is the smallest number of consultants such that every dataset can be read by some consultant?

16. • In a [Take-Grant](/take-grant-model/) graph all vertices $a, \dots, f$ are subjects, and the edges are $a \xrightarrow{t} b$, $c \xrightarrow{g} b$, $c \xrightarrow{t} d$, $d \xrightarrow{r} e$ and $f \xrightarrow{r} a$. Decide $\mathit{can\_share}(r, a, e)$ and $\mathit{can\_share}(r, f, e)$. For the true case, give a sequence of rules.

17. • The [RT0](/trust-management/) credentials are: $\text{Clinic.view} \leftarrow \text{Clinic.partner.doctor}$; $\text{Clinic.partner} \leftarrow \text{HospA}$; $\text{Clinic.partner} \leftarrow \text{Board.licensed}$; $\text{Board.licensed} \leftarrow \text{HospB}$; $\text{HospA.doctor} \leftarrow \text{Dan}$; $\text{HospB.doctor} \leftarrow \text{Eve}$; $\text{HospC.doctor} \leftarrow \text{Fay}$; $\text{Clinic.write} \leftarrow \text{Clinic.view} \cap \text{Clinic.employee}$; $\text{Clinic.employee} \leftarrow \text{Eve}$. Who is in Clinic.view and who is in Clinic.write? What changes if the credential $\text{Board.licensed} \leftarrow \text{HospB}$ is missing?

18. • Classify each as a trace property or not, and as hypersafety ($k$-safety for which $k$) or hyperliveness: (a) no run sends more than five messages; (b) [termination-insensitive noninterference](/termination-insensitive-noninterference/); (c) some two runs give different public outputs.

19. • Take $h$ high, $l$ low and $t$ with initial label $H$, and the program $t := 0;\ \mathbf{if}\ h\ \mathbf{then}\ t := 1\ \mathbf{else}\ \mathbf{skip};\ l := t$. (a) Run the [no-sensitive-upgrade](/no-sensitive-upgrade/) monitor with $h = 1$ and with $h = 0$. (b) Do the same for the program without the first assignment, with $t$ starting at 0. (c) Run [faceted execution](/faceted-execution/) on the first program with $h = \langle 1 : 0 \rangle$ and give the final faceted values of $t$ and $l$.

20. • In the [decentralized label model](/decentralized-label-model/), carol acts for mgr, and $L_1 = \{\mathit{alice}: \mathit{alice}, \mathit{mgr};\ \mathit{bob}: \mathit{bob}, \mathit{mgr}\}$. (a) Who may read a value labeled $L_1$? (b) May a process with the authority of alice relabel it to $\{\mathit{bob}: \mathit{bob}, \mathit{mgr}\}$? (c) To $\{\mathit{alice}: \mathit{alice}, \mathit{mgr}\}$? (d) Without any authority, to $\{\mathit{alice}: \mathit{alice}, \mathit{carol};\ \mathit{bob}: \mathit{bob}, \mathit{mgr}\}$?

21. • The [delimited release](/declassification/) policy has one escape hatch, $h_1 + h_2$, with $h_1, h_2$ secret and $l$ public. Which programs satisfy it: (a) $l := h_1 + h_2$; (b) $h_1 := h_2;\ l := h_1 + h_2$; (c) $\mathbf{if}\ h_1 + h_2 > 10\ \mathbf{then}\ l := 1\ \mathbf{else}\ l := 0$; (d) $l := h_1 - h_2$? For each that fails, give two initial stores that show it.

22. • The secret $h$ is uniform on $\{0, 1, 2, 3\}$, and the program outputs whether $h \ge 1$. Compute the min-entropy leakage, the [g-leakage](/g-leakage/) for an attacker with two tries, and the min-capacity bound.

23. • A storage [covert channel](/covert-channel/) sends one bit per slot and the receiver reads each bit wrongly with probability 0.05, independently. Give its Shannon capacity in bits per second at 200 slots per second and at 50 slots per second, to one decimal, and place each against the TCSEC thresholds.

24. • Apply the [shared resource matrix](/shared-resource-matrix/) method to a lock. The attributes are Lock, Owner and Level. ACQUIRE references Lock and Level and modifies Lock and Owner; RELEASE references Owner and modifies Lock; TEST references Lock. Give the flow edges, the closed sets $R^*$ of the three primitives, and the candidate attributes.

25. ★ Six users each hold all of six permissions except one, a different one for each user: user $i$ lacks $p_i$. Show that the Boolean rank of this matrix is 4, so that role mining saves two roles over the trivial solution.

26. ★ Weak tranquility lets a subject in [Bell-LaPadula](/bell-lapadula-model/) change its current level as long as the new state keeps the \*-property. Give a sequence of four states, each with the simple security property and the \*-property, in which a subject with maximum level $S$ reads a secret object and then writes into an unclassified one. What does the sequence show about the [basic security theorem](/basic-security-theorem/)?

27. ★ In a [Take-Grant](/take-grant-model/) graph, $x$ and $z$ are subjects, $o$ is an object, and the edges are $x \xrightarrow{g} o$, $z \xrightarrow{t} o$ and $z \xrightarrow{r} f$. Neither subject can act on the other directly. Show that $\mathit{can\_share}(r, x, f)$ holds by an explicit sequence of rules, and name the bridge in the theorem of Lipton and Snyder.

28. ★ A deterministic program $y = f(x)$ has a secret input only and always ends. Show that "the [min-capacity](/min-entropy-leakage-bound/) is at most $\log_2 m$ bits" is a $k$-safety [hyperproperty](/hyperproperty/) for $k = m + 1$, and not for any smaller $k$ in general. Which property is the case $m = 1$?

29. ★ The Z-channel has inputs 0 and 1: input 0 always gives output 0, and input 1 gives 0 or 1 with probability $1/2$ each. Compute its min-capacity, its Shannon capacity and the input distribution that reaches the Shannon capacity.
