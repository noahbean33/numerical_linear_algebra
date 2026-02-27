# -*- coding: utf-8 -*-
# Auto-generated from 'LA_vectors_unitVectors.ipynb' on 2025-08-08T15:22:58
# Source: code cells extracted; markdown preserved as comments.

# %% [markdown]
# #     COURSE: Linear algebra: theory and implementation
# ##    SECTION: Vectors
# ###      VIDEO: Unit vector
# 
# #### Instructor: sincxpress.com
# ##### Course url: https://www.udemy.com/course/linear-algebra-theory-and-implementation/?couponCode=202110

# In [ ]
import numpy as np
import matplotlib.pyplot as plt

# In [ ]
# vector
v1 = np.array([ -3, 6 ])

# mu
mu = 1/np.linalg.norm(v1)

v1n = v1*mu

# plot them
plt.plot([0, v1n[0]],[0, v1n[1]],'r',label='v1-norm',linewidth=5)
plt.plot([0, v1[0]],[0, v1[1]],'b',label='v1')

# axis square
plt.axis('square')
plt.axis(( -6, 6, -6, 6 ))
plt.grid()
plt.legend()
plt.show()

