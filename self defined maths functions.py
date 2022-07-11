#!/usr/bin/env python
# coding: utf-8

# In[1]:


from cs515 import map, reduce


# ### Que 1 :Write a factorial function

# In[2]:


def factorial(n):
    if n<0:
        return ("Error, No factorial possible")
    elif n==0:
        return 1
    else:
        if n==1:
            return n
        else:
            return n*factorial(n-1)


# In[3]:


factorial(5)


# In[4]:


factorial(0)


# In[5]:


factorial(-1)


# ### Question 2: Write a mean function

# In[6]:


def mean(L):
    return reduce(lambda x, y: x + y, L)/float(len(L))


# In[7]:


mean([1,1,1])


# In[8]:


mean([1,1,2,2])


# ### Question 3: Testing for Prime Numbers

# In[9]:


def divides(n):
    def div(k):
        return n % k == 0
    return div


# In[10]:


def prime(n):
    if n==1:
        return True
    elif sum(map(divides(n),range (2,(n-1)))) == 0:
        return True
    else:
        return False


# In[11]:


prime(23)


# In[12]:


prime(1)


# In[13]:


prime(20)


# ### Question 4: All Primes up to N

# In[14]:


def allPrimes(n):
    a=[]
    for i in range (1,n+1):
        if i==1:
            a.append(i)
        elif sum(map(divides(i),range (2,i))) != 0:
            pass
        else:
            a.append(i)
    return a


# In[15]:


allPrimes(23)


# In[16]:


allPrimes(20)

