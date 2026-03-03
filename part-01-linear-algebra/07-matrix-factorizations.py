# -*- coding: utf-8 -*-
# Auto-generated from '07-matrix-factorizations.ipynb' on 2025-08-08T15:22:58
# Source: code cells extracted; markdown preserved as comments.

# %% [markdown]
# # Chapter 7. Matrix factorizations

# %% [markdown]
# ## Computing eigenvalues

# %% [markdown]
# ### Power iteration in practice

# In [1]
import numpy as np

# In [2]
def power_iteration(
    A: np.ndarray, 
    n_max_steps: int = 100000,
    convergence_threshold: float = 1e-10,
    x_init: np.ndarray = None,
    normalize: bool = False
):
    """
    Performs the power iteration method to find an approximation of the dominant eigenvector 
    of a square matrix.

    Parameters
    ----------
    A : np.ndarray
        A square matrix whose dominant eigenvector is to be computed.
    n_max_steps : int, optional
        The maximum number of iterations to perform. Default is 100000.
    convergence_threshold : float, optional
        The convergence threshold for the difference between successive approximations. Default is 1e-10.
    x_init : np.ndarray, optional
        The initial guess for the eigenvector. If None, a random vector is used. Default is None.
    normalize : bool, optional
        If True, the resulting vector is normalized to unit length. Default is False.

    Returns
    -------
    np.ndarray
        The approximate dominant eigenvector of the matrix `A`.

    Raises
    ------
    ValueError
        If the input matrix `A` is not square.
    """

    n, m = A.shape
    
    # checking the validity of the input
    if n != m:
        raise ValueError("the matrix A must be square")
    
    # reshaping or defining the initial vector
    if x_init is not None:
        x = x_init.reshape(-1, 1)
    else:
        x = np.random.normal(size=(n, 1))
        
    # performing the iteration    
    for step in range(n_max_steps):
        x_transformed = A @ x    # applying the transform
        x_new = x_transformed / np.linalg.norm(x_transformed, ord=np.inf)    # scaling the result
        
        # quantifying the difference between the new and old vector
        diff = np.linalg.norm(x - x_new)
        x = x_new
        
        # stopping the iteration in case of convergence
        if diff < convergence_threshold:
            break
    
    # normalizing the result if required
    if normalize:
        return x / np.linalg.norm(x)
    
    return x

# In [3]
A = np.array([[2, 1], [1, 2]])
u_1 = power_iteration(A, normalize=True)

# In [4]
u_1

# In [5]
A @ u_1 / u_1

# %% [markdown]
# ### Power iteration for the rest of the eigenvectors

# In [6]
def get_orthogonal_complement_projection(u: np.ndarray):
    """
    Compute the projection matrix onto the orthogonal complement of the vector u.
    
    This function returns a projection matrix P such that for any vector v, 
    P @ v is the projection of v onto the subspace orthogonal to u.

    Parameters
    ----------
    u : np.ndarray
        A 1D or 2D array representing the vector u. It will be reshaped to a column vector.
    
    Returns
    -------
    np.ndarray
        The projection matrix onto the orthogonal complement of u. This matrix
        has shape (n, n), where n is the length of u.
    """

    u = u.reshape(-1, 1)
    n, _ = u.shape
    return np.eye(n) - u @ u.T / np.linalg.norm(u, ord=2)**2

# In [7]
def find_eigenvectors(A: np.ndarray, x_init: np.ndarray):
    """
    Find the eigenvectors of the matrix A using the power iteration method.
    
    This function computes the eigenvectors of the matrix A by iteratively 
    applying the power iteration method and projecting out previously found 
    eigenvectors to find orthogonal eigenvectors.

    Parameters
    ----------
    A : np.ndarray
        A square matrix of shape (n, n) for which eigenvectors are to be computed.
    
    x_init : np.ndarray
        A 1D array representing the initial vector used for the power iteration.
    
    Returns
    -------
    List[np.ndarray]
        A list of eigenvectors, each represented as a 1D numpy array of length n.
    """

    n, _ = A.shape
    eigenvectors = []
    
    for _ in range(n):
        ev = power_iteration(A, x_init=x_init)
        proj = get_orthogonal_complement_projection(ev)
        x_init = proj @ x_init
        x_init = x_init / np.linalg.norm(x_init, ord=np.inf)
        eigenvectors.append(ev)
    
    return eigenvectors

# In [8]
A = np.array([[2.0, 1.0], [1.0, 2.0]])
x_init = np.random.rand(2, 1)

# In [9]
find_eigenvectors(A, x_init)

# In [10]
def diagonalize_symmetric_matrix(A: np.ndarray, x_init: np.ndarray):
    """
    Diagonalize a symmetric matrix A using its eigenvectors.
    
    Parameters
    ----------
    A : np.ndarray
        A symmetric matrix of shape (n, n) to be diagonalized. The matrix should
        be square and symmetric.
    
    x_init : np.ndarray
        A 1D array representing the initial guess for the power iteration.

    Returns
    -------
    Tuple[np.ndarray, np.ndarray] containing:
        - U : np.ndarray
            A matrix of shape (n, n) whose columns are the normalized eigenvectors
            of A.
        - np.ndarray
            A diagonal matrix (n, n) of the eigenvalues of A, computed as U @ A @ U.T.
    """

    eigenvectors = find_eigenvectors(A, x_init)
    U = np.hstack(eigenvectors) / np.linalg.norm(np.hstack(eigenvectors), axis=0, ord=2)
    return U, U @ A @ U.T

# In [11]
diagonalize_symmetric_matrix(A, x_init)

# %% [markdown]
# ## The QR algorithm

# %% [markdown]
# ### The QR decomposition

# In [12]
def projection_coeff(x: np.ndarray, to: np.ndarray):
    """
    Compute the scalar coefficient for the projection of vector x onto vector to.

    Parameters
    ----------
    x : np.ndarray
        A 1D array representing the vector onto which the projection is computed.
    
    to : np.ndarray
        A 1D array representing the vector onto which x is being projected.
    
    Returns
    -------
    float
        The scalar coefficient representing the projection of x onto to.
    """
    return np.dot(x, to)/np.dot(to, to)

# In [13]
from typing import List

def projection(x: np.ndarray, to: List[np.ndarray], return_coeffs: bool = True):
    """
    Computes the orthogonal projection of a vector `x` onto the subspace spanned by a set of vectors `to`.

    Parameters
    ----------
    x : np.ndarray
        A 1D array representing the vector to be projected onto the subspace.
    
    to : List[np.ndarray]
        A list of 1D arrays, each representing a vector spanning the subspace onto which `x` is projected.
    
    return_coeffs : bool, optional, default=True
        If True, the function returns the list of projection coefficients. If False, only the projected vector is returned.

    Returns
    -------
    Tuple[np.ndarray, List[float]] or np.ndarray
        - If `return_coeffs` is True, returns a tuple where the first element is the projected vector and
          the second element is a list of the projection coefficients for each vector in `to`.
        - If `return_coeffs` is False, returns only the projected vector.
    """

    p_x = np.zeros_like(x)
    coeffs = []
    
    for e in to:
        coeff = projection_coeff(x, e)
        coeffs.append(coeff)
        p_x += coeff*e
    
    if return_coeffs:
        return p_x, coeffs
    else:
        return p_x

# In [14]
def QR(A: np.ndarray):
    """
    Computes the QR decomposition of matrix A using the Gram-Schmidt orthogonalization process.

    Parameters
    ----------
    A : np.ndarray
        A 2D array of shape (n, m) representing the matrix to be decomposed. 
        The matrix A should have full column rank for a valid QR decomposition.
    
    Returns
    -------
    Tuple[np.ndarray, np.ndarray]
        - Q : np.ndarray
            An orthogonal matrix of shape (n, m), whose columns are orthonormal.
        - R : np.ndarray
            An upper triangular matrix of shape (m, m), representing the coefficients of the 
            linear combinations of the columns of A.
    """
    n, m = A.shape
    
    A_columns = [A[:, i] for i in range(A.shape[1])]
    Q_columns, R_columns = [], []
    
    Q_columns.append(A_columns[0])
    R_columns.append([1] + (m-1)*[0])
    
    for i, a in enumerate(A_columns[1:]):
        p, coeffs = projection(a, Q_columns, return_coeffs=True)
        next_q = a - p
        next_r = coeffs + [1] + max(0, m - i - 2)*[0]
        
        Q_columns.append(next_q)
        R_columns.append(next_r)
    
    # assembling Q and R from its columns
    Q, R = np.array(Q_columns).T, np.array(R_columns).T
    
    # normalizing Q's columns
    Q_norms = np.linalg.norm(Q, axis=0)
    Q = Q/Q_norms
    R = np.diag(Q_norms) @ R
    return Q, R

# In [15]
A = np.random.rand(3, 3)
Q, R = QR(A)

# In [16]
np.allclose(A, Q @ R)

# In [17]
np.allclose(Q.T @ Q, np.eye(3))

# In [18]
np.allclose(R, np.triu(R))

# %% [markdown]
# ### Iterating the QR decomposition

# In [19]
def QR_algorithm(A: np.ndarray, n_iter: int = 1000):
    """
    Computes the QR algorithm to find the eigenvalues of a matrix A.

    Parameters
    ----------
    A : np.ndarray
        A square matrix of shape (n, n) for which the eigenvalues are to be computed.
    
    n_iter : int, optional, default=1000
        The number of iterations to run the QR algorithm. More iterations may lead to more accurate results,
        but the algorithm typically converges quickly.

    Returns
    -------
    np.ndarray
        A matrix that has converged, where the diagonal elements are the eigenvalues of the original matrix A.
        The off-diagonal elements should be close to zero.
    """
        
    for _ in range(n_iter):
        Q, R = QR(A)
        A = R @ Q
    
    return A

# In [20]
A = np.array([[2.0, 1.0], [1.0, 2.0]])
QR_algorithm(A)

# In [21]
A = np.array([[0.0, 1.0], [1.0, 0.0]])
QR_algorithm(A)

