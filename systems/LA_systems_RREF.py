# -*- coding: utf-8 -*-
# Auto-generated from 'LA_systems_RREF.ipynb' on 2025-08-08T15:22:58
# Source: code cells extracted; markdown preserved as comments.

# %% [markdown]
# #     COURSE: Linear algebra: theory and implementation
# ##    SECTION: Solving systems of equations
# ###      VIDEO: Reduced row echelon form
# 
# #### Instructor: sincxpress.com
# ##### Course url: https://www.udemy.com/course/linear-algebra-theory-and-implementation/?couponCode=202110

# In [ ]
import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D
from IPython import display
import time
from sympy import *

# In [ ]
# make some random matrices (using sympy package)
A = Matrix( np.random.randn(4,4) )
B = Matrix( np.random.randn(4,3) )

# compute RREF
rrefA = A.rref()
rrefB = B.rref()

# print out the matrix and its rref
print(np.array(rrefA[0]))
print(' ')
print(np.array(rrefB[0]))

