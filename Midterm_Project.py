#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Question 1

def count_frequency(dict): 
    # creat an empty dictionary
    freq = {} 
    for item in dict: 
        if (item in freq): 
            freq[item] += 1
        else: 
            freq[item] = 1
  
    for key, value in freq.items(): 
        print ("% d : % d"%(key, value)) 
    print('Explanation:')
    for key, value in freq.items(): 
        print('Here % d occurs % d times'%(key, value))
  
if __name__ == "__main__":  
    dict = [2,4,6,8,4,5,2,1,9,0,4,6,7,4,3,2,1,9,10,3,7,9,6,0,1,3,5,6,7,8,9,10,2,3,6,8,9,10,6,7,4,3]

    count_frequency(dict) 
    
# Bar Graph code
import matplotlib.pyplot as plt
import numpy as np

dict = [2,4,6,8,4,5,2,1,9,0,4,6,7,4,3,2,1,9,10,3,7,9,6,0,1,3,5,6,7,8,9,10,2,3,6,8,9,10,6,7,4,3]
freq = {} 
for item in dict: 
    if (item in freq): 
        freq[item] += 1
    else: 
        freq[item] = 1 
keys = freq.keys()
values = freq.values()
plt.bar(keys, values)
plt.title("Frequencies")

# Store dictionary results in JSON
import json

# a Python object (dict):
dict = [2,4,6,8,4,5,2,1,9,0,4,6,7,4,3,2,1,9,10,3,7,9,6,0,1,3,5,6,7,8,9,10,2,3,6,8,9,10,6,7,4,3]
freq = {} 
for item in dict: 
    if (item in freq): 
        freq[item] += 1
    else: 
        freq[item] = 1

# convert into JSON:
y = json.dumps(freq, indent = 4)

# output JSON
with open("./output.json", "w") as out:
    json.dump(freq, out)

# the result is a JSON string:
print(y)


# In[3]:


# Start of Question 2: Choice 1

import pandas as pd

df = pd.read_json('your_posts_1.json')
df.head(3)


# In[4]:


# rename the timestamp column
df.rename(columns={'timestamp': 'date'}, inplace=True)

#drop some unnecessary columns
df = df.drop(['attachments', 'title', 'tags'], axis=1)

# making sure it's datetime format
pd.to_datetime(df['date'])

df.head(3)


# In[5]:


print(df.shape)
df.tail(3)


# In[6]:


# Monthly posts
df = df.set_index('date')
post_counts = df['data'].resample('MS').size()
post_counts


# In[7]:


# Visualize FaceBook data
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# rename the data column
df.rename(columns={'data': 'Number of Posts'}, inplace=True)

# set figure size and font size
sns.set(rc={'figure.figsize':(40,20)})
sns.set(font_scale=3)

# set x labels
x_labels = post_counts.index

#create bar plot
sns.barplot(x_labels, post_counts, color="green")

# only show x-axis labels for Jan 1 of every other year
tick_positions = np.arange(10, len(x_labels), step=24)

#reformat date to display year onlyplt.ylabel("post counts")
plt.xticks(tick_positions, x_labels[tick_positions].strftime("%Y"))

#plot title
plt.title('My Monthly Facebook Posts')

# display the plot
plt.show()


# In[ ]:




