# Lecture 6: Conditioning & Stability

These notes cover the fundamental concepts of numerical analysis, specifically focusing on how algorithms and mathematical problems behave under small perturbations.

---

## 1. Core Concepts: Problem vs. Algorithm

In numerical methods, we often represent a mathematical model as a mapping from an input to an output:

$$f: X \to Y$$

Here, $x$ represents specific data instances within a broader collection $X$, which the function $f$ maps to a result $y$ in $Y$. When solving linear algebra problems, $f$ is typically a matrix multiplication ($Ax = y$).

To understand how reliable our results are, we must distinguish between **Conditioning** and **Stability**:

| Concept | Focus | Definition |
|---|---|---|
| **Conditioning** | The Problem | The behavior of the mathematical problem itself under perturbations. |
| **Stability** | The Algorithm | The behavior of a specific computational method (like Gram-Schmidt or Householder) under perturbations. |

We use different algorithms for the same problem (e.g., three ways to do QR decomposition) because some are more stable than others, preventing calculations from "blowing up" during iterations.

---

## 2. Defining Conditioning

Conditioning measures how sensitive the output $f(x)$ is to small changes in the input $x$.

- **Well-conditioned:** Small perturbations in $x$ lead to small changes in $f(x)$.
- **Ill-conditioned:** Small perturbations in $x$ lead to large changes in $f(x)$. This is problematic because results may become "complete garbage" due to numerical noise.

### Absolute Condition Number ($\hat{\kappa}$)

The absolute condition number is defined as the supremum of the ratio of the change in output to the change in input as the perturbation approaches zero:

$$\hat{\kappa} = \lim_{\delta \to 0} \sup_{\|\Delta x\| \leq \delta} \frac{\|\Delta f\|}{\|\Delta x\|}$$

If $f$ is differentiable, this is simply the norm of the Jacobian matrix ($J$) at $x$:

$$\hat{\kappa} = \|J(x)\|$$

### Relative Condition Number ($\kappa$)

In practice, we use the relative condition number because it normalizes for the scale of the data. It measures the relative change in output versus the relative change in input:

$$\kappa = \lim_{\delta \to 0} \sup_{\|\Delta x\| \leq \delta} \frac{\|\Delta f\| / \|f(x)\|}{\|\Delta x\| / \|x\|}$$

For differentiable functions, this simplifies to:

$$\kappa = \frac{\|J(x)\| \cdot \|x\|}{\|f(x)\|}$$

---

## 3. Conditioning in Linear Algebra

For the linear mapping $f(x) = Ax$, we can calculate the condition number specifically for the matrix $A$.

### Matrix Condition Number Formula

For a square, non-singular matrix $A$, the condition number is the product of the norm of $A$ and the norm of its inverse:

$$\kappa(A) = \|A\| \cdot \|A^{-1}\|$$

### Connection to Singular Value Decomposition (SVD)

The SVD provides the most practical way to compute $\kappa$.

- The norm $\|A\|$ is the largest singular value, $\sigma_1$.
- The norm $\|A^{-1}\|$ is the reciprocal of the smallest singular value, $1/\sigma_n$.

Therefore, the condition number is the ratio of the largest to smallest singular values:

$$\kappa(A) = \frac{\sigma_1}{\sigma_n}$$

---

## 4. Practical Implications

How do we interpret these numbers in a real-world computing environment?

### Numerical Thresholds

Most modern computers use double-precision arithmetic, which has a numerical roundoff of approximately $10^{-16}$.

- **$\kappa \approx 1$ to $10^2$:** Well-conditioned.
- **$\kappa \approx 10^6$ to $10^{16}$:** Ill-conditioned. If $\kappa$ is near $10^{16}$, the matrix is effectively singular, and results cannot be trusted.

### Physical Interpretation

An ill-conditioned matrix often indicates rank deficiency or redundancy.

- If the columns of $A$ are nearly the same, the determinant is close to zero.
- In this state, the condition number approaches infinity.
- Small numerical roundoff errors will be amplified significantly, making it impossible to distinguish the true solution from noise.
