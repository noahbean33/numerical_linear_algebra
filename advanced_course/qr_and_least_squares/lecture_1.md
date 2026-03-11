# Lecture 1: Applied Linear Algebra & Matrix Decompositions

This lecture introduces the central theme of the course: solving the linear system $Ax = b$ at scale using matrix decompositions. While simple in concept, solving these systems efficiently is the foundation of modern data science and scientific computing.

---

## 1. The Challenge of Scale

In contemporary data science (e.g., at Google, Facebook, or Amazon), the matrix $A$ can reach dimensions of trillions by trillions.

- **Gaussian Elimination:** This standard method learned in basic linear algebra is $O(n^3)$.
- **The Problem:** For a billion-by-billion matrix, $O(n^3)$ results in $10^{27}$ operations, which is computationally impossible.
- **The "Career Advice":** Using $O(n^3)$ algorithms for large-scale data analysis is a sure way to get fired; scientific computing requires faster, more efficient algorithms.

---

## 2. Core Matrix Decompositions

The goal of decomposition is to break matrix $A$ into simpler parts (e.g., triangular or diagonal) to solve $Ax = b$ more rapidly.

### LU Decomposition

- **Structure:** $A = LU$, where $L$ is lower triangular and $U$ is upper triangular.
- **Method:** Instead of one hard problem, you solve two easy ones: $Ly = b$ (via forward substitution) and then $Ux = y$ (via back substitution).
- **Efficiency:** Substitution costs only $O(n^2)$. While the decomposition itself costs $O(n^3)$, you only perform it once and can reuse it for many different $b$ values.

### QR Decomposition

- **Structure:** $A = QR$, where $Q$ is a unitary matrix and $R$ is upper triangular.
- **Unitary Advantage:** A unitary matrix has orthogonal columns of unit length, meaning its inverse is simply its transpose complex conjugate ($Q^*$).
- **Method:** To solve, you compute $y = Q^*b$ and then use back substitution on $Rx = y$.

### Eigenvalue Decomposition (Eigen-Decomposition)

- **Structure:** $A = V\Lambda V^{-1}$, where $V$ contains eigenvectors and $\Lambda$ is a diagonal matrix of eigenvalues.
- **Method:** This transforms the system into a new coordinate variable $y$, where the equations become "decoupled" (independent one-by-one equations).
- **Constraint:** This decomposition is not guaranteed for every matrix and requires specific properties.

---

## 3. The "Hammer": Singular Value Decomposition (SVD)

The SVD is the most important and powerful decomposition in linear algebra.

| Feature | SVD Details |
|---|---|
| **Structure** | $A = U\Sigma V^*$, breaking $A$ into two unitary matrices ($U, V$) and one diagonal matrix ($\Sigma$). |
| **Flexibility** | Uses two different orthogonal coordinate systems, providing more freedom than the single coordinate system in eigen-decomposition. |
| **Universality** | Guaranteed to work for any matrix: square, non-square, singular, complex, or otherwise. |
| **Solving** | Projects $x$ and $b$ into new embeddings ($\hat{x}$ and $\hat{b}$) where the system is diagonal and trivial to solve. |

---

## 4. Other Specialized Decompositions

- **Schur Decomposition:** Used for square matrices.
- **Cholesky Decomposition:** An extremely fast method used specifically for square and symmetric matrices.

---

## Summary: Computational Costs

| Method | Complexity | Note |
|---|---|---|
| Gaussian Elimination | $O(n^3)$ | Slowest; avoid for large systems. |
| Substitution ($L$ or $U$) | $O(n^2)$ | Rapid; used after decomposition. |
| Decomposition-based Solving | $O(n^2)$ | Achieved once the matrix is factored. |
