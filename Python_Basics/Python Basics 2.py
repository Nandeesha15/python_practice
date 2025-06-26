#!/usr/bin/env python
# coding: utf-8

# # 0. Variables

# In[1]:


space_name = 'Nandish'


# In[3]:


print(space_name)


# In[4]:


type(space_name)


# # 1. Data Types

# In[9]:


# declaring a variable as a string
a = "Nandish"
print(a)
type(a)


# In[8]:


# declaring a variable as a int
a = 10
print(a)
type(a)


# In[7]:


# declaring a variable as a float
a = 10.23
print(a)
type(a)


# In[10]:


# declaring a variable as a boolean
a = True
print(a)
type(a)


# In[2]:


# declaring a variable as a tuple
a = (10,20,30.233,40.312)
print(a)
type(a)

b = {"nandish","karan","sumanth"}
print(b)
type(b)


# In[4]:


# declaring a variable as a list//mutable
b = [10,20,30.233,40.312,10,20,30]
print(b)
type(b)



# In[ ]:


# declaring a variable as a tuple //immutable
a = (10,20,30.233,40.312)
print(a)
type(a)

b = {"nandish","karan","sumanth"}
print(b)
type(b)


# In[1]:


# declaring a variable as a set //immutable
a = {10,20,30.233,40.312}
print(a)
type(a)



# In[6]:


# typecasting list to set and back to list to remove dublicates
list(set(b))


# In[10]:


# declaring a variable as a dictionary //immutable
a = {'name':'nandish','age':19,'fav_color':'red'}
print(a)
type(a)



# # 2. Lists
# 

# In[11]:


#create
names = ["nandish","karan","karthik","sumanth","anjan"]


# In[15]:


#read
names


# In[14]:


# reading using indexing
names[0]


# In[16]:


names[-1]


# In[18]:


len(names)


# In[20]:


#update
names[-1] = "ruhan"
names


# In[22]:


#add value to list 
names.append("anjan")
names


# In[24]:


# add at specific place 
names.insert(2,"amogh")
names


# In[29]:


#delete
del names[-1]
names


# # 3. Dictionaries

# In[4]:


#create
employees = {
    'name':'nandish',
    'age':10,
    'gender':'male' }



# In[5]:


#read
employees


# In[6]:


employees['age']


# In[7]:


employees.keys()


# In[9]:


#update
employees['age'] = 10
employees



# In[10]:


employees['fav_fruit'] = 'mango'
employees


# In[20]:


#delete
del employees['gender']


# In[21]:


employees


# In[ ]:




