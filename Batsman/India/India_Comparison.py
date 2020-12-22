#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[10]:


#load data file
data = pd.read_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Batsman/India/India.csv')


# In[11]:


data.head()


# In[12]:


players = ['P1','P2','P3','P4','P5','P6','P7','P8','P9','P10','P11']
player_scores = ['P1_S','P2_S','P3_S','P4_S','P5_S','P6_S','P7_S','P8_S','P9_S','P10_S','P11_S']


# In[13]:


x = set()


# In[14]:


for i in players:
    for j in range(len(data[i].unique())):
        x.add(data[i].unique()[j])


# In[15]:


print(x)


# In[16]:


len(x)


# In[17]:


unique_list = list(x)
print(unique_list)


# In[18]:


column_names = ["player_name", "sum", "avg"]

result = pd.DataFrame(columns = column_names)


# In[19]:


#individual avg of players = sum of scores in matches/no. of matches played
dictionary = dict()

for indx, name in enumerate(unique_list):
    count = 0
    sum = 0
    for index, row in data.iterrows():
        for ind, p in enumerate(players):
                if(data.iloc[index][p] == name ):
                    sum = sum + data.iloc[index][player_scores[ind]] 
                    count += 1
    avg = round((sum/count),2)
    print(name," : sum=",sum," , count=",count," , average=",round(avg,2))    
    dictionary[name] = avg
    result = result.append({'player_name':name, 'sum':sum, 'avg':avg}, ignore_index=True)
    
print(dictionary)


# In[32]:


#Comparing individual avg with 2 grams combinations avg


# In[33]:


#load data file
data2grams = pd.read_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Batsman/India/India_2grams.csv')


# In[34]:


data2grams.head()


# In[35]:


data2grams.shape


# In[36]:


data2grams = data2grams[data2grams.avg != 0.0]


# In[37]:


data2grams.shape


# In[40]:


data2grams.head()


# In[41]:


data2grams = data2grams.reset_index(drop=True)


# In[42]:


data2grams.head()


# In[43]:


new_column_names = ["player-1", "player-2", "combined_avg","sum_of_individual"]

India_beautiful2grams = pd.DataFrame(columns = new_column_names)


# In[44]:


for index, row in data2grams.iterrows():
    player1 = data2grams.iloc[index]['player-1']
    player2 = data2grams.iloc[index]['player-2']
    combined = data2grams.iloc[index]['avg']
    individual_avg_sum = dictionary.get(player1)+dictionary.get(player2)
    if(combined > individual_avg_sum):
        India_beautiful2grams = India_beautiful2grams.append({'player-1':player1, 'player-2':player2, 'combined_avg': combined, 'sum_of_individual':individual_avg_sum}, ignore_index=True)


# In[45]:


India_beautiful2grams.head()


# In[46]:


India_beautiful2grams.shape


# In[47]:


India_beautiful2grams.to_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Batsman/India/India_beautiful2grams.csv')


# In[54]:


#Comparing individual avg with 3 grams combinations avg


# In[55]:


#load data file
data3grams = pd.read_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Batsman/India/India_3grams.csv')


# In[56]:


data3grams.head()


# In[57]:


del data3grams["Unnamed: 0"]


# In[58]:


data3grams.shape


# In[59]:


data3grams = data3grams[data3grams.avg != 0.0]


# In[60]:


data3grams.head()


# In[61]:


data3grams = data3grams.reset_index(drop=True)


# In[63]:


data3grams.head()


# In[64]:


data3grams.shape


# In[65]:


new_column_names = ["player-1", "player-2", "player-3", "combined_avg","sum_of_individual"]

India_beautiful3grams = pd.DataFrame(columns = new_column_names)


# In[66]:


for index, row in data3grams.iterrows():
    player1 = data3grams.iloc[index]['player-1']
    player2 = data3grams.iloc[index]['player-2']
    player3 = data3grams.iloc[index]['player-3']
    combined = data3grams.iloc[index]['avg']
    individual_avg_sum = dictionary.get(player1)+dictionary.get(player2)+dictionary.get(player3)
    if(combined > individual_avg_sum):
        India_beautiful3grams = India_beautiful3grams.append({'player-1':player1, 'player-2':player2,'player-3':player3, 'combined_avg': combined, 'sum_of_individual':individual_avg_sum}, ignore_index=True)


# In[68]:


India_beautiful3grams.head()


# In[69]:


India_beautiful3grams.shape


# In[70]:


India_beautiful3grams.to_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Batsman/India/India_beautiful3grams.csv')


# In[71]:


#Comparing individual avg with 4 grams combinations avg


# In[72]:


#load data file
data4grams = pd.read_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Batsman/India/India_4grams.csv')


# In[73]:


del data4grams["Unnamed: 0"]


# In[74]:


data4grams.head()


# In[75]:


data4grams.shape


# In[76]:


data4grams = data4grams[data4grams.avg != 0.0]


# In[77]:


data4grams.shape


# In[78]:


data4grams


# In[79]:


data4grams = data4grams.reset_index(drop=True)


# In[80]:


new_column_names = ["player-1", "player-2", "player-3", "player-4", "combined_avg","sum_of_individual"]

India_beautiful4grams = pd.DataFrame(columns = new_column_names)


# In[81]:


for index, row in data4grams.iterrows():
    player1 = data4grams.iloc[index]['player-1']
    player2 = data4grams.iloc[index]['player-2']
    player3 = data4grams.iloc[index]['player-3']
    player4 = data4grams.iloc[index]['player-4']
    combined = data4grams.iloc[index]['avg']
    individual_avg_sum = dictionary.get(player1)+dictionary.get(player2)+dictionary.get(player3)+dictionary.get(player4)
    if(combined > individual_avg_sum):
        India_beautiful4grams = India_beautiful4grams.append({'player-1':player1, 'player-2':player2,'player-3':player3, 'player-4':player4,'combined_avg': combined, 'sum_of_individual':individual_avg_sum}, ignore_index=True)


# In[82]:


India_beautiful4grams.head()


# In[83]:


India_beautiful4grams.shape


# In[84]:


India_beautiful4grams.to_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Batsman/India/India_beautiful4grams.csv')


# In[ ]:




