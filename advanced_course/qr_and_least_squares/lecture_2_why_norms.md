# Lecture 2 Supplement: Why and When to Use Different Norms

---

## 1. The $L_1$ Norm (The Sparsity King)

The $L_1$ norm (or "City Block" norm) is the most important alternative to $L_2$.

- **Purpose:** Promotes **sparsity** — forces as many components of the solution vector $x$ to be exactly zero as possible.
- **Why use it:** In fields like compressed sensing or feature selection, you often want the simplest possible model that uses only a few pieces of data.
- **Geometry:** Because the $L_1$ unit ball is a diamond, the "corners" of the diamond often intersect with the solution space exactly on the axes, which results in zero-value coordinates.

---

## 2. The $L_0$ "Norm" (The Ideal Filter)

Though technically a semi-norm, $L_0$ simply counts the number of non-zero elements in a vector.

- **Purpose:** Find the absolute minimum number of variables needed to satisfy a system.
- **The Catch:** Optimizing with $L_0$ is **NP-hard** because it requires a combinatorial search — checking every possible combination of variables.
- **Modern Use:** Researchers are currently developing manageable algorithms to approximate $L_0$ computations, but it remains a "frontier" of numerical linear algebra.

---

## 3. The $L_\infty$ Norm (The Maximum Bound)

This norm only cares about the single largest component in a vector.

- **Purpose:** Used in "worst-case scenario" engineering.
- **Use Case:** If you are designing a system where no single component can exceed a specific stress or voltage limit, you use the $L_\infty$ norm to ensure the maximum value remains within bounds.

---

## 4. Hyperparameter Tuning

In practice, you might even combine these norms. For example, in overdetermined systems, you might minimize the error using $L_2$ while simultaneously penalizing the solution with an $L_1$ norm to keep it sparse.

- **Lambda ($\lambda$):** These norms are weighted by "hyperparameters" that the user tunes to balance different features of the solution.
- **Customization:** Tuning these parameters is a routine part of training deep neural networks and other data-driven models.
