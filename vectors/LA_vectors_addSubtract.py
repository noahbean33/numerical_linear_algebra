"""Linear Algebra: Vector Addition and Subtraction

This module demonstrates vector addition and subtraction in 2D space with
geometric visualization using the parallelogram law.

Course: Linear algebra: theory and implementation
Section: Vectors
Topic: Vector addition/subtraction
"""

import numpy as np
import matplotlib.pyplot as plt


def visualize_vector_addition(v1, v2):
    """Visualize vector addition using the parallelogram/triangle method.
    
    Parameters
    ----------
    v1 : array_like
        First 2D vector.
    v2 : array_like
        Second 2D vector.
        
    Notes
    -----
    The function shows three vectors:
    - v1 starting from origin (blue)
    - v2 starting from tip of v1 (red)
    - v1 + v2 starting from origin (black)
    """
    v1 = np.asarray(v1)
    v2 = np.asarray(v2)
    v3 = v1 + v2
    
    # Create the plot
    plt.figure(figsize=(10, 10))
    
    # Plot v1 from origin
    plt.arrow(0, 0, v1[0], v1[1], head_width=0.3, head_length=0.2, 
              fc='blue', ec='blue', linewidth=2, label='v1')
    
    # Plot v2 from tip of v1
    plt.arrow(v1[0], v1[1], v2[0], v2[1], head_width=0.3, head_length=0.2, 
              fc='red', ec='red', linewidth=2, label='v2')
    
    # Plot v1 + v2 from origin
    plt.arrow(0, 0, v3[0], v3[1], head_width=0.3, head_length=0.2, 
              fc='black', ec='black', linewidth=2, linestyle='--', 
              label='v1 + v2', alpha=0.7)
    
    # Also plot v2 from origin (to show parallelogram)
    plt.arrow(0, 0, v2[0], v2[1], head_width=0, head_length=0, 
              fc='none', ec='red', linewidth=1, linestyle=':', alpha=0.5)
    
    # Plot v1 from tip of v2 (to complete parallelogram)
    plt.arrow(v2[0], v2[1], v1[0], v1[1], head_width=0, head_length=0, 
              fc='none', ec='blue', linewidth=1, linestyle=':', alpha=0.5)
    
    plt.legend(loc='best', fontsize=12)
    plt.axis('equal')
    plt.xlim(-1, max(6, v3[0] + 1))
    plt.ylim(min(-2, v1[1] - 1), max(6, v3[1] + 1))
    plt.grid(True, alpha=0.3)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.title('Vector Addition: Parallelogram Law', fontsize=14)
    plt.axhline(y=0, color='k', linewidth=0.5)
    plt.axvline(x=0, color='k', linewidth=0.5)
    plt.show()


def demonstrate_vector_arithmetic():
    """Demonstrate basic vector arithmetic operations."""
    print("Vector Arithmetic Operations")
    print("=" * 60)
    
    v1 = np.array([3, -1])
    v2 = np.array([2, 4])
    
    print(f"Vector v1: {v1}")
    print(f"Vector v2: {v2}")
    print()
    
    # Addition
    v_sum = v1 + v2
    print(f"v1 + v2 = {v_sum}")
    print()
    
    # Subtraction
    v_diff = v1 - v2
    print(f"v1 - v2 = {v_diff}")
    print()
    
    # Scalar multiplication
    v_scaled = 2 * v1
    print(f"2 * v1 = {v_scaled}")
    print()
    
    # Verify commutative property
    print("Verifying commutativity: v1 + v2 = v2 + v1")
    print(f"v1 + v2 = {v1 + v2}")
    print(f"v2 + v1 = {v2 + v1}")
    print(f"Equal: {np.allclose(v1 + v2, v2 + v1)}")
    print()


def demonstrate_vector_subtraction():
    """Demonstrate vector subtraction geometrically."""
    print("Vector Subtraction")
    print("=" * 60)
    
    v1 = np.array([4, 3])
    v2 = np.array([2, 1])
    v_diff = v1 - v2
    
    print(f"v1 = {v1}")
    print(f"v2 = {v2}")
    print(f"v1 - v2 = {v_diff}")
    print()
    
    plt.figure(figsize=(10, 10))
    
    # Plot vectors
    plt.arrow(0, 0, v1[0], v1[1], head_width=0.2, head_length=0.15, 
              fc='blue', ec='blue', linewidth=2, label='v1')
    plt.arrow(0, 0, v2[0], v2[1], head_width=0.2, head_length=0.15, 
              fc='red', ec='red', linewidth=2, label='v2')
    plt.arrow(v2[0], v2[1], v_diff[0], v_diff[1], head_width=0.2, head_length=0.15, 
              fc='green', ec='green', linewidth=2, label='v1 - v2')
    
    plt.legend(loc='best', fontsize=12)
    plt.axis('equal')
    plt.xlim(-1, 5)
    plt.ylim(-1, 4)
    plt.grid(True, alpha=0.3)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.title('Vector Subtraction', fontsize=14)
    plt.axhline(y=0, color='k', linewidth=0.5)
    plt.axvline(x=0, color='k', linewidth=0.5)
    plt.show()


def main():
    """Main function to run all vector addition/subtraction demonstrations."""
    print("=" * 60)
    print("Vector Addition and Subtraction Demonstrations")
    print("=" * 60)
    print()
    
    demonstrate_vector_arithmetic()
    
    # Visualize addition
    v1 = np.array([3, -1])
    v2 = np.array([2, 4])
    visualize_vector_addition(v1, v2)
    
    # Visualize subtraction
    demonstrate_vector_subtraction()


if __name__ == '__main__':
    main()
