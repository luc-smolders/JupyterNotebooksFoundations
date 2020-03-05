#!/usr/bin/env python
# coding: utf-8

# # Visualizations

# Importing some required packages.  `%matplotlib` is a directive to show plots in the notebook. These are standard imports required for display.

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import numpy as np


# Creating a plural of numbers

# In[4]:


x = np.arange(0, 10, .5)
x


# In[5]:


y = x ** 2 #vectprized-operation
y


# In[3]:


plt.plot(x,y);


# Same data except with a scatter plot

# In[6]:


x = np.arange(0, 10, .5)
y = x ** 2

plt.scatter(x,y);


# Same kind of plot but with `linspace`, use Jupyter's tooltip to see what `linspace` does.

# In[7]:


x = np.linspace(0, 10, 50)
y = x ** 2

plt.plot(x, y);


# Here we are loading some sample data from scikit learn, you can bring in data from whatever kind of datasource that you would like. This is already a part of the scikitlearn library. `load_iris` returns a Python dictionary.
# 
# **TIP**: If the cell is too big and you need to understand what is going on, **SPLIT THE CELL!**. We will also discuss a scratchpad later

# In[9]:


from sklearn.datasets import load_iris
iris = load_iris();
x_axis = iris.data[:, 0]
y_axis = iris.data[:, 1]
x_column_name = iris.feature_names[0]
y_column_name = iris.feature_names[1]
target = iris.target


# In[10]:


plt.scatter(x_axis, y_axis);


# Above is the scatter plot for iris data

# In[11]:


plt.scatter(x_axis, y_axis)
plt.xlabel(x_column_name)
plt.ylabel(y_column_name);


# In[12]:


plt.scatter(x_axis, y_axis)
plt.xlabel(x_column_name)
plt.ylabel(y_column_name)
plt.title("Iris Dataset (%s vs. %s)" % (x_column_name, y_column_name));


# In[13]:


plt.scatter(x_axis, y_axis, c=target)
plt.xlabel(x_column_name)
plt.ylabel(y_column_name)
plt.title("Iris Dataset (%s vs. %s)" % (x_column_name, y_column_name));


# In[14]:


# Make sure that figure is the first line
plt.figure(figsize=(10,5))
plt.scatter(x_axis, y_axis, c=target, alpha=0.5)
plt.xlabel(x_column_name)
plt.ylabel(y_column_name)
plt.title("Iris Dataset (%s vs. %s)" % (x_column_name, y_column_name));


# **Example 10:** Let's add a colormap. You can choose any kind of colormap and choose [your own color map](https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html). Keep in mind accessibility, some colors are not distinguishable.

# In[15]:


# Make sure that figure is the first line
plt.figure(figsize=(10,5))
plt.scatter(x_axis, y_axis, c=target, alpha=0.5, cmap='winter')
plt.xlabel(x_column_name)
plt.ylabel(y_column_name)
plt.title("Iris Dataset (%s vs. %s)" % (x_column_name, y_column_name));


# In[16]:


# Make sure that figure is the first line
import seaborn as sns
plt.figure(figsize=(10,5))
sns.set_style("whitegrid")
plt.scatter(x_axis, y_axis, c=target, alpha=0.5, cmap='winter')
plt.xlabel(x_column_name)
plt.ylabel(y_column_name)
plt.title("Iris Dataset (%s vs. %s)" % (x_column_name, y_column_name));


# In[17]:


# Make sure that figure is the first line
import seaborn as sns
plt.figure(figsize=(10,5))
sns.set_style("dark")
plt.scatter(x_axis, y_axis, c=target, alpha=0.5, cmap='winter')
plt.xlabel(x_column_name)
plt.ylabel(y_column_name)
plt.title("Iris Dataset (%s vs. %s)" % (x_column_name, y_column_name));


# In[18]:


# Make sure that figure is the first line
import seaborn as sns
plt.figure(figsize=(10,5))
sns.set_style("darkgrid")
plt.scatter(x_axis, y_axis, c=target, alpha=0.5, cmap='winter')
plt.xlabel(x_column_name)
plt.ylabel(y_column_name)
plt.title("Iris Dataset (%s vs. %s)" % (x_column_name, y_column_name));


# In[19]:


# Make sure that figure is the first line
import seaborn as sns
plt.figure(figsize=(10,5))
sns.set_style("ticks")
plt.scatter(x_axis, y_axis, c=target, alpha=0.5, cmap='winter')
plt.xlabel(x_column_name)
plt.ylabel(y_column_name)
plt.title("Iris Dataset (%s vs. %s)" % (x_column_name, y_column_name));


# What if we have only one set of data? How do we plot the distribution?

# In[20]:


x_axis = iris.data[:, 0]
y_axis = np.zeros(iris.data.shape[0])
import seaborn as sns
plt.figure(figsize=(10,1))
sns.set_style("ticks")
plt.scatter(x_axis, y_axis, c=target, alpha=0.5, cmap='winter')
plt.xlabel(x_column_name)
plt.title("Sepal Length Distribution");


# In[21]:


x_axis = iris.data[:, 0]
import seaborn as sns
plt.figure(figsize=(10,5))
sns.set_style("ticks")
plt.hist(x_axis)
plt.title("Sepal Length Distribution");


# In[22]:


x_axis = iris.data[:, 0]
import seaborn as sns
plt.figure(figsize=(10,5))
sns.set_style("ticks")
plt.hist(x_axis, bins=20, histtype='stepfilled')
plt.title("Sepal Length Distribution");


# In[23]:


import seaborn as sns
sns.set_style("ticks")
plt.figure(figsize=(10,5))

#First plot the first column
first_column = iris.data[:, 0]
first_column_name = iris.feature_names[0]
plt.hist(first_column, bins=20, alpha=0.5, histtype='stepfilled', label="%s Distribution" % first_column_name);

first_column = iris.data[:, 1]
first_column_name = iris.feature_names[1]
plt.hist(first_column, bins=20, alpha=0.5, histtype='stepfilled', label="%s Distribution" % first_column_name);

plt.title("Sepal Distribution")
plt.xlabel("Measurement (cm)")
plt.ylabel("Count")
plt.minorticks_on()
plt.legend();


# In[24]:


import seaborn as sns
sns.set_style("ticks")
plt.figure(figsize=(10,5))

#First plot the first column
first_column = iris.data[:, 2]
first_column_name = iris.feature_names[2]
plt.hist(first_column, bins=20, alpha=0.5, histtype='stepfilled', label="%s Distribution" % first_column_name);

first_column = iris.data[:, 3]
first_column_name = iris.feature_names[3]
plt.hist(first_column, bins=20, alpha=0.5, histtype='stepfilled', label="%s Distribution" % first_column_name);

plt.title("Petal Distribution")
plt.xlabel("Measurement (cm)")
plt.ylabel("Count")
plt.minorticks_on()
plt.legend();


# In[25]:


import seaborn as sns
sns.set_style("whitegrid")
plt.figure(figsize=(10,5))
plt.boxplot(iris.data, labels=iris.feature_names, showmeans=True, meanline=True);

