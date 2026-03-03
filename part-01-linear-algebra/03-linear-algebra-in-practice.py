# -*- coding: utf-8 -*-
# Auto-generated from '03-linear-algebra-in-practice.ipynb' on 2025-08-08T15:22:58
# Source: code cells extracted; markdown preserved as comments.

# %% [markdown]
# # Chapter 3. Linear algebra in practice

# In [1]
import numpy as np

x = np.array([1.8, -4.5, 9.2, 7.3])
y = np.array([-5.2, -1.1, 0.7, 5.1])

# In [2]
def add(x: np.ndarray, y: np.ndarray):
    x_plus_y = np.zeros(shape=len(x))
    
    for i in range(len(x_plus_y)):
        x_plus_y[i] = x[i] + y[i]
        
    return x_plus_y

# In [3]
add(x, y)

# In [4]
np.equal(x + y, add(x, y))

# In [5]
1.0 == 0.3*3 + 0.1

# In [6]
0.3*3 + 0.1

# In [7]
all(np.equal(x + y, add(x, y)))

# %% [markdown]
# ## Vectors in NumPy

# In [8]
def just_a_quadratic_polynomial(x):
    return 3*x**2 + 1

# In [9]
x = np.array([1.8, -4.5, 9.2, 7.3])
just_a_quadratic_polynomial(x)

# In [10]
from math import exp

exp(x)

# In [11]
def naive_exp(x: np.ndarray):
    x_exp = np.empty_like(x)
    
    for i in range(len(x)):
        x_exp[i] = exp(x[i])
        
    return x_exp

# In [12]
naive_exp(x)

# In [13]
def bit_less_naive_exp(x: np.ndarray):
    return np.array([exp(x_i) for x_i in x])

# In [14]
bit_less_naive_exp(x)

# In [15]
np.exp(x)

# In [16]
all(np.equal(naive_exp(x), np.exp(x)))

# In [17]
all(np.equal(bit_less_naive_exp(x), np.exp(x)))

# In [18]
from timeit import timeit


n_runs = 100000
size = 1000


t_naive_exp = timeit(
    "np.array([exp(x_i) for x_i in x])",
    setup=f"import numpy as np; from math import exp; x = np.ones({size})",
    number=n_runs
)

t_numpy_exp = timeit(
    "np.exp(x)",
    setup=f"import numpy as np; from math import exp; x = np.ones({size})",
    number=n_runs
)


print(f"Built-in exponential:    \t{t_naive_exp:.5f} s")
print(f"NumPy exponential:       \t{t_numpy_exp:.5f} s")
print(f"Performance improvement: \t{t_naive_exp/t_numpy_exp:.5f} times faster")

# In [19]
def naive_sum(x: np.ndarray):
    val = 0
    
    for x_i in x:
        val += x_i
        
    return val

# In [20]
naive_sum(x)

# In [21]
sum(x)

# In [22]
np.sum(x)

# In [23]
x.sum()

# In [24]
t_naive_sum = timeit(
    "sum(x)",
    setup=f"import numpy as np; x = np.ones({size})",
    number=n_runs
)

t_numpy_sum = timeit(
    "np.sum(x)",
    setup=f"import numpy as np; x = np.ones({size})",
    number=n_runs
)


print(f"Built-in sum:            \t{t_naive_sum:.5f} s")
print(f"NumPy sum:               \t{t_numpy_sum:.5f} s")
print(f"Performance improvement: \t{t_naive_sum/t_numpy_sum:.5f} times faster")

# In [25]
np.prod(x)

# %% [markdown]
# ### Norms, distances, and dot products

# In [26]
def euclidean_norm(x: np.ndarray):
    return np.sqrt(np.sum(x**2))

# In [27]
x = np.array([-3.0, 1.2, 1.2, 2.1])    # a 1D array with 4 elements, which is a vector in 4-dimensional space
y = np.array([8.1, 6.3])               # a 1D array with 2 elements, which is a vector in 2-dimensional space

# In [28]
euclidean_norm(x)

# In [29]
euclidean_norm(y)

# In [30]
np.linalg.norm(x)

# In [31]
np.equal(euclidean_norm(x), np.linalg.norm(x))

# In [32]
type(np.inf)

# In [33]
def p_norm(x: np.ndarray, p: float):
    if np.isinf(p):
        return np.max(np.abs(x))
    elif p >= 1:
        return (np.sum(np.abs(x)**p))**(1/p)
    else:
        raise ValueError("p must be a float larger or equal than 1.0 or inf.")

# In [34]
x = np.array([-3.0, 1.2, 1.2, 2.1])

for p in [1, 2, 42, np.inf]:
    print(f"p-norm for p = {p}: \t {p_norm(x, p=p):.5f}")

# In [35]
for p in [1, 2, 42, np.inf]:
    print(f"p-norm for p = {p}: \t {np.linalg.norm(x, ord=p):.5f}")

# In [36]
def euclidean_distance(x: np.ndarray, y: np.ndarray):
    return np.linalg.norm(x - y, ord=2)

# In [37]
def dot_product(x: np.ndarray, y: np.ndarray):
    return np.sum(x*y)

# In [38]
x = np.array([-3.0, 1.2, 1.2, 2.1])
y = np.array([1.9, 2.5, 3.9, 1.2])

dot_product(x, y)

# In [39]
x = np.array([-3.0, 1.2, 1.2, 2.1])
y = np.array([1.9, 2.5])

dot_product(x, y)

# In [40]
x = np.array([-3.0, 1.2, 1.2, 2.1])
y = np.array([2.0])

dot_product(x, y)

# In [41]
x*y

# In [42]
x = np.array([-3.0, 1.2, 1.2, 2.1])
y = np.array([1.9, 2.5, 3.9, 1.2])

np.dot(x, y)

# In [43]
x = np.array([-3.0, 1.2, 1.2, 2.1])
y = np.array([2.0])

np.dot(x, y)

# %% [markdown]
# ### The Gram-Schmidt orthogonalization process

# In [44]
vectors = [np.random.rand(5) for _ in range(5)]    # randomly generated vectors in a list

# In [45]
vectors

# In [46]
from typing import List


def projection(x: np.ndarray, to: List[np.ndarray]):
    """
    Computes the orthogonal projection of the vector `x`
    onto the subspace spanned by the set of vectors `to`.
    """
    p_x = np.zeros_like(x)
    
    for e in to:
        e_norm_square = np.dot(e, e)
        p_x += np.dot(x, e)*e/e_norm_square
        
    return p_x

# In [47]
x = np.array([1.0, 2.0])
e = np.array([2.0, 1.0])

x_to_e = projection(x, to=[e])

# In [48]
import matplotlib.pyplot as plt

with plt.style.context("seaborn-v0_8"):
    plt.figure(figsize=(7, 7))
    plt.xlim([-0, 3])
    plt.ylim([-0, 3])
    plt.arrow(0, 0, x[0], x[1], head_width=0.1, color="r", label="x", linewidth=2)
    plt.arrow(0, 0, e[0], e[1], head_width=0.1, color="g", label="e", linewidth=2)
    plt.arrow(x_to_e[0], x_to_e[1], x[0] - x_to_e[0], x[1] - x_to_e[1], linestyle="--")
    plt.arrow(0, 0, x_to_e[0], x_to_e[1], head_width=0.1, color="b", label="projection(x, to=[e])")
    plt.legend()
    plt.show()

# In [49]
np.allclose(np.dot(e, x - x_to_e), 0.0)

# In [50]
def gram_schmidt(vectors: List[np.ndarray]):
    """
    Creates an orthonormal set of vectors from the input
    that spans the same subspaces.
    """
    output = []
    
    # 1st step: finding an orthogonal set of vectors
    output.append(vectors[0])
    for v in vectors[1:]:
        v_proj = projection(v, to=output)
        output.append(v - v_proj)
    
    # 2nd step: normalizing the result
    output = [v/np.linalg.norm(v, ord=2) for v in output]
    
    return output 

# In [51]
gram_schmidt([np.array([2.0, 1.0, 1.0]), 
              np.array([1.0, 2.0, 1.0]),
              np.array([1.0, 1.0, 2.0])])

# In [52]
test_vectors = [np.array([1.0, 0.0, 0.0]), 
                np.array([1.0, 1.0, 0.0]),
                np.array([1.0, 1.0, 1.0])]

# In [53]
gram_schmidt(test_vectors)

# %% [markdown]
# ## Matrices, the workhorses of linear algebra

# %% [markdown]
# ### Matrices as arrays

# In [54]
from typing import Tuple


class Matrix:
    def __init__(self, shape: Tuple[int, int]):
        if len(shape) != 2:
            raise ValueError("The shape of a Matrix object must be a two-dimensional tuple.")
            
        self.shape = shape
        self.data = [0.0 for _ in range(shape[0]*shape[1])]    
    
    def _linear_idx(self, i: int, j: int):
        return i*self.shape[1] + j
    
    def __getitem__(self, key: Tuple[int, int]):
        linear_idx = self._linear_idx(*key)
        return self.data[linear_idx]
        
    def __setitem__(self, key: Tuple[int, int], value):     
        linear_idx = self._linear_idx(*key)
        self.data[linear_idx] = value
        
    def __repr__(self):
        array_form = [
            [self[i, j] for j in range(self.shape[1])]
            for i in range(self.shape[0])
        ]
        return "\n".join(["\t".join([f"{x}" for x in row]) for row in array_form])

# In [55]
M = Matrix(shape=(3, 4))

# In [56]
M[1, 2] = 3.14

# In [57]
M[1, 2]

# In [58]
M

# %% [markdown]
# ### Matrices in NumPy

# In [59]
import numpy as np

A = np.array([[0, 1, 2, 3],
              [4, 5, 6, 7],
              [8, 9, 10, 11]])

B = np.array([[5, 5, 5, 5],
              [5, 5, 5, 5],
              [5, 5, 5, 5]])

# In [60]
A

# In [61]
A + B       # pointwise addition

# In [62]
A*B         # pointwise multiplication

# In [63]
np.exp(A)   # pointwise application of the exponential function

# In [64]
np.transpose(A)

# In [65]
A.T         # is the same as np.transpose(A)

# In [66]
A[1, 2]    # 1st row, 2nd column (if we index rows and columns from zero)

# In [67]
A[:, 2]    # 2nd column

# In [68]
A[1, :]    # 1st row

# In [69]
A[2, 1:4]   # 2nd row, 1st-4th elements

# In [70]
A[1]        # 1st row

# In [71]
for row in A:
    print(row)

# In [72]
np.zeros(shape=(4, 5))

# In [73]
A = np.array([[0, 1, 2, 3],
              [4, 5, 6, 7],
              [8, 9, 10, 11]])

# In [74]
A

# In [75]
A.shape

# In [76]
A.reshape(6, 2)    # reshapes A into a 6 x 2 matrix

# In [77]
A

# In [78]
A.reshape(-1, 2)

# In [79]
A.reshape(-1, 4)

# %% [markdown]
# ### Matrix multiplication, revisited

# In [80]
from itertools import product


def matrix_multiplication(A: np.ndarray, B: np.ndarray):
    # checking if multiplication is possible
    if A.shape[1] != B.shape[0]:
        raise ValueError("The number of columns in A must match the number of rows in B.")
    
    # initializing an array for the product
    AB = np.zeros(shape=(A.shape[0], B.shape[1]))
    
    # calculating the elements of AB
    for i, j in product(range(A.shape[0]), range(B.shape[1])):
        AB[i, j] = np.sum(A[i, :]*B[:, j])
        
    return AB

# In [81]
A = np.ones(shape=(4, 6))
B = np.ones(shape=(6, 3))

# In [82]
matrix_multiplication(A, B)

# In [83]
np.matmul(A, B)

# In [84]
for _ in range(100):
    n, m, l = np.random.randint(1, 100), np.random.randint(1, 100), np.random.randint(1, 100)
    A = np.random.rand(n, m)
    B = np.random.rand(m, l)
    
    if not np.allclose(np.matmul(A, B), matrix_multiplication(A, B)):
        print(f"Result mismatch for\n{A}\n and\n{B}")
        break
else:
    print("All good! Yay!")

# In [85]
A = np.ones(shape=(4, 6))
B = np.ones(shape=(6, 3))

np.allclose(A @ B, np.matmul(A, B))

# %% [markdown]
# ### Matrices and data

# In [86]
x1 = np.array([2, 0, 0, 0])       # first data point
x2 = np.array([-1, 1, 0, 0])      # second data point

A = np.array([[0, 1, 2, 3],
              [4, 5, 6, 7],
              [8, 9, 10, 11]])    # a feature transformation

# In [87]
A.shape

# In [88]
x1.shape

# In [89]
np.matmul(A, x1)

# In [90]
np.hstack([x1, x2])    # np.hstack takes a list of np.ndarrays as its argument

# In [91]
# x.reshape(-1,1) turns x into a column vector
data = np.hstack([x1.reshape(-1, 1), x2.reshape(-1, 1)])

# In [92]
data

# In [93]
np.matmul(A, data)

# %% [markdown]
# ## Problems

# %% [markdown]
# **Problem 3.**

# In [94]
def p_norm(x: np.ndarray, p: float):
    if p >= 1:
        return (np.sum(np.abs(x)**p))**(1/p)
    elif np.isinf(p):
        return np.max(np.abs(x))
    else:
        raise ValueError("p must be a float larger or equal than 1.0 or inf.")

