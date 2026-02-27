# -*- coding: utf-8 -*-
# Auto-generated from 'LA_quadform_generalized.ipynb' on 2025-08-08T15:22:58
# Source: code cells extracted; markdown preserved as comments.

# %% [markdown]
# #     COURSE: Linear algebra: theory and implementation
# ##    SECTION: Quadratic form and definiteness
# ###     VIDEO: Quadratic form of generalized eigendecomposition
# 
# #### Instructor: sincxpress.com
# ##### Course url: https://www.udemy.com/course/linear-algebra-theory-and-implementation/?couponCode=202110

# In [ ]
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from scipy import linalg

# In [ ]
# create two symmetric matrices
m = 14
n = 1000

# create A as random sine-modulated noise, then its covariance matrix
A = np.zeros((m,n))
for i in range(n):
    A[:,i] = np.random.randn(m) * np.cos(np.linspace(0,np.pi,m))

A = A@A.T


# B is the same thing, just different random numbers
B = np.zeros((m,n))
for i in range(n):
    B[:,i] = np.random.randn(m) * np.cos(np.linspace(0,np.pi,m))

B = B@B.T


# generalized eigendecomposition
evals,evecs = linalg.eigh(A,B)

# In [ ]
## some plotting

fig = plt.subplots(1,figsize=(10,6))

# W'W
plt.subplot(231)
plt.imshow(evecs.T@evecs,extent=[-m,m,-m,m])
plt.xticks([])
plt.title('W$^T$W')

# one row of W'W
tmp = evecs.T@evecs
plt.subplot(234)
plt.plot(tmp[1,:],'s-')
plt.title('W$_j^T$W')

# W'AW
plt.subplot(232)
plt.imshow(evecs.T@A@evecs,extent=[-m,m,-m,m])
plt.xticks([])
plt.title('W$^T$AW')

# one row of W'AW
plt.subplot(235)
plt.plot(np.diag(evecs.T@A@evecs),'s-')
plt.plot(evals,'r.')
plt.title('diag(W$^T$AW)')

# W'BW
plt.subplot(233)
plt.imshow(evecs.T@B@evecs,extent=[-m,m,-m,m])
plt.xticks([])
plt.title('W$^T$BW')

# diagonal of W'BW
plt.subplot(236)
plt.plot(np.diag(evecs.T@B@evecs),'s-')
plt.title('diag(W$^T$BW)')

plt.show()

# In [ ]

