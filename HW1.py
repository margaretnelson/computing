#!/usr/bin/env python
# coding: utf-8

# In[6]:


colors = ["teal","yellow", "periwinkle"]
print(colors)


# In[4]:


nums = list(range(30, 60, 3))
print(type(nums))
print(nums)


# In[8]:


dictionary = {"Sunny": "play", "Rainy": "watching TV", "Cloudy": "walk"}
print(type(dictionary))
print(dictionary)


# In[9]:


dictionary.update({"snowy": "ski"})
print(dictionary)


# In[34]:


score = 82
if score>=90:
    print('A')
elif score>=80 and score<90:
    print('B')
elif score>=70 and score<80:
    print('C')
else: 
    print('F')


# In[ ]:




