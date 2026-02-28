# Lecture 19: Stability of Least Squares Algorithms

This lecture asks: of the methods for solving least squares (normal equations, Householder QR, SVD), which ones are backward stable, and what does that mean concretely for accuracy? The answer: Householder QR is backward stable; normal equations are not.

---

## The Setup

Given $A \in \mathbb{R}^{m \times n}$ ($m \geq n$, full rank) and $b \in \mathbb{R}^m$, find:

$$x^* = \arg\min_x \|b - Ax\|_2$$

In floating point you get $\tilde{x}$ instead of $x^*$. How close is it?

---

## Two Subproblems, Two Condition Numbers

Least squares involves **two** subproblems with different conditioning — a subtlety absent from square systems.

**Subproblem 1: Finding $y = Ax^*$ (projection of $b$ onto the column space).**

$$\kappa_{\text{projection}} \sim \kappa(A) / \cos\theta$$

where $\theta$ is the angle between $b$ and the column space. Small residual ($\theta \approx 0$): well-conditioned. Large residual ($\theta \approx \pi/2$): worse.

**Subproblem 2: Finding $x^*$ from $y = Ax^*$.** Condition number $\kappa(A)$.

**Overall sensitivity:**

$$\kappa_{\text{least squares}} \sim \kappa(A) + \kappa(A)^2 \tan\theta$$

- **Small residual:** $\tan\theta \approx 0$, effective $\kappa \approx \kappa(A)$. Behaves like a square system.
- **Large residual:** $\tan\theta \sim 1$, effective $\kappa \approx \kappa(A)^2$. Much harder. This is inherent — no algorithm can avoid it.

---

## Backward Stability of Householder QR

Householder QR computes $\tilde{x}$ that is the **exact** least squares solution of a slightly perturbed problem:

$$\tilde{x} = \arg\min_x \|(b + \delta b) - (A + \delta A)x\|_2$$

with $\|\delta A\|/\|A\| = O(\epsilon_{\text{machine}})$ and $\|\delta b\|/\|b\| = O(\epsilon_{\text{machine}})$.

Forward error:

$$\frac{\|\tilde{x} - x^*\|}{\|x^*\|} \lesssim \left(\kappa(A) + \kappa(A)^2 \tan\theta\right) \epsilon_{\text{machine}}$$

---

## Why Normal Equations Are NOT Backward Stable

Forming $A^TA$ **squares the condition number**: $\kappa(A^TA) = \kappa(A)^2$.

Cholesky on $A^TAx = A^Tb$ is backward stable for the $n \times n$ system, but a perturbation of relative size $\epsilon$ to $A^TA$ corresponds to $\sim \kappa(A) \cdot \epsilon$ in $A$. The effective backward error in $A$ is $O(\kappa(A) \cdot \epsilon_{\text{machine}})$.

**Concrete disaster.** $A$ is $100 \times 10$, $\kappa(A) = 10^8$, small residual:

- Householder QR: error $\lesssim 10^8 \cdot 10^{-16} = 10^{-8}$ → 8 correct digits
- Normal equations: $\kappa(A^TA) = 10^{16}$, error $\lesssim 10^{16} \cdot 10^{-16} = 1$ → **zero correct digits**

---

## Where Normal Equations Are Acceptable

If $\kappa(A)^2 \cdot \epsilon_{\text{machine}} \ll 1$, normal equations work fine and are cheaper.

**Rule of thumb:** safe when $\kappa(A) \ll 10^8$ in double precision.

**Example:** $\kappa(A) = 100 \Rightarrow \kappa(A^TA) = 10^4$, error $\sim 10^{-12}$. Twelve correct digits, and cheaper than QR ($mn^2 + n^3/3$ vs $2mn^2$).

---

## The Role of the Residual Size

The $\kappa^2 \tan\theta$ term means **large-residual problems are inherently harder**.

- **Small residual** (fitting data that nearly satisfies the model): well-determined coefficients
- **Large residual** (scattered data, poor model): coefficients wobble under perturbation

This is why in statistics, high $R^2$ (small residual) → reliable regression coefficients, low $R^2$ (large residual) → uncertain coefficients. The $\kappa^2 \tan\theta$ formula makes this precise.

---

## The T&B Experiment: Fitting $e^{\sin(4t)}$ by Degree-14 Polynomial

100 equally spaced points, Vandermonde matrix $100 \times 15$. The fit is excellent (small residual), but $\kappa(A) \approx 2.3 \times 10^{10}$.

| Method | $|x_{15} - 1|$ | Digits lost |
|---|---|---|
| Householder QR (backslash) | $\sim 10^{-7}$ | ~7 |
| Householder QR (no pivoting) | $\sim 10^{-7}$ | ~7 |
| MGS (augmented matrix trick) | $\sim 10^{-8}$ | ~8 |
| MGS (direct $Q^Tb$) | $\sim 10^{-2}$ | catastrophic |
| Normal equations | total failure | all digits |
| SVD | $\sim 10^{-8}$ | ~8 |

The MGS "augmented matrix" trick: apply MGS to $[A \; b]$ simultaneously, then solve $R_{1:n,1:n} x = R_{1:n,n+1}$. This avoids the loss from a non-orthogonal $Q$.

---

## Summary

| Method | Backward stable? | Effective $\kappa$ | Cost |
|---|---|---|---|
| Householder QR | Yes | $\kappa + \kappa^2\tan\theta$ | $2mn^2$ |
| Normal equations | No | $\kappa^2 + \kappa^2\tan\theta$ | $mn^2 + n^3/3$ |
| SVD | Yes | $\kappa + \kappa^2\tan\theta$ | $2mn^2 + 11n^3$ |

## The Takeaway

Normal equations square $\kappa$, which can be fatal. Householder QR is backward stable and achieves the best accuracy the problem allows. SVD handles rank deficiency but costs more. Use normal equations only when $\kappa(A) \ll 10^8$.
