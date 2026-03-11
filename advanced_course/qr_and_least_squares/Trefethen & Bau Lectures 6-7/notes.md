# Lecture 6: Projectors

Projectors are the geometric engine behind least squares, Gram-Schmidt, and iterative methods. They "drop" part of a vector while keeping the rest.

---

## What Is a Projector?

A projector is a square matrix $P$ satisfying:

$$P^2 = P$$

Apply it once, you've projected. Apply it again, nothing changes — you're already in the subspace. This property is called **idempotence**.

**Example 1:** $P = \begin{pmatrix}1&0\\0&0\end{pmatrix}$ projects onto the $x$-axis: $P\begin{pmatrix}a\\b\end{pmatrix} = \begin{pmatrix}a\\0\end{pmatrix}$.

**Example 2:** $P = \frac{1}{2}\begin{pmatrix}1&1\\1&1\end{pmatrix}$ projects onto the line $x_1 = x_2$: $P\begin{pmatrix}a\\b\end{pmatrix} = \begin{pmatrix}\frac{a+b}{2}\\\frac{a+b}{2}\end{pmatrix}$.

---

## The Complementary Projector

If $P$ is a projector, so is $I - P$. It projects onto whatever $P$ kills:

$$v = Pv + (I - P)v$$

The first piece lives in the range of $P$, the second in the range of $I - P$. Every vector splits cleanly into "the part $P$ keeps" and "the part $P$ throws away."

---

## Orthogonal vs. Oblique Projectors

An **orthogonal projector** satisfies both $P^2 = P$ and $P^T = P$ (symmetric). The "throwing away" direction is perpendicular to the subspace.

An **oblique projector** satisfies $P^2 = P$ but $P^T \neq P$. It still projects onto a subspace, but along a non-perpendicular direction.

**Concrete comparison.** Both project onto the line $y = x$ in $\mathbb{R}^2$:

- **Orthogonal:** $P_\perp = \frac{1}{2}\begin{pmatrix}1&1\\1&1\end{pmatrix}$. For $v = (3,1)^T$: $P_\perp v = (2,2)^T$. Residual $(1,-1)^T$ is perpendicular to the target line.

- **Oblique:** $P_{\text{oblique}} = \begin{pmatrix}0&1\\0&1\end{pmatrix}$. For $v = (3,1)^T$: $P_{\text{oblique}} v = (1,1)^T$. Residual $(2,0)^T$ is horizontal, not perpendicular.

Both satisfy $P^2 = P$, but the orthogonal one gives the **closest point** on the subspace. This is why orthogonal projectors dominate numerical linear algebra: they minimize $\|v - Pv\|$.

---

## Constructing Orthogonal Projectors

Given an orthonormal basis $q_1, \ldots, q_k$ for a subspace $S$, pack them as columns of $\hat{Q}$ ($m \times k$). The orthogonal projector onto $S$ is:

$$P = \hat{Q}\hat{Q}^T$$

**Verification:**
- $P^2 = \hat{Q}\hat{Q}^T\hat{Q}\hat{Q}^T = \hat{Q}I\hat{Q}^T = P$ ✓ (since $\hat{Q}^T\hat{Q} = I_k$)
- $P^T = (\hat{Q}\hat{Q}^T)^T = \hat{Q}\hat{Q}^T = P$ ✓

**Example in $\mathbb{R}^3$:** Project onto the $xy$-plane using $q_1 = (1,0,0)^T$, $q_2 = (0,1,0)^T$:

$$P = \begin{pmatrix}1&0\\0&1\\0&0\end{pmatrix}\begin{pmatrix}1&0&0\\0&1&0\end{pmatrix} = \begin{pmatrix}1&0&0\\0&1&0\\0&0&0\end{pmatrix}$$

For $v = (3,4,5)^T$: $Pv = (3,4,0)^T$. The $z$-component is killed.

If the basis isn't orthonormal, use the general formula with a matrix $A$ whose columns span the subspace:

$$P = A(A^TA)^{-1}A^T$$

---

## Rank-1 Projectors

The simplest orthogonal projector is onto a line through a unit vector $q$:

$$P = qq^T$$

The complementary projector $I - qq^T$ projects onto the hyperplane perpendicular to $q$. The decomposition $v = qq^Tv + (I - qq^T)v$ is the atomic operation of Gram-Schmidt and Householder reflections.

---

## Properties of Orthogonal Projectors

If $P$ is an orthogonal projector onto a subspace of dimension $k$ in $\mathbb{R}^m$:

- **Eigenvalues** are only 0 and 1 (from $P^2 = P$: if $Px = \lambda x$, then $\lambda^2 = \lambda$)
- Exactly $k$ eigenvalues equal 1, and $m - k$ equal 0
- $\text{trace}(P) = k$ (sum of eigenvalues = rank)
- $\|P\|_2 = 1$ (unless $P = 0$)
- $Pv$ is the **closest point** in the subspace to $v$

---

# Lecture 7: QR Factorization

The QR factorization is the constructive version of "find an orthonormal basis for the column space." It is Gram-Schmidt orthogonalization written in matrix language.

---

## The Statement

Any $m \times n$ matrix $A$ with $m \geq n$ can be factored as:

$$A = \hat{Q}\hat{R}$$

where $\hat{Q}$ is $m \times n$ with orthonormal columns and $\hat{R}$ is $n \times n$ upper triangular. This is the **reduced QR factorization**.

The **full QR** is $A = QR$ where $Q$ is $m \times m$ orthogonal and $R$ is $m \times n$ upper triangular (padded with zero rows).

---

## Geometric Meaning

The columns $a_1, a_2, \ldots, a_n$ of $A$ get replaced by orthonormal vectors $q_1, q_2, \ldots, q_n$ such that:

- $q_1$ spans the same line as $a_1$
- $q_1, q_2$ span the same plane as $a_1, a_2$
- $q_1, q_2, q_3$ span the same 3D subspace as $a_1, a_2, a_3$
- ...and so on

The $R$ matrix records how to get back: each $a_j$ is a linear combination of $q_1, \ldots, q_j$, and the sequential construction makes $R$ upper triangular.

---

## Concrete $3 \times 2$ Example

$$A = \begin{pmatrix}1&1\\0&1\\1&0\end{pmatrix}$$

**Step 1:** Normalize $a_1$: $q_1 = \frac{a_1}{\|a_1\|} = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\0\\1\end{pmatrix}$

**Step 2:** Remove the $q_1$ component from $a_2$, then normalize.

$q_1^T a_2 = \frac{1}{\sqrt{2}}$, subtract: $a_2 - (q_1^Ta_2)q_1 = \begin{pmatrix}\frac{1}{2}\\1\\-\frac{1}{2}\end{pmatrix}$

Normalize: $q_2 = \frac{1}{\sqrt{6}}\begin{pmatrix}1\\2\\-1\end{pmatrix}$

**Result:**

$$\hat{Q} = \begin{pmatrix}\frac{1}{\sqrt{2}}&\frac{1}{\sqrt{6}}\\0&\frac{2}{\sqrt{6}}\\\frac{1}{\sqrt{2}}&\frac{-1}{\sqrt{6}}\end{pmatrix}, \qquad \hat{R} = \begin{pmatrix}\sqrt{2}&\frac{1}{\sqrt{2}}\\0&\sqrt{\frac{3}{2}}\end{pmatrix}$$

Check: $\hat{Q}\hat{R} = A$ ✓, columns of $\hat{Q}$ are orthonormal ✓, $\hat{R}$ is upper triangular ✓.

---

## Reading the $R$ Factor

- **Diagonal entry $r_{jj}$:** the norm of what's left of $a_j$ after removing components along $q_1, \ldots, q_{j-1}$. This is the "new information" in $a_j$.
- **Off-diagonal entry $r_{ij}$ ($i < j$):** the component of $a_j$ along $q_i$. How much of $a_j$ was already explained by earlier directions.
- If $r_{jj}$ is zero (or tiny), $a_j$ was (nearly) linearly dependent on the preceding columns — the rank is deficient.

---

## Reduced vs. Full QR

For the example above, the full QR adds $q_3 = \frac{1}{\sqrt{3}}(1,-1,-1)^T$ to make $Q$ a $3 \times 3$ orthogonal matrix. This $q_3$ spans the left nullspace of $A$.

**When to use which:**
- **Reduced $(\hat{Q}\hat{R})$:** solving least squares, computing column spaces. Almost always what you want.
- **Full $(QR)$:** when you need the orthogonal complement (left nullspace), or theoretical arguments requiring a square orthogonal matrix.

---

## Uniqueness

If $A$ has full column rank, the reduced QR factorization is **unique** provided we require the diagonal entries of $\hat{R}$ to be positive (analogous to requiring $r > 0$ in polar coordinates).

---

## Connection to Gram-Schmidt

The construction above is the **classical Gram-Schmidt** algorithm. Lecture 8 covers the modified version (better numerics), and Lectures 10–11 introduce Householder reflections (even better numerics). The three approaches differ in *how* they compute the factorization, not *what* they compute.

---

## Why QR Matters: Solving Least Squares

Given an overdetermined system $Ax \approx b$, the least squares solution minimizes $\|Ax - b\|_2$.

With $A = \hat{Q}\hat{R}$:

$$\|Ax - b\|_2 = \|\hat{Q}\hat{R}x - b\|_2$$

Since multiplying by $Q^T$ preserves norms:

$$= \|\hat{R}x - \hat{Q}^Tb\|_2$$

Since $\hat{R}$ is square upper triangular (invertible for full-rank $A$), just solve:

$$\hat{R}x = \hat{Q}^Tb$$

by back-substitution. No need to form $A^TA$ (which squares the condition number).

**Concrete example:** Fit a line $y = c_1 + c_2 t$ through $(0,1)$, $(1,2)$, $(2,4)$:

$$A = \begin{pmatrix}1&0\\1&1\\1&2\end{pmatrix}, \quad b = \begin{pmatrix}1\\2\\4\end{pmatrix}$$

Compute $\hat{Q}\hat{R}$, then solve $\hat{R}x = \hat{Q}^Tb$.

---

## The Takeaway

QR factorization is the constructive version of "find an orthonormal basis for the column space." $Q$ gives the basis, $R$ tells you how the original columns decompose into that basis, and the triangular structure makes solving systems cheap. It's the foundation of stable least squares solving and the starting point for eigenvalue algorithms.
