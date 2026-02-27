# -*- coding: utf-8 -*-
# Auto-generated from 'LA_quadform_definiteness.ipynb' on 2025-08-08T15:22:58
# Source: code cells extracted; markdown preserved as comments.

# %% [markdown]
# #     COURSE: Linear algebra: theory and implementation
# ##    SECTION: Quadratic form and definiteness
# ###     VIDEO: Matrix definiteness, geometry, and eigenvalues
# 
# #### Instructor: sincxpress.com
# ##### Course url: https://www.udemy.com/course/linear-algebra-theory-and-implementation/?couponCode=202110

# In [ ]
import numpy as np
import matplotlib.pyplot as plt

# In [ ]
# some different matrices
S = np.zeros((5,), dtype=np.object)
S[0] = [ [ 4, 4], [ 4, 9] ]
S[1] = [ [-4,-1], [-3,-5] ]
S[2] = [ [ 0, 1], [ 2, 0] ]
S[3] = [ [ 1, 1], [ 1, 1] ]
S[4] = [ [-1,-2], [-3,-6] ]



# range for vector w
n = 30
wr = 2
wRange = np.linspace(-wr,wr,n)

# initialize quadratic form matrix
qf = np.zeros( (n,n) )


fig = plt.subplots(1,figsize=(8,8))

for i in range(5):
    
    # compute QF
    for xi in range(n):
        for yi in range(n):
            # this w
            w = np.transpose([ wRange[xi], wRange[yi] ])
            
            # QF
            qf[xi,yi] = w.T@S[i]@w
    
    # show the map
    plt.subplot(2,3,i+1)
    plt.imshow(qf.T,extent=[-wr,wr,-wr,wr])
    
    ## compute the matrix's definiteness based on the eigenvalues
    
    # get eigenvalues
    evals = np.linalg.eig(S[i])[0]
    
    # we care about their signs
    esign = np.sign(evals)
    
    # test for signs (note: this test is valid only for 2x2 matrices!)
    if sum(esign)==2:
        defcat = 'Pos. def.'
    elif sum(esign)==1:
        defcat = 'Pos. semidef.'
    elif sum(esign)==0:
        defcat = 'Indeterminant'
    elif sum(esign)==-1:
        defcat = 'Neg. semidef.'
    elif sum(esign)==-2:
        defcat = 'Neg. def.'
    
    # add title
    plt.title(defcat)

plt.show()

