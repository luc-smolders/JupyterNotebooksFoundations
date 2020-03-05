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

# In[ ]:





# ## Exercise 2
# 
# 1. Import the standard packages and their conventions to perform plotting
# 2. Be sure to include `import seaborn as sns`

# In[ ]:





# ## Exercise 3
# 1. Run the following cells to clean up the data, the new cleaned up `DataFrame` is called `clean_characters` 
# 2. Create a bar plot showing how many characters belong to each house, use `x_axis` and `y_axis`
# 3. To get started with a bar plot, use `plt.bar`

# In[ ]:


clean_characters = characters[['Name', 'House']].dropna()
clean_characters.head()


# In[ ]:


value_counts = clean_characters['House'].value_counts()
value_counts


# In[35]:


x_axis = value_counts.index
y_axis = value_counts.values


# In[ ]:


x_axis


# In[ ]:


y_axis


# In[ ]:





# In[ ]:





# In[ ]:




