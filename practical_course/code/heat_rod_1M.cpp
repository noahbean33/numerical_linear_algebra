#include <iostream>
#include <vector>
#include <chrono>
#include <Eigen/Sparse>
#include <Eigen/SparseLU>

int main() {
    const int n = 1000000;  // 1 million interior points

    // ── Step 1: Assemble using the Triplet method (O(n)) ──────────────
    Eigen::SparseMatrix<double> A(n, n);
    {   // Scope the triplet vector so it is freed after compression.
        // For n=10^6, the vector alone takes ~72 MB; no reason to keep it.
        using T = Eigen::Triplet<double>;
        std::vector<T> triplets;
        triplets.reserve(3 * n);  // at most 3 non-zeros per row

        for (int i = 0; i < n; ++i) {
            triplets.push_back(T(i, i, 2.0));          // diagonal
            if (i > 0)     triplets.push_back(T(i, i - 1, -1.0));  // sub-diagonal
            if (i < n - 1) triplets.push_back(T(i, i + 1, -1.0));  // super-diagonal
        }

        A.setFromTriplets(triplets.begin(), triplets.end());
    }   // triplets freed here
    A.makeCompressed();

    // ── Step 2: Right-hand side (uniform heat source) ─────────────────
    Eigen::VectorXd b = Eigen::VectorXd::Ones(n);

    // ── Step 3: Solve with a sparse direct solver ─────────────────────
    auto t0 = std::chrono::high_resolution_clock::now();

    Eigen::SparseLU<Eigen::SparseMatrix<double>> solver;
    solver.analyzePattern(A);
    solver.factorize(A);

    if (solver.info() != Eigen::Success) {
        std::cerr << "Factorization failed!\n";
        return 1;
    }

    Eigen::VectorXd u = solver.solve(b);

    if (solver.info() != Eigen::Success) {
        std::cerr << "Solve failed!\n";
        return 1;
    }

    auto t1 = std::chrono::high_resolution_clock::now();
    double elapsed = std::chrono::duration<double>(t1 - t0).count();

    // ── Step 4: Verify ────────────────────────────────────────────────
    double rel_residual = (A * u - b).norm() / b.norm();

    std::cout << "n = " << n << "\n";
    std::cout << "Non-zeros in A: " << A.nonZeros() << "\n";
    std::cout << "Memory for A:   ~" << A.nonZeros() * 12 / (1024*1024)
              << " MB\n";
    std::cout << "Solve time:     " << elapsed << " s\n";
    std::cout << "Relative residual: " << rel_residual << "\n";
    std::cout << "u[0] = " << u(0) << ",  u[n/2] = " << u(n / 2)
              << ",  u[n-1] = " << u(n - 1) << "\n";

    return 0;
}
