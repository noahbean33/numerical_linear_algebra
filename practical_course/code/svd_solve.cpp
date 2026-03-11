#include <iostream>
#include <Eigen/Dense>

int main() {
    // ── Build a test problem: overdetermined system (least squares) ───
    const int m = 200;   // equations
    const int n = 50;    // unknowns  (m > n)

    Eigen::MatrixXd A = Eigen::MatrixXd::Random(m, n);
    Eigen::VectorXd x_true = Eigen::VectorXd::LinSpaced(n, 1.0, 5.0);
    Eigen::VectorXd b = A * x_true + 0.01 * Eigen::VectorXd::Random(m);

    // ── SVD solve ─────────────────────────────────────────────────────
    auto svd = A.bdcSvd(Eigen::ComputeThinU | Eigen::ComputeThinV);

    // Even the "indestructible" SVD can fail on NaN/Inf input.
    if (svd.info() != Eigen::Success) {
        std::cerr << "SVD decomposition failed!\n";
        return 1;
    }

    Eigen::VectorXd x = svd.solve(b);

    // ── Diagnostics ───────────────────────────────────────────────────
    const auto& S = svd.singularValues();
    int rank = svd.rank();
    double cond = S(0) / S(S.size() - 1);

    std::cout << "System: " << m << " x " << n << "\n";
    std::cout << "Numerical rank:     " << rank << "\n";
    std::cout << "Condition number:   " << cond << "\n";
    std::cout << "Largest  sigma:     " << S(0) << "\n";
    std::cout << "Smallest sigma:     " << S(S.size() - 1) << "\n\n";

    // ── Residual check ────────────────────────────────────────────────
    double rel_residual = (A * x - b).norm() / b.norm();
    double rel_error    = (x - x_true).norm() / x_true.norm();

    std::cout << "Relative residual ||Ax-b||/||b||: " << rel_residual << "\n";
    std::cout << "Relative error    ||x-x*||/||x*||: " << rel_error << "\n";

    // ── Demonstrate rank-deficient case ───────────────────────────────
    std::cout << "\n--- Rank-deficient example ---\n";
    Eigen::MatrixXd A2(4, 3);
    A2 << 1, 2, 3,    // row 3 = row 1 + row 2
          4, 5, 6,
          5, 7, 9,    // linearly dependent
          2, 4, 6;    // = 2 * row 1

    Eigen::Vector4d b2(1, 2, 3, 2);

    auto svd2 = A2.bdcSvd(Eigen::ComputeThinU | Eigen::ComputeThinV);

    if (svd2.info() != Eigen::Success) {
        std::cerr << "SVD decomposition failed (rank-deficient example)!\n";
        return 1;
    }

    Eigen::VectorXd x2 = svd2.solve(b2);

    std::cout << "A is " << A2.rows() << "x" << A2.cols()
              << ", rank = " << svd2.rank() << "\n";
    std::cout << "Singular values: "
              << svd2.singularValues().transpose() << "\n";
    std::cout << "SVD solution: " << x2.transpose() << "\n";
    std::cout << "Residual: " << (A2 * x2 - b2).norm() << "\n";

    return 0;
}
