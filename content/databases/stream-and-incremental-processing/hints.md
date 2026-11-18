1. The true average is $500 / 4 = 125$; the average of the store averages is $(100 + 200)/2 = 150$. The view should store the sum and the count per store, from which any average over a group of stores follows.

2. The join has $(1,1,u)$, $(2,1,u)$ and $(2,2,v)$, so $V = \{1{:}1, 2{:}2\}$. The term $\Delta R \bowtie S$ gives $3{:}{+1}$; the term $R \bowtie \Delta S$ gives $1{:}{-1}$, $2{:}{-1}$ and $3{:}{+1}$; the term $\Delta R \bowtie \Delta S$ gives $3{:}{-1}$. So $\Delta V = \{1{:}{-1}, 2{:}{-1}, 3{:}{+1}\}$ and the new view is $\{2{:}1, 3{:}1\}$, as a recomputation gives. A script checked both.

4. Phase 1 overdeletes $p_{23}$, $p_{24}$, $p_{13}$ and $p_{14}$, since each has a derivation through the edge $2 \to 3$. Phase 2 rederives $p_{24}$ from the edge $2 \to 4$. The insert phase adds $p_{14}$ from $\mathit{edge}(1,2)$ and $p_{24}$. The new model is $p_{12}$, $p_{14}$, $p_{24}$ and $p_{34}$. A script that runs the three phases checked this.

5. Write each relation as old plus delta and expand the product. Every term that uses at least one delta remains, which gives $2^3 - 1 = 7$. With $j$ changed relations there are $2^j - 1$ terms.

7. The two terms give $\{1{:}{-1}, 2{:}{-1}, 3{:}0\}$, so $a = 3$ would wrongly be missing from the view. Since $R = R' - \Delta R$ and $S = S' - \Delta S$, bilinearity gives $\Delta V = \Delta R \bowtie S' + R' \bowtie \Delta S - \Delta R \bowtie \Delta S$. A script checked both versions on the data.

8. On the chain DRed overdeletes the 25 facts $p_{xy}$ with $x \le 5 < y$, rederives none and adds none, and the new model has 20 facts. With the extra edges, DRed still overdeletes 25 facts, rederives 9 and adds 15, so the new model has 44 facts and loses only $p_{56}$. A script that runs DRed on both graphs checked these counts.

10. Every path fact has a derivation that uses the edge $n \to 1$, by going round the cycle. After the deletion only the edges remain, so phase 2 finds the $n - 1$ edge facts. The insert phase builds the paths of the chain $1 \to \cdots \to n$ of length at least 2. A script checked $n = 3, 5, 6$.
