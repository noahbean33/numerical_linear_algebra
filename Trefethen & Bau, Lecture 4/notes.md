# Lecture 4: The Singular Value Decomposition (SVD)

This is the most important factorization in the book. The SVD says: **every matrix, no matter how ugly, is just a rotation, then a stretch along the axes, then another rotation.**

---

## The Statement

Any $m \times n$ matrix $A$ (real or complex, any shape) can be factored as:

$$A = U \Sigma V^T$$

where:

- $V$ is $n \times n$ orthogonal — rotates/reflects the input space
- $\Sigma$ is $m \times n$ diagonal — stretches along each axis by $\sigma_1 \geq \sigma_2 \geq \cdots \geq \sigma_p \geq 0$ (where $p = \min(m,n)$)
- $U$ is $m \times m$ orthogonal — rotates/reflects the output space

The $\sigma_i$ are the **singular values**. The columns of $U$ are **left singular vectors**. The columns of $V$ are **right singular vectors**.

---

## Concrete Examples

### Diagonal matrix

$$A = \begin{pmatrix} 3 & 0 \\ 0 & 1 \end{pmatrix}$$

Already diagonal, so the SVD is trivial: $U = I$, $\Sigma = A$, $V = I$. Singular values: $\sigma_1 = 3$, $\sigma_2 = 1$. The matrix turns the unit circle into an ellipse with semi-axes 3 and 1.

### Non-diagonal symmetric matrix

$$A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$$

Eigenvalues are 3 and 1 (symmetric, so singular values = absolute eigenvalues):

$$A = \frac{1}{\sqrt{2}}\begin{pmatrix}1&1\\1&-1\end{pmatrix} \begin{pmatrix}3&0\\0&1\end{pmatrix} \frac{1}{\sqrt{2}}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$$

Geometrically:

1. $V^T$ rotates 45° — aligns the input with the "natural axes" of $A$
2. $\Sigma$ stretches by 3 along one axis, 1 along the other
3. $U$ rotates back 45°

The unit circle maps to an ellipse with semi-axes 3 and 1, oriented at 45°.

---

## The Geometry: Circles Become Ellipses

This is the key picture of the lecture. Take the unit sphere $\{x : \|x\| = 1\}$ in $\mathbb{R}^n$. Apply $A$. You get an ellipsoid (possibly squashed into a lower dimension) in $\mathbb{R}^m$.

- The **lengths** of the semi-axes are $\sigma_1, \sigma_2, \ldots$
- The **directions** of the semi-axes are the columns of $U$
- The input directions that map onto these axes are the columns of $V$

So $\sigma_1$ is the longest axis — that's $\|A\|_2$, the maximum stretch. $\sigma_p$ is the shortest axis — the minimum stretch.

---

## Rectangular Matrices

The SVD works even when $A$ isn't square. For a $3 \times 2$ embedding matrix:

$$A = \begin{pmatrix} 1 & 0 \\ 0 & 1 \\ 0 & 0 \end{pmatrix}$$

This embeds $\mathbb{R}^2$ into $\mathbb{R}^3$. The SVD has $\sigma_1 = \sigma_2 = 1$. The unit circle in $\mathbb{R}^2$ maps to a unit circle in the $xy$-plane of $\mathbb{R}^3$. No distortion, just embedding.

### Full vs. Thin SVD

For a tall matrix ($m > n$), the last $m - n$ columns of $U$ describe the orthogonal complement of the range — dead weight that doesn't affect $A$. The **thin (reduced) SVD** drops them:

$$A = U_1 \Sigma_1 V^T$$

where $U_1$ is $m \times n$ with orthonormal columns, and $\Sigma_1$ is $n \times n$ diagonal.

**Important distinction:** $U_1^* U_1 = I_n$ (orthonormal columns), but $U_1 U_1^* \neq I_m$ (not a unitary matrix since it isn't square). The product $U_1 U_1^*$ is actually the orthogonal projector onto the column space of $A$.

---

## What the Singular Values Tell You

- **Rank:** The number of nonzero singular values equals the rank.
- **2-norm:** $\|A\|_2 = \sigma_1$ (maximum stretch).
- **Frobenius norm:** $\|A\|_F = \sqrt{\sigma_1^2 + \sigma_2^2 + \cdots + \sigma_p^2}$ (total stretch).
- **Inverse norm:** If $A$ is invertible, $\|A^{-1}\|_2 = 1/\sigma_n$.
- **Condition number:** $\kappa(A) = \sigma_1 / \sigma_n$. If $\kappa = 10^{10}$, solving $Ax = b$ loses about 10 digits of accuracy in floating point.

---

## The Rank-$k$ Approximation (Eckart–Young Theorem)

Write the SVD as a sum of rank-1 outer products:

$$A = \sigma_1 u_1 v_1^T + \sigma_2 u_2 v_2^T + \cdots + \sigma_r u_r v_r^T$$

The best rank-$k$ approximation to $A$ (in both 2-norm and Frobenius norm) is simply:

$$A_k = \sigma_1 u_1 v_1^T + \cdots + \sigma_k u_k v_k^T$$

Just truncate the sum. The error is $\sigma_{k+1}$.

**Concrete example — image compression.** A $1000 \times 1000$ grayscale image stored as a matrix. Full storage: 1,000,000 numbers. Keeping the top 50 SVD terms:

- Storage: $50 \times (1000 + 1000) = 100{,}000$ numbers (10% of original)
- The SVD found the 50 most important "patterns" (each a rank-1 outer product) and discarded the rest as fine detail.

---

## Connection to the Four Fundamental Subspaces

The SVD makes all four subspaces explicit. If $A$ has rank $r$:

- **Range (column space):** spanned by $u_1, \ldots, u_r$ — directions $A$ can actually produce.
- **Nullspace:** spanned by $v_{r+1}, \ldots, v_n$ — inputs that get killed.
- **Row space:** spanned by $v_1, \ldots, v_r$ — inputs that produce nontrivial output.
- **Left nullspace:** spanned by $u_{r+1}, \ldots, u_m$ — output directions $A$ can never reach.

---

## The Takeaway

The SVD is the universal structure theorem for matrices. It decomposes any linear map into its essential geometry: which directions get stretched, by how much, and where they end up. Every major concept — rank, norms, condition number, best approximation, the four subspaces — falls out as a direct corollary. The rest of the book is largely about how to compute this factorization and its relatives efficiently and stably.
