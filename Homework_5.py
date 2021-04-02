#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Question 1
class Clock():
    def __init__(self, time):
        self.time = time
    def print_time(self):
        time = '6:30'
        print(self.time)
        
clock = Clock('5:30')
clock.print_time()


# In[6]:


# Question 2
class Clock():
    def __init__(self, time):
        self.time = time
    def print_time(self, time):
        print(time)

clock = Clock('5:30')
clock.print_time('10:30')


# In[28]:


# Question 3
class Clock():
    def __init__(self, time):
        self.time = time
    def print_time(self):
        print(self.time)
        
class Clock1(Clock):
    pass

boston_clock = Clock('5:30')
paris_clock = Clock1('10:30')

boston_clock.print_time()
paris_clock.print_time()


# In[47]:


# Question 4
class Queue():
    def __init__(self):
        self.line = []
    def print(self):
        print(self.line)
    def insert(self, k):
        self.line.append(k)
    def remove(self):
        try:
            result = self.line.pop(0)
        except:
            return 'queue is empty now'
    

queue = Queue()
queue.insert(5)
queue.insert(6)
queue.print()

queue.insert(7)
queue.remove()
queue.print()

queue.remove()
queue.remove()
queue.remove()


# In[ ]:




