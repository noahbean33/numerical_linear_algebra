# Lecture 9: Practical Computation & Gram-Schmidt Stability

This is a practical interlude connecting theory to computation. The lecture originally focuses on MATLAB, but all concepts translate directly to Python/NumPy. The key experiments demonstrate the stability differences between CGS, MGS, and Householder QR.

---

## The Python/NumPy Equivalent

Python with NumPy provides the same matrix-centric environment. The core tools:

```python
import numpy as np
from scipy import linalg

A = np.array([[1, 2], [3, 4]])       # 2x2 matrix
I = np.eye(5)                         # 5x5 identity
Z = np.zeros((3, 4))                  # 3x4 of zeros
R = np.random.randn(5, 5)             # 5x5 random (normal)
D = np.diag([1, 2, 3])                # 3x3 diagonal
```

**Subarray access (slicing):**
```python
A[1, :]       # row 2 (0-indexed)
A[:, 2]       # column 3
A[0:3, 1:5]   # rows 0-2, columns 1-4
```

---

## Solving Linear Systems

NumPy's equivalent of MATLAB's backslash:

```python
x = np.linalg.solve(A, b)            # square A: uses LU
x = np.linalg.lstsq(A, b, rcond=None)[0]  # rectangular: least squares
```

**Never write** `np.linalg.inv(A) @ b`. Use `solve` or `lstsq` — they're faster and more stable.

**Factorizations:**
```python
Q, R = np.linalg.qr(A)               # reduced QR (Householder)
Q, R = np.linalg.qr(A, mode='complete')  # full QR
U, S, Vt = np.linalg.svd(A)          # full SVD
U, S, Vt = np.linalg.svd(A, full_matrices=False)  # reduced SVD
```

**Least squares — four ways (only the first three are good):**
```python
x1 = np.linalg.lstsq(A, b, rcond=None)[0]   # auto least squares
Q, R = np.linalg.qr(A); x2 = np.linalg.solve(R, Q.T @ b)  # explicit QR
x3 = np.linalg.pinv(A) @ b                   # pseudoinverse (SVD)
x4 = np.linalg.solve(A.T @ A, A.T @ b)       # normal equations (DON'T)
```

The fourth forms $A^TA$, squaring the condition number. If $\kappa(A) = 10^8$, then $\kappa(A^TA) = 10^{16}$ — all digits lost.

---

## Norms and Condition Numbers

```python
np.linalg.norm(x)            # 2-norm (default)
np.linalg.norm(x, 1)         # 1-norm
np.linalg.norm(x, np.inf)    # infinity norm
np.linalg.norm(A, 2)         # matrix 2-norm (= sigma_1)
np.linalg.norm(A, 'fro')     # Frobenius norm
np.linalg.cond(A)            # condition number
```

**The Hilbert matrix** $H_{ij} = 1/(i+j-1)$ is the classic ill-conditioned matrix. Its condition number grows exponentially with size. A $20 \times 20$ Hilbert matrix has $\kappa \approx 10^{28}$ — solving $Hx = b$ gives essentially zero correct digits in double precision.

---

## Experiment 1: Diagonal of $R$ Tracks Singular Values

Construct an $80 \times 80$ matrix with prescribed singular values $\sigma_j = 2^{-j}$ (exponential decay). The diagonal entries of $R$ from QR factorization should track these singular values — but how far?

- **MGS:** Tracks singular values until they drop to $\sim \epsilon_{\text{machine}} \approx 10^{-16}$, then levels off.
- **CGS:** Departs from the true values at $\sim \sqrt{\epsilon_{\text{machine}}} \approx 10^{-8}$ — only half the available digits.

**Single precision test ($\epsilon \approx 10^{-7}$):** The same pattern holds at the new precision level. MGS departs at $\sim 10^{-7}$, CGS at $\sim 10^{-3.5}$.

**Hypothesis:** Roundoff at precision $\epsilon$ affects MGS at level $\epsilon$, but CGS at level $\sqrt{\epsilon}$.

In Python, single precision is obtained with `A.astype(np.float32)`. Note: NumPy follows the same promotion rule as Julia — `float32 + float64 → float64` — so all intermediate arrays must also be `float32`.

---

## Experiment 2: Loss of Orthogonality with Nearly Parallel Columns

Even MGS loses orthogonality when columns are nearly parallel. Example:

$$A = \begin{pmatrix}\pi & \sqrt{2} \\ 355/113 & \sqrt{2}\end{pmatrix}$$

The columns are nearly parallel (since $355/113 \approx \pi$). After orthogonalization, the remainder is tiny ($\sim 10^{-8}$), meaning ~7 of 16 significant digits are lost to cancellation. The resulting $\|Q^TQ - I\| \approx 10^{-9}$ — far from machine precision.

This loss of orthogonality is so important that practical implementations (Arnoldi, Lanczos) re-orthogonalize regularly.

---

## Floating-Point Realities

IEEE double precision: ~16 decimal digits ($\epsilon_{\text{machine}} \approx 10^{-16}$).

```python
(1 + 1e-16) - 1    # returns 0.0, not 1e-16
(1 + 1e-15) - 1    # returns ~1.1e-15 (slightly wrong)
```

This is **catastrophic cancellation** — subtracting nearly equal numbers destroys relative accuracy. It's exactly why CGS fails: it computes small differences of large dot products.

**Checking orthogonality after Householder QR:**
```python
A = np.random.randn(100, 50)
Q, R = np.linalg.qr(A)
np.linalg.norm(Q.T @ Q - np.eye(50))   # ~1e-15 (machine precision)
```

---

## Dense vs. Sparse

A dense $10{,}000 \times 10{,}000$ matrix stores $10^8$ numbers. A sparse one with $10^5$ nonzeros stores only those, and sparse factorization can be orders of magnitude faster.

```python
from scipy import sparse
A = sparse.random(10000, 10000, density=0.001, format='csr')
```

SciPy's sparse solvers (`scipy.sparse.linalg.spsolve`) automatically exploit sparsity.

---

## Timing and Complexity

- QR on $1000 \times 1000$: fraction of a second. Complexity $\sim \frac{2}{3}mn^2$.
- SVD is more expensive: $\sim 11n^3$ for the full decomposition.
- **Rule of thumb:** doubling $n$ multiplies time by ~8 for $O(n^3)$ algorithms.

---

## The Takeaway

Use `np.linalg.solve` / `lstsq` instead of explicit inversion. Never form normal equations when you can use QR. Check condition numbers before trusting solutions. Floating-point arithmetic makes the stability distinctions from earlier lectures (CGS vs MGS vs Householder) concretely measurable — run `np.linalg.cond(hilbert(20))` and you understand ill-conditioning viscerally.
