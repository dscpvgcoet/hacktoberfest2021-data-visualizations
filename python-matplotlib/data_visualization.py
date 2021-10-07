#!/usr/bin/env python
# coding: utf-8

# # Sine,Cosine Curve-Multiplot

# In[6]:


import matplotlib.pyplot as plt
import numpy as np
import math
x=np.arange(0, math.pi*2, 0.05)
fig=plt.figure()
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes
axes2 = fig.add_axes([0.55, 0.55, 0.3, 0.3]) # inset axes
y=np.sin(x)
axes1.plot(x, y, 'b')
axes2.plot(x,np.cos(x),'r')
axes1.set_title('sine')
axes2.set_title("cosine")
plt.show()


# advertisement expenses and sales figures of TV and
# smartphone in the form of line plots. Line representing TV is a solid line with yellow colour
# and square markers whereas smartphone line is a dashed line with green colour and circle
# marker

# In[7]:


import matplotlib.pyplot as plt
y = [1, 4, 9, 16, 25,36,49, 64]
x1 = [1, 16, 30, 42,55, 68, 77,88]
x2 = [1,6,12,18,28, 40, 52, 65]
fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
l1=ax.plot(x1,y,'ys-') # solid line with yellow colour and square marker
l2=ax.plot(x2,y,'go--') # dash line with green colour and circle marker
ax.legend(labels=('tv', 'Smartphone'), loc='lower right') 
ax.set_title("Advertisement effect on sales")
ax.set_xlabel('medium')
ax.set_ylabel('sales')
plt.show()


# # Barplot

# Following is a simple example of the Matplotlib bar plot. It shows the number of students
# enrolled for various courses offered at an institute

# In[8]:


import matplotlib.pyplot as plt
fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
langs=['C', 'C++', 'Java', 'Python', 'PHP']
students=[23,17,35,29,12]
ax.bar(langs,students)
plt.show()


# In[ ]:




