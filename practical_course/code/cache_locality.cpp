#include <iostream>
#include <vector>
#include <chrono>

int main() {
    const int n = 4096;

    // ── Allocate a flat n x n matrix (row-major in memory) ────────────
    std::vector<double> A(static_cast<size_t>(n) * n, 1.0);

    auto time_it = [&](const char* label, auto fn) {
        auto t0 = std::chrono::high_resolution_clock::now();
        double s = fn();
        auto t1 = std::chrono::high_resolution_clock::now();
        double ms = std::chrono::duration<double, std::milli>(t1 - t0).count();
        std::cout << label << ": " << ms << " ms  (sum = " << s << ")\n";
    };

    // ── Row-major traversal: A[i][j] with j in inner loop ────────────
    // Each step moves +1 in memory → contiguous → cache hits
    time_it("Row-major (fast)", [&]() {
        double sum = 0.0;
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
                sum += A[static_cast<size_t>(i) * n + j];
        return sum;
    });

    // ── Column-major traversal: A[i][j] with i in inner loop ─────────
    // Each step moves +n in memory → stride-n → cache misses
    time_it("Col-major (slow)", [&]() {
        double sum = 0.0;
        for (int j = 0; j < n; ++j)
            for (int i = 0; i < n; ++i)
                sum += A[static_cast<size_t>(i) * n + j];
        return sum;
    });

    return 0;
}
