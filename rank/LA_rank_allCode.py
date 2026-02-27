# -*- coding: utf-8 -*-
# Auto-generated from 'LA_rank_allCode.ipynb' on 2025-08-08T15:22:58
# Source: code cells extracted; markdown preserved as comments.

# %% [markdown]
# #     COURSE: Linear algebra: theory and implementation
# ##    SECTION: Matrix rank
# 
# #### Instructor: sincxpress.com
# ##### Course url: https://www.udemy.com/course/linear-algebra-theory-and-implementation/?couponCode=202110

# In [ ]
import numpy as np
import matplotlib.pyplot as plt
import math

# %% [markdown]
# 
# ---
# # VIDEO: Computing rank: theory and practice
# ---

# In [ ]
# make a matrix
m = 4
n = 6

# create a random matrix
A = np.random.randn(m,n)

# what is the largest possible rank?
ra = np.linalg.matrix_rank(A)
print('rank = ' + str(ra))

# set last column to be repeat of penultimate column
B = A
B[:,-1] = B[:,-2]

rb = np.linalg.matrix_rank(B)
# print('rank = ' + str(rb))

# In [ ]
## adding noise to a rank-deficient matrix

# square for convenience
A = np.round( 10*np.random.randn(m,m) )

# reduce the rank
A[:,-1] = A[:,-2]

# noise level
noiseamp = .001

# add the noise
B = A + noiseamp*np.random.randn(m,m)

print('rank (w/o noise) = ' + str(np.linalg.matrix_rank(A)))
print('rank (with noise) = ' + str(np.linalg.matrix_rank(B)))

# %% [markdown]
# 
# ---
# # VIDEO: Rank of A^TA and AA^T
# ---

# In [ ]
# matrix sizes
m = 14
n =  3

# create matrices
A = np.round( 10*np.random.randn(m,n) )

AtA = A.T@A
AAt = A@A.T

# get matrix sizes
sizeAtA = AtA.shape
sizeAAt = AAt.shape

# print info!
print('AtA: %dx%d, rank=%d' %(sizeAtA[0],sizeAtA[1],np.linalg.matrix_rank(AtA)))
print('AAt: %dx%d, rank=%d' %(sizeAAt[0],sizeAAt[1],np.linalg.matrix_rank(AAt)))

# %% [markdown]
# 
# ---
# # VIDEO: Making a matrix full-rank by "shifting"
# ---

# In [ ]
# size of matrix
m = 30

# create the square symmetric matrix
A = np.random.randn(m,m)
A = np.round( 10*A.T@A )

# reduce the rank
A[:,0] = A[:,1]

# shift amount (l=lambda)
l = .01

# new matrix
B = A + l*np.eye(m,m)

# print information
print('rank(w/o shift) = %d' %np.linalg.matrix_rank(A))
print('rank(with shift) = %d' %np.linalg.matrix_rank(B))

