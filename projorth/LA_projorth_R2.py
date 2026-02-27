"""Linear Algebra: Vector Projections in R^2

This module demonstrates how to compute and visualize the projection of one
vector onto another in 2D space.

Course: Linear algebra: theory and implementation
Section: Projections and orthogonalization
Topic: Projections in R^2
"""

import numpy as np
import matplotlib.pyplot as plt


def project_vector(b, a):
    """Project vector b onto vector a.
    
    Parameters
    ----------
    b : array_like
        Vector to be projected.
    a : array_like
        Vector onto which b is projected.
        
    Returns
    -------
    tuple
        (beta, projection) where:
        - beta is the scalar coefficient
        - projection is the projected vector (beta * a)
        
    Notes
    -----
    The projection of b onto a is: proj_a(b) = (a^T b / a^T a) * a
    The scalar beta = a^T b / a^T a gives the component of b along a.
    """
    b = np.asarray(b)
    a = np.asarray(a)
    
    # Compute the scalar projection coefficient
    beta = np.dot(a, b) / np.dot(a, a)
    
    # Compute the projection vector
    projection = beta * a
    
    return beta, projection


def visualize_projection(b, a):
    """Visualize the projection of vector b onto vector a.
    
    Parameters
    ----------
    b : array_like
        Vector to be projected (2D).
    a : array_like
        Vector onto which b is projected (2D).
    """
    b = np.asarray(b)
    a = np.asarray(a)
    
    # Compute projection
    beta, proj_b = project_vector(b, a)
    
    # Compute orthogonal component (b - projection)
    orthogonal = b - proj_b
    
    # Create the plot
    plt.figure(figsize=(10, 10))
    
    # Plot vector b
    plt.arrow(0, 0, b[0], b[1], head_width=0.3, head_length=0.2,
              fc='black', ec='black', linewidth=2, label='b')
    
    # Plot vector a
    plt.arrow(0, 0, a[0], a[1], head_width=0.3, head_length=0.2,
              fc='blue', ec='blue', linewidth=2, label='a')
    
    # Plot projection of b onto a
    plt.arrow(0, 0, proj_b[0], proj_b[1], head_width=0.3, head_length=0.2,
              fc='green', ec='green', linewidth=2, linestyle='--',
              label=f'proj_a(b) = {beta:.2f}a', alpha=0.7)
    
    # Plot the orthogonal component (from projection to b)
    plt.plot([proj_b[0], b[0]], [proj_b[1], b[1]], 'r--', linewidth=2,
             label='b - proj_a(b)', alpha=0.7)
    
    # Add point markers
    plt.plot(b[0], b[1], 'ko', markersize=10)
    plt.plot(proj_b[0], proj_b[1], 'go', markersize=10)
    
    plt.axis('equal')
    plt.xlim(-1, max(6, b[0] + 1, a[0] + 1))
    plt.ylim(-1, max(6, b[1] + 1, a[1] + 1))
    plt.grid(True, alpha=0.3)
    plt.legend(loc='best', fontsize=11)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.title('Vector Projection in R²', fontsize=14, fontweight='bold')
    plt.axhline(y=0, color='k', linewidth=0.5)
    plt.axvline(x=0, color='k', linewidth=0.5)
    plt.show()


def demonstrate_projection():
    """Demonstrate vector projection with numerical output."""
    print("Vector Projection in R²")
    print("=" * 60)
    
    # Define vectors
    b = np.array([4, 1])
    a = np.array([2, 5])
    
    print(f"Vector b: {b}")
    print(f"Vector a: {a}")
    print()
    
    # Compute projection
    beta, proj_b = project_vector(b, a)
    
    print(f"Scalar coefficient beta: {beta:.4f}")
    print(f"Projection of b onto a: {proj_b}")
    print()
    
    # Compute orthogonal component
    orthogonal = b - proj_b
    print(f"Orthogonal component (b - proj): {orthogonal}")
    print()
    
    # Verify orthogonality
    dot_product = np.dot(orthogonal, a)
    print(f"Dot product of orthogonal component with a: {dot_product:.2e}")
    print(f"Is orthogonal? {np.allclose(dot_product, 0)}")
    print()
    
    # Verify decomposition: b = proj + orthogonal
    reconstructed = proj_b + orthogonal
    print(f"Reconstruction (proj + orthogonal): {reconstructed}")
    print(f"Matches original b? {np.allclose(reconstructed, b)}")
    print()


def demonstrate_multiple_projections():
    """Demonstrate projections with different angles."""
    print("Multiple Projection Examples")
    print("=" * 60)
    
    a = np.array([1, 0])  # Unit vector along x-axis
    
    test_vectors = [
        np.array([3, 2]),
        np.array([1, 3]),
        np.array([-2, 1])
    ]
    
    for i, b in enumerate(test_vectors, 1):
        beta, proj = project_vector(b, a)
        print(f"Example {i}: b = {b}")
        print(f"  Projection onto a={a}: {proj}")
        print(f"  Coefficient: {beta:.4f}")
        print()


def main():
    """Main function to run all projection demonstrations."""
    print("=" * 60)
    print("Vector Projection Demonstrations in R²")
    print("=" * 60)
    print()
    
    demonstrate_projection()
    demonstrate_multiple_projections()
    
    # Visualize
    b = np.array([4, 1])
    a = np.array([2, 5])
    visualize_projection(b, a)


if __name__ == '__main__':
    main()
