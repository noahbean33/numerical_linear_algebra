# Numerical Linear Algebra in C++

## The course that should exist but doesn't.

Every numerical linear algebra course teaches you theorems in MATLAB. This one teaches you algorithms in C++. Every textbook assumes you already know why you should care. This one shows you.

You will learn numerical linear algebra the way it's actually used: implemented in C++, visualized in real time, and understood from the ground up through hand computation, geometric intuition, and working code.

**$100. ~10 hours. No prerequisites beyond basic linear algebra and some C++.**

---

## The Problem

You took linear algebra in college. You can prove that Gram-Schmidt produces an orthonormal basis. You have no idea why you'd ever use it.

You opened Trefethen and Bau. It's elegant, concise, and assumes you already have the intuition it was supposed to give you. No motivating examples. No numerical demonstrations. No connection to the code you'll actually write.

You looked at the Eigen docs. They're reference material for people who already understand everything.

You watched the free lectures on YouTube. A professor improvises at a blackboard, skips steps, and says "clearly" before the one thing that isn't clear.

There is no single resource that connects the math to the implementation to the hardware. You're expected to stitch together a theory textbook, an HPC manual, and library documentation on your own and hope the result is coherent.

This course fixes that.

---

## What You Get

Each topic follows the same structure:

**Motivation.** Why does this algorithm exist? What problem does it solve? When do you reach for it instead of something else?

**Hand calculation.** Work through a small concrete example on paper. If you can't do a 3×3 QR factorization by hand, you don't understand QR. This is where you see the mechanics, and where numerical instability stops being abstract.

**Visual intuition.** Interactive real-time visualizations built with raylib. Watch SVD decompose a unit sphere into an ellipsoid. See what ill-conditioning looks like geometrically. Rotate, scale, and transform meshes with the matrices you just computed by hand.

**C++ implementation.** Build it yourself, then see how Eigen does it. Understand expression templates, cache-aware blocking, and why loop order matters. Learn why your naive implementation is 10× slower and what the fix looks like.

**Quizzes.** Constant knowledge checks forcing active recall. Not "did you memorize the theorem" but "given this matrix, what happens and why."

---

## Topics

- Floating point arithmetic and why it breaks your math
- Vector and matrix norms — what they measure and when each one matters
- The SVD — geometrically, computationally, and practically
- Least squares and why it's half of applied mathematics
- QR factorization via Gram-Schmidt, Householder, and Givens — when to use which
- LU and Cholesky — structure you can exploit
- Conditioning and stability — why your answer is wrong and how wrong it is
- Eigenvalue algorithms — QR iteration, what LAPACK actually does
- Iterative methods — GMRES, conjugate gradient, when direct solvers stop scaling
- Performance — cache lines, loop order, SIMD, blocking, and why MATLAB hides all of it from you

---

## Who This Is For

- Engineers who took linear algebra and still don't know when to use SVD vs QR
- Programmers who can optimize memory access patterns but don't understand the math they're optimizing
- Scientists who write numerical code in Python and want to understand what's happening underneath
- Anyone who tried to learn from Trefethen and Bau and bounced off the wall of unmotivated abstraction

## Who This Is Not For

- Mathematicians who want proofs without applications
- People looking for a credential or certificate
- Anyone satisfied with MATLAB

---

## About

This course was built while learning the material, not after. Every missing explanation, every moment where the textbook assumed what it shouldn't, every "why didn't anyone just say that" — captured in real time and turned into the course that should have existed already.