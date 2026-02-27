# -*- coding: utf-8 -*-
# Auto-generated from 'LA_vectors_outerProduct.ipynb' on 2025-08-08T15:22:58
# Source: code cells extracted; markdown preserved as comments.

# %% [markdown]
# #     COURSE: Linear algebra: theory and implementation
# ##    SECTION: Vectors
# ###      VIDEO: Vector outer product
# 
# #### Instructor: sincxpress.com
# ##### Course url: https://www.udemy.com/course/linear-algebra-theory-and-implementation/?couponCode=202110

# In [ ]
import numpy as np

# In [ ]
# two vectors
v1 = np.array([  1, 2, 3 ])
v2 = np.array([ -1, 0, 1 ])

# outer product
np.outer(v1,v2)

# terrible programming, but helps conceptually:
op = np.zeros((len(v1),len(v2)))
for i in range(0,len(v1)):
    for j in range(0,len(v2)):
        op[i,j] = v1[i] * v2[j]

print(op)

