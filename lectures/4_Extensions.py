#!/usr/bin/env python
# coding: utf-8

# # Extensions
# 
# Package contains a collection of community-contributed unofficial extensions that add functionality to the Jupyter notebook. These extensions are mostly written in Javascript and will be loaded locally in your browser.
# 
# In order to install these extensions we ran either one of these commands. Keep in mind **you don't need to run these commands for this class**
# 
# Conda:
# 
# ```sh
# conda install -c conda-forge jupyter_contrib_nbextensions
# ```
# 
# Pip:
# 
# ```sh
# pip install jupyter_contrib_nbextensions
# ```
# 
# There are various extensions that can change the way you interact with your notebook.
# 
# We will start with two of them that you may find interesting, _Scratchpad_ and _ExecuteTime_

# In[ ]:


a = 3
b = 10


# In[ ]:


import time
time.sleep(10)
30 + 10

