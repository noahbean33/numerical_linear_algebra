# -*- coding: utf-8 -*-
# Auto-generated from 'LA_vectors_hadamard.ipynb' on 2025-08-08T15:22:58
# Source: code cells extracted; markdown preserved as comments.

# %% [markdown]
# #     COURSE: Linear algebra: theory and implementation
# ##    SECTION: Vectors
# ###      VIDEO: Vector Hadamard multiplication¶
# 
# #### Instructor: sincxpress.com
# ##### Course url: https://www.udemy.com/course/linear-algebra-theory-and-implementation/?couponCode=202110

# In [ ]
import numpy as np

# In [ ]
# create vectors
w1 = [ 1, 3, 5 ]
w2 = [ 3, 4, 2 ]

w3 = np.multiply(w1,w2)

print(w3)

# In [ ]
# can use * if numpy arrays:
w3 = np.array(w1)*np.array(w2)

