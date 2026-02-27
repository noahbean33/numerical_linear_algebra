# -*- coding: utf-8 -*-
# Auto-generated from 'LA_introMatrices_allCode.ipynb' on 2025-08-08T15:22:58
# Source: code cells extracted; markdown preserved as comments.

# %% [markdown]
# #     COURSE: Linear algebra: theory and implementation
# ##    SECTION: Introduction to matrices
# 
# #### Instructor: sincxpress.com
# ##### Course url: https://www.udemy.com/course/linear-algebra-theory-and-implementation/?couponCode=202110

# In [ ]
import numpy as np

# %% [markdown]
# 
# ---
# # VIDEO: A zoo of matrices
# ---

# In [ ]

# square vs. rectangular
S = np.random.randn(5,5)
R = np.random.randn(5,2) # 5 rows, 2 columns
print(S), print(' ')
print(R)

# identity
I = np.eye(3)
print(I), print(' ')

# zeros
Z = np.zeros((4,4))
print(Z), print(' ')

# diagonal
D = np.diag([ 1, 2, 3, 5, 2 ])
print(D), print(' ')

# create triangular matrix from full matrices
S = np.random.randn(5,5)
U = np.triu(S)
L = np.tril(S)
print(L), print(' ')

# concatenate matrices (sizes must match!)
A = np.random.randn(3,2)
B = np.random.randn(4,4)
C = np.concatenate((A,B),axis=1)
print(C)

# %% [markdown]
# 
# ---
# # VIDEO: Matrix addition and subtraction
# ---

# In [ ]

# create random matrices
A = np.random.randn(5,4)
B = np.random.randn(5,3)
C = np.random.randn(5,4)

# try to add them
A+B
A+C



# "shifting" a matrix
l = .03 # lambda
N = 5  # size of square matrix
D = np.random.randn(N,N) # can only shift a square matrix

Ds = D + l*np.eye(N)
print(D), print(' '), print(Ds)

# %% [markdown]
# 
# ---
# # VIDEO: Matrix-scalar multiplication
# ---

# In [ ]
# define matrix and scalar
M = np.array([ [1, 2], [2, 5] ])
s = 2

# pre- and post-multiplication is the same:
print( M*s )
print( s*M )

# %% [markdown]
# # VIDEO: Transpose

# In [ ]
M = np.array([ [1,2,3],
               [2,3,4] ])

print(M), print('')
print(M.T), print('') # one transpose
print(M.T.T), print('') # double-transpose returns the original matrix

# can also use the function transpose
print(np.transpose(M))

# In [ ]
# warning! be careful when using complex matrices
C = np.array([ [4+1j , 3 , 2-4j] ])

print(C), print('')
print(C.T), print('')
print(np.transpose(C)), print('')

# Note: In MATLAB, the transpose is the Hermitian transpose; 
#       in Python, you need to call the Hermitian explicitly by first converting from an array into a matrix
print(C.conjugate().T) # note the sign flips!
# Another note: the code I used in the video will soon be depreciated; use the above line instead.

# %% [markdown]
# 
# ---
# # VIDEO: Diagonal and trace
# ---

# In [ ]

M = np.round( 6*np.random.randn(4,4) )
print(M), print(' ')
# extract the diagonals
d = np.diag(M)

# notice the two ways of using the diag function
d = np.diag(M) # input is matrix, output is vector
D = np.diag(d) # input is vector, output is matrix
print(d)
print(D)

# trace as sum of diagonal elements
tr = np.trace(M)
tr2 = sum( np.diag(M) )
print(tr,tr2)

# %% [markdown]
# 
# ---
# # VIDEO: Broadcasting matrix arithmetic
# ---

# In [ ]
# create a matrix
A = np.reshape(np.arange(1,13),(3,4),'F') # F=column, C=row

# and two vectors
r = [ 10, 20, 30, 40 ]
c = [ 100, 200, 300 ]

print(A), print(' ')
print(r), print(' ')
print(c), print(' ');

# In [ ]
# broadcast on the rows
# print(A+r), print(' ')

# broadcast on the columns
print(A+c)
# print(A+np.reshape(c,(len(c),1))) # only works for explicit column vectors

