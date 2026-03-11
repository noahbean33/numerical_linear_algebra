# Lecture 9: Numerical Conditioning and Stability of $Ax = b$

---

## 1. Overview of Modern Numerical Solvers

In contemporary scientific computing, languages like **MATLAB** and **Python** provide "bulletproof" and stable algorithms for solving linear systems. While numerical linear algebra textbooks from the 1980s required manual tuning of algorithms for stability, modern off-the-shelf tools are designed to be well-conditioned and robust.

- **Robustness:** It is intentionally difficult to "break" $Ax = b$ solvers in these environments.
- **Backslash Command (`\`):** This is a highly intelligent operator that automatically detects the structure of a matrix — whether it is overdetermined, underdetermined, or square — and applies the most efficient, stable solution strategy.

---

## 2. Solution Strategies by System Type

The behavior of solvers changes significantly depending on the dimensions of the matrix $A$.

| System Type | Dimensions | Characteristics | Solver Behavior |
|---|---|---|---|
| **Overdetermined** | Rows > Cols ($40 \times 20$) | More constraints than unknowns. | Backslash is equivalent to the **pseudo-inverse**; both provide a least-squares fit. |
| **Underdetermined** | Rows < Cols ($20 \times 40$) | More unknowns than constraints. | Backslash uses **QR pivoting** (often yields sparse solutions), whereas the pseudo-inverse provides a least-squares solution. |
| **Square** | Rows = Cols ($40 \times 40$) | Standard linear system. | Backslash typically utilizes **LU decomposition**. |

---

## 3. Diagnosing "Bad" Problems: Determinants vs. Condition Numbers

A critical lesson in numerical linear algebra is that the **determinant** is an unreliable metric for assessing the solvability of a system.

- **The Determinant Trap:** In a singular matrix (where columns are identical), the determinant should theoretically be zero. However, due to numerical instability, a singular $40 \times 40$ matrix might still return a massive determinant (e.g., $10^6$), leading a user to falsely believe the system is well-posed.
- **Condition Number:** This is the ratio of the largest singular value to the smallest. It is the "gold standard" for evaluating stability.
  - **Well-conditioned:** Condition numbers around 1–100.
  - **Ill-conditioned:** Condition numbers near $10^{15}$ to $10^{17}$ indicate the system is effectively singular.

---

## 4. Breaking and "Fixing" the Solver

To demonstrate conditioning, the lecture examines a system where the last column of $A$ is an exact copy of the first (making it rank deficient).

- **The "Broken" State:** The solver will issue a warning that the matrix is close to singular. It still attempts a solution, but the results are untrustworthy, often reaching magnitudes of $10^{15}$.
- **Regularization via Noise:** Adding a tiny amount of random noise (e.g., $10^{-14}$) to the identical column "ticks" the matrix back into a solvable state.
  - Adding noise can drop the condition number by 13 orders of magnitude.
  - The resulting solution stabilizes from $10^{15}$ down to order 1 values.
- **Noise Sensitivity:** While noise makes the system solvable, the specific "middle" values of the solution vector remain sensitive to the specific realization of the noise used.

---

## 5. Practical Stability and QR Decomposition

The **QR decomposition** (specifically using Householder triangularization) is highlighted as an exceptionally stable method for solving $Ax = b$.

- **Algorithm Path:** $A = QR \to Qy = b \to Rx = y$. Because $R$ is upper triangular, the final step uses back substitution, which is computationally efficient.
- **The $10^{14}$ Rule:** Generally, you only need to worry about the validity of your solution if the condition number exceeds $10^{14}$. If it is lower, even if "large" (like $10^{11}$), the modern algorithms typically yield perfectly fine answers.

> **Conclusion:** While you must be a "responsible citizen" and respect solver warnings, modern numerical tools are designed to allow you to focus on science rather than fearing the collapse of your code.
