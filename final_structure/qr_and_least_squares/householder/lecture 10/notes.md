# Lecture 10: Householder Triangularization

This lecture introduces the Householder algorithm — the method actually used in practice to compute QR. It applies a sequence of orthogonal reflections that zero out columns of $A$ below the diagonal, one column at a time. Unconditionally stable, machine-precision orthogonality, every time.

---

## The Core Idea: Reflections

A **Householder reflector** is a matrix of the form:

$$H = I - 2vv^T$$

where $v$ is a unit vector. This reflects every vector across the hyperplane perpendicular to $v$.

### 2D examples

**$v = (0, 1)^T$:** $H = \begin{pmatrix}1&0\\0&-1\end{pmatrix}$ — flips the $y$-component. Reflection across the $x$-axis.

**$v = \frac{1}{\sqrt{2}}(1, 1)^T$:** $H = \begin{pmatrix}0&-1\\-1&0\end{pmatrix}$ — swaps and negates. Reflection across the line $y = -x$.

### Key properties of $H$

- **Orthogonal:** $H^TH = I$ (reflections preserve lengths)
- **Symmetric:** $H^T = H$
- **Its own inverse:** $H^2 = I$ (reflect twice = do nothing)

---

## The Trick: Zeroing Out a Vector Below Its First Entry

Given a vector $x$, find a Householder reflector $H$ such that:

$$Hx = \|x\| \, e_1 = \begin{pmatrix}\|x\|\\0\\\vdots\\0\end{pmatrix}$$

The reflection maps $x$ onto the first coordinate axis — all the "stuff" in $x$ gets concentrated into one entry.

**How to find $v$:** The bisector of $x$ and $\|x\|e_1$ gives:

$$v = \frac{x - \|x\|e_1}{\|x - \|x\|e_1\|}$$

(In practice, choose the sign $x \pm \|x\|e_1$ to avoid cancellation.)

### Concrete example

$x = (3, 4)^T$, $\|x\| = 5$.

$$w = x - 5e_1 = (-2, 4)^T, \quad v = \frac{1}{\sqrt{5}}(-1, 2)^T$$

$$H = I - 2vv^T = \begin{pmatrix}3/5&4/5\\4/5&-3/5\end{pmatrix}$$

Check: $H(3, 4)^T = (5, 0)^T$ ✓.

---

## Householder QR: Column by Column

To factor an $m \times n$ matrix $A$ into $QR$, apply $n$ Householder reflectors to progressively zero out subdiagonal entries:

**Step 1:** Find $H_1$ that zeros out column 1 below the diagonal.

$$H_1 A = \begin{pmatrix} r_{11} & * & * \\ 0 & * & * \\ 0 & * & * \\ 0 & * & * \end{pmatrix}$$

**Step 2:** Find $H_2$ that zeros out column 2 below the diagonal, leaving column 1 alone. $H_2$ only acts on the lower-right $(m-1) \times (m-1)$ submatrix:

$$H_2 H_1 A = \begin{pmatrix} r_{11} & r_{12} & * \\ 0 & r_{22} & * \\ 0 & 0 & * \\ 0 & 0 & * \end{pmatrix}$$

**Step 3:** Continue until all subdiagonal entries are eliminated:

$$H_n \cdots H_2 H_1 A = R$$

Since each $H_k$ is orthogonal, $Q^T = H_n \cdots H_1$ is orthogonal, giving $A = QR$ with $Q = H_1 H_2 \cdots H_n$.

---

## Full Concrete Example

$$A = \begin{pmatrix}1&1\\0&1\\1&0\end{pmatrix}$$

**Step 1:** Column 1: $x = (1, 0, 1)^T$, $\|x\| = \sqrt{2}$.

Compute $v$ from $x - \sqrt{2}\,e_1$, normalize, build $H_1$ (a $3 \times 3$ matrix). Apply $H_1 A$: first column becomes $(\sqrt{2}, 0, 0)^T$.

**Step 2:** Look at the lower-right $2 \times 2$ block of $H_1 A$. Find a $2 \times 2$ Householder reflector, embed it:

$$H_2 = \begin{pmatrix}1&0&0\\0&\multicolumn{2}{c}{\tilde{H}_2}\end{pmatrix}$$

Apply $H_2 H_1 A = R$ (upper triangular). Done.

---

## Why Householder Beats Gram-Schmidt

- **Gram-Schmidt:** applies *triangular* operations to $A$ to produce orthogonal $Q$. Triangular operations can amplify errors.
- **Householder:** applies *orthogonal* operations to $A$ to produce triangular $R$. Orthogonal operations preserve norms — errors never amplify.

**Concrete comparison** ($100 \times 50$ matrix, $\kappa(A) = 10^{10}$):

| Method | $\|Q^TQ - I\|$ |
|---|---|
| Classical Gram-Schmidt | $\sim 10^{4}$ (complete garbage) |
| Modified Gram-Schmidt | $\sim 10^{-6}$ (lost 10 digits) |
| Householder | $\sim 10^{-15}$ (machine precision) |

Householder achieves machine precision **regardless of the condition number**.

---

## The Implicit $Q$

You never form $Q$ explicitly. Store the $n$ Householder vectors $v_1, \ldots, v_n$ instead. Each $v_k$ has $m - k + 1$ entries, so total storage is $\sim mn - n^2/2$ — about the same as $R$.

When you need $Q^Tb$ (for least squares), apply each reflector sequentially:

$$Q^Tb = H_n \cdots H_2 H_1 b$$

Each application $H_k b = b - 2v_k(v_k^Tb)$ costs $O(m)$ flops — a rank-1 update, not a full matrix multiply.

For $m = 10{,}000$, $n = 100$: storing $Q$ takes $10^8$ entries; storing the Householder vectors takes $\sim 10^6$ — a 100× savings.

---

## Operation Count

Total cost of Householder QR on an $m \times n$ matrix:

$$\sim 2mn^2 - \frac{2}{3}n^3 \text{ flops}$$

For square $n \times n$: $\sim \frac{4}{3}n^3$ (about twice LU, but you get orthogonality).

| Method | Cost | Orthogonality |
|---|---|---|
| Classical Gram-Schmidt | $2mn^2$ | Terrible |
| Modified Gram-Schmidt | $2mn^2$ | Mediocre |
| Householder | $2mn^2 - \frac{2}{3}n^3$ | Machine precision |

Same cost, vastly better stability.

---

## When Gram-Schmidt Still Wins

Gram-Schmidt produces the $q$ vectors **one at a time**, left to right. Householder works on the whole matrix at once — individual columns of $Q$ only emerge at the end.

This matters for **iterative methods** (Arnoldi, GMRES) where you generate one new orthogonal vector per iteration and might stop at any point. Modified Gram-Schmidt is the natural choice there.

---

## The Big Picture

Householder triangularization is the standard algorithm for computing QR in practice — behind `numpy.linalg.qr()`, LAPACK's `dgeqrf`, and every serious numerical library. The key insight: work with orthogonal operations (reflections) rather than triangular ones (projections), because orthogonal operations are inherently stable. The price is that $Q$ is stored implicitly, but this is actually an advantage for large problems.
