# -*- coding: utf-8 -*-
# Auto-generated from 'LA_introMatrices_broadcasting.ipynb' on 2025-08-08T15:22:58
# Source: code cells extracted; markdown preserved as comments.

# %% [markdown]
# #     COURSE: Linear algebra: theory and implementation
# ##    SECTION: Introduction to matrices
# ###      VIDEO: Broadcasting matrix arithmetic
# 
# #### Instructor: sincxpress.com
# ##### Course url: https://www.udemy.com/course/linear-algebra-theory-and-implementation/?couponCode=202110

# In [ ]
import numpy as np

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

