#!/usr/bin/env python
# coding: utf-8

# # Creating your first sheet
# 
# **Instructions:**
# 
# 1. Don't use the mouse and see if you can do it. You have all the power in world on the keyboard!
# 2. Create the following cells

# **Exercise 1:**
# 
# 1. Create a cell underneath (use keyboard please)
# 2. Create a header called "Biography"
# 2. Write a little bit about yourself
# 3. Include an unordered bulleted list of all the technologies and skills that you have
# 4. For the skills that you are an expert in, make that in bold

# **Exercise 2:**
# 
# 1. Create a cell underneath (use keyboard please)
# 2. Import `pandas` in the standard convention
# 1. Create a `DataFrame` from the file located in `../data/characters.csv`, this will contain all the characters from the Harry Potter Universe.  The data is separated by a `;` so use tooltips to figure out how to do stipulate a separator.
# 3. Assign the `DataFrame` to a variable called `characters`

# **Exercise 3:**
# 
# 1. Let's find all the Slytherin! 
# 2. Create a cell underneath this cell
# 2. Type: `characters.House == 'Slytherin'` or `characters['House'] == 'Slytherin'`
# 3. Notice the Results

# **Exercise 4:**
# 
# 1. Let's mask this data so we only see the Slytherin
# 5. Create a cell underneath this cell
# 6. Type: `characters[characters.House == 'Slytherin']`
# 7. This process is called masking
# 
