# Lecture 12: Conditioning and Condition Numbers

This lecture draws a sharp line between two questions: **is the problem sensitive to perturbations in the data?** (conditioning) vs. **does the algorithm introduce extra errors?** (stability). This lecture is purely about the first — a property of the mathematical problem itself, not of any algorithm.

---

## The Core Idea

A problem is **well-conditioned** if small input changes cause small output changes. It's **ill-conditioned** if small input changes cause large output changes. This has nothing to do with your computer or code — it's a fact about the mathematics.

**Analogy.** $x^2 - 2x + 1 = (x-1)^2 = 0$: a perturbation of $10^{-4}$ in the constant term destroys the answer (no real roots). Ill-conditioned. Compare: $x^2 - 2x = 0$ has roots at 0 and 2; perturbing by $10^{-4}$ barely moves them. Well-conditioned.

---

## The Condition Number of a Problem

For $f: x \mapsto y$, the **relative condition number** is:

$$\kappa = \lim_{\delta \to 0} \sup_{\|\delta x\| \leq \delta} \frac{\|\delta f\| / \|f(x)\|}{\|\delta x\| / \|x\|}$$

For differentiable $f$: $\kappa = \frac{\|J(x)\| \cdot \|x\|}{\|f(x)\|}$.

### Scalar examples

- **$f(x) = x^2$:** $\kappa = 2$. Perfectly conditioned.
- **$f(x) = x - 1$ at $x = 1.00001$:** $\kappa = 100{,}001$. Catastrophic cancellation quantified.
- **$f(x) = \sqrt{x}$:** $\kappa = 1/2$. Actually contractive — square roots improve relative accuracy.

---

## The Condition Number of $Ax = b$

Given square invertible $A$, the problem $b \mapsto x = A^{-1}b$ has condition number:

$$\kappa(A) = \|A\| \cdot \|A^{-1}\| = \frac{\sigma_1}{\sigma_n}$$

### What $\kappa(A)$ means concretely

- **$\kappa = 1$ (identity):** perturbations pass through unchanged.
- **$\kappa = 100$:** lose ~2 digits.
- **$\kappa = 10^{10}$:** lose ~10 digits; about 6 correct digits in double precision.
- **$\kappa \geq 10^{16}$:** hopeless in double precision.

**Rule of thumb:** $\kappa(A) \approx 10^k$ → expect $16 - k$ correct digits in double precision.

### The Hilbert matrix

| Size | $\kappa(H_n)$ | Digits lost |
|---|---|---|
| $n = 5$ | $4.8 \times 10^5$ | ~6 |
| $n = 10$ | $1.6 \times 10^{13}$ | ~13 |
| $n = 15$ | $3.7 \times 10^{17}$ | all of them |

### Geometry of ill-conditioning

The SVD maps the unit sphere to an ellipsoid with semi-axes $\sigma_1, \ldots, \sigma_n$. Large $\kappa$ means the ellipsoid is extremely elongated. Perturbations near the thin direction cause wild jumps in the solution.

---

## Conditioning vs. Stability

- **Conditioning** = sensitivity of the *problem*. Property of the mathematics. Can't fix with a better algorithm.
- **Stability** = accuracy of the *algorithm*. Property of the method. *Can* fix by choosing better.

A well-conditioned problem + unstable algorithm = bad results (fixable). An ill-conditioned problem + stable algorithm = bad results (unfixable).

---

# Lecture 13: Floating Point Arithmetic

How computers represent and manipulate real numbers, and why every computation introduces tiny errors.

---

## The Representation

IEEE double precision:

$$\pm 1.d_1 d_2 \ldots d_{52} \times 2^e$$

- 53 bits of mantissa (~16 decimal digits)
- Exponent range: $-1022$ to $+1023$
- Smallest positive normal: $\sim 2.2 \times 10^{-308}$
- Largest: $\sim 1.8 \times 10^{308}$

**Machine epsilon:** $\epsilon_{\text{machine}} = 2^{-52} \approx 1.11 \times 10^{-16}$ — the gap between 1 and the next representable number.

---

## Relative, Not Absolute

The gaps in the floating point number line are relative. Near 1, spacing is $\sim 10^{-16}$. Near $10^{10}$, spacing is $\sim 10^{-6}$. Same relative precision (~16 digits) everywhere.

---

## The Fundamental Axiom

$$\text{fl}(x) = x(1 + \epsilon), \quad |\epsilon| \leq \epsilon_{\text{machine}}$$

Each arithmetic operation is computed exactly then rounded:

$$\text{fl}(x \mathbin{\text{op}} y) = (x \mathbin{\text{op}} y)(1 + \epsilon), \quad |\epsilon| \leq \epsilon_{\text{machine}}$$

---

## Catastrophic Cancellation

Subtracting nearly equal numbers destroys relative accuracy.

**Example:** $f(x) = \sqrt{1+x} - 1$ at $x = 10^{-14}$. Both operands have 16 digits, but agree in 14. Subtraction leaves only 2 digits of real information.

**Fix:** Rationalize: $\frac{x}{\sqrt{1+x}+1}$. No cancellation, full precision.

**Quadratic formula example:** $x^2 - 10^8 x + 1 = 0$. Standard formula gives $r_2 = 0$ (wrong). Fix: compute $r_1$ via the non-cancelling branch, then $r_2 = 1/r_1$ via Vieta's formula.

---

## Floating Point Is Not Associative

$a = 1$, $b = c = 10^{-16}$: $(a + b) + c = 1$ but $a + (b + c) = 1 + 2\epsilon$. Order matters — add small numbers first.

---

## Connection to Conditioning

Stable algorithm: $\frac{\|\hat{x} - x\|}{\|x\|} \lesssim \kappa(A) \cdot \epsilon_{\text{machine}}$

Unstable algorithm: $\frac{\|\hat{x} - x\|}{\|x\|} \lesssim f(n) \cdot \kappa(A) \cdot \epsilon_{\text{machine}}$

The goal: make $f(n)$ as close to 1 as possible.

---

## The Takeaway

Every operation is accurate to ~16 digits individually, but errors accumulate. The dangerous pattern is cancellation. The fundamental accuracy limit is $\kappa \cdot \epsilon_{\text{machine}}$. You can't reduce $\epsilon_{\text{machine}}$ (hardware) or usually $\kappa$ (the problem). What you *can* control is whether your algorithm stays close to this limit or wastes digits. That's the stability question (Lecture 14).
