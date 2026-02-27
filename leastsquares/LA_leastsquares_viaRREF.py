# -*- coding: utf-8 -*-
# Auto-generated from 'LA_leastsquares_viaRREF.ipynb' on 2025-08-08T15:22:58
# Source: code cells extracted; markdown preserved as comments.

# %% [markdown]
# #     COURSE: Linear algebra: theory and implementation
# ##    SECTION: Least-squares
# ###      VIDEO: Least-squares via row-reduction
# 
# #### Instructor: sincxpress.com
# ##### Course url: https://www.udemy.com/course/linear-algebra-theory-and-implementation/?couponCode=202110

# In [ ]
import numpy as np
import matplotlib.pyplot as plt
from sympy import *

# In [ ]
m = 10
n = 3

# create data
X = np.random.randn(m,n) # "design matrix"
y = np.random.randn(m,1) # "outcome measures (data)"

np.shape(y)

# In [ ]
# try directly applying RREF
Xy = Matrix( np.concatenate([X,y],axis=1) )
print( Xy.rref() )

# In [ ]
# now reapply to the normal equations
XtX = X.T@X
Xty = X.T@y
normEQ = Matrix( np.concatenate( [XtX,Xty],axis=1 ) )

Xsol = normEQ.rref()
Xsol = Xsol[0]
beta = Xsol[:,-1]

print(np.array(Xsol)), print(' ')
print(beta), print(' ')

# compare to left-inverse
beta2 = np.linalg.inv(XtX) @ Xty
print(beta2), print(' ')

# and with the python solver
beta3 = np.linalg.solve(XtX,Xty)
print(beta3)

# In [ ]

