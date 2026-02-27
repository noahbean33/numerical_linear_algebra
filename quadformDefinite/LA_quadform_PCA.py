# -*- coding: utf-8 -*-
# Auto-generated from 'LA_quadform_PCA.ipynb' on 2025-08-08T15:22:58
# Source: code cells extracted; markdown preserved as comments.

# %% [markdown]
# #     COURSE: Linear algebra: theory and implementation
# ##    SECTION: Quadratic form and definiteness
# ###     VIDEO: Application of the normalized quadratic form: PCA
# 
# #### Instructor: sincxpress.com
# ##### Course url: https://www.udemy.com/course/linear-algebra-theory-and-implementation/?couponCode=202110

# In [ ]
import numpy as np
import matplotlib.pyplot as plt

# In [ ]
# simulation parameters
N = 1000 # time points
M =   20 # channels

# time vector (radian units)
t = np.linspace(0,6*np.pi,N)

# relationship across channels (imposing covariance)
chanrel = np.sin(np.linspace(0,2*np.pi,M))

# initialize data
data = np.zeros((M,N))

# create dataset
for i in range(M):
    data[i,:] = np.sin(t) * chanrel[i]

# add noise
data = data + np.random.randn(M,N)/3
    
# mean-center
for i in range(M):
    data[i,:] = data[i,:] - np.mean(data[i,:])


# compute covariance matrix
covmat = data@data.T/(N-1)


### show me the data!!
fig,ax = plt.subplots(1,2,figsize=(12,5))

# draw time series
for i in range(M):
    ax[0].plot(t,data[i,:]+i*2)
ax[0].set_yticks([])
ax[0].set_ylabel('Channels')
ax[0].set_xlabel('Time (a.u.)')

# show covariance matrix
ax[1].imshow(covmat)
ax[1].set_ylabel('Channels')
ax[1].set_xlabel('Channels')


plt.show()

# In [ ]
# eigendecomposition of the covariance matrix
evals,evecs = np.linalg.eig( covmat )

# sort eigenvalues and eigenvectors
idx   = np.argsort(evals)[::-1]   
evals = np.real( evals[idx] )
evecs = evecs[:,idx]

# convert eigenvalues to percent variance explained
evals = 100*evals/np.sum(evals)


# compute component time series
r = 2 # two components
comp_time_series = evecs[:,:r].T@data


# visualize and interpret the results

fig = plt.subplots(121,figsize=(10,4))
# eigenvalues
plt.subplot(121)
plt.plot(evals,'s-')
plt.xlabel('Component number')
plt.ylabel('$\lambda$ (% total variance)')
plt.title('Eigenspectrum')

# eigenvectors
plt.subplot(122)
plt.plot(evecs[:,0],label='PC1')
plt.plot(evecs[:,1],label='PC2')
plt.xlabel('Channel')
plt.ylabel('PC weight')
plt.title('Eigenvectors')
plt.legend()
plt.show()

# original channel modulator
plt.plot(chanrel)
plt.xlabel('Channel')
plt.ylabel('Channel weight')
plt.title('Ground truth channel weights')
plt.show()

# component time series
plt.plot(comp_time_series[0,:],label='PC1')
plt.plot(comp_time_series[1,:],label='PC2')
plt.xlabel('Time (a.u.)')
plt.ylabel('Activity')
plt.legend()
plt.title('Time course plots')
plt.show()

