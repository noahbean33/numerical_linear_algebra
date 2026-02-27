# -*- coding: utf-8 -*-
# Auto-generated from 'LA_rank_AtA_AAt.ipynb' on 2025-08-08T15:22:58
# Source: code cells extracted; markdown preserved as comments.

# %% [markdown]
# #     COURSE: Linear algebra: theory and implementation
# ##    SECTION: Matrix rank
# ###      VIDEO: Rank of A^TA and AA^T
# 
# #### Instructor: sincxpress.com
# ##### Course url: https://www.udemy.com/course/linear-algebra-theory-and-implementation/?couponCode=202110

# In [ ]
import numpy as np
import matplotlib.pyplot as plt
import math

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

