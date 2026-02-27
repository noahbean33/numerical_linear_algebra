# -*- coding: utf-8 -*-
# Auto-generated from 'LA_systems_algebraGeom.ipynb' on 2025-08-08T15:22:58
# Source: code cells extracted; markdown preserved as comments.

# %% [markdown]
# #     COURSE: Linear algebra: theory and implementation
# ##    SECTION: Solving systems of equations
# ###      VIDEO: Systems of equations: algebra and geometry
# 
# #### Instructor: sincxpress.com
# ##### Course url: https://www.udemy.com/course/linear-algebra-theory-and-implementation/?couponCode=202110

# In [ ]
import numpy as np
import matplotlib.pyplot as plt
import math
from IPython import display
import time
from sympy import *

# In [ ]

# 3 these are the coefficients of the equation:
# ay = bx + c;
eq1o = [1., 2, 1] # [a b c]
eq2o = [2., 1, 3]


for i in range(10):
    
    # clear plot
    plt.cla()
    
    # randomly update equations
    eq1 = np.add(eq2o,np.random.randn(1)*eq1o)
    eq2 = np.add(eq1o,np.random.randn(1)*eq2o)
    
    # plot new lines (solutions)
    y = ([eq1[1]*-3, eq1[1]*3] + eq1[2])/eq1[0]
    plt.plot([-3,3],y)
    
    y = ([eq2[1]*-3, eq2[1]*3] + eq2[2])/eq2[0]
    plt.plot([-3,3],y)
    plt.axis([-3,3,-3,6])
    
    # pause to allow inspection
    display.clear_output(wait=True)
    display.display(plt.gcf())
    time.sleep(.1)
    
# In [ ]
# these are the coefficients of the equation:
# az = bx + cy + d
eq1o = [1, 2, 3, -1] # [a b c d]
eq2o = [2, 1, 3,  3]

# set up for 3D plot
fig = plt.figure()
ax = fig.add_subplot(projection='3d')


for i in range(0,10):
    
#     plt.cla()
    
    # randomly update equations
    eq1 = np.add(eq2o,np.random.randn(1)*eq1o)
    eq2 = np.add(eq1o,np.random.randn(1)*eq2o)
    
    # plot new lines (solutions)
    y = ([eq1[1]*-3, eq1[1]*3] + eq1[3])/eq1[0]
    z = ([eq1[2]*-3, eq1[2]*3] + eq1[3])/eq1[0]
    ax.plot([-3,3],y,z)
    
    # plot new lines (solutions)
    y = ([eq2[1]*-3, eq2[1]*3] + eq2[3])/eq2[0]
    z = ([eq2[2]*-3, eq2[2]*3] + eq2[3])/eq2[0]
    ax.plot([-3,3],y,z)
    
    # axis limits
    ax.set_xlim3d(-3,6)
    ax.set_ylim3d(-3,6)
    ax.set_zlim3d(-1,10)
    
    # pause to allow inspection
    display.clear_output(wait=True)
    display.display(plt.gcf())
    time.sleep(.1)
    
    
