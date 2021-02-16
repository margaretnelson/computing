#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Question 0
marks = {'Andy':88, 'Amy':66, 'James':90, 'Jules':55, 'Arthur':77}
marks


# In[7]:


# Question 1
for student, marks in marks.items():
    print(f' {student} {marks}')


# In[8]:


# Question 2
marks = [88, 66, 90, 55, 77]
def marks_sum(marks):
    total = 0
    for mark in marks:
        total += mark
    return total
def marks_mean(marks):
    return marks_sum(marks) / float(len(marks))
print("The students' mean grade is:", marks_mean(marks))
print("The students' maximum grade is:", max(marks))
print("The students' minimal grade is:", min(marks))


# In[9]:


# Question 3
for marks in ['Andy', 'Amy', 'James', 'Jules', 'Arthur']:
    if 'J' in marks:
        break
    print(marks)


# In[12]:


# Question 4
for marks in ['Andy', 'Amy', 'James', 'Jules', 'Arthur']:
    if 'J' in marks:
        continue
    print(marks)


# In[13]:


# Question 5
def print_student (student_name):
    marks = {'Andy':88, 'Amy':66, 'James':90, 'Jules':55, 'Arthur':77}
    for student in marks:
        if student == student_name:
            print(marks[student])
            break
    else:
        print("Cannot find student's name.")

print_student("James")
print_student("Kevin")


# In[ ]:




