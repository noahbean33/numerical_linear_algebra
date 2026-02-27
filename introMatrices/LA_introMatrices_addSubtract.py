"""Linear Algebra: Matrix Addition and Subtraction

This module demonstrates matrix addition, subtraction, and the concept of 
matrix "shifting" using the identity matrix.

Course: Linear algebra: theory and implementation
Section: Introduction to matrices
Topic: Matrix addition and subtraction
"""

import numpy as np


def test_matrix_addition():
    """Demonstrate valid and invalid matrix addition operations.
    
    Matrix addition requires matrices to have the same dimensions.
    """
    print("Matrix Addition Compatibility")
    print("=" * 60)
    
    # Create random matrices with different dimensions
    A = np.random.randn(5, 4)
    B = np.random.randn(5, 3)
    C = np.random.randn(5, 4)
    
    print(f"Matrix A shape: {A.shape}")
    print(f"Matrix B shape: {B.shape}")
    print(f"Matrix C shape: {C.shape}")
    print()
    
    # Try A + B (should fail - incompatible dimensions)
    print("Testing A + B:")
    try:
        result = A + B
        print(f"  Success! Result shape: {result.shape}")
    except ValueError as e:
        print(f"  Failed: Incompatible shapes (5x4 + 5x3)")
    print()
    
    # Try A + C (should succeed - compatible dimensions)
    print("Testing A + C:")
    try:
        result = A + C
        print(f"  Success! Result shape: {result.shape}")
    except ValueError as e:
        print(f"  Failed: {e}")
    print()


def demonstrate_matrix_shifting():
    """Demonstrate matrix "shifting" by adding a scaled identity matrix.
    
    Shifting adds a constant to the diagonal elements of a matrix.
    This is commonly used in regularization (e.g., ridge regression).
    """
    print("Matrix Shifting (Adding Scaled Identity)")
    print("=" * 60)
    
    # Parameters
    lambda_shift = 0.03  # Shift amount
    N = 5  # Size of square matrix
    
    # Create random square matrix
    D = np.random.randn(N, N)
    
    # Shift the matrix by adding lambda times identity
    D_shifted = D + lambda_shift * np.eye(N)
    
    print(f"Original matrix D ({N}x{N}):")
    print(D)
    print()
    
    print(f"Shifted matrix (D + {lambda_shift}*I):")
    print(D_shifted)
    print()
    
    print("Diagonal elements comparison:")
    print(f"Original diagonal:   {np.diag(D)}")
    print(f"Shifted diagonal:    {np.diag(D_shifted)}")
    print(f"Difference:          {np.diag(D_shifted) - np.diag(D)}")
    print()


def demonstrate_matrix_operations():
    """Demonstrate basic matrix arithmetic operations."""
    print("Basic Matrix Arithmetic")
    print("=" * 60)
    
    # Create simple matrices for clear demonstration
    A = np.array([[1, 2, 3],
                  [4, 5, 6]])
    
    B = np.array([[10, 20, 30],
                  [40, 50, 60]])
    
    print("Matrix A:")
    print(A)
    print()
    
    print("Matrix B:")
    print(B)
    print()
    
    print("A + B:")
    print(A + B)
    print()
    
    print("A - B:")
    print(A - B)
    print()
    
    print("2*A (scalar multiplication):")
    print(2 * A)
    print()


def main():
    """Main function to run all demonstrations."""
    print("=" * 60)
    print("Matrix Addition and Subtraction Demonstrations")
    print("=" * 60)
    print()
    
    demonstrate_matrix_operations()
    test_matrix_addition()
    demonstrate_matrix_shifting()


if __name__ == '__main__':
    main()
