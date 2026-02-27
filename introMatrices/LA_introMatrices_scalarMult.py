# -*- coding: utf-8 -*-
# Auto-generated from 'LA_introMatrices_scalarMult.ipynb' on 2025-08-08T15:22:58
# Source: code cells extracted; markdown preserved as comments.

# %% [markdown]
# #     COURSE: Linear algebra: theory and implementation
# ##    SECTION: Introduction to matrices
# ###      VIDEO: Matrix-scalar multiplication
# 
# #### Instructor: sincxpress.com
# ##### Course url: https://www.udemy.com/course/linear-algebra-theory-and-implementation/?couponCode=202110

# In [ ]
import numpy as np

# In [ ]
# define matrix and scalar
M = np.array([ [1, 2], [2, 5] ])
s = 2

# pre- and post-multiplication is the same:
print( M*s )
print( s*M )

