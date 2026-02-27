# Lecture 1: Matrix-Vector Multiplication

## Matrix Times Vector

A matrix right-multiplied by a column vector — that is, $Ax$ — is a **linear combination of the columns of $A$**, with coefficients given by the entries of $x$.

For example, let

$$
A = \begin{pmatrix} 8 & 1 & 6 \\ 3 & 5 & 7 \\ 4 & 9 & 2 \end{pmatrix}, \quad x = \begin{pmatrix} -1 \\ 2 \\ 1 \end{pmatrix}
$$

Then:

$$
Ax = x_1 \cdot A_{:,1} + x_2 \cdot A_{:,2} + x_3 \cdot A_{:,3} = (-1)\begin{pmatrix}8\\3\\4\end{pmatrix} + (2)\begin{pmatrix}1\\5\\9\end{pmatrix} + (1)\begin{pmatrix}6\\7\\2\end{pmatrix} = \begin{pmatrix}0\\14\\16\end{pmatrix}
$$

In this context it's clear why the number of entries in $x$ has to be the same as the number of columns in $A$.

### Left-Multiplication by a Vector

If you left-multiply a matrix by a vector, it should be a row vector. Using column vectors exclusively, we transpose to get the row shape. Transposition of the product makes the interpretation clear:

$$
y^* A = (A^* y)^*
$$

which is the conjugate transpose of the columns of $A^*$, i.e., the rows of $A$.

### Linear Combinations Beyond Ordinary Vectors

Linear algebra is built in large part on linear combinations. The vectors that one combines need not be ordinary vectors in $\mathbb{C}^n$. For instance, a polynomial is a linear combination of monomials:

$$
c_0 + c_1 t + \cdots + c_n t^n = \begin{pmatrix} 1 & t & \cdots & t^n \end{pmatrix} \begin{pmatrix} c_0 \\ c_1 \\ \vdots \\ c_n \end{pmatrix}
$$

The "matrix" here is sometimes called a **quasimatrix**. From here it's a small step to imagine choosing many values of $t$ in an interval and converting the quasimatrix into a proper matrix.

---

## Matrix Times Matrix

A matrix-matrix product can be viewed as a collection of matrix-vector products. For example, if $C = AB$, then each column of $C$ is $A$ times the corresponding column of $B$:

$$
C_{:,j} = A \cdot B_{:,j}
$$

Hence the number of rows in $B$ has to be the same as the number of columns in $A$.

### Outer Product

In the special case where $A$ is a column vector $u$ and $B$ is a row vector $v^*$, the result $uv^*$ is called a **vector outer product**.

For example, with $u = \begin{pmatrix}1\\2\\3\\4\end{pmatrix}$ and $v = \begin{pmatrix}i & -i & 1\end{pmatrix}$:

$$
uv^* = \begin{pmatrix} i & -i & 1 \\ 2i & -2i & 2 \\ 3i & -3i & 3 \\ 4i & -4i & 4 \end{pmatrix}
$$

Every row is a multiple of $v^*$. Every column is a multiple of $u$. This matrix has **rank 1**.

---

## Rank and Inverse

The rank and inverse of a matrix are of critical importance in linear algebra. However, they are **not robust to perturbations**.

For example, this matrix is clearly singular and of rank 1:

$$
A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}, \quad \text{rank}(A) = 1
$$

However, any perturbation of the second row, no matter how small, mathematically changes the rank to 2 and makes the matrix invertible:

$$
B = A + \begin{pmatrix} 0 & 0 \\ 10^{-12} & 0 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 10^{-12} & 0 \end{pmatrix}, \quad \text{rank}(B) = 2
$$

In numerical computation, representation of and arithmetic with real numbers cannot be exact. Therefore, the notions of rank and invertibility must be carefully reconsidered. It is questionable whether you should ever compute a matrix rank in finite precision.

---

## Change of Basis

A matrix is the expression of a linear transformation relative to a particular basis. Unless stated otherwise, when we write out the numerical values of a matrix, we have chosen the **standard basis**, whose elements are the columns of an identity matrix.

Say we have a basis whose elements, expressed in the standard basis, are the columns of a square matrix $A$. Let a vector $v$ be given as coordinates $x_1, x_2, \ldots$ in that basis. Then we can convert the coordinates of $v$ to standard by matrix-vector multiplication:

$$
v_{\text{standard}} = A x
$$

Consequently, we can convert from standard coordinates to the "$A$-basis" through multiplication by $A^{-1}$:

$$
v_{A\text{-basis}} = A^{-1} v_{\text{standard}}
$$

> **Note:** While computing $A^{-1} b$ directly works, it is not recommended. A mathematically equivalent but computationally preferable approach is to solve $Ax = b$ (using backslash `\` in MATLAB, or `numpy.linalg.solve` in Python).

---

## Key Concepts Summary

### Two Views of $Ax$

- **Row-oriented (dot products):** Each entry of $b = Ax$ is the dot product of a row of $A$ with $x$. This is the mechanical "high school" view.
- **Column-oriented (linear combination):** $Ax$ is a linear combination of the columns of $A$, weighted by entries of $x$. This reveals where $b$ lives — in the column space of $A$.

### Rank

**Rank** is the number of linearly independent columns (or rows) of a matrix — the dimension of the output space the matrix can actually reach.

- A rank-deficient matrix collapses some dimensions.
- A full-rank square matrix is invertible.

### Range (Column Space)

The **range** of $A$ is the set of all vectors $b$ for which $Ax = b$ has a solution — everything the matrix can produce.

- For a full-rank $n \times n$ matrix, the range is all of $\mathbb{R}^n$.
- For a rank-deficient matrix, the range is a proper subspace.

### Nullspace

The **nullspace** of $A$ is the set of all inputs $x$ such that $Ax = 0$ — the inputs the matrix destroys.

- **Key relationship:** $\text{rank}(A) + \dim(\text{null}(A)) = n$ (number of columns).
- A full-rank square matrix has nullspace $= \{0\}$.

### Inverse

If $A$ is square and full-rank (nullspace $= \{0\}$, range $= \mathbb{R}^n$), then $A$ is a bijection and $A^{-1}$ reverses the map. Rank-deficient matrices are not invertible because they map distinct inputs to the same output.

### Outer Product and the SVD Connection

Any matrix can be decomposed as a sum of rank-1 outer products. The **SVD** picks the "best" rank-1 pieces ordered by importance. Truncating that sum gives optimal low-rank approximations — the foundation of dimensionality reduction, compression, and signal extraction.
