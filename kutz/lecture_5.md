# Lecture 5: Householder Triangularization

This lecture explores the Householder triangularization, a method for matrix decomposition developed in 1958 by Alston Householder. It serves as a numerically stable alternative to the Gram-Schmidt process for achieving QR decomposition.

---

## Core Goal: QR Decomposition

The objective is to decompose a matrix $A$ into two components:

- **$Q$:** An orthonormal basis (or embedding space).
- **$R$:** An upper triangular matrix.

This decomposition is essential for solving linear systems ($Ax = b$) and finding low-rank orthonormal modes to span the space of $A$.

---

## Gram-Schmidt vs. Householder

While both methods achieve QR decomposition, they approach the problem from opposite directions.

| Feature | Gram-Schmidt | Householder |
|---|---|---|
| **Approach** | Recursive row/column construction. | Recursive matrix breakdown. |
| **Mechanism** | Right-multiplication by triangular matrices ($AR_1 R_2 \cdots = Q$). | Left-multiplication by orthogonal projectors ($Q_n \cdots Q_2 Q_1 A = R$). |
| **Concept** | Triangular Orthogonalization: Using triangular operations to get an orthogonal basis. | Orthogonal Triangularization: Using orthogonal operations to get a triangular matrix. |
| **Stability** | Less numerically stable. | Highly numerically stable and computationally efficient. |

---

## The Householder Mechanism

The process is conceptually similar to Gaussian elimination. It involves picking a "pivot" and zeroing out all elements below the diagonal, column by column.

### 1. Recursive Transformation

- **Step 1 ($Q_1 A$):** Zeros out all elements below the first diagonal entry, updating the remaining columns.
- **Step 2 ($Q_2 Q_1 A$):** Zeros out elements below the second diagonal entry while leaving the previous work (the first row and column) unchanged.
- **Final Step:** Results in a full upper triangular matrix $R$.

### 2. The Structure of the Projector ($Q_k$)

Each step uses a specific matrix $Q_k$ structured to preserve previous work:

$$Q_k = \begin{pmatrix} I_{k-1} & 0 \\ 0 & F \end{pmatrix}$$

- **$I_{k-1}$:** An identity matrix that ensures previously processed rows and columns remain untouched.
- **$F$:** The Householder reflector, a sub-matrix acting on the current subspace.
- **Properties:** $F$ (and $Q_k$) must be unitary and an orthogonal projector.

---

## Constructing the Reflector ($F$)

To zero out elements below a diagonal, $F$ must transform a vector $c$ (the current column segment) into a vector aligned with the first unit vector $e_1$ of that subspace.

### The Geometry of Reflection

The reflector $F$ takes vector $c$ and reflects it across a hyperplane ($H$) to reach the target axis. This is achieved by:

1. Projecting $c$ onto the hyperplane.
2. Moving twice the distance of that projection to reach the opposite side (the reflection).

### The Mathematical Formula

The reflector $F$ acting on a vector $y$ is defined as:

$$F = I - 2\frac{vv^*}{v^*v}$$

where $v$ is the vector defining the reflection ($v = c - \|c\|e_1$).

**Numerical Stability Note:** When projecting, one can choose to project onto $+e_1$ or $-e_1$. To ensure maximum stability, the sign is chosen to avoid "numerical round-off" errors that occur when the vector $c$ is too close to the target projection point.

---

## Algorithmic Implementation

In practice, the algorithm follows these steps:

1. Initialize $Q$ as an identity matrix.
2. Loop through each column $k$.
3. Compute the reflector $v$ for the current sub-block.
4. Update the matrix $A$ by left-multiplication and accumulate the transformations into $Q$.
5. Extract the final $R$ (triangular) and $Q$ (orthogonal) matrices.
