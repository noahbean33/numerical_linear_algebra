# -*- coding: utf-8 -*-
# Auto-generated from 'LA_intro_picSVD.ipynb' on 2025-08-08T15:22:58
# Source: code cells extracted; markdown preserved as comments.

# %% [markdown]
# #     COURSE: Linear algebra: theory and implementation
# ##    SECTION: Introduction
# ###      VIDEO: An enticing start to a linear algebra course!
# 
# #### Instructor: sincxpress.com
# ##### Course url: https://www.udemy.com/course/linear-algebra-theory-and-implementation/?couponCode=202110

# In [ ]
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# In [ ]
# import picture
pic = Image.open('Einstein_tongue.jpg')

# let's have a look
plt.imshow(pic)
plt.show()

# we need to convert it to floating-point precision
pic = np.array(pic)
plt.imshow(pic,cmap='gray')
plt.show()

# In [ ]
# SVD (singular value decomposition)

# do the SVD. Note: You'll understand this decomposition by the end of the
# course! Don't worry if it seems mysterious now!
U,S,V = np.linalg.svd( pic )

# plot the spectrum
plt.plot(S,'s-')
plt.xlim([0,100])
plt.xlabel('Component number')
plt.ylabel('Singular value (\sigma)')
plt.show()

# In [ ]
# reconstruct the image based on some components

# list the components you want to use for the reconstruction
comps = np.arange(0,5)

# reconstruct the low-rank version of the picture
reconPic = U[:,comps]@np.diag(S[comps])@V[comps,:]


# show the original and reconstructed pictures for comparison
plt.figure(figsize=(5,10))
plt.subplot(1,2,1)
plt.imshow(pic,cmap='gray')
plt.title('Original')
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(reconPic,cmap='gray')
plt.title('Components %s-%s' %(comps[0],comps[-1]))
plt.axis('off')

plt.show()

# Aren't you SUPER-curious to know what all of this means and why it
#  works!!??! You're going to learn all about this in the course!

# In [ ]

