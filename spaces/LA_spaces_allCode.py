# -*- coding: utf-8 -*-
# Auto-generated from 'LA_spaces_allCode.ipynb' on 2025-08-08T15:22:58
# Source: code cells extracted; markdown preserved as comments.

# %% [markdown]
# #     COURSE: Linear algebra: theory and implementation
# ##    SECTION: Matrix spaces
# 
# #### Instructor: sincxpress.com
# ##### Course url: https://www.udemy.com/course/linear-algebra-theory-and-implementation/?couponCode=202110

# In [1]
import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D

# In [14]
# matrix S
S = np.array( [ [3,0],
                [5,2],
                [1,2] ] )

# vector v
v = np.array([-3, 1, 5])
# v = np.array([1, 7, 3])


fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# draw plane corresponding to the column space
xx, yy = np.meshgrid(np.linspace(-5,5,10),np.linspace(-5,5,10))
cp = np.cross(S[:,0],S[:,1])
z1 = (-cp[0]*xx - cp[1]*yy)/cp[2]
ax.plot_surface(xx,yy,z1,alpha=.2)


## plot the two vectors from matrix S
ax.plot([0, S[0,0]],[0, S[1,0]],[0, S[2,0]],'k')
ax.plot([0, S[0,1]],[0, S[1,1]],[0, S[2,1]],'k')

# and the vector v
ax.plot([0, v[0]],[0, v[1]],[0, v[2]],'r')


ax.view_init(elev=150,azim=0)
plt.show()

