#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as nm  
import matplotlib.pyplot as mtp  
import pandas as pd  


# In[31]:


dataset1= pd.read_csv('mavoix_ml_sample_dataset.csv')  


# In[32]:


x = dataset1.iloc[:,2:14].values 


# In[33]:


dataset1


# In[34]:


x


# In[40]:


from sklearn.cluster import AgglomerativeClustering
cluster = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='ward')  
y=cluster.fit_predict(x)


# In[39]:


cluster


# In[41]:


y


# In[ ]:




