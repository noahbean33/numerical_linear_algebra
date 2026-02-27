# Lecture 3: Norms

Norms let you measure the "size" of vectors and matrices — the essential tool for saying anything quantitative about errors, convergence, or stability.

---

## Vector Norms

A norm $\|x\|$ assigns a non-negative "length" to every vector. The three you actually use:

### 1-norm (Manhattan distance)

Sum of absolute values:

$$\|x\|_1 = |x_1| + |x_2| + \cdots + |x_n|$$

For $x = \begin{pmatrix}3\\-4\\1\end{pmatrix}$: $\|x\|_1 = 3 + 4 + 1 = 8$.

Think: you're walking on a grid and can only move along axes. This is the total distance traveled.

### 2-norm (Euclidean distance)

The usual length:

$$\|x\|_2 = \sqrt{x_1^2 + x_2^2 + \cdots + x_n^2}$$

For the same $x$: $\|x\|_2 = \sqrt{9 + 16 + 1} = \sqrt{26} \approx 5.1$.

This is straight-line distance from the origin. It's the default in most of numerical linear algebra because of its connection to orthogonality ($\|Qx\|_2 = \|x\|_2$).

### $\infty$-norm (max norm)

Largest absolute entry:

$$\|x\|_\infty = \max_i |x_i|$$

For the same $x$: $\|x\|_\infty = 4$.

Think: the single worst-case component. Useful when you care about the largest entry of an error vector rather than some aggregate.

---

## Unit Balls: Geometric Intuition

The unit ball $\{x : \|x\| \leq 1\}$ in $\mathbb{R}^2$ looks different for each norm:

- **1-norm:** a diamond (rotated square) with corners at $(\pm1, 0)$ and $(0, \pm1)$
- **2-norm:** the familiar circle of radius 1
- **$\infty$-norm:** a square with corners at $(\pm1, \pm1)$

This isn't just a pretty picture. When you see a statement like "find the vector of norm $\leq 1$ that maximizes $a^T x$," the geometry of the unit ball determines the answer. The 1-norm ball has sharp corners, so optimal solutions tend to be **sparse** (one big component, rest zero) — this is why $\ell_1$ regularization promotes sparsity in compressed sensing and LASSO.

---

## Matrix Norms (Induced / Operator Norms)

A matrix norm measures how much $A$ can **stretch** vectors. The induced norm is:

$$\|A\| = \max_{x \neq 0} \frac{\|Ax\|}{\|x\|} = \max_{\|x\|=1} \|Ax\|$$

In words: find the unit-length input that produces the largest output. That maximum stretch factor is the norm of $A$.

### Concrete example

Take $A = \begin{pmatrix}2 & 0\\0 & 3\end{pmatrix}$. This scales the first axis by 2 and the second by 3. The worst-case stretch is in the $e_2$ direction: $Ae_2 = \begin{pmatrix}0\\3\end{pmatrix}$, which has length 3. So $\|A\|_2 = 3$.

For a general matrix, $\|A\|_2 = \sigma_1$ (the largest singular value).

### Simple formulas for 1-norm and $\infty$-norm

- $\|A\|_1 = $ **maximum absolute column sum**
- $\|A\|_\infty = $ **maximum absolute row sum**

For $A = \begin{pmatrix}1 & -3\\2 & 4\end{pmatrix}$:

- $\|A\|_1$: column sums are $|1|+|2|=3$ and $|-3|+|4|=7$. So $\|A\|_1 = 7$.
- $\|A\|_\infty$: row sums are $|1|+|-3|=4$ and $|2|+|4|=6$. So $\|A\|_\infty = 6$.

### Direct computation from the MATLAB examples

For $A = \begin{pmatrix}-2 & 0\\-1 & 3\end{pmatrix}$:

- $\|A\|_1 = \max(\,|-2|+|-1|,\; |0|+|3|\,) = \max(3, 3) = 3$
- $\|A\|_\infty = \max(\,|-2|+|0|,\; |-1|+|3|\,) = \max(2, 4) = 4$

---

## Key Inequalities

### The crucial inequality

$$\|Ax\| \leq \|A\| \, \|x\|$$

The output can't be bigger than the max stretch factor times the input size.

**Why you care:** if your input has error $\delta x$, the output error $A(\delta x)$ is bounded by $\|A\| \, \|\delta x\|$. If $\|A\|$ is big, small input errors cause large output errors.

### Submultiplicativity

$$\|AB\| \leq \|A\| \, \|B\|$$

If $A$ stretches by at most $\|A\|$ and $B$ by at most $\|B\|$, then $AB$ stretches by at most $\|A\|\|B\|$. The actual value might be less (stretching directions might not align), but it can't exceed the product.

---

## Equivalence of Norms

All norms on $\mathbb{R}^n$ are equivalent up to constants:

$$\|x\|_\infty \leq \|x\|_2 \leq \|x\|_1$$

$$\|x\|_1 \leq n \, \|x\|_\infty, \qquad \|x\|_2 \leq \sqrt{n} \, \|x\|_\infty$$

For $x = \begin{pmatrix}1\\1\\1\end{pmatrix}$: $\|x\|_\infty = 1$, $\|x\|_2 = \sqrt{3} \approx 1.73$, $\|x\|_1 = 3$. The gaps are exactly $\sqrt{n}$ and $n$, which is the worst case.

Convergence, boundedness, and similar qualitative statements don't depend on which norm you pick. But the quantitative bounds do, and the factors of $\sqrt{n}$ can matter a lot in high dimensions.

---

## Unitary Matrices Preserve the 2-Norm

A unitary (or real orthogonal) matrix preserves Euclidean distances: $\|Qx\|_2 = \|x\|_2$. Geometrically, they represent rotations and reflections — rigid motions that don't distort.

---

## The Takeaway

Norms let you make vague intuitions precise:

- "The error is small" becomes $\|\delta x\| < \epsilon$.
- "The matrix is well-behaved" becomes $\|A\|$ is moderate.
- "Multiplying by $Q$ is safe" becomes $\|Q\| = 1$.

Every stability and convergence theorem in the rest of the book is stated in terms of norms, so this lecture is building the language you'll need for everything that follows.
