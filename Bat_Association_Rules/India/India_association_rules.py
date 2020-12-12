#!/usr/bin/env python
# coding: utf-8

# In[122]:


from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd
import numpy as np
import math


# In[123]:


match_data = pd.read_csv('E:University Works/4th Year/Semester 8/CO425 - Final Year Project 2/india_rules_02.csv',header=None)


# In[124]:


#remove the first row of the dataset
match_data = match_data.iloc[1:]


# In[125]:


#print the dataset
match_data


# In[126]:


# convert our pandas dataframe into a list of lists,
player_combo = [] #list of lists match players and result
for i in range(1, 112):
    rowItem = []
    for j in range(0, 11):
        rowItem.append(str(match_data.values[i,j]))
    player_combo.append(rowItem)


# In[127]:


#print(player_combo)


# In[128]:


#Creating the dataframe of frequent itemsets
te = TransactionEncoder()
te_ary = te.fit(player_combo).transform(player_combo)
match_df_freq = pd.DataFrame(te_ary, columns=te.columns_)


# In[129]:


#Define the minimum support and obtain the itemsets greater than the min support
#support = No. of times the required itemset occured / total no. of matches
match_sup = apriori(match_df_freq, min_support=0.4,use_colnames=True)
print(match_sup)


# In[130]:


#generate association rules
rules= association_rules(match_sup, metric="lift", min_threshold=1)


# In[131]:


#print the association rules
rules


# In[132]:


#extract only the combinations occured at a winning match
won_rules = rules[(rules['consequents'] == {"won"})]


# In[133]:


won_rules


# In[134]:


#remove the one itemsets
#obtain the final winning combinations
won_rules = won_rules[(won_rules['antecedents'].str.len() > 1)] #Here won_rules['antecedents'] is a frozenset


# In[135]:


#print the winning combinations
won_rules


# In[ ]:




