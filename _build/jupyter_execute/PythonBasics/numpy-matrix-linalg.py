#!/usr/bin/env python
# coding: utf-8

# # Numpy Matrices
# 
# (adapted from  CHEM 1000 - Spring 2023 by Prof. Geoffrey Hutchison, University of Pittsburgh)
# 
# 
# Many applications of Python to science, statistics, engineering, etc. are built on top of the [`numpy`](https://numpy.org/devdocs/user/quickstart.html) module. 
# 
# **Learning Objectives**
# 
# - Understand how to create `numpy` arrays from lists, or regular sets of numbers
# - Apply mathematical operations and functions to `numpy` arrays (e.g. for plotting, analysis, vectors, etc.)
# - Use matrix operations, including determinants, inverses, and solving systems of equations
# 
# **Attribution**
# 
# Some of this material has been adapted from [Mathematical Python by Patrick Wills](https://github.com/patrickwalls/mathematical-python/blob/master/scipy/numpy.ipynb)

# Before we start, we're going to `import numpy` with a standard shorthand `np`
# 
# This means that we refer to functions as `np.sin` and not `numpy.sin`, etc. to save some keystrokes...

# In[1]:


import numpy as np


# ## NumPy Arrays
# 
# As a reminder, the fundamental type provided by the NumPy package is the `ndarray`, which is an *n*-dimensional array - usually of numbers.
# 
# Generally, that means we can store:
# - 1-dimensional lists / vectors
# - 2-dimensional matrices / grids
# - 3-dimensional 'cube' or volumes of data
# - etc. (e.g., cubes of data over time.. maybe an MRI movie or watching a protein move?)
# 
# That flexibility adds complexity, unfortunately, but in this class, we'll mostly work with 1D and 2D arrays, which is not too bad. It just means that the Numpy documentation can be complicated to read because functions have to work on so many *types* of `ndarray`.
# 
# ### Creating Arrays
# 
# The function `numpy.array()` creates a NumPy array from a Python list, or a list of lists (for a matrix).

# In[2]:


M = np.array([[1,2,3],
              [4,5,6]])
print(M.shape)


# Again as a reminder, there are several NumPy functions for [creating arrays](https://docs.scipy.org/doc/numpy/user/quickstart.html#array-creation) - here we're using the standard `np` abbreviation for `numpy`:
# 
# | Function | Description |
# | ---: | :--- |
# | `np.array(a)` | Create $n$-dimensional NumPy array from sequence `a` |
# | `np.linspace(a,b,N)` | Create 1D NumPy array with `N` equally spaced values from `a` to `b` (inclusively)|
# | `np.arange(a,b,step)` | Create 1D NumPy array with values from `a` to `b` (exclusively) incremented by `step`|
# | `np.zeros(N)` | Create 1D NumPy array of zeros of length $N$ |
# | `np.zeros((n,m))` | Create 2D NumPy array of zeros with $n$ rows and $m$ columns |
# | `np.full(N, value)` | Create 1D NumPy array of `value` of length $N$ |
# | `np.fill((n,m), value)` | Create 2D NumPy array of `value` with $n$ rows and $m$ columns |
# | `np.eye(N)` | Create 2D NumPy array with $N$ rows and $N$ columns with ones on the diagonal (ie. the identity matrix of size $N$) |

# In[3]:


# Create a 2D NumPy array with 3 rows and 2 columns, filled with pi
N = np.full((3,2), np.pi) # Mmm pies.. 🥧
print(N)


# In[4]:


# full will let values be lists
# this will create a 3x3 array with 1, 2, 3 across each row
one_two_three = np.full((3, 3), [1, 2, 3])
print(one_two_three)


# In[5]:


# Create the identity matrix of size 4:
I = np.eye(4) # we'll use this again when we get to matrices.. esp. bigger ones
print(I)


# ### Dimension, Shape and Size
# 
# We can think of a 1D NumPy array as a list of numbers, a 2D NumPy array as a matrix, a 3D NumPy array as a cube of numbers, and so on. Given a NumPy array, we can find out how many dimensions it has by accessing its `.ndim` attribute. The result is a number telling us how many dimensions it has.
# 
# For example - let's check that `I` matrix above:

# In[6]:


I.ndim


# The result tells us that `I` has 2 dimensions. The first dimension corresponds to the vertical direction counting the rows and the second dimension corresponds to the horizontal direction counting the columns.
# 
# We can find out how many rows and columns `M` has by accessing its `.shape` attribute:

# In[7]:


M.shape


# Of course, we created M to be a $2\times 5$ matrix, so this may seem pretty silly.. still, for example when multiplying vectors and matrices, we need to know what size they are.
# 
# We can also use the `.size` attribute to give us the total elements - much like we'd use `len()` on a list.

# In[8]:


M.size


# ### Array Operations
# 
# [Arithmetic operators](https://docs.scipy.org/doc/numpy/user/quickstart.html#basic-operations) including addition `+`, subtraction `-`, multiplication `*`, division `/` and exponentiation `**` are applied to arrays *elementwise*. For addition and substraction, these are the familiar vector operations we see in linear algebra:

# In[9]:


v = np.array([1,2,3])
w = np.array([1,0,-1])


# In[10]:


v + w


# In[11]:


v - w


# This also works for multiplying or dividing by scalar numbers:

# In[12]:


2*v


# In[13]:


w / 2


# The exponent operator ** also acts element by element in the array:

# In[14]:


v ** 2


# All of these work as expected with matrix operations. Notice that we use two "[" characters when starting a 2D matrix (and then two "]" characters to end it).

# In[15]:


a = np.array( [[1,2,3],
               [4,5,6],
               [7,8,9]])

b = np.array( [[3,1,4],
               [1,5,9],
               [2,6,5]])

print(2*a + b)


# What about matrix multiplication?
# 
# If we do use "a\*b" we're actually doing element-wise multiplication. Numpy will multiply the contents of each cell, rather than perform matrix multiplication. 😡
# 
# It's fairly easy when you know the right syntax.
# 
# For matrix multiplcation, you want the "@" operator:

# In[16]:


a*b # NOT WHAT I WANTED...


# In[17]:


a@b # ah, that's matrix multiplication


# ### Linear Algebra with Matrices
# 
# There are a few key tasks when using matrices for linear algebra. Most of these are in `numpy.linalg`:
# 
# - Transpose: `A.T` is the transpose of A
# - Trace: `numpy.trace(A)` is the trace of A
# - Determinant: `numpy.linalg.det(A)` is the determinant
# - Inverse: `numpy.linalg.inv(A)` is the inverse
# - Solving systems of equations: `numpy.linalg.solve(A, b)` solves the matrix equation $A \times x = b$

# In[18]:


a.T


# In[19]:


np.trace(a)


# In[20]:


# Even though we already imported numpy, we can save some keystrokes
# by giving it a shortcut name
import numpy.linalg as la

la.det(b)


# In[21]:


la.inv(b)


# In[22]:


# Check b multiplied by inverse
b@la.inv(b)


# In[23]:


la.inv(b)@b


# Notice that $b \times b^{-1}$ is very, very close to the identity matrix:

# In[24]:


np.eye(3)


# Solve the system of equations x + 2y = 1 and 3x + 5y = 2:

# In[25]:


a = np.array([[1, 2],
             [3, 5]])
b = np.array([1,2])

np.linalg.solve(a, b)


# In other words, x = -1 and y = 1

# -------
# This notebook is adapted from Prof. Geoffrey Hutchison, University of Pittsburgh
# https://github.com/ghutchis/chem1000
# 
# Portions have been adapted from [Mathematical Python by Patrick Wills](https://github.com/patrickwalls/mathematical-python/tree/master/scipy)
# 
# <a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a>
