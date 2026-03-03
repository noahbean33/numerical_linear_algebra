# Lecture 20: Tensor Decompositions

---

## I. Introduction to Tensors

In standard linear algebra, we primarily work with matrices — a concept so central to the field that we often assume all data must fit into that rectangular mold. However, a **tensor** is a generalization of a matrix that allows us to represent data in higher dimensions.

- **Scalar:** 0th-order tensor.
- **Vector:** 1st-order tensor.
- **Matrix:** 2nd-order tensor.
- **Data Cube / Hypercube:** 3rd-order tensor or higher.

Most modern data analytics involves multi-dimensional structures (e.g., latitude, longitude, and elevation over time), which are naturally represented as tensors rather than flat matrices.

---

## II. The Vectorization Paradigm

Historically, to make multi-dimensional data compatible with existing linear algebra tools (like SVD or QR decomposition), we use a process called **vectorization**.

### The Process

1. **Reshaping:** Data (like a 2D image or a 3D cube) is "flattened" into a single long vector.
2. **Stacking:** For example, in the Yale Faces dataset, each 2D image is converted into a vector by stacking its columns on top of each other.
3. **Matrix Construction:** These vectors are then placed side-by-side to form a large data matrix $A$, which can then be analyzed using standard decompositions.

### The Consequences of Vectorization

While vectorization allows us to use mature, fast algorithms developed since the 1960s, it has significant drawbacks:

- **Loss of Locality:** Points that are neighbors in physical space (like adjacent pixels) can end up thousands of indices apart in a vectorized string.
- **Massive Scale:** A modest $100 \times 100 \times 100$ data cube becomes a vector of length $1{,}000{,}000$, making the resulting matrices computationally "massive".
- **Breaking Structures:** Vectorization essentially breaks the inherent spatial correlations that exist in the original data dimensions.

---

## III. Mathematical Foundation: SVD as a Sum of Outer Products

To understand how to generalize to tensors, we first view the **Singular Value Decomposition (SVD)** as a sum of rank-1 matrices.

For a matrix $A$, the SVD is given by:

$$A = U \Sigma V^*$$

We can approximate $A$ as a rank-$r$ reconstruction by summing the outer products of the singular vectors:

$$A \approx \sum_{j=1}^{r} \sigma_j (u_j v_j^*)$$

- **$u_j$:** Spans the **column space**.
- **$v_j$:** Spans the **row space**.
- **$\sigma_j$:** The weight (singular value) of that particular correlation.

---

## IV. Higher-Order Tensor Decompositions

Tensor decomposition seeks to perform a similar "low-rank" approximation without flattening the data. Instead of just row and column directions, we look for vectors that span **all $n$ directions** of the data array.

### The Tensor Approximation Formula

For a 3rd-order tensor (data cube) $\mathcal{M}$, the decomposition (often called CP decomposition or Higher-Order SVD) looks like this:

$$\mathcal{M} \approx \sum_{j=1}^{r} \sigma_j (a_j \circ b_j \circ c_j)$$

- **$a_j, b_j, c_j$:** Orthonormal vectors spanning the three different dimensions of the cube.
- **$\circ$:** Represents the outer product extended to three dimensions.
- **Advantages:** By keeping the data in its original form, things that are "close" in the data cube stay "close" in the calculation, preserving spatial correlations.

---

## V. Key Differences and Implementation

| Feature | Matrix SVD | Tensor Decomposition |
|---|---|---|
| **Uniqueness** | One unique way to decompose. | Multiple definitions and methods exist. |
| **Data Form** | Requires vectorization/flattening. | Works directly on the multi-dimensional array. |
| **Spatial Locality** | Often lost during reshaping. | Preserved within the tensor structure. |

### Software and Tools

- **MATLAB:** Use the `rand(n, n, n)` command to create tensors. Specialized packages like **"unarray"** or community codes on MathWorks Central are required as it is not always built-in.
- **Python:** Numerous libraries exist for tensor decomposition (e.g., TensorLy or NumPy-based tools).
- **The "Big" Shift:** What was considered a "big" matrix in 1995 (16x16) is now trivial; "big" today means Google-scale or Facebook-scale (trillions of entries), where these efficient decompositions are vital.

> **Note:** Unlike the SVD, which has a single established algorithm, tensor decompositions are more varied because there isn't one "perfect" way to define the process for higher dimensions.
