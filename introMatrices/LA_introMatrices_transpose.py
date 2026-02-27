"""Linear Algebra: Matrix Transpose Operations

This module demonstrates matrix transpose operations, including regular transpose
and Hermitian transpose for complex matrices.

Course: Linear algebra: theory and implementation
Section: Introduction to matrices
Topic: Transpose
"""

import numpy as np


def demonstrate_transpose():
    """Demonstrate basic transpose operations on a real matrix.
    
    Shows that double transpose returns the original matrix and demonstrates
    both the .T attribute and np.transpose() function.
    """
    print("Basic Transpose Operations")
    print("-" * 40)
    
    M = np.array([[1, 2, 3],
                  [2, 3, 4]])
    
    print("Original matrix:")
    print(M)
    print()
    
    print("Transposed matrix (M.T):")
    print(M.T)
    print()
    
    print("Double transpose (M.T.T) returns original:")
    print(M.T.T)
    print()
    
    print("Using np.transpose() function:")
    print(np.transpose(M))
    print()


def demonstrate_complex_transpose():
    """Demonstrate transpose operations on complex matrices.
    
    Important: In MATLAB, the transpose operator performs a Hermitian transpose
    (conjugate transpose) on complex matrices. In Python/NumPy, the .T attribute
    performs a regular transpose. To get a Hermitian transpose, use .conjugate().T
    or .conj().T
    """
    print("Complex Matrix Transpose Operations")
    print("-" * 40)
    
    # Create a complex matrix
    C = np.array([[4 + 1j, 3, 2 - 4j]])
    
    print("Original complex matrix:")
    print(C)
    print()
    
    print("Regular transpose (C.T):")
    print(C.T)
    print()
    
    print("Using np.transpose():")
    print(np.transpose(C))
    print()
    
    print("Hermitian (conjugate) transpose (C.conjugate().T):")
    print(C.conjugate().T)
    print("Note: Complex numbers are conjugated (sign flips on imaginary part)")
    print()


def verify_transpose_properties():
    """Verify key properties of matrix transpose.
    
    Properties verified:
    1. (A^T)^T = A
    2. (A + B)^T = A^T + B^T
    3. (kA)^T = k(A^T) for scalar k
    """
    print("Transpose Property Verification")
    print("-" * 40)
    
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    k = 3
    
    # Property 1: Double transpose
    print("Property 1: (A^T)^T = A")
    print(f"Match: {np.allclose(A.T.T, A)}")
    print()
    
    # Property 2: Sum of transposes
    print("Property 2: (A + B)^T = A^T + B^T")
    left_side = (A + B).T
    right_side = A.T + B.T
    print(f"Match: {np.allclose(left_side, right_side)}")
    print()
    
    # Property 3: Scalar multiplication
    print("Property 3: (kA)^T = k(A^T)")
    left_side = (k * A).T
    right_side = k * A.T
    print(f"Match: {np.allclose(left_side, right_side)}")
    print()


def main():
    """Main function to run all transpose demonstrations."""
    print("=" * 60)
    print("Matrix Transpose Demonstrations")
    print("=" * 60)
    print()
    
    demonstrate_transpose()
    demonstrate_complex_transpose()
    verify_transpose_properties()


if __name__ == '__main__':
    main()
