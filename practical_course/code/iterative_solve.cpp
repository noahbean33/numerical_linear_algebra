#include <iostream>
#include <vector>
#include <chrono>
#include <Eigen/Sparse>
#include <Eigen/IterativeLinearSolvers>
// GMRES lives in the unsupported module.  If your Eigen install does not
// include unsupported/, comment out the GMRES section below.
#include <unsupported/Eigen/IterativeSolvers>

int main() {
    // ── Build a large sparse system: 2-D Poisson on N x N grid ────────
    const int N = 500;          // 500 x 500 = 250,000 unknowns
    const int n = N * N;

    auto idx = [&](int ix, int iy) { return iy * N + ix; };

    Eigen::VectorXd b = Eigen::VectorXd::Zero(n);
    Eigen::SparseMatrix<double> A(n, n);
    {   // Scope triplets so memory is freed after compression
        using T = Eigen::Triplet<double>;
        std::vector<T> triplets;
        triplets.reserve(5 * n);

        for (int iy = 0; iy < N; ++iy) {
            for (int ix = 0; ix < N; ++ix) {
                int i = idx(ix, iy);
                if (ix == 0 || ix == N-1 || iy == 0 || iy == N-1) {
                    triplets.push_back(T(i, i, 1.0));
                    b(i) = 0.0;
                    continue;
                }
                triplets.push_back(T(i, i,              4.0));
                triplets.push_back(T(i, idx(ix-1, iy), -1.0));
                triplets.push_back(T(i, idx(ix+1, iy), -1.0));
                triplets.push_back(T(i, idx(ix, iy-1), -1.0));
                triplets.push_back(T(i, idx(ix, iy+1), -1.0));
                b(i) = 1.0;
            }
        }

        A.setFromTriplets(triplets.begin(), triplets.end());
    }   // triplets freed here
    A.makeCompressed();

    std::cout << "System size: " << n << "\n";
    std::cout << "Non-zeros:   " << A.nonZeros() << "\n\n";

    // ── Method 1: BiCGSTAB with NO preconditioner ─────────────────────
    //    Fast per iteration, but can stall on hard problems.
    {
        Eigen::BiCGSTAB<Eigen::SparseMatrix<double>> solver;
        solver.setMaxIterations(10000);
        solver.setTolerance(1e-10);

        auto t0 = std::chrono::high_resolution_clock::now();
        solver.compute(A);
        Eigen::VectorXd u = solver.solve(b);
        auto t1 = std::chrono::high_resolution_clock::now();

        if (solver.info() != Eigen::Success) {
            std::cerr << "BiCGSTAB (no precond) failed!\n";
        }

        double ms = std::chrono::duration<double, std::milli>(t1 - t0).count();
        double rel_res = (A * u - b).norm() / b.norm();

        std::cout << "BiCGSTAB (no precond):\n";
        std::cout << "  Iterations:       " << solver.iterations() << "\n";
        std::cout << "  Time:             " << ms << " ms\n";
        std::cout << "  Relative residual: " << rel_res << "\n\n";
    }

    // ── Method 2: BiCGSTAB with ILU preconditioner ────────────────────
    //    Much fewer iterations.  The "deadline" choice.
    {
        Eigen::BiCGSTAB<Eigen::SparseMatrix<double>,
                        Eigen::IncompleteLUT<double>> solver;
        solver.setMaxIterations(10000);
        solver.setTolerance(1e-10);

        solver.preconditioner().setDroptol(1e-4);
        solver.preconditioner().setFillfactor(10);

        auto t0 = std::chrono::high_resolution_clock::now();
        solver.compute(A);
        Eigen::VectorXd u = solver.solve(b);
        auto t1 = std::chrono::high_resolution_clock::now();

        if (solver.info() != Eigen::Success) {
            std::cerr << "BiCGSTAB + ILU failed!\n";
            return 1;
        }

        double ms = std::chrono::duration<double, std::milli>(t1 - t0).count();
        double rel_res = (A * u - b).norm() / b.norm();

        std::cout << "BiCGSTAB + ILU:\n";
        std::cout << "  Iterations:       " << solver.iterations() << "\n";
        std::cout << "  Time:             " << ms << " ms\n";
        std::cout << "  Relative residual: " << rel_res << "\n\n";
    }

    // ── Method 3: GMRES with ILU preconditioner ───────────────────────
    //    The "indestructible" choice.  Monotone residual decrease.
    //    More robust than BiCGSTAB for non-symmetric / near-singular A.
    {
        Eigen::GMRES<Eigen::SparseMatrix<double>,
                     Eigen::IncompleteLUT<double>> solver;
        solver.setMaxIterations(10000);
        solver.setTolerance(1e-10);
        solver.set_restart(100);  // restart after 100 Krylov vectors

        solver.preconditioner().setDroptol(1e-4);
        solver.preconditioner().setFillfactor(10);

        auto t0 = std::chrono::high_resolution_clock::now();
        solver.compute(A);
        Eigen::VectorXd u = solver.solve(b);
        auto t1 = std::chrono::high_resolution_clock::now();

        if (solver.info() != Eigen::Success) {
            std::cerr << "GMRES + ILU failed!\n";
            return 1;
        }

        double ms = std::chrono::duration<double, std::milli>(t1 - t0).count();
        double rel_res = (A * u - b).norm() / b.norm();

        std::cout << "GMRES + ILU:\n";
        std::cout << "  Iterations:       " << solver.iterations() << "\n";
        std::cout << "  Time:             " << ms << " ms\n";
        std::cout << "  Relative residual: " << rel_res << "\n";
        std::cout << "  u at center:      " << u(idx(N/2, N/2)) << "\n";
    }

    return 0;
}
