#include <iostream>
#include <vector>
#include <chrono>
#include <Eigen/Sparse>
#include <Eigen/SparseLU>

int main() {
    // ── 2-D Poisson on an N x N grid → n = N^2 unknowns ──────────────
    const int N = 100;          // grid points per side
    const int n = N * N;        // total unknowns

    // Helper: map grid (ix, iy) → linear index
    auto idx = [&](int ix, int iy) { return iy * N + ix; };

    // ── Triplet assembly ──────────────────────────────────────────────
    Eigen::VectorXd b = Eigen::VectorXd::Zero(n);
    Eigen::SparseMatrix<double> A(n, n);
    {   // Scope triplets so memory is freed after compression
        using T = Eigen::Triplet<double>;
        std::vector<T> triplets;
        triplets.reserve(5 * n);  // 5-point stencil

        for (int iy = 0; iy < N; ++iy) {
            for (int ix = 0; ix < N; ++ix) {
                int i = idx(ix, iy);

                // Boundary: Dirichlet u = 0
                if (ix == 0 || ix == N - 1 || iy == 0 || iy == N - 1) {
                    triplets.push_back(T(i, i, 1.0));
                    b(i) = 0.0;
                    continue;
                }

                // Interior: -Laplacian with 5-point stencil
                triplets.push_back(T(i, i, 4.0));                // center
                triplets.push_back(T(i, idx(ix - 1, iy), -1.0)); // left
                triplets.push_back(T(i, idx(ix + 1, iy), -1.0)); // right
                triplets.push_back(T(i, idx(ix, iy - 1), -1.0)); // down
                triplets.push_back(T(i, idx(ix, iy + 1), -1.0)); // up

                // Heat source: uniform
                b(i) = 1.0;
            }
        }

        A.setFromTriplets(triplets.begin(), triplets.end());
    }   // triplets freed here
    A.makeCompressed();

    std::cout << "Grid: " << N << " x " << N
              << " = " << n << " unknowns\n";
    std::cout << "Non-zeros: " << A.nonZeros()
              << "  (density: "
              << 100.0 * A.nonZeros() / (static_cast<double>(n) * n)
              << "%)\n";

    // ── Solve ─────────────────────────────────────────────────────────
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

    // ── Verify ────────────────────────────────────────────────────────
    double rel_residual = (A * u - b).norm() / b.norm();

    std::cout << "Solve time:        " << elapsed << " s\n";
    std::cout << "Relative residual: " << rel_residual << "\n";
    std::cout << "u at center:       " << u(idx(N / 2, N / 2)) << "\n";
    std::cout << "Max temperature:   " << u.maxCoeff() << "\n";

    return 0;
}
