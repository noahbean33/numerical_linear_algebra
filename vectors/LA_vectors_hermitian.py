# -*- coding: utf-8 -*-
# Auto-generated from 'LA_vectors_hermitian.ipynb' on 2025-08-08T15:22:58
# Source: code cells extracted; markdown preserved as comments.

# %% [markdown]
# #     COURSE: Linear algebra: theory and implementation
# ##    SECTION: Vectors
# ###      VIDEO: Hermitian transpose (a.k.a. conjugate transpose)
# 
# #### Instructor: sincxpress.com
# ##### Course url: https://www.udemy.com/course/linear-algebra-theory-and-implementation/?couponCode=202110

# In [ ]
import numpy as np

# In [ ]
# create a complex number
z = complex(3,4)

# magnitude
print( np.linalg.norm(z) )

# by transpose?
print( np.transpose(z)*z )

# by Hermitian transpose
print( np.transpose(z.conjugate())*z )


# complex vector
v = np.array( [ 3, 4j, 5+2j, complex(2,-5) ] )
print( v.T )
print( np.transpose(v) )
print( np.transpose(v.conjugate()) )

