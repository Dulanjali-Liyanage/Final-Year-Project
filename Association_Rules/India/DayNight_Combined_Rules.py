#!/usr/bin/env python
# coding: utf-8

# In[37]:


from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd
import numpy as np
import math


# In[38]:


match_data = pd.read_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Association_Rules/India/India_data.csv')


# In[39]:


#print the dataset
match_data.head()


# In[40]:


del match_data["Home"]
del match_data["Bat"]
del match_data["Toss"]
del match_data["Opposition"]


# In[41]:


match_data


# In[42]:


match_data['Day_Night'].unique()
#there can be 'N' also in some matches


# In[43]:


# convert our pandas dataframe into a list of lists,
player_combo = [] #list of lists match players and result
for i in range(0, 112):
    rowItem = []
    for j in range(0, 13):
        rowItem.append(str(match_data.values[i,j]))
    player_combo.append(rowItem)


# In[44]:


print(player_combo)


# In[45]:


#Creating the dataframe of frequent itemsets
te = TransactionEncoder()
te_ary = te.fit(player_combo).transform(player_combo)
match_df_freq = pd.DataFrame(te_ary, columns=te.columns_)


# In[46]:


match_df_freq


# In[47]:


#Frequent items sets with D
#match_df_freq = match_df_freq[match_df_freq.D == True]
#match_df_freq = match_df_freq[match_df_freq.won == True]


# In[48]:


#match_df_freq


# In[49]:


#Define the minimum support and obtain the itemsets greater than the min support
#support = No. of times the required itemset occured / total no. of matches
match_sup = apriori(match_df_freq, min_support=0.1,use_colnames=True)
match_sup


# In[50]:


#generate association rules
rules= association_rules(match_sup, metric="lift", min_threshold=1)


# In[51]:


#print the association rules
rules


# In[52]:


#extract only the combinations occured at a winning match
won_rules = rules[(rules['consequents'] == {"won"})]


# In[53]:


won_rules


# In[54]:


#remove the two itemsets
won_rules = won_rules[(won_rules['antecedents'].str.len() > 2)] #Here won_rules['antecedents'] is a frozenset


# In[55]:


#print the winning combinations
won_rules


# In[56]:


#select all the rules where antecedent contains 'D'
#won_rules[(won_rules['antecedents'].apply(lambda x: 'D' in str(x)))]


# In[57]:


won_rules.values[0,:]


# In[58]:


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


# In[59]:


DN_won_rules


# In[60]:


#sorting by confidence --- descending order
DN_won_rules.sort_values(by ='confidence', ascending = False, inplace = True)


# In[61]:


DN_won_rules


# In[62]:


#sorting by support --- descending order
DN_won_rules.sort_values(by ='support', ascending = False, inplace = True)


# In[63]:


DN_won_rules


# In[64]:


import random
import matplotlib.pyplot as plt

support=DN_won_rules['support']
confidence=DN_won_rules['confidence']
 
plt.scatter(support, confidence,marker="*")
plt.xlabel('support')
plt.ylabel('confidence') 
plt.show()


# In[65]:


DN_won_rules.to_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Association_Rules/India/DN_won_rules.csv')


# In[66]:


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


# In[67]:


D_won_rules


# In[68]:


#sorting by confidence --- descending order
D_won_rules.sort_values(by ='confidence', ascending = False, inplace = True)


# In[69]:


D_won_rules


# In[70]:


#sorting by support --- descending order
D_won_rules.sort_values(by ='support', ascending = False, inplace = True)


# In[71]:


D_won_rules


# In[72]:


import random
import matplotlib.pyplot as plt

support=D_won_rules['support']
confidence=D_won_rules['confidence']
 
plt.scatter(support, confidence,marker="*")
plt.xlabel('support')
plt.ylabel('confidence') 
plt.show()


# In[73]:


D_won_rules.to_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Association_Rules/India/D_won_rules.csv')


# In[74]:


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


# In[75]:


N_won_rules#no rules since India has not played Night matches from 2015 to 2020


# In[76]:


N_won_rules.to_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Association_Rules/India/N_won_rules.csv')


# In[ ]:




