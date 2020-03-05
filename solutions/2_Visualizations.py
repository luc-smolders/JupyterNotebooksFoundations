#!/usr/bin/env python
# coding: utf-8

# # Visualizing Data
# 
# **Instructions:**
# 
# 1. Don't use the mouse and see if you can do it. You have all the power in world on the keyboard!
# 2. Create the visualization

# ## Exercise 1
# 
# 1. Create a cell underneath (use keyboard please)
# 2. Import pandas in the standard convention
# 3. Create a DataFrame from the file located in `../data/characters.csv`, this will contain all the characters from the Harry Potter Universe. The data is separated by a ; so use tooltips to figure out how to do stipulate a separator.
# 4. Assign the DataFrame to a variable called `characters`

# In[28]:


import pandas as pd

characters = pd.read_csv('../data/characters.csv', sep=';')
characters


# ## Exercise 2
# 
# 1. Import the standard packages and their conventions to perform plotting

# In[29]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# ## Exercise 3
# 1. Run the following cells to clean up the data, the new cleaned up `DataFrame` is called `clean_characters` 
# 2. Create a bar plot showing how many characters belong to each house. Hint there are fewer columns

# In[33]:


clean_characters = characters[['Name', 'House']].dropna()
clean_characters.head()


# In[34]:


value_counts = clean_characters['House'].value_counts()
value_counts


# In[35]:


x_axis = value_counts.index
y_axis = value_counts.values


# In[37]:


x_axis


# In[38]:


y_axis


# Using Matplotlib

# In[40]:


plt.figure(figsize=(23,5))
sns.set_style("whitegrid")
plt.bar(x_axis, y_axis);


# Using Seaborn

# In[41]:


plt.figure(figsize=(23,5))
sns.set_style("whitegrid")
sns.barplot(x_axis, y_axis);

