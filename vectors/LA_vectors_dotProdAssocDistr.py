# -*- coding: utf-8 -*-
# Auto-generated from 'LA_vectors_dotProdAssocDistr.ipynb' on 2025-08-08T15:22:58
# Source: code cells extracted; markdown preserved as comments.

# %% [markdown]
# #     COURSE: Linear algebra: theory and implementation
# ##    SECTION: Vectors
# ###      VIDEO: Dot product properties: associative and distributive
# 
# #### Instructor: sincxpress.com
# ##### Course url: https://www.udemy.com/course/linear-algebra-theory-and-implementation/?couponCode=202110

# In [ ]
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# In [ ]
## Distributive property

# create random vectors
n = 10
a = np.random.randn(n)
b = np.random.randn(n)
c = np.random.randn(n)

# the two results
res1 = np.dot( a , (b+c) )
res2 = np.dot(a,b) + np.dot(a,c)

# compare them
print([ res1,res2 ])

# In [ ]
## Associative property

# create random vectors
n = 5
a = np.random.randn(n)
b = np.random.randn(n)
c = np.random.randn(n)

# the two results
res1 = np.dot( a , np.dot(b,c) )
res2 = np.dot( np.dot(a,b) , c )

# compare them
print(res1)
print(res2)


### special cases where associative property works!
# 1) one vector is the zeros vector
# 2) a==b==c

