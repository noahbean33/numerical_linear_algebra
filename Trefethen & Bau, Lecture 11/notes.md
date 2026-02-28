# Lecture 11: Least Squares Problems

This lecture answers the question: when $Ax = b$ has no solution (more equations than unknowns), what's the best $x$ you can find? The answer is the $x$ that minimizes $\|Ax - b\|_2$, and the QR factorization computes it stably.

---

## The Setup

You have an $m \times n$ system with $m > n$ (overdetermined). Generically, no exact solution exists — $b$ doesn't lie in the column space of $A$. So you minimize the residual:

$$x^* = \arg\min_x \|b - Ax\|_2$$

**Concrete example.** Fit a line $y = c_1 + c_2 t$ through $(0,1)$, $(1,3)$, $(2,2)$:

$$A = \begin{pmatrix}1&0\\1&1\\1&2\end{pmatrix}, \quad x = \begin{pmatrix}c_1\\c_2\end{pmatrix}, \quad b = \begin{pmatrix}1\\3\\2\end{pmatrix}$$

Three equations, two unknowns. No line passes through all three points, so you find the line that minimizes total squared error.

---

## The Geometry

The column space of $A$ is a subspace of $\mathbb{R}^m$. The closest point in the column space to $b$ is the orthogonal projection of $b$ onto the column space.

- $Ax^*$ is the projection of $b$ onto $\text{range}(A)$
- The residual $r = b - Ax^*$ is **perpendicular** to the column space

Perpendicular to the column space means $A^T r = 0$, giving the **normal equations**:

$$A^T(b - Ax^*) = 0 \implies A^TAx^* = A^Tb$$

For the line-fitting example:

$$A^TA = \begin{pmatrix}3&3\\3&5\end{pmatrix}, \quad A^Tb = \begin{pmatrix}6\\7\end{pmatrix}$$

Solve: $x^* = (4/3, \; 1/2)^T$. Best-fit line: $y = \frac{4}{3} + \frac{1}{2}t$.

The residual $r = b - Ax^* = (-1/3, \; 7/6, \; -1/3)^T$. Check: $A^Tr = (0, 0)^T$ ✓.

---

## Three Methods to Solve Least Squares

### Method 1: Normal Equations

Solve $A^TAx = A^Tb$ directly (e.g., Cholesky factorization).

**Cost:** $mn^2 + \frac{1}{3}n^3$ flops.

**Problem:** $\kappa(A^TA) = \kappa(A)^2$. If $\kappa(A) = 10^8$, then $\kappa(A^TA) = 10^{16}$ — exceeds machine precision. All significant digits lost.

**Concrete disaster:**

$$A = \begin{pmatrix}1&1\\10^{-4}&0\\0&10^{-4}\end{pmatrix}$$

$\kappa(A) \approx 10^4$. Then $A^TA \approx \begin{pmatrix}1&1\\1&1\end{pmatrix}$ in double precision — singular! The tiny but crucial $10^{-8}$ perturbations get wiped out.

### Method 2: QR Factorization (the right way)

Compute $A = \hat{Q}\hat{R}$ (reduced QR via Householder), then solve $\hat{R}x = \hat{Q}^Tb$ by back-substitution.

**Why this works:** Substitute into the normal equations, use $\hat{Q}^T\hat{Q} = I$, cancel $\hat{R}^T$:

$$\hat{R}^T\hat{Q}^T\hat{Q}\hat{R}x = \hat{R}^T\hat{Q}^Tb \implies \hat{R}x = \hat{Q}^Tb$$

**Cost:** $2mn^2$ flops.

**Stability:** You never form $A^TA$. The condition number stays at $\kappa(A)$, not $\kappa(A)^2$.

### Method 3: SVD

Compute $A = U\Sigma V^T$, then $x^* = V\Sigma^{-1}U^Tb$ (pseudoinverse). If $A$ has rank $r$:

$$x^* = \sum_{j=1}^{r} \frac{u_j^T b}{\sigma_j} v_j$$

**Cost:** More expensive ($\sim 2mn^2 + 11n^3$), but handles rank-deficient problems gracefully — drop terms with $\sigma_j = 0$ or $\sigma_j < \text{tolerance}$.

**When to use:** When $A$ is rank-deficient or nearly so.

---

## Geometric Picture (Unified)

The vector $b$ splits as:

$$b = \underbrace{\hat{Q}\hat{Q}^Tb}_{\text{projection} = Ax^*} + \underbrace{(I - \hat{Q}\hat{Q}^T)b}_{\text{residual } r}$$

**Key identity (Pythagorean theorem):** $\|r\|^2 = \|b\|^2 - \|\hat{Q}^Tb\|^2$

---

## Polynomial Fitting: Overfitting vs. Least Squares

Temperature anomaly data (NASA, 5-year averages, 1955–2000):

| Year | 1955 | 1960 | 1965 | 1970 | 1975 | 1980 | 1985 | 1990 | 1995 | 2000 |
|------|------|------|------|------|------|------|------|------|------|------|
| Anomaly | −0.048 | −0.018 | −0.036 | −0.012 | −0.004 | 0.118 | 0.210 | 0.332 | 0.334 | 0.456 |

**Degree-9 interpolation** (10 points, 10 unknowns): passes through every point but oscillates wildly — overfitting. The Vandermonde matrix is nearly singular ($\kappa \sim 10^{17}$).

**Degree-3 least squares** (10 points, 4 unknowns): smooth, physically reasonable fit. The $10 \times 4$ Vandermonde system is overdetermined; QR finds the 4 coefficients minimizing total squared error.

As the polynomial degree rises, the Vandermonde matrix becomes increasingly ill-conditioned — normal equations blow up, but QR stays reliable.

---

## When the Rank Is Deficient

If $A$ is $m \times n$ with rank $r < n$, the least squares problem has infinitely many minimizers. The normal equations are singular. The SVD/pseudoinverse selects the unique **minimum-norm** solution.

**Example:** $A = \begin{pmatrix}1&1\\2&2\\3&3\end{pmatrix}$, $b = (1,2,4)^T$. Rank 1. Any $x = (c_1, c_2)^T$ with $c_1 + c_2 = \text{const}$ gives the same $Ax$. The pseudoinverse picks $c_1 = c_2$ — minimum norm.

---

## The Takeaway

Least squares is the most important application of the QR factorization: project $b$ onto the column space of $A$ and solve in the orthonormal basis. The normal equations are the algebraic formulation but squaring the condition number makes them numerically dangerous. QR avoids this by never forming $A^TA$. The SVD goes further by handling rank deficiency. Virtually every data-fitting, regression, and approximation problem reduces to least squares — this is where the factorization machinery starts earning its keep.
