"""Linear Algebra: Singular Value Decomposition (SVD)

This module demonstrates the Singular Value Decomposition, which factors any
matrix A into three matrices: A = U Σ V^T

Course: Linear algebra: theory and implementation
Section: Singular value decomposition
Topic: Singular value decomposition
"""

import numpy as np
import matplotlib.pyplot as plt


def compute_svd(A):
    """Compute the Singular Value Decomposition of a matrix.
    
    Parameters
    ----------
    A : array_like
        Input matrix to decompose.
        
    Returns
    -------
    U : ndarray
        Left singular vectors (m × m orthogonal matrix).
    S : ndarray
        Singular values (1D array of non-negative values in descending order).
    V : ndarray
        Right singular vectors transposed (n × n orthogonal matrix).
        
    Notes
    -----
    The decomposition satisfies: A = U @ diag(S) @ V
    where diag(S) is the diagonal matrix with S on the diagonal.
    
    In NumPy:
    - S is returned as a 1D vector (not a full matrix)
    - V is already transposed (V^T in mathematical notation)
    """
    A = np.asarray(A)
    U, S, V = np.linalg.svd(A)
    return U, S, V


def reconstruct_from_svd(U, S, V):
    """Reconstruct the original matrix from its SVD components.
    
    Parameters
    ----------
    U : ndarray
        Left singular vectors.
    S : ndarray
        Singular values (1D array).
    V : ndarray
        Right singular vectors (already transposed).
        
    Returns
    -------
    ndarray
        Reconstructed matrix A = U @ diag(S) @ V
    """
    # Create full Sigma matrix with proper dimensions
    m, n = U.shape[0], V.shape[0]
    Sigma = np.zeros((m, n))
    np.fill_diagonal(Sigma, S)
    
    # Reconstruct
    A_reconstructed = U @ Sigma @ V
    return A_reconstructed


def demonstrate_svd():
    """Demonstrate SVD computation and reconstruction."""
    print("Singular Value Decomposition")
    print("=" * 60)
    
    # Create a matrix
    A = np.array([[3, 0, 5],
                  [8, 1, 3]])
    
    print("Original matrix A:")
    print(A)
    print(f"Shape: {A.shape}")
    print()
    
    # Compute SVD
    U, S, V = compute_svd(A)
    
    print("Left singular vectors U:")
    print(U)
    print(f"Shape: {U.shape}")
    print()
    
    print("Singular values S:")
    print(S)
    print(f"Shape: {S.shape}")
    print()
    
    print("Right singular vectors V^T:")
    print(V)
    print(f"Shape: {V.shape}")
    print()
    
    # Reconstruct
    A_reconstructed = reconstruct_from_svd(U, S, V)
    
    print("Reconstructed A (should match original):")
    print(A_reconstructed)
    print()
    
    print(f"Reconstruction error: {np.max(np.abs(A - A_reconstructed)):.2e}")
    print()


def visualize_svd():
    """Visualize the SVD components."""
    print("Visualizing SVD Components")
    print("=" * 60)
    
    # Create matrix
    A = np.array([[3, 0, 5],
                  [8, 1, 3]])
    
    # Compute SVD
    U, S, V = compute_svd(A)
    
    # Create Sigma matrix for visualization
    m, n = A.shape
    Sigma = np.zeros((m, n))
    np.fill_diagonal(Sigma, S)
    
    # Create figure
    fig, axes = plt.subplots(1, 4, figsize=(16, 4))
    
    # Plot A
    im1 = axes[0].imshow(A, cmap='RdBu', aspect='auto')
    axes[0].set_title('A', fontsize=14, fontweight='bold')
    axes[0].axis('off')
    plt.colorbar(im1, ax=axes[0], fraction=0.046)
    
    # Plot U
    im2 = axes[1].imshow(U, cmap='RdBu', aspect='auto')
    axes[1].set_title('U', fontsize=14, fontweight='bold')
    axes[1].axis('off')
    plt.colorbar(im2, ax=axes[1], fraction=0.046)
    
    # Plot Sigma
    im3 = axes[2].imshow(Sigma, cmap='RdBu', aspect='auto')
    axes[2].set_title('Σ', fontsize=14, fontweight='bold')
    axes[2].axis('off')
    plt.colorbar(im3, ax=axes[2], fraction=0.046)
    
    # Plot V^T
    im4 = axes[3].imshow(V, cmap='RdBu', aspect='auto')
    axes[3].set_title('V$^T$', fontsize=14, fontweight='bold')
    axes[3].axis('off')
    plt.colorbar(im4, ax=axes[3], fraction=0.046)
    
    plt.suptitle('SVD: A = U Σ V$^T$', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.show()
    
    print("SVD components visualized successfully.")
    print()


def verify_svd_properties():
    """Verify key properties of SVD matrices."""
    print("Verifying SVD Properties")
    print("=" * 60)
    
    A = np.random.randn(4, 6)
    U, S, V = compute_svd(A)
    
    # Property 1: U is orthogonal (U^T @ U = I)
    print("Property 1: U is orthogonal (U^T @ U = I)")
    UTU = U.T @ U
    print(f"Max deviation from identity: {np.max(np.abs(UTU - np.eye(U.shape[1]))):.2e}")
    print()
    
    # Property 2: V is orthogonal (V @ V^T = I)
    print("Property 2: V is orthogonal (V @ V^T = I)")
    VVT = V @ V.T
    print(f"Max deviation from identity: {np.max(np.abs(VVT - np.eye(V.shape[0]))):.2e}")
    print()
    
    # Property 3: Singular values are non-negative and sorted
    print("Property 3: Singular values are non-negative and sorted descending")
    print(f"All non-negative: {np.all(S >= 0)}")
    print(f"Sorted descending: {np.all(S[:-1] >= S[1:])}")
    print(f"Singular values: {S}")
    print()


def main():
    """Main function to run all SVD demonstrations."""
    print("=" * 60)
    print("Singular Value Decomposition (SVD) Demonstrations")
    print("=" * 60)
    print()
    
    demonstrate_svd()
    visualize_svd()
    verify_svd_properties()


if __name__ == '__main__':
    main()
