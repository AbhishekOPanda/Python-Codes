
# coding: utf-8

# ##### 1. Write two functions that can achieve the conversion between Fahrenheit and Centigrade 
# To convert temperatures in degrees Fahrenheit to Celsius, subtract 32 and multiply by .5556 (or 5/9). 
# 
# To convert temperatures in degrees Celsius to Fahrenheit, multiply by 1.8 (or 9/5) and add 32. 
# 
# Name your functions as ‘CtoF’ and ‘FtoC’.
# 
# 
# Check your function by converting the 0 Centigrade into Fahrenheit then convert it back. 0°C  ->  32°F  -> 0°C

# In[1]:


import math


# In[2]:


def CtoF(num):
    return (num*1.8)+32


# In[3]:


def FtoC(num):
    return (num-32)*(5/9)


# In[4]:


a=CtoF(0)
print a


# In[5]:


FtoC(a)


# #### 2. Define a function addTwoNumbers that takes two numbers as input and return the sum of them (a + b) 

# In[6]:


def addTwoNumbers(a,b):
    return a+b


# In[7]:


print(addTwoNumbers(5,6))


# #### 3.  Define a function multiplyTwoNumbers that takes two numbers as input and return the product of them (a * b) 

# In[8]:


def multiplyTwoNumbers(a,b):
    return a*b


# In[9]:


print( multiplyTwoNumbers(5,6))


# #### 4.  Write a function calculate that takes in a number a  that uses the above functions to do  a^2 + 2. 

# In[10]:


def calculate(a):
    return multiplyTwoNumbers(a,a) + 2


# In[11]:


print( calculate(2))


# In[12]:


print(calculate(3))


# another way

# In[13]:


def calculate1(a):
    return a**2 + 2


# In[14]:


print( calculate1(2))


# In[15]:


print(calculate1(3))

