"""Linear Algebra: Matrix Inverse - Concepts and Uses

This module demonstrates the concept of matrix inverse, how to compute it,
and verifies that A * A^(-1) = I (identity matrix).

Course: Linear algebra: theory and implementation
Section: Matrix inverse
Topic: Concept and uses of the inverse
"""

import numpy as np
import matplotlib.pyplot as plt


def compute_and_verify_inverse(matrix_size=3):
    """Compute the inverse of a random matrix and verify the result.
    
    Parameters
    ----------
    matrix_size : int, optional
        Size of the square matrix (default is 3).
        
    Returns
    -------
    tuple
        (A, A_inv, identity_product) where identity_product = A @ A_inv
        
    Notes
    -----
    For a matrix A and its inverse A^(-1):
    - A @ A^(-1) = I (identity matrix)
    - A^(-1) @ A = I (identity matrix)
    """
    print(f"Matrix Inverse Verification (Size: {matrix_size}x{matrix_size})")
    print("=" * 60)
    
    # Generate random square matrix
    A = np.random.randn(matrix_size, matrix_size)
    
    # Compute its inverse
    try:
        A_inv = np.linalg.inv(A)
    except np.linalg.LinAlgError:
        print("Error: Matrix is singular (not invertible)")
        return None, None, None
    
    # Verify: A @ A^(-1) should equal identity matrix
    identity_product = A @ A_inv
    
    print("Original matrix A:")
    print(A)
    print()
    
    print("Inverse matrix A^(-1):")
    print(A_inv)
    print()
    
    print("A @ A^(-1) (should be identity):")
    print(identity_product)
    print()
    
    # Check if result is close to identity
    identity_expected = np.eye(matrix_size)
    is_identity = np.allclose(identity_product, identity_expected)
    
    print(f"Is A @ A^(-1) = I? {is_identity}")
    print(f"Max deviation from identity: {np.max(np.abs(identity_product - identity_expected)):.2e}")
    print()
    
    return A, A_inv, identity_product


def visualize_matrix_and_inverse(A, A_inv, identity_product):
    """Visualize a matrix, its inverse, and their product.
    
    Parameters
    ----------
    A : ndarray
        Original matrix.
    A_inv : ndarray
        Inverse of A.
    identity_product : ndarray
        Product A @ A_inv.
    """
    if A is None:
        print("Cannot visualize: Matrix is singular")
        return
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    # Plot matrix A
    im1 = axes[0].imshow(A, cmap='RdBu', aspect='auto')
    axes[0].set_title('Matrix A', fontsize=14, fontweight='bold')
    axes[0].set_xlabel('Column')
    axes[0].set_ylabel('Row')
    plt.colorbar(im1, ax=axes[0])
    
    # Plot inverse A^(-1)
    im2 = axes[1].imshow(A_inv, cmap='RdBu', aspect='auto')
    axes[1].set_title('Inverse A$^{-1}$', fontsize=14, fontweight='bold')
    axes[1].set_xlabel('Column')
    axes[1].set_ylabel('Row')
    plt.colorbar(im2, ax=axes[1])
    
    # Plot product A @ A^(-1)
    im3 = axes[2].imshow(identity_product, cmap='RdBu', aspect='auto', vmin=-0.1, vmax=1.1)
    axes[2].set_title('A @ A$^{-1}$ (Identity)', fontsize=14, fontweight='bold')
    axes[2].set_xlabel('Column')
    axes[2].set_ylabel('Row')
    plt.colorbar(im3, ax=axes[2])
    
    plt.tight_layout()
    plt.show()


def demonstrate_inverse_properties():
    """Demonstrate key properties of matrix inverses."""
    print("Matrix Inverse Properties")
    print("=" * 60)
    
    # Create a simple invertible matrix
    A = np.array([[2, 1],
                  [1, 1]], dtype=float)
    
    A_inv = np.linalg.inv(A)
    
    print("Matrix A:")
    print(A)
    print()
    
    print("Inverse A^(-1):")
    print(A_inv)
    print()
    
    # Property 1: A @ A^(-1) = I
    print("Property 1: A @ A^(-1) = I")
    print(A @ A_inv)
    print()
    
    # Property 2: A^(-1) @ A = I
    print("Property 2: A^(-1) @ A = I")
    print(A_inv @ A)
    print()
    
    # Property 3: (A^(-1))^(-1) = A
    print("Property 3: (A^(-1))^(-1) = A")
    A_inv_inv = np.linalg.inv(A_inv)
    print(f"Original A:\n{A}")
    print(f"(A^(-1))^(-1):\n{A_inv_inv}")
    print(f"Are they equal? {np.allclose(A, A_inv_inv)}")
    print()


def demonstrate_determinant_relationship():
    """Demonstrate the relationship between determinants of A and A^(-1)."""
    print("Determinant Relationship")
    print("=" * 60)
    
    A = np.random.randn(4, 4)
    A_inv = np.linalg.inv(A)
    
    det_A = np.linalg.det(A)
    det_A_inv = np.linalg.det(A_inv)
    
    print(f"det(A) = {det_A:.6f}")
    print(f"det(A^(-1)) = {det_A_inv:.6f}")
    print(f"det(A) * det(A^(-1)) = {det_A * det_A_inv:.6f}")
    print(f"Expected: 1 (since det(A @ A^(-1)) = det(I) = 1)")
    print(f"1 / det(A) = {1 / det_A:.6f}")
    print(f"Are det(A^(-1)) and 1/det(A) equal? {np.allclose(det_A_inv, 1 / det_A)}")
    print()


def main():
    """Main function to run all matrix inverse demonstrations."""
    print("=" * 60)
    print("Matrix Inverse: Concepts and Demonstrations")
    print("=" * 60)
    print()
    
    # Compute and verify inverse
    A, A_inv, identity_prod = compute_and_verify_inverse(matrix_size=3)
    
    # Visualize
    visualize_matrix_and_inverse(A, A_inv, identity_prod)
    
    # Demonstrate properties
    demonstrate_inverse_properties()
    
    # Demonstrate determinant relationship
    demonstrate_determinant_relationship()


if __name__ == '__main__':
    main()
