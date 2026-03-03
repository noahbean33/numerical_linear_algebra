# Lecture 18: Randomized Linear Algebra

This lecture introduces the concept of **Randomized Linear Algebra**, a growing field designed to address the challenges of "big data" where traditional matrix decompositions become computationally unfeasible.

---

## I. The "Big Data" Problem

In traditional linear algebra, we use decompositions like **SVD**, **QR**, and **Eigen-decompositions** to solve $Ax = b$ or find patterns (like PCA). However, modern datasets face two major bottlenecks:

1. **Memory Constraints:** Matrices ($m \times n$) are often so massive that they cannot fit into a single computer's RAM.
2. **Computational Complexity:** Standard decompositions typically scale at $O(m^3)$. Doubling the matrix size results in an **8x increase** in computation time.

**Industry Use Cases:** Companies like Google and Facebook utilize randomized algorithms because their customer databases are too large to process with standard PCA on a single machine.

---

## II. The Core Strategy: Low-Rank Approximation

The fundamental goal is to approximate a massive matrix $A$ using two smaller matrices, $E$ and $F$:

$$A \approx EF$$

- **$A$:** $m \times n$ (Massive)
- **$E$:** $m \times r$ (Tall and skinny)
- **$F$:** $r \times n$ (Short and fat)

This approach relies on the **Major Assumption** that the data contains a **low-rank structure** of dimension $r$, meaning the essential "features" can be represented in a much smaller subspace.

---

## III. The Two-Stage Randomized Process

The algorithm is split into two distinct phases to navigate the dimensionality of the data.

### Stage A: Finding the Subspace (The "In")

The goal is to find an orthonormal matrix $Q$ ($m \times k$) that spans the column space of $A$.

1. **Random Projection:** Multiply $A$ by a random matrix $\Omega$ to sample the column space.

$$Y = A\Omega$$

2. **QR Decomposition:** Perform an "economy" QR decomposition on $Y$ to get $Q$.

$$Y = QR$$

### Stage B: Computation and Reconstruction (The "Out")

Once the subspace $Q$ is found, we move the computation to a smaller scale.

1. **Projection:** Project the massive matrix $A$ into the low-dimensional space.

$$B = Q^T A$$

2. **Work:** Perform the desired decomposition (e.g., SVD) on the much smaller matrix $B$.

$$B = \tilde{U}\tilde{\Sigma}\tilde{V}^*$$

3. **Back-Projection:** Reconstruct the original space by multiplying the reduced results by $Q$.

$$U = Q\tilde{U}$$

---

## IV. Why Randomization Works

- **Orthogonality in High Dimensions:** In very high-dimensional spaces ($m, n \gg 1$), random vectors are **highly likely to be nearly orthogonal**. This allows us to sample the column space efficiently without needing to compute an expensive orthogonal basis from scratch.
- **Memory Efficiency:** To compute $Y = A\Omega$, you only need to load $A$ into memory **piece by piece** (row by row or column by column). The full matrix $A$ never needs to sit in RAM at once.
- **Speed:** By choosing $k$ (the number of random samples) slightly larger than the target rank $r$ (e.g., $k = r + 10$), we can approximate the feature space much faster than a full SVD.

---

## V. Summary of the Computational Flow

| Step | Operation | Purpose |
|---|---|---|
| 1 | $Y = A\Omega$ | Randomly sample the column space of $A$. |
| 2 | $[Q, R] = \text{qr}(Y, 0)$ | Create an orthonormal basis $Q$ for that sample. |
| 3 | $B = Q^T A$ | Project $A$ into the low-rank subspace. |
| 4 | $[\tilde{U}, \tilde{\Sigma}, \tilde{V}] = \text{svd}(B)$ | Perform SVD on the small matrix $B$. |
| 5 | $U = Q\tilde{U}$ | Recover the high-dimensional singular vectors. |

> **Crucial Metric:** The quality of the approximation is evaluated by how much information is lost during the projection:
>
> $$\|A - QQ^T A\|$$
