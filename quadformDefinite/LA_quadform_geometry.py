# -*- coding: utf-8 -*-
# Auto-generated from 'LA_quadform_geometry.ipynb' on 2025-08-08T15:22:58
# Source: code cells extracted; markdown preserved as comments.

# %% [markdown]
# #     COURSE: Linear algebra: theory and implementation
# ##    SECTION: Quadratic form and definiteness
# ###     VIDEO: The quadratic form in geometry
# 
# #### Instructor: sincxpress.com
# ##### Course url: https://www.udemy.com/course/linear-algebra-theory-and-implementation/?couponCode=202110

# In [ ]
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# In [ ]
# some different matrices
S = np.zeros((4,), dtype=np.object)

S[0] = [ [ 4, 4], [4, 9] ]
S[1] = [ [-4,-1], [3,-5] ]
S[2] = [ [ 0, 1], [2, 0] ]
S[3] = [ [ 1, 1], [1, 1] ]

# range for vector w
n = 30
wRange = np.linspace(-2,2,n)

# initialize quadratic form matrix
qf = np.zeros( (n,n) )


for i in range(4):
    
    # compute QF
    for xi in range(n):
        for yi in range(n):
            # this w
            w = np.transpose([ wRange[xi], wRange[yi] ])
            
            # QF
            qf[xi,yi] = w.T@S[i]@w
    
    # show the map
    plt.subplot(2,2,i+1)
    plt.imshow(qf,extent=[wRange[0],wRange[-1],wRange[0],wRange[-1]])

plt.show()

# In [ ]
# 3D plotting code

mycmap = plt.get_cmap('gist_earth')
X,Y = np.meshgrid(wRange,wRange)

for i in range(4):
    
    for xi in range(n):
        for yi in range(n):
            w = np.array([ wRange[xi], wRange[yi] ])
            qf[xi,yi] = w.T@S[i]@w
    
    # show the map 
    fig = plt.figure(figsize=(10,6))
    ax1 = fig.add_subplot(221+i, projection='3d')
    surf1 = ax1.plot_surface(X, Y, qf.T, cmap=mycmap)
    ax1.view_init(azim=-30, elev=30)

plt.show()

# In [ ]
# compute and visualize the normalized quadratic form

A = np.array([[-2,3],[2,8]])

n = 30
xi = np.linspace(-2,2,n)

# for the visualization
X,Y = np.meshgrid(xi,xi)

# initialize
qf  = np.zeros((n,n))
qfN = np.zeros((n,n))

for i in range(n):
    for j in range(n):
        
        # create x (coordinate) vector
        x = np.transpose([ xi[i],xi[j] ])

        # compute the quadratic forms
        qf[i,j]  = x.T@A@x
        qfN[i,j] = qf[i,j] / (x.T@x)


fig = plt.figure(figsize=(5,5))
ax1 = fig.add_subplot(projection='3d')
surf1 = ax1.plot_surface(X, Y, qf.T, cmap=mycmap)
ax1.view_init(azim=-30, elev=30)
ax1.set_title('Non-normalized quadratic form')

fig = plt.figure(figsize=(5,5))
ax1 = fig.add_subplot(111, projection='3d')
surf1 = ax1.plot_surface(X, Y, qfN.T, cmap=mycmap, antialiased=False)
ax1.view_init(azim=-30, elev=30)
ax1.set_title('Normalized quadratic form')

plt.show()

