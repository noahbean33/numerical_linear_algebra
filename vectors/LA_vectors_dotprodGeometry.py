# -*- coding: utf-8 -*-
# Auto-generated from 'LA_vectors_dotprodGeometry.ipynb' on 2025-08-08T15:22:58
# Source: code cells extracted; markdown preserved as comments.

# %% [markdown]
# #     COURSE: Linear algebra: theory and implementation
# ##    SECTION: Vectors
# ###      VIDEO: The dot product from a geometric perspective
# 
# #### Instructor: sincxpress.com
# ##### Course url: https://www.udemy.com/course/linear-algebra-theory-and-implementation/?couponCode=202110

# In [ ]
import numpy as np
import matplotlib.pyplot as plt

# In [ ]

# two vectors
v1 = np.array([ 2,  4, -3 ])
v2 = np.array([ 0, -3, -3 ])

# compute the angle (radians) between two vectors
ang = np.arccos( np.dot(v1,v2) / (np.linalg.norm(v1)*np.linalg.norm(v2)) )


# draw them
fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
ax = plt.axes(projection = '3d')
ax.plot([0, v1[0]],[0, v1[1]],[0, v1[2]],'b')
ax.plot([0, v2[0]],[0, v2[1]],[0, v2[2]],'r')

plt.axis((-6, 6, -6, 6, -6, 6))
plt.title('Angle between vectors: %s rad.' %ang)
plt.show()

# In [ ]
## equivalence of algebraic and geometric dot product formulas

# two vectors
v1 = np.array([ 2,  4, -3 ])
v2 = np.array([ 0, -3, -3 ])


# algebraic
dp_a = np.dot( v1,v2 )

# geometric
dp_g = np.linalg.norm(v1)*np.linalg.norm(v2)*np.cos(ang)

# print dot product to command
print(dp_a)
print(dp_g)

# In [ ]

