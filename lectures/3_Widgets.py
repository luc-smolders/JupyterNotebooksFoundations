#!/usr/bin/env python
# coding: utf-8

# # Widgets
# 
# ## `interact`
# The interact function (`ipywidgets.interact`) automatically creates user interface (UI) controls for exploring code and data interactively. It is the easiest way to get started using IPython’s widgets.

# At the most basic level, interact autogenerates UI controls for function arguments, and then calls the function with those arguments when you manipulate the controls interactively. To use interact, you need to define a function that you want to explore.

# Importing the required packages

# In[ ]:


from ipywidgets import interact
import ipywidgets as widgets


# Create a function to interact with the widget

# In[ ]:


def power_squared(x):
    return x ** 2


# In[ ]:


interact(power_squared, x=10);


# `interact` can be given a 3-tuple which represents minimum, maximum, and step

# In[ ]:


interact(power_squared, x=(-10, 100, 10));


# `fixed` will always use the same value, and will not offer your end users the ability to change the value

# In[ ]:


def h(p, q):
    return (p, q)


# In[ ]:


from ipywidgets import fixed
interact(h, p=5, q=fixed(20));


# ## Widget Abbreviations

# When you pass an integer-valued keyword argument of `10` (`x=10`) to `interact`, it generates an integer-valued slider control with a range of $[-10,+3*10]$. In this case, `10` is an abbreviation for an actual slider widget called `widgets.IntSlider`

# Using the full `IntSlider`

# In[ ]:


interact(power_squared, x=widgets.IntSlider(min=-10, max=30, step=1, value=10));


# If the keyword argument is a Widget instance with a value attribute, that widget is used. Any widget with a value attribute can be used, even custom ones.
# 
# Otherwise, the value is treated as a widget abbreviation that is converted to a widget before it is used.
# 
# The following table gives an overview of different widget abbreviations:
# 
# | Keyword Argument                                                             | Widget      |
# |------------------------------------------------------------------------------|-------------|
# | True or False                                                                | Checkbox    |
# | `value` `(min, max)` or `(min, max, step`)                                   | IntSlider   |
# |  if float `value` `(min, max)` or `(min, max, step`)                         | FloatSlider |
# | List of elements `['red', 'yellow', 'orange']` or `[('one', 1), ('two', 2)]` | Dropdown    |

# Example of interaction using default values and the widget that it represents

# In[ ]:


def compute(x, y, z):
    if (z):
       return x + y
    else: 
       return x * y


# In[ ]:


interact(compute, x = 10, y = (-10, 10, 2), z=True);


# ## `interactive`
# 
# * you want to reuse the widgets that are produced or access the data that is bound to the UI controls.
# * Unlike `interact`, the return value of the function _will not be displayed automatically_, 
# * You can display a value inside the function with a call to `IPython.display.display`
# * You will also be using `display` twice
#   1. For displaying the value
#   2. For displaying the widget

# Using `display` to display the elements

# In[ ]:


from IPython.display import display
def my_adder(a, b):
    display("the result of %d and %d is %d" % (a, b,  a + b))
    return a+b


# In[ ]:


from ipywidgets import interactive
w = interactive(my_adder, a=10, b=20)
display(w)


# ### Retaining the state of the `widget`
# 
# What is interesting about the reference to the widget is that it will maintain the state of the values

# In[ ]:


print(w.kwargs)


# It also holds the result of the interaction

# In[ ]:


print(w.result)


# ## Manual interaction
# 
# In case the evaluation takes a lot of time, you can use `interact_manual` to specify when it is being evaluated.
# 
# Here is a slow function where we are evaluating the time using a "magic command" called `%timeit`

# In[ ]:


from time import sleep
def slow_function(i):
    print('Given a value of %d' % i)
    sleep(2.5)
    print('Slept for 2.5 seconds')
    return


# In[ ]:


get_ipython().run_line_magic('timeit', 'slow_function(1e6)')


# Here is the slow function if we were to run an interact with it, notice how slow it becomes every time we decide to move the slider. Notice the hour glass favicon in your tab, or listen to the computer fan.  

# In[ ]:


interact(slow_function,i=widgets.FloatSlider(min=1e5, max=1e7, step=1e5));


# `interact_manual` gives you the opportunity to update whenever you require it and will not do so automatically

# In[ ]:


from ipywidgets import interact_manual
interact_manual(slow_function,i=widgets.FloatSlider(min=1e5, max=1e7, step=1e5));


# ## Continuous Update
# 
# Continuous Update is an addition `kwargs` (extra python argument) that will determine whether it will calculated on all mouse movements, not just mouse releases. When set to `False` it will only update with a mouse release

# `continuous_update` is set to `False` thus _only_ listening to mouse release events not movement.

# In[ ]:


interact(slow_function,i=widgets.FloatSlider(min=1e5, max=1e7, step=1e5, continuous_update=False));


# ## Interactive Output
# 
# * `interactive_output` does not generate a user interface for the widgets. 
# * You can connect widget controls to a function
# * Gives you more control over the widget and its layout. 

# In[ ]:


a = widgets.IntSlider()
b = widgets.IntSlider()
c = widgets.IntSlider()

#Horizontal Box
ui = widgets.HBox([a, b, c]) 

def f(a, b, c):
    print((a, b, c))

out = widgets.interactive_output(f, {'a': a, 'b': b, 'c': c})

#Nothing happens until we do a display
display(ui, out)


# ## `link`
# 
# `link` can be used to tie two widgets together.

# In[ ]:


a = widgets.FloatText()
b = widgets.FloatSlider()
display(a,b)

mylink = widgets.link((a, 'value'), (b, 'value'))


# ## `jslink`
# 
# `jslink` can be used to tie two widgets together. This is browser level and doesn't involve sending information back to the kernel.

# In[ ]:


a = widgets.FloatText()
b = widgets.FloatSlider()
display(a,b)

mylink = widgets.jslink((a, 'value'), (b, 'value'))


# ### Widgets and $LaTeX$

# In[ ]:


widgets.IntSlider(description=r'\(\int_0^t f\)')


# In[ ]:


from ipywidgets import Label
Label(value=r'\(e=mc^2\)')


# ## Interesting Widgets
# 
# There are many standard widgets such as `IntSlider`, `FloatSlider`. There are some other interesting ones as well.

# ### `DatePicker` 
# 
# Note: Not available in Safari

# In[ ]:


import datetime
w = widgets.DatePicker(
    description='Pick a Date',
    disabled=False
)
w.value = datetime.datetime.now()

display(w)


# ### `ColorPicker`

# In[ ]:


w = widgets.ColorPicker(
    concise=False,
    description='Pick a color',
    value='pink',
    disabled=False
)
display(w)


# ## Widgets Layouts
# 
# All widgets have a CSS style layout elements that impact the look and feel of these widgets where dashes are replaced by underscores.

# In[ ]:


from ipywidgets import Button, Layout

b = Button(description='(50% width, 80px height) button',
           layout=Layout(width='50%', height='80px'))
b


# Layout can be used as a reference, in the following example `b.layout` is using the same layout as the `b` widget above

# In[ ]:


Button(description='Another button with the same layout', layout=b.layout)


# ### Descriptions too long
# 
# Styles can be adjusted if the descriptions are too long

# In[ ]:


from ipywidgets import IntSlider

IntSlider(description='A too long description')


# In[ ]:


style = {'description_width': 'initial'}
IntSlider(description='A too long description', style=style)


# Using `Label` directly and place it in an `HBox` layout can show full customization.

# In[ ]:


from ipywidgets import HBox, Label

HBox([Label('A too long description'), IntSlider()])


# ## Layouts
# 
# ### `Box`, `HBox` and `VBox`
# 
# Natural sizes, and arrangements using `HBox` and `VBox`
# Most of the core-widgets have default heights and widths that tile well together. This allows simple layouts based on the `HBox` and `VBox` helper functions to align naturally

# In[ ]:


from ipywidgets import Button, HBox, VBox

words = ['Andorra', 'Bolivia', 'Bangladesh', 'Cambodia']
items = [Button(description=w) for w in words]
left_box = VBox([items[0], items[1]])
right_box = VBox([items[2], items[3]])
HBox([left_box, right_box])


# ### `Flexbox`
# 
# `Flexbox` is modeled after the CSS Flexbox design. Where different flows can be created
# 
# https://css-tricks.com/snippets/css/a-guide-to-flexbox/
# 

# In[ ]:


from ipywidgets import Button, HBox, VBox, Box

words = ['Andorra', 'Bolivia', 'Bangladesh', 
         'Cambodia', 'Mexico', 'Canada', 
         'Japan', 'South Africa']

buttons = [Button(description=w) for w in words]

buttons_layout = Layout(width='auto')

box_layout = Layout(display='flex',
                    flex_flow='column',
                    align_items='stretch',
                    border='solid',
                    border_width='1px',
                    width='50%')

items = [Button(description=word, 
                layout=buttons_layout, 
                button_style='success') for word in words]

box = Box(children=items, layout=box_layout)
box

