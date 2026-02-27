"""Linear Algebra: Vector Dot Product

This module demonstrates various methods for computing the dot product of two vectors
using NumPy and Python.

Course: Linear algebra: theory and implementation
Section: Vectors
Topic: Vector-vector multiplication: the dot product
"""

import numpy as np
import matplotlib.pyplot as plt


def dot_product_manual(v1, v2):
    """Compute dot product using element-wise multiplication and sum.
    
    Parameters
    ----------
    v1 : array_like
        First vector.
    v2 : array_like
        Second vector (must have same length as v1).
        
    Returns
    -------
    float
        The dot product of v1 and v2.
        
    Raises
    ------
    ValueError
        If vectors have different lengths.
    """
    v1 = np.asarray(v1)
    v2 = np.asarray(v2)
    
    if len(v1) != len(v2):
        raise ValueError(f"Vectors must have same length: {len(v1)} != {len(v2)}")
    
    return np.sum(np.multiply(v1, v2))


def dot_product_loop(v1, v2):
    """Compute dot product using a loop (educational purposes).
    
    Parameters
    ----------
    v1 : array_like
        First vector.
    v2 : array_like
        Second vector (must have same length as v1).
        
    Returns
    -------
    float
        The dot product of v1 and v2.
        
    Raises
    ------
    ValueError
        If vectors have different lengths.
    """
    v1 = np.asarray(v1)
    v2 = np.asarray(v2)
    
    if len(v1) != len(v2):
        raise ValueError(f"Vectors must have same length: {len(v1)} != {len(v2)}")
    
    result = 0
    for i in range(len(v1)):
        result += v1[i] * v2[i]
    
    return result


def compare_dot_product_methods():
    """Compare different methods for computing the dot product.
    
    Demonstrates four different approaches:
    1. Manual: element-wise multiplication with sum
    2. np.dot(): NumPy's dot function
    3. np.matmul(): NumPy's matrix multiplication
    4. Loop: explicit loop (for educational purposes)
    
    All methods should produce identical results.
    """
    print("Comparing Dot Product Methods")
    print("-" * 60)
    
    # Create two vectors of the same length
    v1 = np.array([1, 2, 3, 4, 5, 6])
    v2 = np.array([0, -4, -3, 6, 5, 2])  # Fixed: added 6th element
    
    print(f"Vector 1: {v1}")
    print(f"Vector 2: {v2}")
    print()
    
    # Method 1: Manual with np.multiply and sum
    dp1 = dot_product_manual(v1, v2)
    print(f"Method 1 (manual multiply + sum): {dp1}")
    
    # Method 2: np.dot
    dp2 = np.dot(v1, v2)
    print(f"Method 2 (np.dot):                {dp2}")
    
    # Method 3: np.matmul or @ operator
    dp3 = np.matmul(v1, v2)
    print(f"Method 3 (np.matmul):             {dp3}")
    
    # Method 4: Explicit loop
    dp4 = dot_product_loop(v1, v2)
    print(f"Method 4 (explicit loop):         {dp4}")
    
    # Method 5: @ operator (Python 3.5+)
    dp5 = v1 @ v2
    print(f"Method 5 (@ operator):            {dp5}")
    
    print()
    print(f"All methods produce same result: {dp1 == dp2 == dp3 == dp4 == dp5}")
    print()


def demonstrate_geometric_interpretation():
    """Demonstrate the geometric interpretation of dot product.
    
    The dot product can be expressed as:
    v1 · v2 = ||v1|| * ||v2|| * cos(θ)
    
    where θ is the angle between the vectors.
    """
    print("Geometric Interpretation of Dot Product")
    print("-" * 60)
    
    # Create two simple 2D vectors
    v1 = np.array([3, 0])
    v2 = np.array([2, 2])
    
    # Compute dot product
    dot = np.dot(v1, v2)
    
    # Compute magnitudes
    mag_v1 = np.linalg.norm(v1)
    mag_v2 = np.linalg.norm(v2)
    
    # Compute angle
    cos_theta = dot / (mag_v1 * mag_v2)
    theta_rad = np.arccos(cos_theta)
    theta_deg = np.degrees(theta_rad)
    
    print(f"Vector 1: {v1}")
    print(f"Vector 2: {v2}")
    print(f"\nDot product: {dot}")
    print(f"||v1||: {mag_v1:.4f}")
    print(f"||v2||: {mag_v2:.4f}")
    print(f"Angle between vectors: {theta_deg:.2f}°")
    print()


def main():
    """Main function to run all dot product demonstrations."""
    print("=" * 60)
    print("Vector Dot Product Demonstrations")
    print("=" * 60)
    print()
    
    compare_dot_product_methods()
    demonstrate_geometric_interpretation()


if __name__ == '__main__':
    main()
