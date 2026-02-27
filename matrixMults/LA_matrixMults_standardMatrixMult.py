"""Linear Algebra: Standard Matrix Multiplication

This module demonstrates the rules and validity of matrix multiplication operations.
For two matrices A (m×n) and B (n×k), the product AB is valid only when the
number of columns in A equals the number of rows in B, resulting in an (m×k) matrix.

Course: Linear algebra: theory and implementation
Section: Matrix multiplications
Topic: Standard matrix multiplication, parts 1 & 2
"""

import numpy as np
import matplotlib.pyplot as plt


def check_multiplication_validity(A, B, operation_name=""):
    """Check if matrix multiplication A @ B is valid and attempt it.
    
    Parameters
    ----------
    A : ndarray
        First matrix.
    B : ndarray
        Second matrix.
    operation_name : str, optional
        Description of the operation for display purposes.
        
    Returns
    -------
    bool
        True if multiplication is valid, False otherwise.
    """
    try:
        result = np.matmul(A, B)
        print(f"✓ {operation_name:30s} Valid   Shape: {result.shape}")
        return True
    except ValueError as e:
        print(f"✗ {operation_name:30s} Invalid (Shape mismatch)")
        return False


def demonstrate_multiplication_rules():
    """Demonstrate rules for valid matrix multiplication.
    
    Tests various matrix multiplication combinations to show which are valid
    based on dimension compatibility rules.
    """
    print("Matrix Multiplication Validity Rules")
    print("=" * 70)
    print()
    
    # Set dimensions
    m, n, k = 4, 3, 6
    
    # Create random matrices with specific dimensions
    A = np.random.randn(m, n)  # 4×3 matrix
    B = np.random.randn(n, k)  # 3×6 matrix
    C = np.random.randn(m, k)  # 4×6 matrix
    
    print(f"Matrix A: shape {A.shape} ({m}×{n})")
    print(f"Matrix B: shape {B.shape} ({n}×{k})")
    print(f"Matrix C: shape {C.shape} ({m}×{k})")
    print()
    print("Testing multiplication validity:")
    print("-" * 70)
    
    # Test various multiplications
    check_multiplication_validity(A, B, "A @ B")
    check_multiplication_validity(A, A, "A @ A")
    check_multiplication_validity(A.T, C, "A.T @ C")
    check_multiplication_validity(B, B.T, "B @ B.T")
    check_multiplication_validity(B.T, B, "B.T @ B")
    check_multiplication_validity(B, C, "B @ C")
    check_multiplication_validity(C, B, "C @ B")
    check_multiplication_validity(C.T, B, "C.T @ B")
    check_multiplication_validity(C, B.T, "C @ B.T")
    check_multiplication_validity(A.T, A, "A.T @ A")
    check_multiplication_validity(A, A.T, "A @ A.T")
    
    print()


def explain_multiplication_rule():
    """Explain the fundamental rule of matrix multiplication."""
    print("Matrix Multiplication Rule")
    print("=" * 70)
    print()
    print("For matrix multiplication A @ B to be valid:")
    print("  • A must have shape (m, n)")
    print("  • B must have shape (n, p)")
    print("  • The number of columns in A must equal the number of rows in B")
    print("  • The result will have shape (m, p)")
    print()
    print("Example:")
    print("  A: (4, 3) @ B: (3, 6) = Result: (4, 6) ✓ Valid")
    print("  A: (4, 3) @ C: (4, 6) = Cannot multiply (3 ≠ 4) ✗ Invalid")
    print()


def demonstrate_matrix_multiplication():
    """Demonstrate actual matrix multiplication with small examples."""
    print("Matrix Multiplication Example")
    print("=" * 70)
    print()
    
    # Create small matrices for clear visualization
    A = np.array([[1, 2],
                  [3, 4]])
    
    B = np.array([[5, 6],
                  [7, 8]])
    
    print("Matrix A:")
    print(A)
    print()
    
    print("Matrix B:")
    print(B)
    print()
    
    print("A @ B = ")
    print(A @ B)
    print()
    
    # Show that matrix multiplication is not commutative
    print("B @ A = ")
    print(B @ A)
    print()
    
    print("Note: A @ B ≠ B @ A (matrix multiplication is not commutative)")
    print(f"Are they equal? {np.allclose(A @ B, B @ A)}")
    print()


def main():
    """Main function to run all matrix multiplication demonstrations."""
    print("=" * 70)
    print("Standard Matrix Multiplication Demonstrations")
    print("=" * 70)
    print()
    
    explain_multiplication_rule()
    demonstrate_multiplication_rules()
    demonstrate_matrix_multiplication()


if __name__ == '__main__':
    main()
