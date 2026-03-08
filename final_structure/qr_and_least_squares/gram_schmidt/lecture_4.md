# Lecture 4: Projectors & Modified Gram-Schmidt

Today we dig into the QR Decomposition, specifically focusing on the deeper theory of projectors and how they lead us to a more stable Modified Gram-Schmidt formulation.

---

## 1. The QR Decomposition Overview

The fundamental goal is to take a set of $n$ vectors in an $m$-dimensional space (where $m \ge n$) and find an equivalent orthonormal basis.

- **Input:** A matrix $A \in \mathbb{C}^{m \times n}$ assumed to be full rank (linearly independent columns).
- **Transformation:** We find an upper triangular matrix $R$ that transforms $A$ into $Q$, where $Q$ has orthonormal columns.
- **The Equation:** $A = QR$.
- **Gram-Schmidt Foundation:** This is achieved by taking a vector, normalizing it, and then ensuring all subsequent vectors are orthogonal to the previous ones by subtracting their projections.

---

## 2. Geometric Intuition

Think of the process as a recursive subtraction of "shadows":

- **Start:** Pick the direction of the first vector $a_1$ and normalize it to get $q_1$.
- **Orthogonalize:** Take the next vector $a_2$ and subtract its projection onto $q_1$.
- **Result:** This leaves only the component of $a_2$ that is perpendicular to $q_1$, which we then normalize to get $q_2$.
- **Repeat:** For $a_3$, subtract the projections onto both $q_1$ and $q_2$, and so on.

---

## 3. Mathematical Theory of Projectors

A projector is a linear transformation that maps a vector onto a specific subspace.

### Representation of a Vector

Given a matrix $Q$ with orthonormal columns, a generic vector $x$ can be decomposed as:

$$x = r + \sum_{j=1}^n (q_j^* x)\,q_j$$

- **Subspace Component:** The summation represents the projection of $x$ onto the column space of $Q$.
- **Residual ($r$):** This component is orthogonal to the span of $Q$ and represents the information in $x$ that cannot be represented by the basis $Q$.

### The Projector Matrix

In compact linear algebra form, the projector $P$ onto the range of $Q$ is defined as:

$$P = QQ^*$$

When this matrix hits a vector $x$, it outputs the portion of $x$ that resides within the $n$-dimensional subspace.

---

## 4. Properties of Projectors

Projectors have specific algebraic characteristics that make them useful for matrix computations:

| Property | Definition | Notes |
|---|---|---|
| **Idempotency** | $P^2 = P$ | Applying a projector twice is the same as applying it once. |
| **Orthogonal vs. Oblique** | Orthogonal: $P = P^*$ | Orthogonal projectors are Hermitian (symmetric); oblique ones are not. |
| **Complementary** | $I - P$ | This is also a projector ($(I-P)^2 = I-P$). |
| **Range/Null Space** | $\text{Range}(I - P) = \text{Null}(P)$ | The complement projects onto the space orthogonal to $P$. |

**Rank One Projection:** To project onto a single unit vector $q$, use $P_q = qq^*$. To project onto the space orthogonal to $q$, use the complement: $P_{\perp q} = I - qq^*$.

---

## 5. Modified Gram-Schmidt (MGS)

While the "classical" Gram-Schmidt approach is theoretically sound, the Modified Gram-Schmidt algorithm uses these projector ideas to improve numerical stability.

### The Recursive Algorithm

Instead of subtracting all projections at once, MGS proceeds iteratively:

1. Start with $v_j = a_j$.
2. For each previous orthonormal vector $q_k$ ($k < j$), project $v_j$ onto the space orthogonal to $q_k$:

$$v_j \leftarrow (I - q_k q_k^*)\,v_j$$

This simplifies to $v_j = v_j - (q_k^* v_j)\,q_k$.

3. Once all previous components are removed, normalize the remaining vector:

$$q_j = \frac{v_j}{\|v_j\|}$$

This "modified" approach is more robust for computer execution than the classical version.
