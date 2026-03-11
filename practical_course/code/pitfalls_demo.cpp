#include <iostream>
#include <chrono>
#include <cmath>
#include <limits>
#include <Eigen/Dense>
#include <Eigen/Sparse>
#include <Eigen/SparseLU>

// ── Pitfall 1: Silent failure ─────────────────────────────────────────
void demo_silent_failure() {
    std::cout << "=== Pitfall 1: Silent Failure ===\n";

    // Singular matrix
    Eigen::Matrix3d A;
    A << 1, 2, 3,
         4, 5, 6,
         7, 8, 9;  // rank 2, singular

    Eigen::Vector3d b(1, 2, 3);

    // SparseLU on a dense-to-sparse conversion to show the pattern
    Eigen::SparseMatrix<double> As = A.sparseView();
    Eigen::SparseLU<Eigen::SparseMatrix<double>> solver;
    solver.compute(As);

    if (solver.info() != Eigen::Success) {
        std::cout << "  [CAUGHT] Factorization failed (matrix is singular)\n";
        std::cout << "  Without this check, solve() would return garbage.\n\n";
        return;
    }

    Eigen::VectorXd x = solver.solve(b);
    std::cout << "  x = " << x.transpose() << "\n\n";
}

// ── Pitfall 2: Comparing to zero ──────────────────────────────────────
void demo_float_compare() {
    std::cout << "=== Pitfall 2: Comparing Floats to Zero ===\n";

    double a = 0.1 + 0.2;
    double b = 0.3;
    double diff = a - b;

    std::cout << "  0.1 + 0.2 - 0.3 = " << diff << "\n";
    std::cout << "  (== 0.0)?  " << (diff == 0.0 ? "true" : "FALSE") << "\n";
    std::cout << "  (< 1e-15)? " << (std::abs(diff) < 1e-15 ? "true" : "false")
              << "\n";

    // Show why absolute tolerances are dangerous:
    // If entries are large, 1e-12 is "zero"; if entries are tiny, it is "huge".
    double big_scale = 1e+10;
    double small_scale = 1e-20;
    double eps = std::numeric_limits<double>::epsilon();

    std::cout << "  Relative tolerance demo:\n";
    std::cout << "    scale=1e10:  eps*scale = " << eps * big_scale << "\n";
    std::cout << "    scale=1e-20: eps*scale = " << eps * small_scale << "\n";
    std::cout << "    (1e-12 is wrong for both cases!)\n\n";
}

// ── Pitfall 3: Allocation in hot loop ─────────────────────────────────
void demo_allocation() {
    std::cout << "=== Pitfall 3: Allocation Inside Loop ===\n";
    const int n = 200;
    const int iters = 1000;

    // BAD: allocate every iteration
    {
        auto t0 = std::chrono::high_resolution_clock::now();
        double dummy = 0;
        for (int k = 0; k < iters; ++k) {
            Eigen::MatrixXd A = Eigen::MatrixXd::Random(n, n);
            dummy += A(0, 0);
        }
        auto t1 = std::chrono::high_resolution_clock::now();
        double ms = std::chrono::duration<double, std::milli>(t1 - t0).count();
        std::cout << "  Alloc inside loop:  " << ms << " ms"
                  << "  (dummy=" << dummy << ")\n";
    }

    // GOOD: allocate once
    {
        Eigen::MatrixXd A(n, n);
        auto t0 = std::chrono::high_resolution_clock::now();
        double dummy = 0;
        for (int k = 0; k < iters; ++k) {
            A.setRandom();
            dummy += A(0, 0);
        }
        auto t1 = std::chrono::high_resolution_clock::now();
        double ms = std::chrono::duration<double, std::milli>(t1 - t0).count();
        std::cout << "  Alloc outside loop: " << ms << " ms"
                  << "  (dummy=" << dummy << ")\n\n";
    }
}

// ── Pitfall 4: Skipping residual check ────────────────────────────────
void demo_residual_check() {
    std::cout << "=== Pitfall 4: Residual Check ===\n";

    // Well-conditioned system
    Eigen::Matrix3d A1;
    A1 << 2, -1, 0,
         -1,  2, -1,
          0, -1,  2;
    Eigen::Vector3d b1(1, 1, 1);
    Eigen::Vector3d x1 = A1.colPivHouseholderQr().solve(b1);
    double res1 = (A1 * x1 - b1).norm() / b1.norm();
    std::cout << "  Well-conditioned:  residual = " << res1 << "\n";

    // Ill-conditioned system (Hilbert matrix)
    const int n = 12;
    Eigen::MatrixXd H(n, n);
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            H(i, j) = 1.0 / (i + j + 1);

    Eigen::VectorXd x_true = Eigen::VectorXd::Ones(n);
    Eigen::VectorXd b2 = H * x_true;
    Eigen::VectorXd x2 = H.colPivHouseholderQr().solve(b2);

    double res2 = (H * x2 - b2).norm() / b2.norm();
    double err2 = (x2 - x_true).norm() / x_true.norm();

    std::cout << "  Hilbert(12):       residual = " << res2 << "\n";
    std::cout << "  Hilbert(12):       error    = " << err2
              << "  (solution is garbage!)\n";
    std::cout << "  Condition number:  "
              << H.bdcSvd().singularValues()(0) /
                 H.bdcSvd().singularValues()(n-1) << "\n\n";
}

// ── Pitfall 5: Aliasing ──────────────────────────────────────────────
void demo_aliasing() {
    std::cout << "=== Pitfall 5: Aliasing ===\n";

    Eigen::Matrix2d A;
    A << 1, 2,
         3, 4;

    // A = A * B (different matrix) -- Eigen 3.3+ handles this correctly
    Eigen::Matrix2d B;
    B << 5, 6,
         7, 8;
    Eigen::Matrix2d AB_safe = A;  // copy to test
    AB_safe = AB_safe * B;        // safe in Eigen 3.3+
    std::cout << "  A*B (Eigen handles A=A*B for different B):\n"
              << AB_safe << "\n\n";

    // A = A * A -- the classic silent killer
    // Even though Eigen 3.3+ may detect this, don't rely on it.
    Eigen::Matrix2d A_squared = (A * A).eval();  // SAFE: explicit .eval()
    std::cout << "  A^2 (with .eval() -- always safe):\n"
              << A_squared << "\n\n";

    // Verify against manual computation
    Eigen::Matrix2d A2_manual;
    A2_manual << 1*1+2*3, 1*2+2*4,
                 3*1+4*3, 3*2+4*4;
    double diff = (A_squared - A2_manual).norm();
    std::cout << "  Verification ||A^2 - manual||: " << diff << "\n";
    std::cout << "  Rule: same matrix on both sides of '=' => use .eval()\n\n";
}

int main() {
    demo_silent_failure();
    demo_float_compare();
    demo_allocation();
    demo_residual_check();
    demo_aliasing();

    std::cout << "=== All pitfalls demonstrated ===\n";
    return 0;
}
