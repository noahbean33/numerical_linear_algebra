# -*- coding: utf-8 -*-
# Auto-generated from 'LA_introMatrices_diagonalTrace.ipynb' on 2025-08-08T15:22:58
# Source: code cells extracted; markdown preserved as comments.

# %% [markdown]
# #     COURSE: Linear algebra: theory and implementation
# ##    SECTION: Introduction to matrices
# ###      VIDEO: Diagonal and trace
# 
# #### Instructor: sincxpress.com
# ##### Course url: https://www.udemy.com/course/linear-algebra-theory-and-implementation/?couponCode=202110

# In [ ]
import numpy as np

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

# In [ ]
# trace as sum of diagonal elements
tr = np.trace(M)
tr2 = sum( np.diag(M) )
print(tr,tr2)

