#!/usr/bin/env python
# coding: utf-8

# # Widgets
# 
# For this exercise let's take some world population data and make it sparkle with interactivity! Also, notice how we are telling a story with this particular notebook

# ## Getting Data
# 
# I wanted to get some data about the world's population, and found a csv online that I can use from a wonderful repository called [Github Datasets](https://github.com/datasets)

# In[ ]:


import pandas as pd

real_population = pd.read_csv('https://raw.githubusercontent.com/datasets/population/master/data/population.csv')


# ## Engineering Data
# 
# Next, I needed to remove the entries that aren't actual countries

# In[ ]:


clean_population = real_population[~real_population['Country Code'].str.contains('CSS|ARB|CEB|EAR|EAS|EAP|TEA|EMU|ECS|ECA|TEC|EUU|FCS|HPC|HIC|IBRD|IBD|IBT|IDB|IDX|IDA|LTE|LCN|LAC|TLA|LDC|LMY|LIC|LMC|MEA|MNA|TMN|MIC|NAC|OED|OSS|PSS|PST|PRE|SST|SAS|TSA|SSF|SSA|TSS|UMC|WLD')]


# Since these entries had multiple years, I just wanted to find the highest one, regardless of year. Yes, I am assuming that population is increasing for most countries

# In[130]:


grouped = clean_population.groupby(['Country Code'])['Value'].max()
grouped


# I then realized that the above entry had no continent data, so I got another source of information.

# In[131]:


continents = pd.read_csv('https://pkgstore.datahub.io/JohnSnowLabs/country-and-continent-codes-list/country-and-continent-codes-list-csv_csv/data/b7876b7f496677669644f3d1069d3121/country-and-continent-codes-list-csv_csv.csv')
continents


# Merging both together

# In[ ]:


merged = pd.merge(grouped, continents, how="left", left_on="Country Code", right_on="Three_Letter_Country_Code")


# Dropping all information that has empty data since that would be useless to me

# In[133]:


merged.dropna(inplace=True)


# ## Creating a function to dynamically display
# 
# The following function will take two arguments, `selection` and `topk`. `selection` is the continent, and `topk` is for the top number of countries in a continent.

# In[134]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def show_top(selection, topk):
    plt.figure(figsize=(23,5))
    sns.set_style("whitegrid")
    result = merged[merged['Continent_Name'] == selection].sort_values('Value', ascending=False).head(topk)
    barplot= sns.barplot(result['Country_Name'], result['Value'])
    barplot.set_xticklabels(barplot.get_xticklabels(),rotation=45)


# Here we just get all the unique continent names

# In[136]:


items = merged['Continent_Name'].unique()
items


# ## Exercise 1 
# 
# 1. Create a drop down widget that shows the continents
# 2. Create a slider widget that will set the top number of countries, make the number 1 through 25.
# 3. Call `interact` with the `show_top` function above

# In[128]:


from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
drop_down = widgets.Dropdown(
    options=items,
    description='Continent:',
    disabled=False,
)


# In[129]:


interact(show_top, selection=drop_down, topk=(1, 25));

