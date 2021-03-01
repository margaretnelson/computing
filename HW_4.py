#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Question 1
import numpy as np
np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])


# In[15]:


# Question 2, part I
x_integer_array = np.arange(1, 7)
type(x_integer_array)
x_integer_array


# In[14]:


# Question 2, part II
y_integer_array = np.arange(5, 11)
type(y_integer_array)
y_integer_array


# In[16]:


# Question 3
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 2, 3, 4, 5, 6])
ypoints = np.array([ 5,  6,  7,  8,  9, 10])

plt.plot(xpoints, ypoints)
plt.show()


# In[23]:


# Question 4
import matplotlib.pyplot as plt
import numpy as np

x = np.array([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0])
y1 = np.array([1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0])
y2 = np.array([5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0])
y3 = np.array([9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0])

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
               
plt.xlabel("X Label")
plt.ylabel("Y Label")

plt.show()


# In[27]:


# Question 5
import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22])

plt.subplot(2, 2, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([1, 20, 2, 18, 3, 17, 4, 16, 5, 15, 4])

plt.subplot(2, 2, 2)
plt.plot(x,y)

#plot 3:
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([20, 10, 18, 5, 19, 3, 19, 5, 18, 10, 20])

plt.subplot(2, 2, 3)
plt.plot(x,y)

#plot 4:
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([1, 5, 3, 7, 2, 9, 3, 11, 4, 13, 5])

plt.subplot(2, 2, 4)
plt.plot(x,y)

plt.show()


# In[ ]:




