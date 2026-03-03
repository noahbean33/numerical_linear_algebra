# -*- coding: utf-8 -*-
# Auto-generated from '01-vectors-and-vector-spaces.ipynb' on 2025-08-08T15:22:58
# Source: code cells extracted; markdown preserved as comments.

# %% [markdown]
# # Chapter 1. Vectors and vector spaces

# In [1]
from sklearn.datasets import load_iris

data = load_iris()

X, y = data["data"], data["target"]

# In [2]
X[:10]

# In [3]
X.shape

# In [4]
y

# In [5]
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

sns.set_theme(style="white", rc={"axes.facecolor": (0, 0, 0, 0)})

# Create the data
x = X.ravel()
labels = ["sepal length", "sepal width", "petal length", "petal width"]
g = np.tile(labels, len(X))
df = pd.DataFrame(dict(x=x, g=g))

# Initialize the FacetGrid object
pal = sns.cubehelix_palette(10, rot=-.25, light=.7)
g = sns.FacetGrid(df, row="g", hue="g", aspect=10, height=1.5, palette=pal)

# Draw the densities
g.map(sns.kdeplot, "x", bw_adjust=.5, clip_on=False, fill=True, alpha=1, linewidth=1.5)
g.map(sns.kdeplot, "x", clip_on=False, color="w", lw=2, bw_adjust=.5)

# Add reference line
g.refline(y=0, linewidth=2, linestyle="-", color=None, clip_on=False)

# Label each plot
g.map(lambda x, color, label: plt.gca().text(0, .2, label, fontweight="bold", color=color,
                                             ha="left", va="center", transform=plt.gca().transAxes), "x")

# Adjust subplots and aesthetics
g.figure.subplots_adjust(hspace=-.25)
g.set_titles("")
g.set(yticks=[], ylabel="")
g.despine(bottom=True, left=True)

plt.show()

# In [6]
X_scaled = (X - X.mean(axis=0))/X.std(axis=0)

# In [7]
X_scaled[:10]

# In [8]
# Create the data
x = X_scaled.ravel()
labels = ["sepal length", "sepal width", "petal length", "petal width"]
g = np.tile(labels, X_scaled.shape[0])
df = pd.DataFrame(dict(x=x, g=g))

# Initialize the FacetGrid object
pal = sns.cubehelix_palette(10, rot=-.25, light=.7)
grid = sns.FacetGrid(df, row="g", hue="g", aspect=10, height=1.5, palette=pal)

# Draw the densities
grid.map(sns.kdeplot, "x", bw_adjust=.5, clip_on=False, fill=True, alpha=1, linewidth=1.5)
grid.map(sns.kdeplot, "x", clip_on=False, color="w", lw=2, bw_adjust=.5)

# Add reference line
grid.refline(y=0, linewidth=2, linestyle="-", color=None, clip_on=False)

# Add labels to each plot
grid.map(lambda x, color, label: plt.gca().text(0, .2, label, fontweight="bold", color=color,
                                                ha="left", va="center", transform=plt.gca().transAxes), "x")

# Adjust subplots and aesthetics
grid.figure.subplots_adjust(hspace=-.25)
grid.set_titles("")
grid.set(yticks=[], ylabel="")
grid.despine(bottom=True, left=True)

plt.show()

# %% [markdown]
# ## Vectors in practice

# %% [markdown]
# ### Tuples

# In [9]
v_tuple = (1, 3.5, -2.71, "a string", 42)

# In [10]
v_tuple

# In [11]
type(v_tuple)

# In [12]
v_tuple[0]

# In [13]
len(v_tuple)

# In [14]
v_tuple[1:4]

# In [15]
v_tuple[0] = 2

# %% [markdown]
# ### Lists

# In [16]
v_list = [1, 3.5, -2.71, "qwerty"]

# In [17]
type(v_list)

# In [18]
v_list[0] = "this is a string"

# In [19]
v_list

# In [20]
v_list_addr = id(v_list)

# In [21]
v_list_addr

# In [22]
v_list.append([42])    # adding the list [42] to the end of our list
v_list

# In [23]
id(v_list) == v_list_addr    # adding elements doesn't create any new objects

# In [24]
v_list.pop(1)    # removing the element at the index "1"
v_list

# In [25]
id(v_list) == v_list_addr    # removing elements still doesn't create any new objects

# In [26]
[1, 2, 3] + [4, 5, 6]

# In [27]
3*[1, 2, 3]

# %% [markdown]
# ### NumPy arrays

# In [28]
l = [2**142 + 1, "a string"]

# In [29]
l.append(lambda x: x)

# In [30]
l

# In [31]
[id(x) for x in l]

# In [32]
import numpy as np

# In [33]
X = np.array([87.7, 4.5, -4.1, 42.1414, -3.14, 2.001])    # creating a NumPy array from a Python list

# In [34]
X

# In [35]
np.ones(shape=7)    # initializing a NumPy array from scratch using ones

# In [36]
np.zeros(shape=5)    # initializing a NumPy array from scratch using zeros

# In [37]
np.random.rand(10)

# In [38]
np.zeros_like(X)

# In [39]
X[0] = 1545.215
X

# In [40]
X[1:4]

# In [41]
X[0] = "str"

# In [42]
X.dtype

# In [43]
val = 23
type(val)

# In [44]
X[0] = val
X

# In [45]
for x in X:
    print(x)

# %% [markdown]
# ### NumPy arrays as vectors

# In [46]
v_1 = np.array([-4.0, 1.0, 2.3])
v_2 = np.array([-8.3, -9.6, -7.7])

# In [47]
v_1 + v_2    # adding v_1 and v_2 together as vectors

# In [48]
10.0*v_1    # multiplying v_1 with a scalar

# In [49]
v_1 * v_2    # the elementwise product of v_1 and v_2

# In [50]
np.zeros(shape=3) + 1

# In [51]
def f(x):
    return 3*x**2 - x**4

# In [52]
f(v_1)

# In [53]
from timeit import timeit


n_runs = 100000
size = 1000


t_add_builtin = timeit(
    "[x + y for x, y in zip(v_1, v_2)]",
    setup=f"size={size}; v_1 = [0 for _ in range(size)]; v_2 = [0 for _ in range(size)]",
    number=n_runs
)

t_add_numpy = timeit(
    "v_1 + v_2",
    setup=f"import numpy as np; size={size}; v_1 = np.zeros(shape=size); v_2 = np.zeros(shape=size)",
    number=n_runs
)


print(f"Built-in addition:       \t{t_add_builtin} s")
print(f"NumPy addition:          \t{t_add_numpy} s")
print(f"Performance improvement: \t{t_add_builtin/t_add_numpy:.3f} times faster")

# %% [markdown]
# ### Is NumPy really faster than Python?

# In [54]
from numpy.random import random as random_np
from random import random as random_py


n_runs = 10000000
t_builtin = timeit(random_py, number=n_runs)
t_numpy = timeit(random_np, number=n_runs)

print(f"Built-in random:\t{t_builtin} s")
print(f"NumPy random:   \t{t_numpy} s")

# In [55]
size = 1000
n_runs = 10000

t_builtin_list = timeit(
    "[random_py() for _ in range(size)]",
    setup=f"from random import random as random_py; size={size}",
    number=n_runs
)

t_numpy_array = timeit(
    "random_np(size)",
    setup=f"from numpy.random import random as random_np; size={size}",
    number=n_runs
)

print(f"Built-in random with lists:\t{t_builtin_list}s")
print(f"NumPy random with arrays:  \t{t_numpy_array}s")

# In [56]
from IPython.core import page
page.page = print

# In [57]
def builtin_random_single(n_runs):
    for _ in range(n_runs):
        random_py()

# In [58]
n_runs = 10000000

%prun builtin_random_single(n_runs)

# In [59]
def numpy_random_single(n_runs):
    for _ in range(n_runs):
        random_np()

# In [60]
%prun numpy_random_single(n_runs)

# In [61]
def builtin_random_list(size, n_runs):
    for _ in range(n_runs):
        [random_py() for _ in range(size)]

# In [62]
size = 1000
n_runs = 10000

%prun builtin_random_list(size, n_runs)

# In [63]
def numpy_random_array(size, n_runs):
    for _ in range(n_runs):
        random_np(size)

# In [64]
%prun numpy_random_array(size, n_runs)

# In [65]
sizes = list(range(1, 100))

runtime_builtin = [
    timeit(
        "[random_py() for _ in range(size)]",
        setup=f"from random import random as random_py; size={size}",
        number=100000
    )
    for size in sizes
]


runtime_numpy = [
    timeit(
        "random_np(size)",
        setup=f"from numpy.random import random as random_np; size={size}",
        number=100000
    )
    for size in sizes
]

# In [66]
import matplotlib.pyplot as plt


with plt.style.context("seaborn-v0_8"):
    plt.figure(figsize=(10, 5))
    plt.plot(sizes, runtime_builtin, label="built-in")
    plt.plot(sizes, runtime_numpy, label="NumPy")
    plt.xlabel("array size")
    plt.ylabel("time (seconds)")
    plt.title("Runtime of random array generation")
    plt.legend()
    plt.show()

# In [ ]

