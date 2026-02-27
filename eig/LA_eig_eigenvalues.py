"""Linear Algebra: Finding Eigenvalues

This module demonstrates how to find and visualize eigenvalues and eigenvectors
using NumPy's linear algebra functions.

Course: Linear algebra: theory and implementation
Section: Eigendecomposition
Topic: Finding eigenvalues
"""

import numpy as np
import matplotlib.pyplot as plt


def extract_eigenvalues(matrix):
    """Extract eigenvalues from a square matrix.
    
    Parameters
    ----------
    matrix : array_like
        A square matrix (2D array) for which to compute eigenvalues.
        
    Returns
    -------
    ndarray
        Array of eigenvalues.
        
    Examples
    --------
    >>> A = np.array([[1, 5], [2, 3]])
    >>> eigenvals = extract_eigenvalues(A)
    """
    eigenvalues, _ = np.linalg.eig(matrix)
    return eigenvalues


def visualize_eigenvector_transformation(matrix):
    """Visualize how a matrix transforms eigenvectors vs regular vectors.
    
    This function plots an eigenvector and a random vector, along with their
    transformations under the given matrix. Eigenvectors maintain their direction
    under transformation (only scaled), while regular vectors change direction.
    
    Parameters
    ----------
    matrix : array_like
        A 2x2 matrix to visualize transformations.
        
    Returns
    -------
    None
        Displays a matplotlib plot.
    """
    # Convert to numpy array if not already
    A = np.asarray(matrix)
    
    # Specify two vectors
    v1 = np.array([1, 1])  # This is an eigenvector for the example matrix
    v2 = np.random.randn(2)  # Unlikely to be an eigenvector
    v2 = v2 / np.linalg.norm(v2)  # Normalize to unit length
    
    # Compute matrix-vector products
    Av1 = A @ v1
    Av2 = A @ v2
    
    # Create the plot
    plt.figure(figsize=(8, 8))
    plt.plot([0, v1[0]], [0, v1[1]], 'r', linewidth=2, label='Eigenvector')
    plt.plot([0, Av1[0]], [0, Av1[1]], 'r--', linewidth=2, label='Av (eigenvector)')
    plt.plot([0, v2[0]], [0, v2[1]], 'k', linewidth=2, label='Random vector')
    plt.plot([0, Av2[0]], [0, Av2[1]], 'k--', linewidth=2, label='Av (random)')
    
    plt.axis('equal')
    plt.xlim([-8, 8])
    plt.ylim([-8, 8])
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.title('Vector Transformations: Eigenvector vs Random Vector')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


def demonstrate_2x2_eigenvalues():
    """Demonstrate eigenvalue extraction for a 2x2 matrix."""
    # Define matrix as numpy array
    A = np.array([[1, 5], 
                  [2, 3]])
    
    # Extract eigenvalues
    eigenvals = extract_eigenvalues(A)
    print(f"Eigenvalues of 2x2 matrix:\n{A}")
    print(f"Eigenvalues: {eigenvals}")
    print()
    
    # Visualize the transformation
    visualize_eigenvector_transformation(A)


def demonstrate_3x3_eigenvalues():
    """Demonstrate eigenvalue extraction for a 3x3 matrix."""
    # Define matrix as numpy array
    A = np.array([[-2,  2, -3],
                  [-4,  1, -6],
                  [-1, -2,  0]])
    
    # Extract eigenvalues
    eigenvals = extract_eigenvalues(A)
    print(f"Eigenvalues of 3x3 matrix:\n{A}")
    print(f"Eigenvalues: {eigenvals}")


def main():
    """Main function to run all demonstrations."""
    print("=" * 60)
    print("Eigenvalue Demonstrations")
    print("=" * 60)
    print()
    
    # Demonstrate 2x2 eigenvalues with visualization
    demonstrate_2x2_eigenvalues()
    print()
    
    # Demonstrate 3x3 eigenvalues
    demonstrate_3x3_eigenvalues()


if __name__ == '__main__':
    main()
