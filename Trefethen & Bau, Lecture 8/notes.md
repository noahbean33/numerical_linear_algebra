# Lecture 8: Gram-Schmidt Orthogonalization

This lecture covers the actual algorithms for computing QR — classical Gram-Schmidt (CGS) and modified Gram-Schmidt (MGS) — and explains why the "obvious" version is numerically terrible and how a simple rewrite fixes it.

---

## The Idea

You have columns $a_1, a_2, \ldots, a_n$ and you want orthonormal vectors $q_1, q_2, \ldots, q_n$ spanning the same successive subspaces:

1. Take $a_1$, normalize it → $q_1$
2. Take $a_2$, subtract its projection onto $q_1$, normalize → $q_2$
3. Take $a_3$, subtract its projections onto $q_1$ and $q_2$, normalize → $q_3$
4. Continue...

At step $j$: remove from $a_j$ everything in the directions $q_1, \ldots, q_{j-1}$, then normalize the remainder.

---

## Classical Gram-Schmidt (CGS)

At step $j$, compute all projections at once against the original $a_j$:

$$v_j = a_j - (q_1^T a_j)\,q_1 - (q_2^T a_j)\,q_2 - \cdots - (q_{j-1}^T a_j)\,q_{j-1}$$

$$q_j = v_j / \|v_j\|$$

### Concrete example

Take $a_1 = (1,1,0)^T$, $a_2 = (1,0,1)^T$, $a_3 = (0,1,1)^T$.

**Step 1:** $q_1 = \frac{1}{\sqrt{2}}(1,1,0)^T$

**Step 2:** $q_1^T a_2 = \frac{1}{\sqrt{2}}$. Subtract:

$$v_2 = \begin{pmatrix}1\\0\\1\end{pmatrix} - \frac{1}{2}\begin{pmatrix}1\\1\\0\end{pmatrix} = \begin{pmatrix}\frac{1}{2}\\-\frac{1}{2}\\1\end{pmatrix}$$

Normalize: $q_2 = \frac{1}{\sqrt{6}}(1,-1,2)^T$

**Step 3:** $q_1^T a_3 = \frac{1}{\sqrt{2}}$, $q_2^T a_3 = \frac{1}{\sqrt{6}}$. After subtracting both projections:

$$v_3 = \begin{pmatrix}-\frac{2}{3}\\\frac{2}{3}\\\frac{2}{3}\end{pmatrix}, \qquad q_3 = \frac{1}{\sqrt{3}}(-1,1,1)^T$$

Check: $q_1^T q_2 = 0$ ✓, $q_1^T q_3 = 0$ ✓, $q_2^T q_3 = 0$ ✓.

---

## The Numerical Disaster

In exact arithmetic, CGS works perfectly. In floating point, it fails badly when columns are nearly dependent.

**Concrete demonstration.** Take $\epsilon = 10^{-8}$ and:

$$a_1 = \begin{pmatrix}1\\0\\0\end{pmatrix}, \quad a_2 = \begin{pmatrix}1\\\epsilon\\0\end{pmatrix}, \quad a_3 = \begin{pmatrix}1\\0\\\epsilon\end{pmatrix}$$

When computing $v_2 = a_2 - (q_1^T a_2) q_1$, you subtract two nearly equal vectors. The result should be $(0, \epsilon, 0)^T$, but **catastrophic cancellation** means the computed $v_2$ has errors $\sim 10^{-16}$ in its first component. After normalization, that error gets amplified relative to the $\epsilon = 10^{-8}$ signal, contaminating $q_2$.

When you then project $a_3$ against this contaminated $q_2$, the error compounds. The resulting $q_3$ can be far from orthogonal to $q_1$ and $q_2$.

---

## Modified Gram-Schmidt (MGS)

The fix: instead of projecting against all previous $q$'s simultaneously using the original $a_j$, subtract one projection at a time, updating the working vector after each subtraction.

**Classical** (all at once against original $a_j$):

$$v_j = a_j - (q_1^T a_j)q_1 - (q_2^T a_j)q_2 - \cdots$$

**Modified** (sequential, updating as you go):

$$v_j^{(1)} = a_j - (q_1^T a_j)q_1$$
$$v_j^{(2)} = v_j^{(1)} - (q_2^T v_j^{(1)})q_2$$
$$v_j^{(3)} = v_j^{(2)} - (q_3^T v_j^{(2)})q_3$$
$$\vdots$$

In exact arithmetic, these are identical. In floating point, the modified version is dramatically better because each subtraction works with an already-partially-orthogonalized vector.

### Why the difference matters

In CGS, all projections use the original $a_j$, which may have large components along the $q_i$ directions. You're computing small differences of large quantities — catastrophic cancellation.

In MGS, after subtracting the $q_1$ component, $v_j^{(1)}$ is already approximately orthogonal to $q_1$. The projections involve smaller numbers, so cancellation is less severe.

**Analogy:** You owe debts of \$999, \$998, and \$997 from a \$3000 balance.

- **CGS:** Compute all debts from the original \$3000, subtract all at once. Each carries full-sized rounding error.
- **MGS:** Pay \$999 (have \$2001), pay \$998 (have \$1003), pay \$997 (have \$6). Each step works with the current smaller balance.

---

## Quantifying the Difference

For an $m \times n$ matrix with condition number $\kappa$:

- **CGS:** $\|Q^TQ - I\| \sim \kappa \cdot \epsilon_{\text{machine}}$. If $\kappa = 10^{10}$ and $\epsilon_{\text{machine}} = 10^{-16}$, only about 6 good digits of orthogonality.
- **MGS:** Similar bound on orthogonality loss, but the $R$ factor is computed much more accurately. The residual $\|A - QR\|$ is small ($\sim \epsilon_{\text{machine}} \|A\|$) even when orthogonality is partially lost.
- **Householder (Lecture 10):** Orthogonality $\sim \epsilon_{\text{machine}}$ regardless of $\kappa$. Full machine precision, always.

---

## The Algorithm (Pseudocode)

```
Modified Gram-Schmidt:
for j = 1 to n:
    v_j = a_j
for j = 1 to n:
    r_jj = ||v_j||
    q_j = v_j / r_jj
    for k = j+1 to n:
        r_jk = q_j^T v_k
        v_k = v_k - r_jk * q_j
```

The crucial difference: the inner loop updates future $v_k$'s immediately using the just-computed $q_j$, rather than computing all projections from the original $a_j$.

**Operation count:** $\sim 2mn^2$ flops — same as CGS.

---

## Gram-Schmidt as Triangular Orthogonalization

Gram-Schmidt applies upper triangular operations to $A$ to produce $Q$:

$$\hat{Q} = A \hat{R}^{-1}$$

It "triangularly orthogonalizes" — makes columns orthonormal using triangular operations.

Contrast with Householder (Lecture 10), which applies orthogonal operations to $A$ to produce $R$:

$$\hat{R} = Q^T A$$

One **triangularly orthogonalizes**, the other **orthogonally triangularizes**. Householder is more stable because orthogonal operations preserve norms, while triangular operations can amplify errors.

---

## The Projector Viewpoint

In CGS, the key step projects onto the orthogonal complement of all previous $q$'s at once:

$$P_j = I - \hat{Q}_j \hat{Q}_j^T$$

This is equivalent to subtracting rank-1 projections one at a time:

$$P_j = I - q_1 q_1^T - q_2 q_2^T - \cdots - q_j q_j^T$$

Or factoring into a product of rank-1 complementary projectors:

$$P_j = (I - q_j q_j^T)(I - q_{j-1} q_{j-1}^T) \cdots (I - q_1 q_1^T)$$

The cross-terms vanish because $q_i^T q_k = 0$. In MGS, we apply each factor as soon as it's found to *all* remaining columns — so by the time we choose a new column, it's already orthogonalized against the entire basis found so far.

---

## The Takeaway

Gram-Schmidt is the natural algorithm for QR: peel off orthogonal components one at a time. The classical version is numerically dangerous because it accumulates projection errors. The modified version — a trivial-looking rewrite — is substantially better because it works with sequentially cleaned-up vectors. But for serious computation, both are inferior to Householder reflections (Lecture 10), which achieve machine-precision orthogonality regardless of conditioning. Gram-Schmidt's advantage is that it produces $q$ vectors one at a time, making it natural for iterative methods (Arnoldi, Lanczos) where you don't know in advance how many vectors you'll need.
