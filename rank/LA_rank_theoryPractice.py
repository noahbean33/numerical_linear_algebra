"""Linear Algebra: Matrix Rank - Theory and Practice

This module demonstrates computing matrix rank, creating rank-deficient matrices,
and the effect of noise on rank.

Course: Linear algebra: theory and implementation
Section: Matrix rank
Topic: Computing rank: theory and practice
"""

import numpy as np
import matplotlib.pyplot as plt


def demonstrate_full_rank_matrix():
    """Demonstrate rank computation for a full-rank random matrix.
    
    For an m×n matrix, the maximum possible rank is min(m, n).
    """
    print("Full Rank Matrix")
    print("=" * 60)
    
    m, n = 4, 6
    
    # Create a random matrix
    A = np.random.randn(m, n)
    
    # Compute rank
    rank_A = np.linalg.matrix_rank(A)
    
    print(f"Matrix dimensions: {m} × {n}")
    print(f"Maximum possible rank: {min(m, n)}")
    print(f"Actual rank: {rank_A}")
    print(f"Is full rank? {rank_A == min(m, n)}")
    print()


def create_rank_deficient_matrix():
    """Create a rank-deficient matrix by making columns linearly dependent."""
    print("Creating Rank-Deficient Matrix")
    print("=" * 60)
    
    m, n = 4, 6
    
    # Create a random matrix
    A = np.random.randn(m, n)
    rank_A = np.linalg.matrix_rank(A)
    
    # Make a copy and set last column equal to penultimate column
    # IMPORTANT: Use .copy() to avoid aliasing
    B = A.copy()
    B[:, -1] = B[:, -2]
    
    rank_B = np.linalg.matrix_rank(B)
    
    print(f"Original matrix A: rank = {rank_A}")
    print(f"Modified matrix B (last column = second-to-last): rank = {rank_B}")
    print(f"Rank decreased by: {rank_A - rank_B}")
    print()
    
    return A, B


def demonstrate_noise_effect_on_rank():
    """Demonstrate how noise affects the rank of a rank-deficient matrix.
    
    Adding noise to a rank-deficient matrix typically restores it to full rank.
    """
    print("Effect of Noise on Matrix Rank")
    print("=" * 60)
    
    m = 4
    
    # Create a square matrix with integer entries
    A = np.round(10 * np.random.randn(m, m))
    
    # Make it rank-deficient by duplicating last column
    A[:, -1] = A[:, -2]
    
    # Compute rank without noise
    rank_no_noise = np.linalg.matrix_rank(A)
    
    # Add small noise
    noise_amplitude = 0.001
    B = A + noise_amplitude * np.random.randn(m, m)
    
    # Compute rank with noise
    rank_with_noise = np.linalg.matrix_rank(B)
    
    print(f"Matrix size: {m} × {m}")
    print(f"Noise amplitude: {noise_amplitude}")
    print(f"Rank without noise: {rank_no_noise}")
    print(f"Rank with noise: {rank_with_noise}")
    print()
    print("Observation: Even tiny numerical noise can make a rank-deficient")
    print("matrix appear full-rank due to floating-point precision.")
    print()


def visualize_rank_deficiency():
    """Visualize the effect of rank deficiency on matrix structure."""
    print("Visualizing Rank Deficiency")
    print("=" * 60)
    
    # Create matrices
    m, n = 6, 8
    
    # Full rank matrix
    A_full = np.random.randn(m, n)
    
    # Rank-deficient: last 2 columns are copies of first 2
    A_deficient = A_full.copy()
    A_deficient[:, -2:] = A_deficient[:, :2]
    
    # Compute ranks
    rank_full = np.linalg.matrix_rank(A_full)
    rank_deficient = np.linalg.matrix_rank(A_deficient)
    
    # Visualize
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    im1 = axes[0].imshow(A_full, cmap='RdBu', aspect='auto')
    axes[0].set_title(f'Full Rank Matrix (rank={rank_full})', fontsize=12, fontweight='bold')
    axes[0].set_xlabel('Column')
    axes[0].set_ylabel('Row')
    plt.colorbar(im1, ax=axes[0])
    
    im2 = axes[1].imshow(A_deficient, cmap='RdBu', aspect='auto')
    axes[1].set_title(f'Rank-Deficient Matrix (rank={rank_deficient})', fontsize=12, fontweight='bold')
    axes[1].set_xlabel('Column')
    axes[1].set_ylabel('Row')
    plt.colorbar(im2, ax=axes[1])
    
    plt.tight_layout()
    plt.show()
    
    print(f"Full rank matrix: {rank_full}/{min(m, n)} (full rank)")
    print(f"Rank-deficient matrix: {rank_deficient}/{min(m, n)} (rank deficient)")
    print()


def main():
    """Main function to run all rank demonstrations."""
    print("=" * 60)
    print("Matrix Rank: Theory and Practice")
    print("=" * 60)
    print()
    
    demonstrate_full_rank_matrix()
    create_rank_deficient_matrix()
    demonstrate_noise_effect_on_rank()
    visualize_rank_deficiency()


if __name__ == '__main__':
    main()
