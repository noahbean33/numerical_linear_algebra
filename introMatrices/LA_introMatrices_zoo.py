# -*- coding: utf-8 -*-
# Auto-generated from 'LA_introMatrices_zoo.ipynb' on 2025-08-08T15:22:58
# Source: code cells extracted; markdown preserved as comments.

# %% [markdown]
# #     COURSE: Linear algebra: theory and implementation
# ##    SECTION: Introduction to matrices
# ###      VIDEO: A zoo of matrices
# 
# #### Instructor: sincxpress.com
# ##### Course url: https://www.udemy.com/course/linear-algebra-theory-and-implementation/?couponCode=202110

# In [ ]
import numpy as np

# In [ ]
# square vs. rectangular
S = np.random.randn(5,5)
R = np.random.randn(5,2) # 5 rows, 2 columns
print(S), print(' ')
print(R)

# In [ ]
# identity
I = np.eye(3)
print(I), print(' ')

# In [ ]
# zeros
Z = np.zeros((4,4))
print(Z), print(' ')

# In [ ]
# diagonal
D = np.diag([ 1, 2, 3, 5, 2 ])
print(D), print(' ')

# In [ ]
# create triangular matrix from full matrices
S = np.random.randn(5,5)
U = np.triu(S)
L = np.tril(S)
print(L), print(' ')

# In [ ]
# concatenate matrices (sizes must match!)
A = np.random.randn(3,2)
B = np.random.randn(4,4)
C = np.concatenate((A,B),axis=1)
print(C)

