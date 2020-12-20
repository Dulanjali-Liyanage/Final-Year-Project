#!/usr/bin/env python
# coding: utf-8

# In[1]:


from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd
import numpy as np
import math


# In[4]:


match_data = pd.read_csv('pak_data.csv')


# In[5]:


match_data.head()


# In[6]:


del match_data["Day_Night"]
del match_data["Home"]
del match_data["Bat"]
del match_data["Toss"]
del match_data["Opposition"]


# In[7]:


match_data


# In[8]:


# convert our pandas dataframe into a list of lists,
player_combo = [] #list of lists match players and result
for i in range(0, 94):
    rowItem = []
    for j in range(0, 12):
        rowItem.append(str(match_data.values[i,j]))
    player_combo.append(rowItem)


# In[9]:


#Creating the dataframe of frequent itemsets
te = TransactionEncoder()
te_ary = te.fit(player_combo).transform(player_combo)
match_df_freq = pd.DataFrame(te_ary, columns=te.columns_)


# In[10]:


match_sup = apriori(match_df_freq, min_support=0.1,use_colnames=True)
print(match_sup)


# In[11]:


rules= association_rules(match_sup, metric="lift", min_threshold=1)


# In[12]:


rules


# In[13]:


won_rules = rules[(rules['consequents'] == {"won"})]


# In[14]:


won_rules


# In[15]:


won_rules = won_rules[(won_rules['antecedents'].str.len() > 1)] #Here won_rules['antecedents'] is a frozenset


# In[16]:


won_rules


# In[17]:


won_rules.to_csv('pak_won_rules.csv')


# In[ ]:




