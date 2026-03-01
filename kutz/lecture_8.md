# Lecture 8: Conditioning of Least Squares

This lecture focuses on the conditioning and stability of the least squares problem, a fundamental aspect of scientific computing used to ensure that small perturbations in data do not lead to massive changes in solutions.

---

## 1. Problem Framework: Overdetermined Systems

The core problem addressed is the linear system $Ax = b$. In the context of least squares fitting, we assume:

- **Matrix Dimensions:** $A$ is an $m \times n$ rectangular matrix where $m > n$ (more constraints than unknowns).
- **Vector Dimensions:** $b$ is an $m \times 1$ vector, and $x$ is the $n \times 1$ solution vector to be discovered.
- **Overdetermined Nature:** Because there are more constraints than unknowns, $Ax = b$ generically cannot be satisfied exactly.
- **Full Rank Assumption:** $A$ is assumed to be full rank, meaning its columns span an $n$-dimensional space with no redundant (linearly dependent) columns.

### The Optimization Goal

Since a perfect solution is often impossible, the goal is to find an $x$ that minimizes the **residual**, specifically the $L_2$ norm between $Ax$ and $b$:

$$\min_{x} \|b - Ax\|_2$$

---

## 2. Geometric Interpretation and Key Variables

To understand conditioning, we must visualize the relationship between the range of $A$ and the target vector $b$.

- **The Range of $A$:** An $n$-dimensional subspace within an $m$-dimensional space.
- **The Projection ($y$):** The vector $y = Ax$ is the projection of $b$ onto the range of $A$.
- **The Residual:** The vector representing the difference between $b$ and $y$.
- **The Angle ($\theta$):** The angle between $b$ and its projection $y$.

> **Key Concept:** Conditioning asks how perturbations in the input data ($A$ and $b$) affect the outputs ($x$ and $y$). A problem is **ill-conditioned** if small changes in $A$ or $b$ result in wildly different solutions.

---

## 3. Metrics for Performance

Three primary quantities are defined to evaluate the conditioning of the least squares problem:

| Metric | Definition | Description | Range |
|---|---|---|---|
| **Condition Number ($\kappa$)** | $\kappa(A) = \sigma_1 / \sigma_n$ | Ratio of the largest to smallest singular values. | $1$ to $\infty$ |
| **Angle ($\theta$)** | $\cos^{-1}(\|y\| / \|b\|)$ | The angle between $b$ and the range of $A$. If $\theta = 0$, $b$ is in the range. | $0$ to $\pi/2$ |
| **Eta ($\eta$)** | $\|A\| \cdot \|x\| / \|y\|$ | The ratio of the solution norm scaled by the matrix norm to the approximation $y$. | $1$ to $\kappa(A)$ |

---

## 4. Sensitivity Theorem

The conditioning of the mapping from inputs ($A, b$) to outputs ($x, y$) can be summarized by the following sensitivities:

- **Perturbing $b$ to find $y$:** The condition number is $\dfrac{1}{\cos \theta}$.
- **Perturbing $b$ to find $x$:** The condition number is $\dfrac{\kappa(A)}{\eta \cos \theta}$.
- **Perturbing $A$ to find $y$:** Sensitive to the condition number and angle $\theta$.
- **Perturbing $A$ to find $x$:** Highly sensitive to $\kappa(A)$ and the squared condition number in certain bounds.

### Derivation Highlights

The Singular Value Decomposition (SVD) is the primary tool for these calculations. By decomposing $A = U\Sigma V^*$, we can transform the problem into a coordinate system where $A$ is diagonal.

- In this diagonal system, the projection $y$ simply "zeroes out" components of $b$ that lie outside the $n$-dimensional range of $A$.
- The solution $x$ is then constrained to the $n \times n$ non-singular subspace.

---

## 5. Summary of Practical Implications

- **Trustworthiness:** You cannot trust the result of an ill-conditioned problem because the answer can vary wildly due to tiny data errors.
- **Detection:** Use SVD to compute singular values; if the ratio $\kappa(A)$ is $10^{10}$ to $10^{16}$, the matrix is poorly conditioned.
- **Correction:** If a problem is ill-conditioned, one must seek a different algorithm or rewrite the problem to make it well-posed for scientific computing.
