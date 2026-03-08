# Lecture 2: Orthogonal Vectors and Matrices

The central claim: **unitary/orthogonal matrices are the rock-solid foundation of numerical linear algebra because they preserve geometry — lengths and angles don't get distorted.**

---

## Adjoint (Hermitian) and Transpose

With real vectors and matrices, the transpose operation is simple and familiar. It also corresponds to what we call the **adjoint** mathematically. In the complex case, one must also conjugate the entries to keep the mathematical structure intact. We call this operator the **Hermitian** of a matrix and use a star superscript $A^*$ for it.

- **Adjoint (conjugate transpose):** $A^* = \overline{A}^T$ — transpose and conjugate all entries.
- **Plain transpose:** $A^T$ — transpose without conjugation.

For real matrices, these are the same operation.

---

## Inner Products

If $u$ and $v$ are column vectors of the same length, their **inner product** is $u^* v$. The result is a scalar.

For example, with $u = \begin{pmatrix} 4 \\ -1 \\ 2+2i \end{pmatrix}$ and $v = \begin{pmatrix} -1 \\ i \\ 1 \end{pmatrix}$:

$$u^* v = \bar{4}(-1) + \overline{(-1)}(i) + \overline{(2+2i)}(1) = -4 - i + 2 - 2i = -2 - 3i$$

### Length via the 2-norm

The inner product defines length:

$$\|u\|^2 = u^* u = |4|^2 + |-1|^2 + |2+2i|^2 = 16 + 1 + 8 = 25$$

$$\|u\| = 5$$

### Angle between vectors

The angle generalizes the familiar dot product:

$$\cos\theta = \frac{u^* v}{\|u\| \, \|v\|}$$

> **Note:** The angle may be complex when the vectors are complex!

### Inverse and Hermitian commute

The operations of inverse and Hermitian commute:

$$(\text{inv}(A))^* = \text{inv}(A^*)$$

So we can unambiguously write $A^{-*}$ for either case.

---

## Orthogonality

Orthogonality, the multidimensional extension of perpendicularity, means $\cos\theta = 0$, i.e., the inner product between vectors is zero. A collection of vectors is **orthogonal** if they are all pairwise orthogonal.

### Orthonormal vectors

Vectors $q_1, q_2, \ldots, q_n$ are **orthonormal** if:

- Each has unit length: $\|q_i\| = 1$
- Each pair is perpendicular: $q_i^* q_j = 0$ for $i \neq j$

**Concrete example in $\mathbb{R}^3$:** The standard basis $e_1, e_2, e_3$.

**A more interesting example:** $q_1 = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\1\end{pmatrix}$, $q_2 = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\-1\end{pmatrix}$. Check: $q_1^T q_2 = \frac{1}{2}(1 - 1) = 0$, and both have length 1. These are the standard axes rotated 45°.

### Testing orthonormality

If $Q$ is a matrix whose columns are the vectors, then $Q^* Q$ is the matrix of all pairwise inner products. The columns are orthonormal if and only if:

$$Q^* Q = I$$

---

## Orthogonal Projections

Given any vector $u$ and a matrix $Q$ with orthonormal columns, we can decompose $u$ into two orthogonal parts:

1. **Coefficients:** $c = Q^* u$ (inner products with each column)
2. **Projection:** $v = Qc$ (the component of $u$ in the column space of $Q$)
3. **Residual:** $r = u - v$ (orthogonal to all columns of $Q$)

We have $u = v + r$ where $v$ lies in the range of $Q$ and $r$ is orthogonal to it. The residual satisfies $Q^* r \approx 0$ (exactly zero in exact arithmetic).

**General formula:** Given an orthonormal basis $q_1, \ldots, q_k$ for a subspace, the projection of $v$ onto that subspace is:

$$\hat{v} = (q_1^* v)\, q_1 + (q_2^* v)\, q_2 + \cdots + (q_k^* v)\, q_k$$

Each coefficient $q_i^* v$ measures "how much of $v$ points in the $q_i$ direction."

**Example:** Project $v = \begin{pmatrix}3\\4\\5\end{pmatrix}$ onto the $xy$-plane (spanned by $e_1, e_2$):

$$\hat{v} = 3e_1 + 4e_2 = \begin{pmatrix}3\\4\\0\end{pmatrix}$$

The residual $v - \hat{v} = \begin{pmatrix}0\\0\\5\end{pmatrix}$ is perpendicular to the subspace. **This is least squares in its purest form.**

---

## Unitary (Orthogonal) Matrices

A matrix whose columns are orthonormal becomes even more special if it is also **square** — we call it **unitary** (or **orthogonal** in the real case).

### Defining property

If $Q$ is $m \times m$ and unitary, then:

$$Q^* Q = I \quad \Longrightarrow \quad Q^* = Q^{-1}$$

**The inverse is free — just take the conjugate transpose.** No Gaussian elimination, no numerical headaches.

### Concrete example: rotation matrix

$$Q = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$$

Check $Q^T Q = I$: the diagonal gives $\cos^2\theta + \sin^2\theta = 1$ and the off-diagonal gives $0$.

### Full-rank projection

Since a unitary $Q$ has rank $m$, any vector $u \in \mathbb{C}^m$ lies in its column space. The projection residual is $r = 0$. Multiplication by $Q^* = Q^{-1}$ is a change of basis to the columns of $Q$.

---

## The Key Property: Preservation of Length

If $Q$ is orthogonal/unitary, then $\|Qx\| = \|x\|$ for every vector $x$.

**Proof in one line:** $\|Qx\|^2 = (Qx)^*(Qx) = x^* Q^* Q x = x^* x = \|x\|^2$.

**Concrete example:** Rotate $x = \begin{pmatrix}3\\4\end{pmatrix}$ by 90°:

$$Q = \begin{pmatrix}0 & -1\\1 & 0\end{pmatrix}, \quad Qx = \begin{pmatrix}-4\\3\end{pmatrix}$$

Original length: $\sqrt{9+16} = 5$. New length: $\sqrt{16+9} = 5$.

This also preserves angles and the **dot product**: $(Qx)^*(Qy) = x^* y$.

---

## Why This Matters Numerically

The big motivation is **numerical stability**. When you multiply by a matrix in floating-point arithmetic, rounding errors accumulate. The damage is proportional to how much the matrix stretches or compresses vectors. An orthogonal matrix does neither — it's a rigid motion.

**Concrete contrast:** Consider

$$A = \begin{pmatrix} 1 & 1 \\ 0 & 10^{-10} \end{pmatrix}$$

This has condition number $\approx 10^{10}$. A rounding error of $10^{-16}$ in the wrong direction gets amplified to $10^{-6}$ after multiplication by $A^{-1}$ — you lose 10 digits of accuracy.

An orthogonal matrix has **condition number exactly 1**. Errors in, same-size errors out. This is why nearly every stable algorithm in the book (QR factorization, Householder reflections, Givens rotations) is built around orthogonal matrices.

---

## The Takeaway

Orthogonal matrices are the "safe" transformations: they rotate and reflect but never distort. Trefethen's entire algorithmic strategy is to factor complicated matrices into products involving orthogonal matrices ($A = QR$, $A = U\Sigma V^T$) so the numerically dangerous parts get isolated into well-understood diagonal or triangular pieces, and the orthogonal factors can be manipulated without fear of error amplification.
