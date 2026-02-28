# Lecture 20: Gaussian Elimination

## The Idea

Gaussian elimination factors a square matrix as $A = LU$, where $L$ is lower triangular and $U$ is upper triangular. Solving $Ax = b$ reduces to two triangular solves: $Ly = b$ (forward substitution), then $Ux = y$ (back substitution). Both are $O(n^2)$; the expensive part is the $O(n^3)$ factorization, done once.

## What It Actually Does

Eliminate entries below the diagonal column by column using row operations. Each row operation is "subtract a multiple of row $k$ from row $j$," and that multiple (the **multiplier**) gets stored in $L$.

**Concrete example:**

$$A = \begin{pmatrix}2&1&1\\4&3&3\\8&7&9\end{pmatrix}$$

**Step 1:** Eliminate below $a_{11} = 2$. Multipliers: $\ell_{21} = 2$, $\ell_{31} = 4$.

**Step 2:** Eliminate below $a_{22} = 1$. Multiplier: $\ell_{32} = 3$.

$$L = \begin{pmatrix}1&0&0\\2&1&0\\4&3&1\end{pmatrix}, \quad U = \begin{pmatrix}2&1&1\\0&1&1\\0&0&2\end{pmatrix}$$

The multipliers go exactly where the zeros were created. Inverting $L_k$ just flips the signs; multiplying them together **interleaves** the multipliers without interaction.

## Solving $Ax = b$

1. $Ly = b$: forward substitution ($O(n^2)$)
2. $Ux = y$: back substitution ($O(n^2)$)

## Operation Count

| Operation | Cost |
|---|---|
| LU factorization | $\frac{2}{3}n^3$ |
| Each triangular solve | $n^2$ |
| QR factorization | $\frac{4}{3}n^3$ |

LU is about twice as fast as QR for square systems.

## The Problem: Instability Without Pivoting

If a pivot is zero → division by zero. If it's small → huge multipliers amplify rounding errors.

**Disaster example:** $A = \begin{pmatrix}10^{-20}&1\\1&1\end{pmatrix}$. Multiplier $= 10^{20}$. Swapping the two rows fixes everything.

---

# Lecture 21: Pivoting

## Partial Pivoting

At step $k$, swap the row with the largest absolute value (in column $k$, at or below diagonal) into the pivot position. This guarantees $|\ell_{jk}| \leq 1$.

**Factorization:** $PA = LU$, where $P$ is a permutation matrix.

## Growth Factor

$$\|\delta A\| \lesssim \rho_n \cdot \epsilon_{\text{machine}} \cdot \|A\|$$

Worst case: $\rho_n \leq 2^{n-1}$ (exponential!). **But in practice this never happens.** Typical $\rho_n \sim O(n^{1/2})$ to $O(n)$. The exponential bound is achieved only by pathological constructions.

## Complete Pivoting

Search the entire remaining submatrix; swap both rows and columns: $PAQ = LU$. Growth bound improves to $\sim O(n^{1/2}\log^{1/2}n)$, but $O(n^3)$ comparisons make it ~2× more expensive. Almost never needed.

## Backward Stability

With partial pivoting (in practice):

$$\frac{\|\tilde{x} - x\|}{\|x\|} \lesssim \kappa(A) \cdot \epsilon_{\text{machine}}$$

Same guarantee as Householder QR, at half the cost.

## The Wilkinson Matrix

The matrix $A$ with $-1$'s below the diagonal, $1$'s on the diagonal and last column, causes $\rho_n = 2^{n-1}$ with partial pivoting. For $n = 53$: $\rho \approx 2^{52} \approx \epsilon_{\text{machine}}^{-1}$, giving ~1% error despite $\kappa(A) \approx 24$. QR has no trouble.

---

# Lecture 23: Cholesky Factorization

## The Setup

When $A$ is **symmetric positive definite (SPD)** — $A = A^T$ and $x^TAx > 0$ for all $x \neq 0$ — you get a specialized factorization: faster, more stable, no pivoting needed.

## Where SPD Matrices Arise

- $A^TA$ (full column rank)
- Covariance matrices
- Stiffness matrices (FEM)
- Discretized Laplacians
- Kernel/Gram matrices (ML)

## The Factorization

$$A = R^*R \quad (= R^TR \text{ for real})$$

$R$ upper triangular with positive diagonal. Unique.

**Algorithm:** square root for diagonal, divide for off-diagonals, subtract rank-1 outer product, recurse.

## Why No Pivoting

All pivots are guaranteed positive (Schur complements of SPD matrices are SPD). No searching, no permutations, completely predictable.

## Cost

$$\sim \frac{1}{3}n^3 \text{ flops}$$

Half of LU, quarter of QR.

## Stability

Backward stable without pivoting. Growth factor is exactly 1 — entries never grow. Best possible stability.

## Cholesky as SPD Test

If Cholesky succeeds → $A$ is SPD. If it encounters a non-positive square root → not SPD. Cheapest reliable test.

## Connection to Normal Equations

$A^TA$ is SPD → Cholesky is the natural solver. Total cost: $mn^2 + \frac{1}{3}n^3$. Cheapest least squares method, but squares $\kappa$.

## Connection to SVD

For SPD: eigenvalues = singular values. $\kappa(R) = \sqrt{\kappa(A)}$ — Cholesky takes the square root of the condition number.

## The Takeaway

Cholesky is the gold standard for SPD: half the cost of LU, no pivoting, perfectly stable, growth factor provably 1. The happy case where structure gives you everything for free.
