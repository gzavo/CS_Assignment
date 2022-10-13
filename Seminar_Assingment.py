#!/usr/bin/env python
# coding: utf-8

# In[4]:


import matplotlib.pyplot as plt
import pandas as pd


# In[25]:


data = pd.read_csv('istherecorrelation.csv',sep=";")
data.head()


# In[28]:


df = pd.DataFrame(data)
col_one = df['Year'].tolist()
col_two = df['WO [x1000]'].tolist()
col_three = df['NL Beer consumption [x1000 hectoliter]'].tolist()


# In[32]:


plt.plot(col_one,col_three)
plt.xlabel('Years')
plt.ylabel('NL Beer consumption [x1000 hectoliter] ')


# In[ ]:




