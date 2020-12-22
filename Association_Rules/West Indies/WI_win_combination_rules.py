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


match_data = pd.read_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Association_Rules/West Indies/WI_data.csv')


# In[3]:


#print the dataset
match_data.head()


# In[4]:


del match_data["Day_Night"]
del match_data["Home"]
del match_data["Bat"]
del match_data["Toss"]
del match_data["Opposition"]


# In[5]:


#print the dataset
match_data


# In[6]:


# convert our pandas dataframe into a list of lists,
player_combo = [] #list of lists match players and result
for i in range(0, 91):
    rowItem = []
    for j in range(0, 12):
        rowItem.append(str(match_data.values[i,j]))
    player_combo.append(rowItem)


# In[7]:


print(player_combo)


# In[8]:


#Creating the dataframe of frequent itemsets
te = TransactionEncoder()
te_ary = te.fit(player_combo).transform(player_combo)
match_df_freq = pd.DataFrame(te_ary, columns=te.columns_)


# In[9]:


#Define the minimum support and obtain the itemsets greater than the min support
#support = No. of times the required itemset occured / total no. of matches
match_sup = apriori(match_df_freq, min_support=0.1,use_colnames=True)
print(match_sup)


# In[10]:


#generate association rules
rules= association_rules(match_sup, metric="lift", min_threshold=1)


# In[11]:


#print the association rules
rules


# In[12]:


#extract only the combinations occured at a winning match
won_rules = rules[(rules['consequents'] == {"won"})]


# In[13]:


won_rules


# In[14]:


#remove the one itemsets
#obtain the final winning combinations
won_rules = won_rules[(won_rules['antecedents'].str.len() > 1)] #Here won_rules['antecedents'] is a frozenset


# In[15]:


#print the winning combinations
won_rules


# In[16]:


#sorting by confidence --- descending order
won_rules.sort_values(by ='confidence', ascending = False, inplace = True)


# In[17]:


won_rules


# In[18]:


#For example let's take the first rule
#if B Kumar, YS Chahal, KM Jadhav, MS Dhoni then won
#112 no of matches have played by the indian team from 2015 to 2020
#here the support is 0.205357 = x/112
#therefore no. of times the antecedent occurs = 0.205357*112 = approx 23 = x
#confidence = 0.958333 = y/23
#No of times the correct rule occured from the 23 instances is = 0.958333*23 = aprox 22 = y


# In[19]:


#sorting by support --- descending order
won_rules.sort_values(by ='support', ascending = False, inplace = True)


# In[20]:


won_rules


# In[21]:


#Support is an indication of how frequently the itemset appears in the dataset.
#Confidence is an indication of how often the rule has been found to be true.


# In[22]:


support=won_rules['support']
confidence=won_rules['confidence']


# In[23]:


import random
import matplotlib.pyplot as plt
 
plt.scatter(support, confidence,marker="*")
plt.xlabel('support')
plt.ylabel('confidence') 
plt.show()


# In[24]:


#select all the rules where antecedent contains 'RG Sharma'
#won_rules[(won_rules['antecedents'].apply(lambda x: 'RG Sharma' in str(x)))]


# In[25]:


won_rules.to_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Association_Rules/West Indies/won_rules.csv')


# In[ ]:




