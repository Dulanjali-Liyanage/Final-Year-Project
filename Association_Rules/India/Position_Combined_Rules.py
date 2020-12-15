#!/usr/bin/env python
# coding: utf-8

# In[71]:


from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd
import numpy as np
import math


# In[72]:


match_data = pd.read_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Association_Rules/India/india_position.csv')


# In[73]:


#print the dataset
match_data.head()


# In[74]:


del match_data["p1"]
del match_data["p2"]
del match_data["p3"]
del match_data["p4"]
del match_data["p5"]
del match_data["p6"]
del match_data["p7"]
del match_data["p8"]
del match_data["p9"]
del match_data["p10"]
del match_data["p11"]


# In[75]:


match_data
#here * --> means position 10 and #--> means position 11


# In[76]:


# convert our pandas dataframe into a list of lists,
player_combo = [] #list of lists match players and result
for i in range(0, 112):
    rowItem = []
    for j in range(0, 12):
        rowItem.append(str(match_data.values[i,j]))
    player_combo.append(rowItem)


# In[77]:


print(player_combo)


# In[78]:


#Creating the dataframe of frequent itemsets
te = TransactionEncoder()
te_ary = te.fit(player_combo).transform(player_combo)
match_df_freq = pd.DataFrame(te_ary, columns=te.columns_)


# In[79]:


#Define the minimum support and obtain the itemsets greater than the min support
#support = No. of times the required itemset occured / total no. of matches
match_sup = apriori(match_df_freq, min_support=0.1,use_colnames=True)
print(match_sup)


# In[80]:


#generate association rules
rules= association_rules(match_sup, metric="lift", min_threshold=1)


# In[81]:


#print the association rules
rules


# In[82]:


#extract only the combinations occured at a winning match
won_rules = rules[(rules['consequents'] == {"won"})]


# In[83]:


won_rules


# In[84]:


#remove the one itemsets
#obtain the final winning combinations
won_rules = won_rules[(won_rules['antecedents'].str.len() > 1)] #Here won_rules['antecedents'] is a frozenset


# In[85]:


#print the winning combinations
won_rules


# In[86]:


#finding winning combinatios with positions
#removing same player combinations because of different postions
#example: remvove antecedents with [V Kohli3,V Kohli5]
col_names = ["antecedents","consequents","antecedent support","consequent support","support","confidence","lift","leverage","conviction"]
position_won_rules = pd.DataFrame(columns = col_names)

i = 0
for x in won_rules['antecedents']:
    itemDup = [] # can have duplicates
    itemSet = set() #without duplicates
    for y in x:
        y[:-1]#remove the last letter from the string
        itemDup.append(y)
        itemSet.add(y)
        
    if len(itemDup) == len(itemSet):
        position_won_rules = position_won_rules.append({'antecedents':won_rules.values[i,0],"consequents":won_rules.values[i,1],"antecedent support":won_rules.values[i,2],"consequent support":won_rules.values[i,3],"support":won_rules.values[i,4],"confidence":won_rules.values[i,5],"lift":won_rules.values[i,6],"leverage":won_rules.values[i,7],"conviction":won_rules.values[i,8]},ignore_index=True)
    i = i + 1


# In[87]:


position_won_rules


# In[88]:


position_won_rules.to_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Association_Rules/India/position_won_rules.csv')

