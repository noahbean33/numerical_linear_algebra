# Lecture 3: QR Decomposition

QR Decomposition is a fundamental matrix factorization technique, considered as vital to data analysis and scientific computing as the Singular Value Decomposition (SVD). While SVD provides a deep look into the structure of a matrix, QR offers a highly efficient way to solve linear systems and handle projections.

---

## I. The Core Concept: $A = QR$

The goal of QR decomposition is to factor a matrix $A$ into the product of two specific types of matrices:

- **$Q$ (Unitary/Orthogonal Matrix):** All columns are orthogonal to one another and have unit length. These matrices are ideal for computation because they are simple to invert (their inverse is just their adjoint, $Q^*$).
- **$R$ (Upper Triangular Matrix):** A matrix where all entries below the main diagonal are zero.

---

## II. Solving $Ax = b$ Using QR

Most linear algebra problems eventually boil down to solving $Ax = b$. If we have the QR decomposition of $A$, the process becomes remarkably simple:

1. **Substitute $A$:** Replace $A$ with its decomposition: $QRx = b$.
2. **Multiply by $Q^*$:** Since $Q$ is unitary, $Q^*Q = I$. Multiplying both sides by $Q^*$ gives: $Rx = Q^*b$.
3. **Define $y$:** Let $y = Q^*b$. This is a simple matrix-vector multiplication.
4. **Back Substitution:** Because $R$ is upper triangular, we can solve $Rx = y$ using back substitution.

This method is efficient because it replaces a complex matrix inversion with one matrix multiplication and one round of back substitution.

---

## III. The Power of Orthogonality

Why go through the trouble of creating an orthonormal basis ($Q$)? It all comes down to how we represent vectors.

- **Non-Orthogonal Basis:** If you have linearly independent columns $a_1, a_2, \dots, a_n$, you can represent any vector $x$ as a sum $\sum_{j=1}^{n} \alpha_j a_j$. However, finding the coefficients ($\alpha_j$) requires solving an $n \times n$ system of equations.
- **Orthonormal Basis ($Q$):** If we use orthonormal vectors $q_1, q_2, \dots, q_n$, the $n \times n$ matrix of inner products collapses into the **Identity Matrix**.
- **The Result:** Solving for the coefficients becomes "trivial". Instead of an $n \times n$ problem, you solve $n$ simple $1 \times 1$ projection problems:

$$\alpha_j = q_j^* \cdot x$$

> **Key Takeaway:** If you can reduce a problem to diagonal matrices, you've basically won the computational game.

---

## IV. The Gram-Schmidt Algorithm

The most common way to construct a QR decomposition is through **Gram-Schmidt Orthogonalization**. This is a recursive process that "strips away" non-orthogonal components:

1. **Start with $a_1$:** Normalize the first column of $A$ to get $q_1$.
2. **Find $q_2$:** Take the second column $a_2$ and subtract its projection onto the $q_1$ direction. Normalize the result to get $q_2$.
3. **Recursion:** For each subsequent vector $a_n$, subtract its projections onto all previously calculated $q$ vectors ($q_1$ through $q_{n-1}$) and normalize.

This process effectively builds the upper triangular matrix $R$ column by column as you move across the data matrix $A$.

---

## V. Variations and Properties

- **Reduced vs. Full QR:**
  - **Reduced QR:** $Q$ has $n$ columns (the same as $A$).
  - **Full QR:** $Q$ is expanded to an $m \times m$ square matrix by adding "silent" columns that are orthogonal to the data but hit by zeros in $R$.
- **Existence:** Every matrix $A$ (where rows $m \ge$ columns $n$) with linearly independent columns is guaranteed to have a QR decomposition.
- **Uniqueness:** For a specific ordering of columns, the QR decomposition is **unique**.

---

## Next Steps

While Gram-Schmidt is easy to understand, it can be numerically unstable.
