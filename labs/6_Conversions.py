#!/usr/bin/env python
# coding: utf-8

# # A Presentation about Jupyter Notebooks!
# 
# ![Jupyter_Logo](https://jupyter.org/assets/main-logo.svg "Jupyter Logo")
# 
# By Enter Your Name Here

# ## Jupyter Notebooks
# 
# We learned about:
#     
# * Creating notebooks efficiently using key commands
# * Using Markdown in cells
# * Using Python in cells
# * Splitting cells and Merging Cells

# ## Visualization
# 
# We then learned about using matplotlib for plotting our data.  Here was an example of one of the simple plots we did.

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


x = np.linspace(0, 10, 50)
y = x ** 2
plt.plot(x, y);


# ## Widgets
# 
# We covered widget which allows us to interact with our notebooks and change things on the fly. Below is one of our simple examples.

# In[3]:


from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets

def power_squared(x):
    return x ** 2

interact(power_squared, x=(-10, 100, 10));


# ## Extensions
# 
# * We also ran some extensions too! 
# * We saw that the community comes together and creates some enhancements for Jupyter Notebook
# * My favorite is ______________

# ## Dashboards
# 
# * We were introduced to Voila. Which can turn our Jupyter Notebooks into an interactive web page
# * We also learned that there are some new libraries built on Voila, that will allow us to move cells around to get our pages like we want to

# ## Conversions
# 
# * We learned about nbconvert and nbviewer 
# * We learned that it is built into our notebook 
# * We learned that we can make pdfs and slidedecks
