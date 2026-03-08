# Lecture 5: More on the SVD

This lecture squeezes out the remaining consequences of the SVD. The big new ideas are the **low-rank approximation theorem**, the **pseudoinverse**, and the **polar decomposition**.

---

## Low-Rank Approximations (Eckart–Young Theorem)

The SVD writes any rank-$r$ matrix as:

$$A = \sum_{j=1}^{r} \sigma_j u_j v_j^T$$

Each $\sigma_j u_j v_j^T$ is a rank-1 "layer." The theorem says: if you want the best rank-$\nu$ approximation to $A$ (with $\nu < r$), just keep the first $\nu$ terms:

$$A_\nu = \sum_{j=1}^{\nu} \sigma_j u_j v_j^T$$

and the approximation error is:

$$\|A - A_\nu\|_2 = \sigma_{\nu+1}$$

**This is optimal.** No other rank-$\nu$ matrix gets closer to $A$ in the 2-norm.

**Concrete example.** A $4 \times 4$ matrix with singular values $\sigma_1 = 10$, $\sigma_2 = 5$, $\sigma_3 = 0.1$, $\sigma_4 = 0.01$. The best rank-2 approximation drops the last two terms, with error $\sigma_3 = 0.1$. You've discarded two dimensions but lost only 1% relative to $\|A\|_2 = 10$.

**Why this is powerful:** many real-world matrices have singular values that decay fast. A $1000 \times 1000$ matrix needs $10^6$ numbers, but if only 20 singular values are significant, a rank-20 approximation needs only $20 \times (1000 + 1000 + 1) \approx 40{,}000$ numbers — a 25× compression with minimal loss.

---

## SVD for Dimension Reduction: Congressional Voting

One of the most far-reaching applications of the SVD is dimension reduction. Given a large data matrix (e.g., congressional voting records), project onto the first few singular vectors to reveal hidden structure.

For the 111th U.S. Congress:

1. Build the voting matrix $A$ (rows = voters, columns = bills), subtract each voter's mean vote.
2. Compute the SVD of $A^T$ (tall and thin).
3. The first two singular directions capture "partisanship" and "bipartisanship."
4. Project each voter into these two coordinates — a scatter plot reveals stark political polarization with no a priori model of party.

---

## The Pseudoinverse $A^+$

When $A$ isn't square or isn't invertible, the SVD provides the next best thing.

If $A = U\Sigma V^T$ and $\Sigma$ has diagonal entries $\sigma_1, \ldots, \sigma_r, 0, \ldots, 0$, define $\Sigma^+$ by inverting the nonzero entries and transposing:

$$\sigma_i^+ = \begin{cases} 1/\sigma_i & \text{if } \sigma_i \neq 0 \\ 0 & \text{if } \sigma_i = 0 \end{cases}$$

Then:

$$A^+ = V \Sigma^+ U^T$$

### Concrete examples

**Tall matrix:** $A = \begin{pmatrix}1&0\\0&2\\0&0\end{pmatrix}$ (3×2, rank 2). Then $A^+ = \begin{pmatrix}1&0&0\\0&\frac{1}{2}&0\end{pmatrix}$ and $A^+ A = I_2$. The pseudoinverse is a left inverse.

**Rank-deficient square matrix:** $A = \begin{pmatrix}1&2\\2&4\end{pmatrix}$ has $\sigma_1 = 5$, $\sigma_2 = 0$. The pseudoinverse inverts the rank-1 part and maps the nullspace part to zero — the "best partial inverse."

---

## What $A^+$ Does for $Ax = b$

The pseudoinverse solves the least squares problem cleanly. $x^+ = A^+ b$ has two optimality properties:

1. It **minimizes** $\|Ax - b\|$ (least squares: gets as close to $b$ as possible)
2. Among all minimizers, it has the **smallest $\|x\|$** (minimum norm: picks the shortest solution)

### Overdetermined system

$$A = \begin{pmatrix}1\\1\\1\end{pmatrix}, \quad b = \begin{pmatrix}2\\3\\4\end{pmatrix}$$

No exact solution. The pseudoinverse gives $x^+ = A^+ b = (2+3+4)/3 = 3$, so $Ax^+ = (3,3,3)^T$ — the projection of $b$ onto the column space. This is least squares regression to a constant (the mean).

### Underdetermined system

$$A = \begin{pmatrix}1&1&1\end{pmatrix}, \quad b = (6)$$

Infinitely many solutions. The pseudoinverse picks $x^+ = (2,2,2)^T$ — the one closest to the origin. It spreads the "load" equally.

---

## The Polar Decomposition

Any square matrix $A$ can be written as:

$$A = UH$$

where $U$ is orthogonal (rotation/reflection) and $H$ is symmetric positive semidefinite (pure stretch).

This is the matrix analog of polar form for complex numbers: $z = e^{i\theta} \cdot r$.

**Construction from SVD:** if $A = U_{\text{svd}} \Sigma V^T$, then:

$$U = U_{\text{svd}} V^T, \qquad H = V \Sigma V^T$$

$U$ is orthogonal. $H$ is symmetric positive semidefinite (eigenvalues are the singular values).

**Why you care:** the polar decomposition isolates "rotation-like" behavior from "stretch-like" behavior. In continuum mechanics, this is the decomposition of a deformation gradient into rigid body rotation and strain. In numerical linear algebra, it clarifies what part of $A$ is "safe" (orthogonal) and what part requires care (stretching).

---

## Summary of Everything the SVD Tells You

Given $A = U\Sigma V^T$ with singular values $\sigma_1 \geq \cdots \geq \sigma_p$:

| Quantity | SVD expression |
|---|---|
| Rank | Number of nonzero $\sigma_i$ |
| 2-norm | $\sigma_1$ |
| Frobenius norm | $\sqrt{\sum \sigma_i^2}$ |
| Condition number | $\sigma_1/\sigma_r$ |
| Inverse (if exists) | $V\Sigma^{-1}U^T$ |
| Pseudoinverse | $V\Sigma^+U^T$ |
| Best rank-$k$ approx | $\sum_{i=1}^k \sigma_i u_i v_i^T$ |
| Range | $\text{span}(u_1,\ldots,u_r)$ |
| Nullspace | $\text{span}(v_{r+1},\ldots,v_n)$ |
| Determinant (square) | $\pm\prod \sigma_i$ |

---

## The Takeaway

The SVD is the Swiss Army knife: once you have it, you can read off essentially every structural property of a matrix. The pseudoinverse gives you the "best possible" solution to any linear system, whether overdetermined, underdetermined, or rank-deficient. The low-rank approximation theorem says the SVD automatically sorts information by importance, and truncation gives optimal compression. The polar decomposition separates rotation from distortion.
