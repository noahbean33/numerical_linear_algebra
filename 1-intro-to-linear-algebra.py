# -*- coding: utf-8 -*-
# Auto-generated from '1-intro-to-linear-algebra.ipynb' on 2025-08-08T15:22:56
# Source: code cells extracted; markdown preserved as comments.

# %% [markdown]
# <a href="https://colab.research.google.com/github/jonkrohn/ML-foundations/blob/master/notebooks/1-intro-to-linear-algebra.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# %% [markdown]
# # Intro to Linear Algebra

# %% [markdown]
# This topic, *Intro to Linear Algebra*, is the first in the *Machine Learning Foundations* series.
# 
# It is essential because linear algebra lies at the heart of most machine learning approaches and is especially predominant in deep learning, the branch of ML at the forefront of today’s artificial intelligence advances. Through the measured exposition of theory paired with interactive examples, you’ll develop an understanding of how linear algebra is used to solve for unknown values in high-dimensional spaces, thereby enabling machines to recognize patterns and make predictions.
# 
# The content covered in *Intro to Linear Algebra* is itself foundational for all the other topics in the Machine Learning Foundations series and it is especially relevant to *Linear Algebra II*.

# %% [markdown]
# Over the course of studying this topic, you'll:
# 
# * Understand the fundamentals of linear algebra, a ubiquitous approach for solving for unknowns within high-dimensional spaces.
# 
# * Develop a geometric intuition of what’s going on beneath the hood of machine learning algorithms, including those used for deep learning.
# * Be able to more intimately grasp the details of machine learning papers as well as all of the other subjects that underlie ML, including calculus, statistics, and optimization algorithms.

# %% [markdown]
# **Note that this Jupyter notebook is not intended to stand alone. It is the companion code to a lecture or to videos from Jon Krohn's [Machine Learning Foundations](https://github.com/jonkrohn/ML-foundations) series, which offer detail on the following:**
# 
# *Segment 1: Data Structures for Algebra*
# 
# * What Linear Algebra Is  
# * A Brief History of Algebra
# * Tensors
# * Scalars
# * Vectors and Vector Transposition
# * Norms and Unit Vectors
# * Basis, Orthogonal, and Orthonormal Vectors
# * Arrays in NumPy  
# * Matrices
# * Tensors in TensorFlow and PyTorch
# 
# *Segment 2: Common Tensor Operations*
# 
# * Tensor Transposition
# * Basic Tensor Arithmetic
# * Reduction
# * The Dot Product
# * Solving Linear Systems
# 
# *Segment 3: Matrix Properties*
# 
# * The Frobenius Norm
# * Matrix Multiplication
# * Symmetric and Identity Matrices
# * Matrix Inversion
# * Diagonal Matrices
# * Orthogonal Matrices

# %% [markdown]
# ## Segment 1: Data Structures for Algebra
# 
# **Slides used to begin segment, with focus on introducing what linear algebra is, including hands-on paper and pencil exercises.**

# %% [markdown]
# ### What Linear Algebra Is

# In [1]
import numpy as np
import matplotlib.pyplot as plt

# In [2]
t = np.linspace(0, 40, 1000) # start, finish, n points

# %% [markdown]
# Distance travelled by robber: $d = 2.5t$

# In [3]
d_r = 2.5 * t

# %% [markdown]
# Distance travelled by sheriff: $d = 3(t-5)$

# In [4]
d_s = 3 * (t-5)

# In [5]
fig, ax = plt.subplots()
plt.title('A Bank Robber Caught')
plt.xlabel('time (in minutes)')
plt.ylabel('distance (in km)')
ax.set_xlim([0, 40])
ax.set_ylim([0, 100])
ax.plot(t, d_r, c='green')
ax.plot(t, d_s, c='brown')
plt.axvline(x=30, color='purple', linestyle='--')
_ = plt.axhline(y=75, color='purple', linestyle='--')

# %% [markdown]
# **Return to slides here.**

# %% [markdown]
# ### Scalars (Rank 0 Tensors) in Base Python

# In [6]
x = 25
x

# In [7]
type(x) # if we'd like more specificity (e.g., int16, uint8), we need NumPy or another numeric library

# In [8]
y = 3

# In [9]
py_sum = x + y
py_sum

# In [10]
type(py_sum)

# In [11]
x_float = 25.0
float_sum = x_float + y
float_sum

# In [12]
type(float_sum)

# %% [markdown]
# ### Scalars in PyTorch
# 
# * PyTorch and TensorFlow are the two most popular *automatic differentiation* libraries (a focus of the [*Calculus I*](https://github.com/jonkrohn/ML-foundations/blob/master/notebooks/3-calculus-i.ipynb) and [*Calculus II*](https://github.com/jonkrohn/ML-foundations/blob/master/notebooks/4-calculus-ii.ipynb) subjects in the *ML Foundations* series) in Python, itself the most popular programming language in ML.
# * PyTorch tensors are designed to be pythonic, i.e., to feel and behave like NumPy arrays.
# * The advantage of PyTorch tensors relative to NumPy arrays is that they easily be used for operations on GPU (see [here](https://pytorch.org/tutorials/beginner/examples_tensor/two_layer_net_tensor.html) for example).
# * Documentation on PyTorch tensors, including available data types, is [here](https://pytorch.org/docs/stable/tensors.html).

# In [13]
import torch

# In [14]
x_pt = torch.tensor(25) # type specification optional, e.g.: dtype=torch.float16
x_pt

# In [15]
x_pt.shape

# %% [markdown]
# ### Scalars in TensorFlow (version 2.0 or later)
# 
# Tensors created with a wrapper, all of which [you can read about here](https://www.tensorflow.org/guide/tensor):  
# 
# * `tf.Variable`
# * `tf.constant`
# * `tf.placeholder`
# * `tf.SparseTensor`
# 
# Most widely-used is `tf.Variable`, which we'll use here.
# 
# As with TF tensors, in PyTorch we can similarly perform operations, and we can easily convert to and from NumPy arrays.
# 
# Also, a full list of tensor data types is available [here](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType).

# In [16]
import tensorflow as tf

# In [17]
x_tf = tf.Variable(25, dtype=tf.int16) # dtype is optional
x_tf

# In [18]
x_tf.shape

# In [19]
y_tf = tf.Variable(3, dtype=tf.int16)

# In [20]
x_tf + y_tf

# In [21]
tf_sum = tf.add(x_tf, y_tf)
tf_sum

# In [22]
tf_sum.numpy() # note that NumPy operations automatically convert tensors to NumPy arrays, and vice versa

# In [23]
type(tf_sum.numpy())

# In [24]
tf_float = tf.Variable(25., dtype=tf.float16)
tf_float

# %% [markdown]
# **Return to slides here.**

# %% [markdown]
# ### Vectors (Rank 1 Tensors) in NumPy

# In [25]
x = np.array([25, 2, 5]) # type argument is optional, e.g.: dtype=np.float16
x

# In [26]
len(x)

# In [27]
x.shape

# In [28]
type(x)

# In [29]
x[0] # zero-indexed

# In [30]
type(x[0])

# %% [markdown]
# ### Vector Transposition

# In [31]
# Transposing a regular 1-D array has no effect...
x_t = x.T
x_t

# In [32]
x_t.shape

# In [33]
# ...but it does we use nested "matrix-style" brackets:
y = np.array([[25, 2, 5]])
y

# In [34]
y.shape

# In [35]
# ...but can transpose a matrix with a dimension of length 1, which is mathematically equivalent:
y_t = y.T
y_t

# In [36]
y_t.shape # this is a column vector as it has 3 rows and 1 column

# In [37]
# Column vector can be transposed back to original row vector:
y_t.T

# In [38]
y_t.T.shape

# %% [markdown]
# ### Zero Vectors
# 
# Have no effect if added to another vector

# In [39]
z = np.zeros(3)
z

# %% [markdown]
# ### Vectors in PyTorch and TensorFlow

# In [40]
x_pt = torch.tensor([25, 2, 5])
x_pt

# In [41]
x_tf = tf.Variable([25, 2, 5])
x_tf

# %% [markdown]
# **Return to slides here.**

# %% [markdown]
# ### $L^2$ Norm

# In [42]
x

# In [43]
(25**2 + 2**2 + 5**2)**(1/2)

# In [44]
np.linalg.norm(x)

# %% [markdown]
# So, if units in this 3-dimensional vector space are meters, then the vector $x$ has a length of 25.6m

# %% [markdown]
# **Return to slides here.**

# %% [markdown]
# ### $L^1$ Norm

# In [45]
x

# In [46]
np.abs(25) + np.abs(2) + np.abs(5)

# %% [markdown]
# **Return to slides here.**

# %% [markdown]
# ### Squared $L^2$ Norm

# In [47]
x

# In [48]
(25**2 + 2**2 + 5**2)

# In [49]
# we'll cover tensor multiplication more soon but to prove point quickly:
np.dot(x, x)

# %% [markdown]
# **Return to slides here.**

# %% [markdown]
# ### Max Norm

# In [50]
x

# In [51]
np.max([np.abs(25), np.abs(2), np.abs(5)])

# %% [markdown]
# **Return to slides here.**

# %% [markdown]
# ### Orthogonal Vectors

# In [52]
i = np.array([1, 0])
i

# In [53]
j = np.array([0, 1])
j

# In [54]
np.dot(i, j) # detail on the dot operation coming up...

# %% [markdown]
# **Return to slides here.**

# %% [markdown]
# ### Matrices (Rank 2 Tensors) in NumPy

# In [55]
# Use array() with nested brackets:
X = np.array([[25, 2], [5, 26], [3, 7]])
X

# In [56]
X.shape

# In [57]
X.size

# In [58]
# Select left column of matrix X (zero-indexed)
X[:,0]

# In [59]
# Select middle row of matrix X:
X[1,:]

# In [60]
# Another slicing-by-index example:
X[0:2, 0:2]

# %% [markdown]
# ### Matrices in PyTorch

# In [61]
X_pt = torch.tensor([[25, 2], [5, 26], [3, 7]])
X_pt

# In [62]
X_pt.shape # pythonic relative to TensorFlow

# In [63]
X_pt[1,:] # N.B.: Python is zero-indexed; written algebra is one-indexed

# %% [markdown]
# ### Matrices in TensorFlow

# In [64]
X_tf = tf.Variable([[25, 2], [5, 26], [3, 7]])
X_tf

# In [65]
tf.rank(X_tf)

# In [66]
tf.shape(X_tf)

# In [67]
X_tf[1,:]

# %% [markdown]
# **Return to slides here.**

# %% [markdown]
# ### Higher-Rank Tensors
# 
# As an example, rank 4 tensors are common for images, where each dimension corresponds to:
# 
# 1. Number of images in training batch, e.g., 32
# 2. Image height in pixels, e.g., 28 for [MNIST digits](http://yann.lecun.com/exdb/mnist/)
# 3. Image width in pixels, e.g., 28
# 4. Number of color channels, e.g., 3 for full-color images (RGB)

# In [68]
images_pt = torch.zeros([32, 28, 28, 3])

# In [69]
# images_pt

# In [70]
images_tf = tf.zeros([32, 28, 28, 3])

# In [71]
# images_tf

# %% [markdown]
# **Return to slides here.**

# %% [markdown]
# ## Segment 2: Common Tensor Operations

# %% [markdown]
# ### Tensor Transposition

# In [72]
X

# In [73]
X.T

# In [74]
X_pt.T

# In [75]
tf.transpose(X_tf) # less Pythonic

# %% [markdown]
# ### Basic Arithmetical Properties

# %% [markdown]
# Adding or multiplying with scalar applies operation to all elements and tensor shape is retained:

# In [76]
X*2

# In [77]
X+2

# In [78]
X*2+2

# In [79]
X_pt*2+2 # Python operators are overloaded; could alternatively use torch.mul() or torch.add()

# In [80]
torch.add(torch.mul(X_pt, 2), 2)

# In [81]
X_tf*2+2 # Operators likewise overloaded; could equally use tf.multiply() tf.add()

# In [82]
tf.add(tf.multiply(X_tf, 2), 2)

# %% [markdown]
# If two tensors have the same size, operations are often by default applied element-wise. This is **not matrix multiplication**, which we'll cover later, but is rather called the **Hadamard product** or simply the **element-wise product**.
# 
# The mathematical notation is $A \odot X$

# In [83]
X

# In [84]
A = X+2
A

# In [85]
A + X

# In [86]
A * X

# In [87]
A_pt = X_pt + 2

# In [88]
A_pt + X_pt

# In [89]
A_pt * X_pt

# In [90]
A_tf = X_tf + 2

# In [91]
A_tf + X_tf

# In [92]
A_tf * X_tf

# %% [markdown]
# ### Reduction

# %% [markdown]
# Calculating the sum across all elements of a tensor is a common operation. For example:
# 
# * For vector ***x*** of length *n*, we calculate $\sum_{i=1}^{n} x_i$
# * For matrix ***X*** with *m* by *n* dimensions, we calculate $\sum_{i=1}^{m} \sum_{j=1}^{n} X_{i,j}$

# In [93]
X

# In [94]
X.sum()

# In [95]
torch.sum(X_pt)

# In [96]
tf.reduce_sum(X_tf)

# In [97]
# Can also be done along one specific axis alone, e.g.:
X.sum(axis=0) # summing over all rows (i.e., along columns)

# In [98]
X.sum(axis=1) # summing over all columns (i.e., along rows)

# In [99]
torch.sum(X_pt, 0)

# In [100]
tf.reduce_sum(X_tf, 1)

# %% [markdown]
# Many other operations can be applied with reduction along all or a selection of axes, e.g.:
# 
# * maximum
# * minimum
# * mean
# * product
# 
# They're fairly straightforward and used less often than summation, so you're welcome to look them up in library docs if you ever need them.

# %% [markdown]
# ### The Dot Product

# %% [markdown]
# If we have two vectors (say, ***x*** and ***y***) with the same length *n*, we can calculate the dot product between them. This is annotated several different ways, including the following:
# 
# * $x \cdot y$
# * $x^Ty$
# * $\langle x,y \rangle$
# 
# Regardless which notation you use (I prefer the first), the calculation is the same; we calculate products in an element-wise fashion and then sum reductively across the products to a scalar value. That is, $x \cdot y = \sum_{i=1}^{n} x_i y_i$
# 
# The dot product is ubiquitous in deep learning: It is performed at every artificial neuron in a deep neural network, which may be made up of millions (or orders of magnitude more) of these neurons.

# In [101]
x

# In [102]
y = np.array([0, 1, 2])
y

# In [103]
25*0 + 2*1 + 5*2

# In [104]
np.dot(x, y)

# In [105]
x_pt

# In [106]
y_pt = torch.tensor([0, 1, 2])
y_pt

# In [107]
np.dot(x_pt, y_pt)

# In [108]
torch.dot(torch.tensor([25, 2, 5.]), torch.tensor([0, 1, 2.]))

# In [109]
x_tf

# In [110]
y_tf = tf.Variable([0, 1, 2])
y_tf

# In [111]
tf.reduce_sum(tf.multiply(x_tf, y_tf))

# %% [markdown]
# **Return to slides here.**

# %% [markdown]
# ### Solving Linear Systems

# %% [markdown]
# In the **Substitution** example, the two equations in the system are:
# $$ y = 3x $$
# $$ -5x + 2y = 2 $$
# 
# The second equation can be rearranged to isolate $y$:
# $$ 2y = 2 + 5x $$
# $$ y = \frac{2 + 5x}{2} = 1 + \frac{5x}{2} $$

# In [112]
x = np.linspace(-10, 10, 1000) # start, finish, n points

# In [113]
y1 = 3 * x

# In [114]
y2 = 1 + (5*x)/2

# In [115]
fig, ax = plt.subplots()
plt.xlabel('x')
plt.ylabel('y')
ax.set_xlim([0, 3])
ax.set_ylim([0, 8])
ax.plot(x, y1, c='green')
ax.plot(x, y2, c='brown')
plt.axvline(x=2, color='purple', linestyle='--')
_ = plt.axhline(y=6, color='purple', linestyle='--')

# %% [markdown]
# **Return to slides here.**

# %% [markdown]
# In the **Elimination** example, the two equations in the system are:
# $$ 2x - 3y = 15 $$
# $$ 4x + 10y = 14 $$
# 
# Both equations can be rearranged to isolate $y$. Starting with the first equation:
# $$ -3y = 15 - 2x $$
# $$ y = \frac{15 - 2x}{-3} = -5 + \frac{2x}{3} $$
# 
# Then for the second equation:
# $$ 4x + 10y = 14 $$
# $$ 2x + 5y = 7 $$
# $$ 5y = 7 - 2x $$
# $$ y = \frac{7 - 2x}{5} $$

# In [116]
y1 = -5 + (2*x)/3

# In [117]
y2 = (7-2*x)/5

# In [118]
fig, ax = plt.subplots()
plt.xlabel('x')
plt.ylabel('y')

# Add x and y axes:
plt.axvline(x=0, color='lightgray')
plt.axhline(y=0, color='lightgray')

ax.set_xlim([-2, 10])
ax.set_ylim([-6, 4])
ax.plot(x, y1, c='green')
ax.plot(x, y2, c='brown')
plt.axvline(x=6, color='purple', linestyle='--')
_ = plt.axhline(y=-1, color='purple', linestyle='--')

# %% [markdown]
# **Return to slides here.**

# %% [markdown]
# ## Segment 3: Matrix Properties

# %% [markdown]
# ### Frobenius Norm

# In [119]
X = np.array([[1, 2], [3, 4]])
X

# In [120]
(1**2 + 2**2 + 3**2 + 4**2)**(1/2)

# In [121]
np.linalg.norm(X) # same function as for vector L2 norm

# In [122]
X_pt = torch.tensor([[1, 2], [3, 4.]]) # torch.norm() supports floats only

# In [123]
torch.norm(X_pt)

# In [124]
X_tf = tf.Variable([[1, 2], [3, 4.]]) # tf.norm() also supports floats only

# In [125]
tf.norm(X_tf)

# %% [markdown]
# **Return to slides here.**

# %% [markdown]
# ### Matrix Multiplication (with a Vector)

# In [126]
A = np.array([[3, 4], [5, 6], [7, 8]])
A

# In [127]
b = np.array([1, 2])
b

# In [128]
np.dot(A, b) # even though technically dot products are between vectors only

# In [129]
A_pt = torch.tensor([[3, 4], [5, 6], [7, 8]])
A_pt

# In [130]
b_pt = torch.tensor([1, 2])
b_pt

# In [131]
torch.matmul(A_pt, b_pt) # like np.dot(), automatically infers dims in order to perform dot product, matvec, or matrix multiplication

# In [132]
A_tf = tf.Variable([[3, 4], [5, 6], [7, 8]])
A_tf

# In [133]
b_tf = tf.Variable([1, 2])
b_tf

# In [134]
tf.linalg.matvec(A_tf, b_tf)

# %% [markdown]
# **Return to slides here.**

# %% [markdown]
# ### Matrix Multiplication (with Two Matrices)

# In [135]
A

# In [136]
B = np.array([[1, 9], [2, 0]])
B

# In [137]
np.dot(A, B)

# %% [markdown]
# Note that matrix multiplication is not "commutative" (i.e., $AB \neq BA$) so uncommenting the following line will throw a size mismatch error:

# In [138]
# np.dot(B, A)

# In [139]
B_pt = torch.from_numpy(B) # much cleaner than TF conversion
B_pt

# In [140]
# another neat way to create the same tensor with transposition:
B_pt = torch.tensor([[1, 2], [9, 0]]).T
B_pt

# In [141]
torch.matmul(A_pt, B_pt) # no need to change functions, unlike in TF

# In [142]
B_tf = tf.convert_to_tensor(B, dtype=tf.int32)
B_tf

# In [143]
tf.matmul(A_tf, B_tf)

# %% [markdown]
# **Return to slides here.**

# %% [markdown]
# ### Symmetric Matrices

# In [144]
X_sym = np.array([[0, 1, 2], [1, 7, 8], [2, 8, 9]])
X_sym

# In [145]
X_sym.T

# In [146]
X_sym.T == X_sym

# %% [markdown]
# **Return to slides here.**

# %% [markdown]
# ### Identity Matrices

# In [147]
I = torch.tensor([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
I

# In [148]
x_pt = torch.tensor([25, 2, 5])
x_pt

# In [149]
torch.matmul(I, x_pt)

# %% [markdown]
# **Return to slides here.**

# %% [markdown]
# ### Answers to Matrix Multiplication Qs

# In [150]
M_q = torch.tensor([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
M_q

# In [151]
V_q = torch.tensor([[-1, 1, -2], [0, 1, 2]]).T
V_q

# In [152]
torch.matmul(M_q, V_q)

# %% [markdown]
# ### Matrix Inversion

# In [153]
X = np.array([[4, 2], [-5, -3]])
X

# In [154]
Xinv = np.linalg.inv(X)
Xinv

# %% [markdown]
# As a quick aside, let's prove that $X^{-1}X = I_n$ as per the slides:

# In [155]
np.dot(Xinv, X)

# %% [markdown]
# ...and now back to solving for the unknowns in $w$:

# In [156]
y = np.array([4, -7])
y

# In [157]
w = np.dot(Xinv, y)
w

# %% [markdown]
# Show that $y = Xw$:

# In [158]
np.dot(X, w)

# %% [markdown]
# **Geometric Visualization**
# 
# Recalling from the slides that the two equations in the system are:
# $$ 4b + 2c = 4 $$
# $$ -5b - 3c = -7 $$
# 
# Both equations can be rearranged to isolate a variable, say $c$. Starting with the first equation:
# $$ 4b + 2c = 4 $$
# $$ 2b + c = 2 $$
# $$ c = 2 - 2b $$
# 
# Then for the second equation:
# $$ -5b - 3c = -7 $$
# $$ -3c = -7 + 5b $$
# $$ c = \frac{-7 + 5b}{-3} = \frac{7 - 5b}{3} $$

# In [159]
b = np.linspace(-10, 10, 1000) # start, finish, n points

# In [160]
c1 = 2 - 2*b

# In [161]
c2 = (7-5*b)/3

# In [162]
fig, ax = plt.subplots()
plt.xlabel('b', c='darkorange')
plt.ylabel('c', c='brown')

plt.axvline(x=0, color='lightgray')
plt.axhline(y=0, color='lightgray')

ax.set_xlim([-2, 3])
ax.set_ylim([-1, 5])
ax.plot(b, c1, c='purple')
ax.plot(b, c2, c='purple')
plt.axvline(x=-1, color='green', linestyle='--')
_ = plt.axhline(y=4, color='green', linestyle='--')

# %% [markdown]
# In PyTorch and TensorFlow:

# In [163]
torch.inverse(torch.tensor([[4, 2], [-5, -3.]])) # float type

# In [164]
tf.linalg.inv(tf.Variable([[4, 2], [-5, -3.]])) # also float

# %% [markdown]
# **Exercises**:
# 
# 1. As done with NumPy above, use PyTorch to calculate $w$ from $X$ and $y$. Subsequently, confirm that $y = Xw$.
# 2. Repeat again, now using TensorFlow.

# %% [markdown]
# **Return to slides here.**

# %% [markdown]
# ### Matrix Inversion Where No Solution

# In [165]
X = np.array([[-4, 1], [-8, 2]])
X

# In [166]
# Uncommenting the following line results in a "singular matrix" error
# Xinv = np.linalg.inv(X)

# %% [markdown]
# Feel free to try inverting a non-square matrix; this will throw an error too.
# 
# **Return to slides here.**

# %% [markdown]
# ### Orthogonal Matrices
# 
# These are the solutions to Exercises 3 and 4 on **orthogonal matrices** from the slides.
# 
# For Exercise 3, to demonstrate the matrix $I_3$ has mutually orthogonal columns, we show that the dot product of any pair of columns is zero:

# In [167]
I = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
I

# In [168]
column_1 = I[:,0]
column_1

# In [169]
column_2 = I[:,1]
column_2

# In [170]
column_3 = I[:,2]
column_3

# In [171]
np.dot(column_1, column_2)

# In [172]
np.dot(column_1, column_3)

# In [173]
np.dot(column_2, column_3)

# %% [markdown]
# We can use the `np.linalg.norm()` method from earlier in the notebook to demonstrate that each column of $I_3$ has unit norm:

# In [174]
np.linalg.norm(column_1)

# In [175]
np.linalg.norm(column_2)

# In [176]
np.linalg.norm(column_3)

# %% [markdown]
# Since the matrix $I_3$ has mutually orthogonal columns and each column has unit norm, the column vectors of $I_3$ are *orthonormal*. Since $I_3^T = I_3$, this means that the *rows* of $I_3$ must also be orthonormal.
# 
# Since the columns and rows of $I_3$ are orthonormal, $I_3$ is an *orthogonal matrix*.

# %% [markdown]
# For Exercise 4, let's repeat the steps of Exercise 3 with matrix *K* instead of $I_3$. We could use NumPy again, but for fun I'll use PyTorch instead. (You're welcome to try it with TensorFlow if you feel so inclined.)

# In [177]
K = torch.tensor([[2/3, 1/3, 2/3], [-2/3, 2/3, 1/3], [1/3, 2/3, -2/3]])
K

# In [178]
Kcol_1 = K[:,0]
Kcol_1

# In [179]
Kcol_2 = K[:,1]
Kcol_2

# In [180]
Kcol_3 = K[:,2]
Kcol_3

# In [181]
torch.dot(Kcol_1, Kcol_2)

# In [182]
torch.dot(Kcol_1, Kcol_3)

# In [183]
torch.dot(Kcol_2, Kcol_3)

# %% [markdown]
# We've now determined that the columns of $K$ are orthogonal.

# In [184]
torch.norm(Kcol_1)

# In [185]
torch.norm(Kcol_2)

# In [186]
torch.norm(Kcol_3)

# %% [markdown]
# We've now determined that, in addition to being orthogonal, the columns of $K$ have unit norm, therefore they are orthonormal.
# 
# To ensure that $K$ is an orthogonal matrix, we would need to show that not only does it have orthonormal columns but it has orthonormal rows are as well. Since $K^T \neq K$, we can't prove this quite as straightforwardly as we did with $I_3$.
# 
# One approach would be to repeat the steps we used to determine that $K$ has orthogonal columns with all of the matrix's rows (please feel free to do so). Alternatively, we can use an orthogonal matrix-specific equation from the slides, $A^TA = I$, to demonstrate that $K$ is orthogonal in a single line of code:

# In [187]
torch.matmul(K.T, K)

# %% [markdown]
# Notwithstanding rounding errors that we can safely ignore, this confirms that $K^TK = I$ and therefore $K$ is an orthogonal matrix.

