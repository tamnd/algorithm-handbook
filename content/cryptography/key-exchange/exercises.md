1. ◦ Run [Diffie-Hellman](/diffie-hellman/) in the toy group $p = 47 = 2 \cdot 23 + 1$, with $g = 2$, which has order 23. Alice picks $x = 5$ and Bob picks $y = 13$. Compute $A$, $B$ and the shared value. How many $Y$ in $[2, 45]$ pass the check $Y^{23} \equiv 1 \pmod{47}$? Then let Mallory, a [man in the middle](/man-in-the-middle-attack/), pick $e = 7$ and send $E = g^e$ to both sides in place of $A$ and $B$. Which key does Alice end with, and which does Bob? The group is far too small for real use.

2. ◦ A company has $n = 200$ users, and every pair must be able to talk in secret. How many keys are needed in all, and how many must each user store, if every pair gets its own key in advance? How many long-term keys are there with a [key distribution center](/key-distribution-center/)? How many new keys does user 201 cause in each case? See the [key distribution problem](/key-distribution-problem/).

3. ◦ Take the toy curve $y^2 = x^3 + x + 6$ over $\mathbb{F}_{11}$, which has 13 points, and $G = (2, 7)$. List the multiples $kG$ for $k = 1, \ldots, 13$. Run [ECDH](/ecdh/) with $d_A = 3$ and $d_B = 5$: give $Q_A$, $Q_B$ and the shared $x$-coordinate. Is $(3, 4)$ a valid public key?

4. ◦ In [Merkle's puzzles](/merkle-puzzles/), Alice makes $N$ puzzles, each of which takes $S$ trial decryptions to open. Take $N = S = 2^{20}$. About how much work do Alice, Bob and a passive eavesdropper do? With $N = S$, what $N$ gives the eavesdropper about $2^{60}$ work, and how much data does Alice send if each puzzle takes 40 bytes?

5. ◦ Run [Shamir's three-pass protocol](/shamir-three-pass-protocol/) with the exponentiation cipher modulo $p = 29$. Alice's lock is $a = 3$, Bob's is $b = 11$, and the secret is $m = 6$. Find the unlocking exponents $a'$ and $b'$, the three messages, and Bob's result. Why must $a$ and $b$ be prime to $p - 1$?

6. ◦ Clamp the scalars. For [X25519](/x25519/), a 32-byte scalar has first byte `a5` and last byte `9b`. For [X448](/x448/), a 56-byte scalar has first byte `a5` and last byte `2b`. Give the clamped first and last bytes in each case, and the number of ladder steps of each function.

7. ◦ [HKDF](/hkdf/) with SHA-256 must give $L = 100$ bytes. How many HMAC calls does Expand make, and how many in all with Extract? What is the largest $L$ for SHA-256 and for SHA-384? If a second call with the same PRK and info asks for 42 bytes, how is its output related to the first?

8. ◦ For each case, say whether a passive recorder who later steals the long-term key (or the PSK) can read the session, that is, whether the session has [forward secrecy](/perfect-forward-secrecy/) in that sense: TLS 1.2 with RSA key transport; a TLS 1.3 handshake with ECDHE; TLS 1.3 resumption in psk_ke mode; resumption in psk_dhe_ke mode; TLS 1.3 0-RTT data. Then say which strength of forward secrecy HMQV and station-to-station have.

9. ◦ In the [hybrid](/hybrid-key-exchange/) group X25519MLKEM768 of TLS, the client's key share is an ML-KEM-768 encapsulation key of 1184 bytes and an X25519 key; the server's is a 1088-byte ciphertext and an X25519 key. How many bytes does each side send, against 32 for X25519 alone? The ML-KEM secret comes first in the concatenation. An implementer feeds only the first 32 bytes of the concatenated secret to the KDF. What must an attacker break to get the key?

10. ◦ Use the cost table of the [group key agreement problem](/group-key-agreement-problem/) for $n = 8$: give rounds, messages and total exponentiations for the [ITW ring](/ingemarsson-tang-wong/), [GDH.2](/group-diffie-hellman/) and [Burmester-Desmedt](/burmester-desmedt/). From which $n$ on does Burmester-Desmedt use fewer exponentiations in total than GDH.2? Why is the cheaper protocol in which a leader sends a key not a solution of the problem?

11. • A server reuses a static exponent $x < q = 101$ in the order-101 subgroup of $\mathbb{Z}_p^*$, $p = 21211 = 2 \cdot 3 \cdot 5 \cdot 7 \cdot 101 + 1$, and answers each received $Y$ with a hash of $Y^x$, with no check on $Y$. Run the [small subgroup attack](/small-subgroup-attack/): the hashes show that $x \equiv 1 \pmod 2$, $x \equiv 2 \pmod 3$, $x \equiv 4 \pmod 5$ and $x \equiv 3 \pmod 7$. Find $x$. How many queries and at most how many trial exponents did this take, and why is $x$ unique? Which one-line check stops the attack?

12. • Invalid-curve attack. The victim of exercise 3 holds $d = 10$ on the curve with $a = 1$, $b = 6$ over $\mathbb{F}_{11}$, never checks that a received point lies on the curve, and returns a hash of the full point $dQ$. The attacker sends $Q_1 = (0, 1)$, of order 7 on $y^2 = x^3 + x + 1$, and $Q_2 = (0, 0)$, of order 2 on $y^2 = x^3 + x$. What does each reply reveal, and what is $d$? Why does the victim's addition formula not notice the change of $b$?

13. • Run [Blom's scheme](/blom-scheme/) over $\mathbb{F}_{13}$ with $k = 1$, $D = \begin{pmatrix} 2 & 7 \\ 7 & 4 \end{pmatrix}$ and public vectors $g_i = (1, i)$. Give $K_{12}$, $K_{13}$ and $K_{23}$, and the secret vectors $a_1 = D g_1$ and $a_2 = D g_2$. Users 1 and 2 pool their vectors: find $D$ and $K_{34}$.

14. • Run Burmester-Desmedt with $n = 4$, $p = 23$, $g = 4$ (order 11) and secrets $x = (2, 3, 5, 7)$. Give the round-1 values $z_i$, the round-2 values $X_i$, the product of the $X_i$, and the key.

15. • Run [J-PAKE](/j-pake/) in the toy group $p = 23$, $q = 11$, $g = 4$, with password value $s = 5$ and secrets $x_1 = 3$, $x_2 = 7$ (Alice) and $x_3 = 2$, $x_4 = 9$ (Bob). Leave out the zero-knowledge proofs. Give the four round-1 values, $A$, $B$ and the key, and check it against $g^{(x_1 + x_3) x_2 x_4 s}$.

16. • A two-message protocol sends nonces $N_A$ and $N_B$ and sets $K = H(g^{ab}, N_A, N_B)$, where $g^a$ and $g^b$ are certified static keys. Eve has stolen Alice's static secret $a$. Show that she can pose as Bob to Alice, that is, a [key compromise impersonation](/key-compromise-impersonation/). Does the protocol have forward secrecy? Why does the same theft not let Eve pose as Bob to Alice in [station-to-station](/station-to-station-protocol/)?

17. • In Kaliski's [unknown key-share](/unknown-key-share-attack/) attack on [MQV](/mqv/), Eve registers a fresh static key on line during the run. Why does proof of possession at the certificate authority not stop it? Which two fixes do?

18. • An attacker runs 100 online guesses a day for a year against a [PAKE](/password-authenticated-key-exchange/) login, and the password is uniform among $2^{20}$ values. What is the largest chance of success? Against [EKE](/encrypted-key-exchange/) with a partition attack, each recorded session leaves a wrong password standing with probability 0.375. Starting from a dictionary of $2^{20}$ words, how many recorded sessions bring the expected number of candidates below 2?

19. • In the [double ratchet](/double-ratchet/), Alice sends $a_0, a_1, a_2$ on her first sending chain, Bob replies with $b_0, b_1$ after his DH ratchet step, and Alice then makes a new ratchet key and sends more. A passive Eve copies Alice's whole state just after Alice sent $a_1$, and then keeps listening. Which of $a_0, a_1, a_2, b_0, b_1$ and Alice's later messages can Eve read?

20. • In [X3DH](/x3dh/), Alice computes $DH_1 = DH(IK_A, SPK_B)$, $DH_2 = DH(EK_A, IK_B)$, $DH_3 = DH(EK_A, SPK_B)$ and $DH_4 = DH(EK_A, OPK_B)$. In each case, say whether a passive recorder learns SK: (a) both identity private keys leak after all ephemeral and prekey secrets are deleted; (b) the private keys of $IK_B$ and $SPK_B$ leak, and no one-time prekey was used; (c) as (b), but a one-time prekey was used and deleted.

21. • The Noise pattern IK is `<- s`, then `-> e, es, s, ss`, then `<- e, ee, se`. How many DH operations does each party do, and how many round trips does the handshake take? With X25519, a 16-byte tag, and empty payloads, how long are the two handshake messages? See the [Noise framework](/noise-protocol-framework/).

22. • In the random key ring scheme of [key predistribution](/key-predistribution-problem/), each device gets $m$ keys from a pool of $P = 10{,}000$, and two rings share a key with probability $p = 1 - \binom{P - m}{m} / \binom{P}{m}$. Find the smallest $m$ with $p \ge 1/2$.

23. • Run MQV in the toy group $q = 1019$, $p = 2039$, $g = 4$, with $w = 5$, so that $\bar R = (R \bmod 2^5) + 2^5$. The static secrets are $a = 15$ and $b = 40$, the ephemeral secrets $x = 77$ and $y = 500$. Find $A$, $B$, $X$, $Y$, $d = \bar X$, $e = \bar Y$, $s_A = x + d a \bmod q$, $s_B = y + e b \bmod q$, and the shared $\sigma$ computed by each side.

24. ★ Prove that no protocol in which Alice sends a single message $m$ and in which neither party has a key or other secret in advance can be a [key agreement](/key-agreement-problem/) secure against a passive eavesdropper, if Bob must compute the same key as Alice with probability at least $1 - \varepsilon$.

25. ★ For Blom's scheme with $G$ a Vandermonde matrix of distinct points, prove that (a) $k + 1$ users together recover $D$, and (b) $k$ users learn nothing about $K_{uv}$ for two other users $u$ and $v$: every value of $K_{uv}$ is equally likely given their data.

26. ★ In [SRP](/secure-remote-password/), $u = H(A \| B)$ is computed after both shares are fixed. Suppose a variant lets the server announce $u$ before the client sends $A$. Show that a thief who stole the verifier $v$ can then log in as the client without the password. Check the attack in the toy group $N = 23$, $g = 5$, $k = 3$, $x = 6$, $u = 4$, $a = 7$, $b = 9$. The group gives no security at all.

27. ★ A [key ratchet](/key-ratchet/) runs the KDF chain $mk_i = F(ck_i, 1)$, $ck_{i+1} = F(ck_i, 2)$ from a random $ck_0$, and erases each $ck_i$ and $mk_i$ after use. Prove that if $F$ is a [PRF](/pseudorandom-function/), an adversary who gets $ck_n$ cannot tell $(mk_0, \ldots, mk_{n-1})$ from random with advantage more than $n \cdot \mathrm{Adv}_{\mathrm{PRF}}$.

28. ★ In [tree-based group Diffie-Hellman](/tree-based-group-diffie-hellman/), every join is inserted at a shallowest leaf. Prove that after $n$ members have joined one by one, with no leaves, the tree has height $\lceil \log_2 n \rceil$.
