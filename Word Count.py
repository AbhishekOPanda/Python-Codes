
# ### Finish the function countWords(l), which takes in a list l. This function DOES NOTmodify l.#The function then returns the words' frequencies as a list

# In[1]:


def countWords(l):
    wordfreq = []
    return list(map(lambda w: l.count(w),l))


# In[2]:


countWords(['hey', 'hi', 'Mark', 'hi', 'mark'])

