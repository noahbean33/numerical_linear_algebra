# Lecture 7: Stability of Algorithms

This lecture transitions from the concept of **conditioning** (a property of the problem itself) to **stability** (a property of the numerical algorithm used to solve the problem).

---

## I. Recap: Conditioning of Problems

Before diving into stability, it is essential to distinguish it from the conditioning discussed in previous sessions:

- **Well-conditioned Problem:** A mapping where small perturbations in the input $x$ lead to small changes in the output $y$.
- **Ill-conditioned Problem:** A mapping where small changes in $x$ lead to large changes in $y$.
- **Matrix Condition Number:** For a matrix $A$, the condition number is defined as the ratio of the largest singular value to the smallest singular value:

$$\kappa(A) = \frac{\sigma_{\max}}{\sigma_{\min}}$$

- **Implications:** If the smallest singular value is zero, the condition number blows up, indicating the matrix is rank-deficient or has a determinant of zero.

---

## II. The Reality of Numerical Representation

While we conceptually think of functions $f$ as continuous mappings, computers use a **finite representation** of the number line.

- **Double Precision:** Most computational architectures represent real numbers accurately to approximately **16 decimal places**.
- **The Mapping Shift:** We must differentiate between the conceptual continuous mapping $f$ and the actual numerical approximation used by the computer, denoted as $\tilde{f}$.
- **Numerical Round-off:** Every number $x$ in a computer is an approximation $x = X + e$, where $e$ represents the numerical round-off.

---

## III. Measuring Error

To evaluate an algorithm's performance, we use two primary metrics:

| Metric | Formula | Description |
|---|---|---|
| **Absolute Error** | $\|f(x) - \tilde{f}(x)\|$ | The raw magnitude of the difference between the true and computed result. |
| **Relative Error** | $\dfrac{\|f(x) - \tilde{f}(x)\|}{\|f(x)\|}$ | The error normalized by the magnitude of the true result. |

---

## IV. Accuracy vs. Numerical Round-off

A common misconception in computing is that taking smaller steps ($\Delta t$) always leads to higher accuracy. In practice, two types of error compete:

1. **Truncation Error:** Error resulting from dropping higher-order terms in a mathematical approximation (e.g., Taylor series). This error **decreases** as $\Delta t \to 0$.
2. **Round-off Error:** Error resulting from the 16-decimal-place limit of floating-point operations. This error **increases** as $\Delta t \to 0$ because you are dividing small numbers by an increasingly small $\Delta t$.

> **Key Takeaway:** If $\Delta t$ is too small, the problem becomes "algorithmically ill-conditioned" because numerical round-off begins to dominate and blow up the total error.

---

## V. Stability: Forward vs. Backward Euler

To illustrate stability, we consider approximating the solution to the differential equation $\frac{dy}{dt} = \lambda y$.

### 1. Forward Euler (The Unstable Approach)

This scheme uses the current state to predict the future:

$$y_{n+1} = y_n + \Delta t (\lambda y_n) = (1 + \lambda \Delta t)\, y_n$$

- **Stability Condition:** If $|1 + \lambda \Delta t| > 1$, the error from initial round-off is multiplied by a factor greater than 1 at every step, eventually growing to infinity.
- **Verdict:** Generically unstable; a small initial perturbation leads to massive errors.

### 2. Backward Euler (The Stable Approach)

This scheme evaluates the right-hand side at the *future* time step:

$$y_{n+1} = y_n + \Delta t (\lambda y_{n+1})$$

Which rearranges to:

$$y_{n+1} = \frac{1}{1 - \lambda \Delta t}\, y_n$$

- **Verdict:** This algorithm is stable almost everywhere. Even though it has the same accuracy as Forward Euler, its **stability properties** make it a far superior algorithm for iterative computation.

---

**Summary:** Stability is the requirement that an iterative numerical method does not let small errors (like round-off) grow uncontrollably over time.
