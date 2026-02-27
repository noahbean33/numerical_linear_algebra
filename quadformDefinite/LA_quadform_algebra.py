# -*- coding: utf-8 -*-
# Auto-generated from 'LA_quadform_algebra.ipynb' on 2025-08-08T15:22:58
# Source: code cells extracted; markdown preserved as comments.

# %% [markdown]
# #     COURSE: Linear algebra: theory and implementation
# ##    SECTION: Quadratic form and definiteness
# ###     VIDEO: The quadratic form in algbebra
# 
# #### Instructor: sincxpress.com
# ##### Course url: https://www.udemy.com/course/linear-algebra-theory-and-implementation/?couponCode=202110

# In [ ]
import numpy as np
import matplotlib.pyplot as plt

# In [ ]
# matrix and vector
S = [ [ 1,  3, -2], 
      [ 0,  3,  4],
      [-5, -2,  4] ]

w = np.transpose([ [-2, 4, 3] ])

# compute the quadratic form
qf = w.T@S@w

print(qf)

# In [ ]
n = len(w) # used for plotting

# show the matrices
plt.subplot(131)
plt.imshow(S)
plt.axis('off')
plt.title('Matrix S')

plt.subplot(132)
plt.imshow(w)
plt.axis('off')
plt.title('Vector w')

plt.subplot(133)
plt.imshow(qf)
plt.title('Quadratic form: w$^T$Sw')
plt.axis('off')

plt.show()

# In [ ]

