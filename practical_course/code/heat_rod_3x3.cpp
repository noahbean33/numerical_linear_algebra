#include <iostream>
#include <Eigen/Dense>

int main() {
    // Build the 3x3 tridiagonal heat-rod matrix
    Eigen::Matrix3d A;
    A <<  2, -1,  0,
         -1,  2, -1,
          0, -1,  2;

    Eigen::Vector3d b(1.0, 1.0, 1.0);

    // Solve Au = b
    Eigen::Vector3d u = A.colPivHouseholderQr().solve(b);

    std::cout << "A =\n" << A << "\n\n";
    std::cout << "b = " << b.transpose() << "\n\n";
    std::cout << "u = " << u.transpose() << "\n\n";

    // Verify: relative residual
    double rel_residual = (A * u - b).norm() / b.norm();
    std::cout << "Relative residual ||Au - b|| / ||b|| = "
              << rel_residual << "\n";

    return 0;
}
