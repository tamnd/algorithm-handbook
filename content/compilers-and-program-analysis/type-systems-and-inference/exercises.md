1. ◦ Find the principal type of each term by hand with the rules of the [Hindley-Milner type system](/hindley-milner-type-system/), or show that it has none: (a) `fun f -> fun g -> fun x -> f x (g x)`; (b) `fun x -> fun y -> fun z -> x`; (c) `fun x -> x x`.

2. ◦ By the [Curry-Howard correspondence](/curry-howard-correspondence/), a simple type has a closed term exactly when it is provable in intuitionistic implicational logic. For each type, give a closed term or show that there is none: (a) $\alpha \to (\alpha \to \beta) \to \beta$; (b) $((\alpha \to \alpha) \to \beta) \to \beta$; (c) $((\alpha \to \beta) \to \beta) \to \alpha$.

3. ◦ Let $P_1 = \{x{:}\mathsf{Int}\}$ and $P_2 = \{x{:}\mathsf{Int}, y{:}\mathsf{Int}\}$. With width [subtyping](/subtyping/) for records and the rule S-Arrow, decide each claim: (a) $P_1 \to P_2 <: P_2 \to P_1$; (b) $P_2 \to P_2 <: P_1 \to P_2$; (c) $(P_1 \to \mathsf{Int}) \to \mathsf{Int} <: (P_2 \to \mathsf{Int}) \to \mathsf{Int}$; (d) $(P_2 \to \mathsf{Int}) \to \mathsf{Int} <: (P_1 \to \mathsf{Int}) \to \mathsf{Int}$.

4. ◦ Under the [value restriction](/value-restriction/) of Standard ML, which of these bindings get a polymorphic type scheme? `let f = fun x -> x`, `let g = (fun x -> x) (fun y -> y)`, `let p = (fun x -> x, [])`, `let r = ref []` and `let h = fun x -> (fun y -> y) x`.

5. ◦ For each term, say whether it is typable in the linear, affine, relevant and ordered systems of the [linear types](/linear-types/) entry: (a) `fun f -> fun x -> f x`; (b) `fun x -> fun f -> f x`; (c) `fun f -> fun x -> f (f x)`; (d) `fun x -> fun y -> fun z -> x`.

6. ◦ In [gradual typing](/gradual-typing/), which pairs of types are consistent? (a) $? \to \mathsf{int}$ and $\mathsf{bool} \to\ ?$; (b) $\mathsf{int} \to \mathsf{int}$ and $? \to \mathsf{bool}$; (c) $?$ and $\mathsf{int} \to \mathsf{bool}$; (d) $(? \to ?) \to \mathsf{int}$ and $\mathsf{int} \to \mathsf{int}$.

7. ◦ With [dependent types](/dependent-types/), let $+$ be defined by recursion on its first argument, so $\mathsf{zero} + n \equiv n$ and $\mathsf{succ}\ m + n \equiv \mathsf{succ}\ (m + n)$, and let $n$ be a variable. Write $0$ for $\mathsf{zero}$ and $1$ for $\mathsf{succ}\ \mathsf{zero}$. Which of these types are definitionally equal to $\mathsf{Vec}\ A\ (\mathsf{succ}\ n)$? (a) $\mathsf{Vec}\ A\ (1 + n)$; (b) $\mathsf{Vec}\ A\ (n + 1)$; (c) $\mathsf{Vec}\ A\ (\mathsf{succ}\ (0 + n))$; (d) $\mathsf{Vec}\ A\ (\mathsf{succ}\ (n + 0))$.

8. ◦ The program `let x0 = 1 in let x1 = (x0, x0) in let x2 = (x1, x1) in ... in xk` has $k + 1$ bindings and uses no polymorphism. How many nodes does the type of `xk` have when it is written as a tree, and how many as a DAG that shares equal subtrees? Give both numbers for $k = 10$, and say what this means for printing the result of [type inference](/type-inference-problem/).

9. ◦ In the region [effect system](/effect-system/), give the type and the effect of `fun r -> fun s -> s := !r`, where `r` has type $\mathsf{ref}_{\rho_1}\ \mathsf{int}$ and `s` has type $\mathsf{ref}_{\rho_2}\ \mathsf{int}$. Then give the least solution of the inclusion constraints $\{\mathsf{read}\ \rho\} \cup \varsigma_2 \subseteq \varsigma_1$, $\{\mathsf{write}\ \pi\} \cup \varsigma_1 \subseteq \varsigma_2$ and $\{\mathsf{alloc}\ \rho\} \cup \varsigma_1 \subseteq \varsigma_3$.

10. • Run [algorithm W](/algorithm-w/) on `let pair = fun x -> fun y -> fun f -> f x y in (pair 1 true, pair true 1)`. Give the type scheme of `pair` and the type of the whole term. Then do the same for `(fun pair -> (pair 1 true, pair true 1)) (fun x -> fun y -> fun f -> f x y)`, and for the version of it whose body is only `pair 1 true`.

11. • Show that `fun x -> fun y -> (x y, y x)` has no Hindley-Milner type: write the equations that inference produces and find the one that fails. Then give a [System F](/system-f/) term, in System F with pairs, whose erasure is this term, and its type.

12. • Use the rules of [bidirectional type checking](/bidirectional-type-checking/) (Var⇒, Lit⇒, Anno⇒, App⇒, Add⇒, Abs⇐, If⇐, Sub⇐) to decide whether each term checks against the given type with no annotation inside: (a) `fun x -> x + 1` against $\mathsf{Int} \to \mathsf{Int}$; (b) `(fun x -> x + 1) 2` against $\mathsf{Int}$; (c) `fun f -> f 3` against $(\mathsf{Int} \to \mathsf{Int}) \to \mathsf{Int}$. Repair the term that fails with one annotation, and count the rule uses in the derivation for (c).

13. • This Haskell function on a nested type needs [polymorphic recursion](/polymorphic-recursion-undecidability/):

```haskell
data Twice a = One a | More (Twice (a, a))
size (One _)  = 1
size (More t) = 2 * size t
```

(a) When `size` is used at type `Twice a`, at which type is the recursive call made? (b) Show that inference without a signature fails. (c) Evaluate `size (More (More (One ((1, 2), (3, 4)))))` and list the types at which `size` is called. (d) Which signature makes the program typable?

14. • List the instance set that [monomorphization](/monomorphization/) computes for `let id = fun x -> x in let app = fun f -> fun x -> f x in (app id 1, app id true, app (fun b -> b) false)`, and the number of specialized copies of `id` and `app` it makes.

15. • Run the SOLVE loop of [liquid types](/liquid-types/) on `let abs x = if x < 0 then 0 - x else x`, with the qualifiers $0 \leq \nu$, $\star \leq \nu$ and $\nu \leq \star$, where $\star$ ranges over the variable `x`. The then branch gives the constraint $C_1$ and the else branch $C_2$, and each pass handles $C_1$ before $C_2$. List the candidates removed in each pass, count the validity queries, and give the inferred type of `abs`.

16. • Read [recursive types](/recursive-types/) equi-recursively, and let $X = \mu\alpha.\ \mathsf{int} \to \alpha$, $Y = \mu\beta.\ \mathsf{int} \to \mathsf{int} \to \beta$ and $Z = \mu\gamma.\ \mathsf{bool} \to \gamma$. Which of them are equal? Prove one equality with a bisimulation, a finite relation closed under unfolding. What changes with iso-recursive types?

17. • With [row polymorphism](/row-polymorphism/), `f = fun r -> r.x + r.y` has the type $\forall\rho.\ \{x : \mathsf{int}; y : \mathsf{int} \mid \rho\} \to \mathsf{int}$. Which of these applications are well typed, and what is $\rho$ in each? (a) `f {x = 1; y = 2; z = true}`; (b) `f {y = 1; x = 2}`; (c) `f {x = 1; z = 2}`; (d) `f {x = 1; y = true}`.

18. • Does [borrow checking](/borrow-checking/) accept this Rust fragment? Explain with liveness and outlives constraints.

```rust
let mut x = 1;          // P1
let a = &x;             // P2
let b = a;              // P3
x = 2;                  // P4
println!("{}", b);      // P5
```

Then say what happens when P5 prints `a` in place of `b`, when P5 is deleted, and when P4 and P5 change places.

19. • Take the typed language of booleans and numbers (`true`, `false`, `if`, `0`, `succ`, `pred`, `iszero`). Replace the rule for `if` by T-Weird: if $\vdash t_1 : \mathsf{Bool}$ and $\vdash t_2 : T$, then $\vdash \mathsf{if}\ t_1\ \mathsf{then}\ t_2\ \mathsf{else}\ t_3 : T$, with no premise on $t_3$. Which half of [type soundness](/type-soundness/) fails, progress or preservation? Give a small counterexample, and show that a well-typed term can now get stuck.

20. • In System F, $\mathsf{CBool} = \forall\alpha.\ \alpha \to \alpha \to \alpha$, with $\mathit{tru} = \Lambda\alpha.\lambda t{:}\alpha.\lambda f{:}\alpha.\ t$ and $\mathit{fls} = \Lambda\alpha.\lambda t{:}\alpha.\lambda f{:}\alpha.\ f$. Write $\mathit{not} : \mathsf{CBool} \to \mathsf{CBool}$ and $\mathit{and} : \mathsf{CBool} \to \mathsf{CBool} \to \mathsf{CBool}$, and reduce $\mathit{not}\ \mathit{tru}$ to its normal form.

21. ★ In the gradual language, label the outer application of `(fun (f : ?) -> f 1) (fun (x : bool) -> x)` with $\ell_1$ and the inner one, `f 1`, with $\ell_2$. Insert the casts, run the cast calculus step by step, and say which label is blamed. Explain why the blame-subtyping theorem allows that cast to fail. What is the result when the argument is `fun (x : int) -> x`?

22. ★ With equi-recursive types and record width subtyping, decide $P <: Q$ and $Q <: P$ for $P = \mu\alpha.\ \{x{:}\mathsf{int}, f{:}\alpha \to \mathsf{int}\}$ and $Q = \mu\beta.\ \{f{:}\beta \to \mathsf{int}\}$. Then decide $P' <: Q'$ for $P' = \mu\alpha.\ \{x{:}\mathsf{int}, \mathit{next}{:}\alpha\}$ and $Q' = \mu\beta.\ \{\mathit{next}{:}\beta\}$. Explain the difference, which object-oriented languages meet as the problem of binary methods.

23. ★ Show that `let rec f = fun x -> f` has no type in ML even with Mycroft's rule for polymorphic recursion, which lets the body use `f` at any instance of its own scheme. Then give the type it has with equi-recursive types.

24. ★ Liquid types are run twice on the same program, once with a qualifier set $Q$ and once with $Q' \supseteq Q$. Prove that if SOLVE reports no error with $Q$, it reports no error with $Q'$. Then show by an example that the converse fails.

25. ★ With dependent types, define $\mathit{append} : \Pi(A{:}\mathcal U).\ \Pi(m\ n{:}\mathsf{Nat}).\ \mathsf{Vec}\ A\ m \to \mathsf{Vec}\ A\ n \to \mathsf{Vec}\ A\ (m + n)$ by the clauses `append nil ys = ys` and `append (cons x xs) ys = cons x (append xs ys)`. Show that both clauses check by conversion when $+$ recurses on its first argument. Then let $+$ recurse on its second argument, so $m + \mathsf{zero} \equiv m$ and $m + \mathsf{succ}\ n \equiv \mathsf{succ}\ (m + n)$. Show that both clauses fail to check, and name the lemmas that repair them and how they are proved.
