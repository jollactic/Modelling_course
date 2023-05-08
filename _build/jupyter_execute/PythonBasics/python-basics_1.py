#!/usr/bin/env python
# coding: utf-8

# # Python Basics
# (adapted from CHEM 1000 - Spring 2023 by Prof. Geoffrey Hutchison, University of Pittsburgh)
# 
# The best way to learn coding or a new programming language is to do something useful. Not only will you have more motivation, but the time invested for the skill will be repaid in (hopefully) doing that useful task.
# 
# **Learning Objectives**
# 
# By the end of this recitation / notebook, you should be able to:
# - Read and write basic Python
# - Assign variables in Python
# - Call Python functions and methods
# - Load Python modules with `import`
# - Understand simple `for` and `while` loops
# 
# **Attribution**
# 
# Much of this recitation has been adapted from [Software Carpentry - Scientific Python Basics](https://bids.github.io/2016-01-14-berkeley/python/00-python-intro.html) and [Mathematical Python by Patrick Wills](https://github.com/patrickwalls/mathematical-python/tree/master/python)

# ## Variables / Things
# 
# The most basic component of any programming language are "things", also called variables or (in special cases) objects.
# 
# The most common basic "things" in Python are:
# - integers (e.g., `0`, `1`, `-2`, etc.)
# - floats (i.e., floating-point decimals like `2.5`, `3.14159`, `6.02e23` = $6.02 \times 10^{23}$, `1.5e-10` = $1.5\times10^{-10}$, etc.)
# - strings (e.g., `'Chem 1000'`, `'H2P'`, `"Math for Chemistry"`)
# - booleans (i.e., `True` and `False` - note that these are case-sensitive)
# - some special objects of various types.
# We'll meet many of these as we go through the lesson.
# 
# **TIP:** To run the code in a cell quickly, press `Ctrl-Enter`.

# In[1]:


# a thing
2


# In[2]:


# Use print to show multiple things in the same cell
# Note that you can use single or double quotes for strings
print(2)
print('hello')


# ### Assign Values to Variables
# 
# Sometimes we want a label for a number, string, etc. Like we don't always want to type out 3.141592653589793238 every time we refer to $\pi$.
# 
# Variables are just a programmer term for labels for out information .. floats, strings, lists, etc.
# 
# We assign a value to a variable using the assignment operator `=`. For example, assign the integer 2 to the variable `x`:

# In[3]:


# Things can be stored as variables
x = 2
y = 'hello' # strings can be in single quotes or double quotes
z = True  # True and False are case sensitive


# The assignment operator does not produce any output and so the cell above does not produce any output in a Jupyter notebook. Use the built-in function `print` to display the value assigned to a variable:

# In[4]:


print(x)


# ## Naming Conventions
# 
# We can use any set of letters, numbers and underscores to make variable names however a variable name *cannot* begin with a number. There are many different kinds of naming conventions and we refer to the [Style Guide for Python Code (PEP8)](https://www.python.org/dev/peps/pep-0008/#naming-conventions) for a summary.
# 
# In general, in Python, people use `lower_case_with_underscores` variable names and single lowercase letter variable names such as `x`. It is good practice to use descriptive variable names, like `height_in_meters` to make your code more readable for other people (including yourself looking back later).
# 
# However there are words that we should not use as variable names because these words already have special meaning in Python, including [reserved words](https://docs.python.org/3.3/reference/lexical_analysis.html#keywords) and built-in functions For example, do not use `class`, `import`, `sum`, `min`, `max`, `list` or `sorted` as a variable name. See the full list of [builtin functions](https://docs.python.org/3/library/functions.html). Generally if you either use single letters or descriptive `words_with_underscores` you should be fine.

# ## Commands that operate on things
# 
# Just storing data in variables isn't much use to us. Right away, we'd like to start performing operations and manipulations on data and variables.
# 
# There are three very common means of performing an operation on a thing.
# 
# ### Use an operator
# All of the basic math operators work like you think they should for numbers. They can also do some useful operations on other things, like strings.
# 
# Number operators include `+`, `-`, `*`, and `/` as well as `%` for integer remainder and `**` for exponents:
# 
# | operator name|operator|syntax|How to read|
# |---|---|---|---|
# | addition|+|a + b|a plus b|
# | subtraction|-|a - b|a minus b|
# | multiplication|\*|a \* b|a times b|
# | division|\/|a \/ b|a divided by b|
# | remainder|%|a % b|a modulo b|
# | power|**|a**b|a to the power b|

# In[5]:


# Standard math operators work as expected on numbers
a = 2
b = 3


# Okay, we can add them:

# In[6]:


a + b


# We can subtract:

# In[7]:


a - b


# Multiply:

# In[8]:


a * b


# Divide:

# In[9]:


a / b


# Get a remainder:

# In[10]:


b % a


# And perform powers / exponents:

# In[11]:


a**b


# A few notes.. we can also perform exponents with fractions (e.g., square root). Note that the parentheses will take precedence over the exponent:

# In[12]:


2**(1/2)


# In[13]:


# There are also operators for strings
print('hello' + 'world') # notice that the + operator won't include a space
print('hello' * 3) # This can be very useful for building up larger strings as sequences


# ## Use a function
# 
# These will be very familiar to anyone who has programmed in any language, and work like you
# would expect. Functions have a syntax like:
# 
# `name( *parameters* ) # sometimes with multiple parameters.`
# 
# **TIP:** Many useful functions are not in the Python itself, but are in external "modules" or "libraries". These need to be imported into your Python notebook (or program) before they can be used. Some of the most important of these are `math`, `numpy` and `matplotlib`.

# In[14]:


print(round(3.3))

import numpy
print(numpy.sqrt(4))
print(numpy.pi) # just a constant
print(round(numpy.pi, 4)) # round pi to 4 decimal places - use "from sigfig import round" for the sigfig version
print(numpy.sin(numpy.pi/2))


# ## Modules
# 
# As mentioned above, much of the power of Python is that there are many, many useful modules, particularly for science, math, statistics, machine learning, .. We load these tools with statements like:
# 
# `import cmath`
# 
# `from sympy import ode`
# 
# These statements will load additional functions to our Python notebooks and scripts. To prevent confusion, we will typically use a prefix for these functions:
# 
# - `math.sqrt` (from the math module)
# - `numpy.sqrt` (from the numpy module)
# 

# ## Collections
# 
# While it is interesting to explore your own height, in science we work with larger  slightly more complex datasets. In this example, we are interested in the characteristics and distribution of heights. Python provides us with a number of objects to handle collections.
# 
# Probably 99% of your work in scientific Python will use `lists` and `numpy` `arrays`. We'll talk about `numpy` in another session - basically, it offers ways to do math on lists/vectors, matrices, and the like.

# Lists are probably the handiest and most flexible type of container.
# 
# Lists are declared with square brackets `[]`.
# 
# Individual elements of a list can be selected using the syntax `a[ind]`.
# 
# One "gotcha" for people new to programming is that lists in Python (and many other programming languages) start at 0.

# In[15]:


# Lists are created with square bracket syntax
pies = ['blueberry', 'strawberry', 'apple', 'rubarb', 'cherry']
print(pies, type(pies))


# In[16]:


# Lists (and all collections) are also indexed with square brackets
# NOTE: The first index is zero, not one
print(pies[0])
print(pies[1])

## You can also count from the end of the list
print('last item is:', pies[-1])
print('second to last item is:', pies[-2]) # notice that the comma between things in a print() adds spaces


# In[17]:


# We can add things to the list
pies.append('pumpkin')
print('last item is now:', pies[-1])


# What is a method? It's a type of function. Some types of variables, called objects contain data as well as functions (called methods) to manipulate that data. Everything in Python is an object! The list `pies` in the cell above contains the string entries (the data) but it also has methods like `append()` to manipulate the data. 

# In[18]:


# lists have a .sort(method) .. and a .reverse() method
pies.sort()
pies.reverse()
print(pies)
# you can also remove items (e.g., if my kids eat one of the pies)
pies.remove('cherry')
print(pies)
# if you try to remove something not in the list, you'll get an error
pies.remove('cherry') # we only had one cherry pie, sorry


# ## Loops
# 
# Let's say you're asked to take a cognitive test and count backwards from 100 by 7:

# In[19]:


number = 100
while number > 0:
    print(number)
    number = number - 7
print('Congrats, you passed the test')


# Notice that inside the `while` loop, we *indent* the code. You can do this by typing `Tab` as you type code, and Jupyter will insert 4 spaces. Any code that should run after the loop should have the same indentation as the `while` statement (i.e., at the left edge of the cell) like the final `print()` statement. Python uses indentation to track which code lines should run in particular scope / context (e.g, as part of a loop or not).
# 
# Loops like these are a common case in programming, and we can do the same thing with a `for` loop. We'll use a new function - the `range()` function has three options:
# - start (100)
# - end (0)
# - step (-7 each time through the loop)

# In[20]:


# repeat starting at 100, ending at 0, and going by -7 each time
for number in range(100, 0, -7):
    print(number)
print('Finished')


# This is an important lesson - there are usually many ways to do the same thing in programming. For this class, we're using a small amount of code to help us get the correct answer. I don't care what the code looks like, although we need to read it for grading, and it needs to work. 😀 
# 
# This is the origin of "Software Carpentry" for scientists - teaching researchers the key computing skills they need to get more done in less time and with less pain - not necessarily building large programs.

# ## Final Thoughts
# 
# There's obviously a lot more to Python programming, but this should cover the basics we need for this course. If you have questions about the tutorial here, or code in the future, please don't hestiate to ask at the labs or at the tuorial sessions. You can also ask questions in the Studium discussion forum.

# -------
# This notebook is adapted from Prof. Geoffrey Hutchison, University of Pittsburgh
# https://github.com/ghutchis/chem1000
# 
# Portions have been adapted from [Software Carpentry - Scientific Python Basics](https://bids.github.io/2016-01-14-berkeley/python/00-python-intro.html) and [Mathematical Python by Patrick Wills](https://github.com/patrickwalls/mathematical-python/tree/master/python)
# 
# <a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a>
