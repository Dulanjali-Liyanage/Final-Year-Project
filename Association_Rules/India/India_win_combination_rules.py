#!/usr/bin/env python
# coding: utf-8

# In[1]:


from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd
import numpy as np
import math


# In[2]:


match_data = pd.read_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Association_Rules/India/India_data.csv')


# In[3]:


#print the dataset
match_data.head()


# In[4]:


del match_data["Day_Night"]
del match_data["Home"]
del match_data["Bat"]
del match_data["Toss"]
del match_data["Opposition"]


# In[6]:


#print the dataset
match_data


# In[7]:


# convert our pandas dataframe into a list of lists,
player_combo = [] #list of lists match players and result
for i in range(0, 112):
    rowItem = []
    for j in range(0, 12):
        rowItem.append(str(match_data.values[i,j]))
    player_combo.append(rowItem)


# In[8]:


print(player_combo)


# In[9]:


#Creating the dataframe of frequent itemsets
te = TransactionEncoder()
te_ary = te.fit(player_combo).transform(player_combo)
match_df_freq = pd.DataFrame(te_ary, columns=te.columns_)


# In[10]:


#Define the minimum support and obtain the itemsets greater than the min support
#support = No. of times the required itemset occured / total no. of matches
match_sup = apriori(match_df_freq, min_support=0.1,use_colnames=True)
print(match_sup)


# In[11]:


#generate association rules
rules= association_rules(match_sup, metric="lift", min_threshold=1)


# In[12]:


#print the association rules
rules


# In[13]:


#extract only the combinations occured at a winning match
won_rules = rules[(rules['consequents'] == {"won"})]


# In[14]:


won_rules


# In[15]:


#remove the one itemsets
#obtain the final winning combinations
won_rules = won_rules[(won_rules['antecedents'].str.len() > 1)] #Here won_rules['antecedents'] is a frozenset


# In[16]:


#print the winning combinations
won_rules


# In[17]:


#select all the rules where antecedent contains 'RG Sharma'
#won_rules[(won_rules['antecedents'].apply(lambda x: 'RG Sharma' in str(x)))]


# In[18]:


won_rules.to_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Association_Rules/India/won_rules.csv')


# In[ ]:




