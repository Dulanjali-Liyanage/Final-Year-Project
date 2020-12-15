#!/usr/bin/env python
# coding: utf-8

# In[62]:


from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd
import numpy as np
import math


# In[63]:


match_data = pd.read_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Association_Rules/India/India_data.csv')


# In[64]:


#print the dataset
match_data.head()


# In[65]:


del match_data["Home"]
del match_data["Bat"]
del match_data["Toss"]
del match_data["Opposition"]


# In[66]:


match_data


# In[67]:


match_data['Day_Night'].unique()
#there can be 'N' also in some matches


# In[68]:


# convert our pandas dataframe into a list of lists,
player_combo = [] #list of lists match players and result
for i in range(0, 112):
    rowItem = []
    for j in range(0, 13):
        rowItem.append(str(match_data.values[i,j]))
    player_combo.append(rowItem)


# In[69]:


print(player_combo)


# In[70]:


#Creating the dataframe of frequent itemsets
te = TransactionEncoder()
te_ary = te.fit(player_combo).transform(player_combo)
match_df_freq = pd.DataFrame(te_ary, columns=te.columns_)


# In[71]:


match_df_freq


# In[72]:


#Frequent items sets with D
#match_df_freq = match_df_freq[match_df_freq.D == True]
#match_df_freq = match_df_freq[match_df_freq.won == True]


# In[73]:


#match_df_freq


# In[74]:


#Define the minimum support and obtain the itemsets greater than the min support
#support = No. of times the required itemset occured / total no. of matches
match_sup = apriori(match_df_freq, min_support=0.1,use_colnames=True)
match_sup


# In[75]:


#generate association rules
rules= association_rules(match_sup, metric="lift", min_threshold=1)


# In[76]:


#print the association rules
rules


# In[77]:


#extract only the combinations occured at a winning match
won_rules = rules[(rules['consequents'] == {"won"})]


# In[78]:


won_rules


# In[79]:


#remove the two itemsets
won_rules = won_rules[(won_rules['antecedents'].str.len() > 2)] #Here won_rules['antecedents'] is a frozenset


# In[80]:


#print the winning combinations
won_rules


# In[81]:


#select all the rules where antecedent contains 'D'
#won_rules[(won_rules['antecedents'].apply(lambda x: 'D' in str(x)))]


# In[82]:


won_rules.values[0,:]


# In[83]:


#finding winning combinatios when match is played Day and Night
col_names = ["antecedents","consequents","antecedent support","consequent support","support","confidence","lift","leverage","conviction"]
DN_won_rules = pd.DataFrame(columns = col_names)

i = 0
for x in won_rules['antecedents']:
    for y in x:
        if y == 'DN':
            #print(won_rules.values[i,0])
            DN_won_rules = DN_won_rules.append({'antecedents':won_rules.values[i,0],"consequents":won_rules.values[i,1],"antecedent support":won_rules.values[i,2],"consequent support":won_rules.values[i,3],"support":won_rules.values[i,4],"confidence":won_rules.values[i,5],"lift":won_rules.values[i,6],"leverage":won_rules.values[i,7],"conviction":won_rules.values[i,8]},ignore_index=True)
    i = i + 1


# In[84]:


DN_won_rules


# In[85]:


DN_won_rules.to_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Association_Rules/India/DN_won_rules.csv')


# In[86]:


#finding winning combinatios when match is played Day
col_names = ["antecedents","consequents","antecedent support","consequent support","support","confidence","lift","leverage","conviction"]
D_won_rules = pd.DataFrame(columns = col_names)

i = 0
for x in won_rules['antecedents']:
    for y in x:
        if y == 'D':
            #print(won_rules.values[i,0])
            D_won_rules = D_won_rules.append({'antecedents':won_rules.values[i,0],"consequents":won_rules.values[i,1],"antecedent support":won_rules.values[i,2],"consequent support":won_rules.values[i,3],"support":won_rules.values[i,4],"confidence":won_rules.values[i,5],"lift":won_rules.values[i,6],"leverage":won_rules.values[i,7],"conviction":won_rules.values[i,8]},ignore_index=True)
    i = i + 1


# In[87]:


D_won_rules#no rules


# In[88]:


D_won_rules.to_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Association_Rules/India/D_won_rules.csv')


# In[89]:


#finding winning combinatios when match is played Night
col_names = ["antecedents","consequents","antecedent support","consequent support","support","confidence","lift","leverage","conviction"]
N_won_rules = pd.DataFrame(columns = col_names)

i = 0
for x in won_rules['antecedents']:
    for y in x:
        if y == 'N':
            #print(won_rules.values[i,0])
            N_won_rules = N_won_rules.append({'antecedents':won_rules.values[i,0],"consequents":won_rules.values[i,1],"antecedent support":won_rules.values[i,2],"consequent support":won_rules.values[i,3],"support":won_rules.values[i,4],"confidence":won_rules.values[i,5],"lift":won_rules.values[i,6],"leverage":won_rules.values[i,7],"conviction":won_rules.values[i,8]},ignore_index=True)
    i = i + 1


# In[90]:


N_won_rules#no rules since India has not played Night matches from 2015 to 2020


# In[91]:


N_won_rules.to_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Association_Rules/India/N_won_rules.csv')


# In[ ]:




