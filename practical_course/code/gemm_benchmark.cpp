#include <iostream>
#include <chrono>
#include <Eigen/Dense>

int main() {
    const int n = 1024;

    // Random matrices
    Eigen::MatrixXd A = Eigen::MatrixXd::Random(n, n);
    Eigen::MatrixXd B = Eigen::MatrixXd::Random(n, n);

    // ── Naive triple loop (ijk) ───────────────────────────────────────
    {
        Eigen::MatrixXd C = Eigen::MatrixXd::Zero(n, n);
        auto t0 = std::chrono::high_resolution_clock::now();

        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
                for (int k = 0; k < n; ++k)
                    C(i, j) += A(i, k) * B(k, j);

        auto t1 = std::chrono::high_resolution_clock::now();
        double ms = std::chrono::duration<double, std::milli>(t1 - t0).count();
        double gflops = 2.0 * n * n * n / (ms * 1e6);
        std::cout << "Naive ijk loop:  " << ms << " ms  ("
                  << gflops << " GFLOP/s)\n";
    }

    // ── Eigen GEMM (dispatches to BLAS if linked) ─────────────────────
    {
        auto t0 = std::chrono::high_resolution_clock::now();

        Eigen::MatrixXd C = A * B;  // Expression template -> GEMM call

        auto t1 = std::chrono::high_resolution_clock::now();
        double ms = std::chrono::duration<double, std::milli>(t1 - t0).count();
        double gflops = 2.0 * n * n * n / (ms * 1e6);
        std::cout << "Eigen GEMM:      " << ms << " ms  ("
                  << gflops << " GFLOP/s)\n";
    }

    // ── Verify both give the same result ──────────────────────────────
    {
        Eigen::MatrixXd C_naive = Eigen::MatrixXd::Zero(n, n);
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
                for (int k = 0; k < n; ++k)
                    C_naive(i, j) += A(i, k) * B(k, j);

        Eigen::MatrixXd C_eigen = A * B;
        double diff = (C_naive - C_eigen).norm() / C_eigen.norm();
        std::cout << "Relative difference: " << diff << "\n";
    }

    return 0;
}
