# -*- coding: utf-8 -*-
# Auto-generated from '05-matrices-and-equations.ipynb' on 2025-08-08T15:22:58
# Source: code cells extracted; markdown preserved as comments.

# In [1]
import warnings
warnings.filterwarnings('ignore')

# %% [markdown]
# # Chapter 5. Matrices and equations

# %% [markdown]
# ## The LU decomposition

# %% [markdown]
# ### Implementing the LU decomposition

# In [2]
import numpy as np


def elimination_matrix(
    A: np.ndarray,
    step: int, 
):
    """
    Computes the step-th elimination matrix and its inverse.
    
    Args:
        A (np.ndarray): The matrix of shape (n, n) for which 
            the LU decomposition is being computed.
        step (int): The current step of elimination, an integer
            between 1 and n-1

    Returns:
        elim_mtx (np.ndarray): The step-th elimination matrix
            of shape (n, n)
        elim_mtx_inv (np.ndarray): The inverse of the
            elimination matrix of shape (n, n)
    """
    
    n = A.shape[0]
    elim_mtx = np.eye(n)
    elim_mtx_inv = np.eye(n)
    
    if 0 < step < n:
        a = A[:, step-1]/A[step-1, step-1]
        elim_mtx[step:, step-1] = -a[step:]
        elim_mtx_inv[step:, step-1] = a[step:]
    
    return elim_mtx, elim_mtx_inv

# In [3]
def LU(A: np.ndarray):
    """
    Computes the LU factorization of a square matrix A.
    
    Args:
        A (np.ndarray): A square matrix of shape (n, n) to be factorized. 
            It must be non-singular (invertible) for the 
            decomposition to work.

    Returns:
        L (np.ndarray): A lower triangular matrix of shape (n, n) 
            with ones on the diagonal.
        U (np.ndarray): An upper triangular matrix of shape (n, n).
    """
    
    n = A.shape[0]
    L = np.eye(n)
    U = np.copy(A)
    
    for step in range(1, n):
        elim_mtx, elim_mtx_inv = elimination_matrix(U, step=step)
        U = np.matmul(elim_mtx, U)
        L = np.matmul(L, elim_mtx_inv)
    
    return L, U

# In [4]
A = 10*np.random.rand(4, 4) - 5
A

# In [5]
L, U = LU(A)

print(f"Lower:\n{L}\n\nUpper:\n{U}")

# In [6]
np.allclose(np.matmul(L, U), A)

# %% [markdown]
# ### Inverting a matrix, for real

# In [7]
def invert_lower_triangular_matrix(L: np.ndarray):
    """
    Computes the inverse of a lower triangular matrix.

    Args:
        L (np.ndarray): A square lower triangular matrix of shape (n, n). 
                        It must have non-zero diagonal elements for the 
                        inversion to succeed.

    Returns:
        np.ndarray: The inverse of the lower triangular matrix L, with
                        shape (n, n).
    """
    n = L.shape[0]
    G = np.eye(n)
    D = np.copy(L)
    
    for step in range(1, n):
        elim_mtx, _ = elimination_matrix(D, step=step)
        G = np.matmul(elim_mtx, G)
        D = np.matmul(elim_mtx, D)
        
    D_inv = np.eye(n)/np.diagonal(D)   # NumPy performs this operation elementwise
    
    return np.matmul(D_inv, G)

# In [8]
def invert(A: np.ndarray):
    """
    Computes the inverse of a square matrix using its LU decomposition.

    Args:
        A (np.ndarray): A square matrix of shape (n, n). The matrix must be 
                        non-singular (invertible) for the inversion to succeed.

    Returns:
        np.ndarray: The inverse of the input matrix A, with shape (n, n).
    """
    L, U = LU(A)
    L_inv = invert_lower_triangular_matrix(L)
    U_inv = invert_lower_triangular_matrix(U.T).T
    return np.matmul(U_inv, L_inv)

# In [9]
A = np.random.rand(3, 3)
A_inv = invert(A)

print(f"A:\n{A}\n\nA⁻¹:\n{A_inv}\n\nAA⁻¹:\n{np.matmul(A, A_inv)}")

# In [10]
for _ in range(1000):
    n = np.random.randint(1, 10)
    A = np.random.rand(n, n)
    A_inv = invert(A)
    if not np.allclose(np.matmul(A, A_inv), np.eye(n), atol=1e-5):
        print("Test failed.")

# %% [markdown]
# ### How to actually invert matrices

# In [11]
A = np.random.rand(3, 3)
A_inv = np.linalg.inv(A)

print(f"A:\n{A}\n\nNumPy's A⁻¹:\n{A_inv}\n\nAA⁻¹:\n{np.matmul(A, A_inv)}")

# In [12]
from timeit import timeit


n_runs = 100
size = 100
A = np.random.rand(size, size)

t_inv = timeit(lambda: invert(A), number=n_runs)
t_np_inv = timeit(lambda: np.linalg.inv(A), number=n_runs)


print(f"Our invert:              \t{t_inv} s")
print(f"NumPy's invert:          \t{t_np_inv} s")
print(f"Performance improvement: \t{t_inv/t_np_inv} times faster")

# %% [markdown]
# ## Determinants in practice

# %% [markdown]
# ### The recursive way

# In [13]
def det(A: np.ndarray):
    """
    Recursively computes the determinant of a square matrix A.

    Args:
        A (np.ndarray): A square matrix of shape (n, n) for which the 
        determinant is to be calculated.

    Returns:
        float: The determinant of matrix A.

    Raises:
        ValueError: If A is not a square matrix.
    """

    n, m = A.shape
    
    # making sure that A is a square matrix
    if n != m:
        raise ValueError("A must be a square matrix.")
        
    if n == 1:
        return A[0, 0]
    
    else:
        return sum([(-1)**j*A[0, j]*det(np.delete(A[1:], j, axis=1)) for j in range(n)])

# In [14]
A = np.array([[1, 2],
              [3, 4]])

# In [15]
det(A)    # should be -2

# In [16]
from timeit import timeit

A = np.random.rand(10, 10)
t_det = timeit(lambda: det(A), number=1)

print(f"The time it takes to compute the determinant of a 10 x 10 matrix: {t_det} seconds")

# %% [markdown]
# ### How to actually compute determinants

# In [17]
def fast_det(A: np.ndarray):
    """
    Computes the determinant of a square matrix using LU decomposition.
    
    Args:
        A (np.ndarray): A square matrix of shape (n, n) for which the determinant 
                         needs to be computed. The matrix must be non-singular (invertible).

    Returns:
        float: The determinant of the matrix A..
    """

    L, U = LU(A)
    return np.prod(np.diag(U))

# In [18]
A = np.random.rand(10, 10)


t_fast_det = timeit(lambda : fast_det(A), number=1)
print(f"The time it takes to compute the determinant of a 10 x 10 matrix: {t_fast_det} seconds")

# In [19]
print(f"Recursive determinant:   \t{t_det} s")
print(f"LU determinant:          \t{t_fast_det} s")
print(f"Performance improvement: \t{t_det/t_fast_det} times faster")

# %% [markdown]
# ## Problems

# %% [markdown]
# **Problem 3.** Before we wrap this chapter up, let's go back to the definition of determinants. Even though we have lots of reasons against using the determinant formula, we have one for it: it is a good exercise, and implementing it will deepen your understanding. So, in this problem, you are going to build
# 
# $$
#     \det A = \sum_{\sigma \in S_n} \mathrm{sign}(\sigma) a_{\sigma(1)1} \dots a_{\sigma(n)n},
# $$
# 
# one step at a time.
# 
# *(i)* Implement a function that, given an integer $ n $, returns all permutations of the set $ \{0, 1, \dots, n-1\} $. Represent each permutation $ \sigma $ as a list. For example, 
# 
# ```
# [2, 0, 1]
# ```
# 
# would represent the permutation $ \sigma $, where $ \sigma(0) = 2, \sigma(1) = 0 $, and $ \sigma(2) = 1 $.

# %% [markdown]
# *(ii)* Let $ \sigma \in S_n $ be a permutation of the set $ {0, 1, \dots, n-1} $. Its *inversion number* is defined by
# 
# $$
#     \mathrm{inversion}(\sigma) = \big| \{ (i, j): i < j \text{ and } \sigma(i) > \sigma(j) \} \big|,
# $$
# 
# where $ |\cdot| $ denotes the number of elements in the set. Essentially, inversion describes the number of times a permutation reverses the order of a pair of numbers.
# 
# Turns out, the sign of $ \sigma $ can be written as
# 
# $$
#     \mathrm{sign}(\sigma) = (-1)^{\mathrm{inversion}(\sigma)}.
# $$
# 
# Implement a function that first calculates the inversion number, then the sign of an arbitrary permutation. (Permutations are represented like in the previous problem.)

# %% [markdown]
# *(iii)* Put the solutions for Problem 1. and Problem 2. together and calculate the determinant of a matrix using the permutation formula. What do you think the time complexity of this algorithm is?

# %% [markdown]
# ### Solutions
# 
# **Problem 3.** *(i)*

# In [20]
from copy import deepcopy


def permutations(n: int):
    if n == 0:
        return [[0]]
    else:
        prev_permutations = permutations(n - 1)
        
        new_permutations = []
        
        for p in prev_permutations:
            for i in range(len(p)+1):
                p_new = deepcopy(p)
                p_new.insert(i, n)
                new_permutations.append(p_new)
                
        return new_permutations

# %% [markdown]
# *(ii)*

# In [21]
from itertools import product


def inversion(permutation: list):
    n = len(permutation)
    inversions = sum([1 for i, j in product(range(n), range(n)) if i < j and permutation[i] > permutation[j]])
    return inversions

# In [22]
def sign(permutation: list):
    i = inversion(permutation)
    return (-1)**i

# %% [markdown]
# *(iii)*

# In [23]
def permutation_formula(A: np.ndarray):
    n, _ = A.shape
    S_n = permutations(n-1)
    determinant = sum([sign(p)*np.prod([A[p[i], i] for i in range(n)]) for p in S_n])
    return determinant

