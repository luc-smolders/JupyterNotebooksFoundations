#!/usr/bin/env python
# coding: utf-8

# # Jupyter Notebook
# 
# This shows how a jupyter notebook works.  It uses markdown. 
# It is also a way for you to help learn content. It merges documentation, code, and visualizations to create a compelling story. 

# ## Cell Manipulation

# ### Basic Keyboard
# 
# * **C** Copy
# * **X** Cut
# * **V** Paste
# * **Z** Redo

# ### Evaluating Cells
# 
# * When editing a cell you are in _Edit mode_
# * When are done editing and you run the cell you will be in _Command Mode_
# * You have diffent flavors of running cells
#   * ⇧↩ or **SHIFT + ENTER** run cell, select below
#   * ⌃↩ or **CTRL + ENTER** run selected cells
#   * ⌥↩ or **OPTION + ENTER** run cell and insert below

# In[5]:


a = 30
b = 10


# ### Adding Cells
# 
# * A Cell above can be created by pressing **A** in Command Mode
# * A Cell below can be created by pressing **B** in Command Mode

# In[ ]:





# ### Deleting Cells
# 
# A cell can be deleted with **D,D**

# In[ ]:


print("Hello")


# In[ ]:


print("World")


# ### Splitting Cells
# 
# A cell can be split in _Edit Mode_ using **⌃⇧Minus** or **CTRL+SHIFT+MINUS**
# 
# ### Merging Cells
# 
# A cell can be merged in _Command Mode_ after selecting multiple cells using **⇧M** or **SHIFT+M**

# In[ ]:


a = 30
b = 10


# ## Types of Cells
# 
# Cells can either be:
# 
# * **Markdown -** Using markdown to create documentation cells
# * **Code -** Cells representing code, runnable
# * **Raw -** Cells with no formatting, and no interpretation since it is not code

# ## Markdown

# ### Bullet Lists
# 
# * One
# * Two
# * Three

# ### Strikethrough
# 
# ~~This should strikethrough~~

# ### Tables
# 
# The following is a table
# 
# | Column 1 | Column 2 |
# | ---------|----------|
# | One      | `1`      |
# | Two      | `2`      |

# ### Checkboxes 
# 
# You can have displayed checkboxes, although Jupyter notebooks has widgets that do a better job.
# 
# - [X] One
# - [ ] Two
# - [ ] Three

# ### Carriage Returns
# 
# Carriage Returns can be done with two spaces at the end of the line:
# 
# <hr>
# 
# Space, The final frontier  
# These are the voyages of Starship Enterprise  
# In its continuing missions  
# To seek out new life, and new civilization  
# To boldly go where no one has gone before  
# 
# <hr>

# ### Code
# 
# Inline `code` has `back-ticks around` it.
# 
# Block `code` has triple tick marks around it, and an optional language which offers syntax highligting
# 
# ```python
# s = "Python syntax highlighting"
# print s
# ```
# 
# You can also indent four spaces
# 
#     def main() {
#         print("Hello")
#     }
# 
# **NOTE:** Some markdown features do not work. This include footnotes and ancillary comments

# 
# ### Displaying Images
# 
# #### Displaying images in the markdown cells 
# 
# Use standard markdown to display images: The following uses markdown to display the image
# 
# ![Jupyter_Logo](https://jupyter.org/assets/main-logo.svg "Jupyter Logo")

# ## $\LaTeX$ 
# 
# We can also have formulas by flanking dollar signs around a Latex formula.  See cheatsheet for more options https://wch.github.io/latexsheet/ or go see the following cells.  For example, $e=mc^2$

# **TIP:** Import images from the web for a nice cheatsheet
# 
# ![latex_0](https://wch.github.io/latexsheet/latexsheet-0.png)
# ![latex_1](https://wch.github.io/latexsheet/latexsheet-1.png)

# Here is a $\LaTeX$ example that will make us look and feel really smart: $\idotsint_V \mu(u_1,\dots,u_k) \,du_1 \dots du_k$ and $\sum_{n=1}^{\infty} 2^{-n} = 1$

# ## Code
# 
# Turn on code by typing 'Y' on a cell.  The cell below is already a code cell. There is nothing that you need to do, but if you were to create your own cells, and you want to ensure that it is for creating code, then hit 'Y'

# In[6]:


print('foo')


# ### Evaluating Code in Jupyter Notebooks
# 
# The last statement in a cell will be evaluated and displayed underneath the cell. `In` represents the input, and `Out` represents the output.

# In[7]:


a = 10
b = 50
a + b


# If there is no return type, or a function that is a side-effect then you will not receive an output

# In[8]:


c = 40


# In[9]:


print("This will print, but notice no Out[Num]")


# ### Tooltips
# 
# Tooltips can be perform by using the **SHIFT+TAB** key as long as your cursor is in the method name. Try it below by putting the cursor inside the `print` and hitting **SHIFT+TAB**. Try it once, twice, three, and four times!

# In[ ]:


print('foo')


# ### Code Completion
# 
# Code completion offers choices for methods and variables that you would like to use.  To invoke a code completion, hit **TAB** after establishing an assignment

# In[ ]:


my_string = "Hello to Jupyter!"
my_string


# ### Images in Code Cells
# 
# You can display other images using code. You can include an image from a file or from a URL.

# In[10]:


from IPython.display import Image, display
url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Python.svg/1024px-Python.svg.png'
display(Image(url, width='20%', height='20%')) 


# ### Line Numbers
# 
# **L** will toggle line numbers in a code cell you have selected.  
# **⇧L** or **SHIFT+L** will toggle line numbers in all code and raw cells in your jupyter notebook

# In[11]:


a = 10
b = 50
a + b

## Raw cells don't do much, it isn't code, nor is formatted text. It is just raw data. You can change a cell to raw, by pressing **R** on the cell.

**TIP:** Use Raw format for a cell to comment it out, but leave it around in case you need it.def not_sure_about_this():
    for item in items:
        bits = []

        try:
            bits.append(str(item['item'].attr_x))
        except:
            bits.append('ERR')

        try:
            bits.append(str(item['item'].attr_x.attr_x))
        except:
            bits.append('ERR')

        
        output.append('"{line}"'.format(line='","'.join([s.replace('"', "'") for s in bits])))
# ## Python Programming
# 
# Python is the preferred language for data science and in Jupyter Notebooks. Let's start with a slight introduction. Of course O'Reilly Media has various books and courses on Python that you can use inside of a Jupyter Notebook.

# In[12]:


nums = [1,2,3,4,5,6]
nums


# ### Using Numpy 
# 
# Numpy is high performance, C backed number crunching framework

# In[13]:


import numpy as np
numpy_array = np.array([1,2,3,4,5])
numpy_array


# ### Using Pandas
# 
# Pandas is a library to manipulate data. It stands for "Panel Data".  
# 
# #### `pd.Series`
# 
# A series is an optimized list in Python which has labels associated with the elements.

# In[14]:


import pandas as pd
population = pd.Series([1_433_783_686,
                        1_366_417_754,
                        329_064_917,
                        270_625_568,
                        216_565_318], 
         
                       index = ['China', 
                                'India', 
                                'United States', 
                                'Indonesia', 
                                'Pakistan'])
population


# Here is an example of that Series with different labels

# In[15]:


import pandas as pd
area_sq_km = pd.Series([16_376_870,
                        9_388_211,
                        9_147_420,
                        9_093_510,
                        8_358_140], 
                       index = ['Russia', 
                                'China', 
                                'United States', 
                                'Canada', 
                                'Brazil'])
area_sq_km


# #### `pd.DataFrame` 
# 
# `DataFrame` is of the Pandas package and it combines multiple `Series` into a `DataFrame`. It is analogous to a small Excel sheet.

# In[16]:


country_df = pd.DataFrame([area_sq_km, population], index= ['Area (km²)', 'Population'])
country_df


# There are a whole lot of great things we can do with Pandas like drop empty values and transpose.  Here is an example.

# In[17]:


flipped_country_df = country_df.transpose()
flipped_country_df


# In[18]:


big_pop_big_area = flipped_country_df.dropna()
big_pop_big_area


# ### Bringing in data from a source

# In[19]:


import pandas as pd

real_population = pd.read_csv('https://raw.githubusercontent.com/datasets/population/master/data/population.csv')
real_population



# ### Accessing columns

# In[20]:


real_population['Year']


# ### Another way to go about retaining a column

# In[22]:


real_population.Year


# ### What are the differences?
# 
# 1. Using brackets is great if you specifically want the column and want to avoid conflicts between column name and method a name
# 2. Using the period style, is great when you need the help of auto-completion. Try erasing 'Year' above and use code completion

# ## Filtering
# 
# To filter data, use a process called masking to filter out content, but first let's ask it to only show data after 2010.

# In[23]:


real_population.Year > 2010


# ### Filtering using a process called masking
# 
# To actually perform the actual filtering we can "re-feed the above results back in.

# In[24]:


real_population[real_population.Year > 2010]


# ### Going deeper into Data Engineering and Data Science
# 
# There is a rich environment for doing data filtering, grouping, and numerical operations. If you love this, then definitely get a copy of these books:
# 
# Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow, 2nd Edition  
# by Aurélien Géron  
# Publisher: O'Reilly Media, Inc.  
# Release Date: September 2019  
# ISBN: 9781492032649  
#   
# ![Hands_On](https://learning.oreilly.com/library/cover/9781492032632/)

# Python Data Science Handbook  
# by Jake VanderPlas  
# Publisher: O'Reilly Media, Inc.  
# Release Date: November 2016  
# ISBN: 9781491912058  
# 
# ![Python_Data_Science_Handbook](https://learning.oreilly.com/library/cover/9781491912126/)
