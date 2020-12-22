#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


#load data file
data = pd.read_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Batsman/West Indies/WI.csv')


# In[3]:


data.head()


# In[4]:


players = ['P1','P2','P3','P4','P5','P6','P7','P8','P9','P10','P11']
player_scores = ['P1_S','P2_S','P3_S','P4_S','P5_S','P6_S','P7_S','P8_S','P9_S','P10_S','P11_S']


# In[5]:


x = set()


# In[6]:


for i in players:
    for j in range(len(data[i].unique())):
        x.add(data[i].unique()[j])


# In[7]:


print(x)


# In[8]:


len(x)


# In[9]:


unique_list = list(x)
print(unique_list)


# In[10]:


column_names = ["player_name", "sum", "avg"]

result = pd.DataFrame(columns = column_names)


# In[11]:


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


# In[12]:


#load data file
data2grams = pd.read_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Batsman/West Indies/WI_2grams.csv')


# In[13]:


data2grams.head()


# In[14]:


del data2grams["Unnamed: 0"]


# In[15]:


data2grams.shape


# In[16]:


data2grams = data2grams[data2grams.avg != 0.0]


# In[17]:


data2grams.shape


# In[18]:


data2grams.head()


# In[19]:


data2grams = data2grams.reset_index(drop=True)


# In[20]:


data2grams.head()


# In[21]:


new_column_names = ["player-1", "player-2", "combined_avg","sum_of_individual"]

WI_beautiful2grams = pd.DataFrame(columns = new_column_names)


# In[22]:


for index, row in data2grams.iterrows():
    player1 = data2grams.iloc[index]['player-1']
    player2 = data2grams.iloc[index]['player-2']
    combined = data2grams.iloc[index]['avg']
    individual_avg_sum = dictionary.get(player1)+dictionary.get(player2)
    if(combined > individual_avg_sum):
        WI_beautiful2grams = WI_beautiful2grams.append({'player-1':player1, 'player-2':player2, 'combined_avg': combined, 'sum_of_individual':individual_avg_sum}, ignore_index=True)


# In[23]:


WI_beautiful2grams.head()


# In[24]:


WI_beautiful2grams.shape


# In[25]:


WI_beautiful2grams.to_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Batsman/West Indies/WI_beautiful2grams.csv')


# In[26]:


#Comparing individual avg with 3 grams combinations avg


# In[27]:


#load data file
data3grams = pd.read_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Batsman/West Indies/WI_3grams.csv')


# In[28]:


data3grams.head()


# In[29]:


del data3grams["Unnamed: 0"]


# In[30]:


data3grams.shape


# In[31]:


data3grams = data3grams[data3grams.avg != 0.0]


# In[32]:


data3grams.head()


# In[33]:


data3grams = data3grams.reset_index(drop=True)


# In[34]:


data3grams.head()


# In[35]:


data3grams.shape


# In[36]:


new_column_names = ["player-1", "player-2", "player-3", "combined_avg","sum_of_individual"]

WI_beautiful3grams = pd.DataFrame(columns = new_column_names)


# In[37]:


for index, row in data3grams.iterrows():
    player1 = data3grams.iloc[index]['player-1']
    player2 = data3grams.iloc[index]['player-2']
    player3 = data3grams.iloc[index]['player-3']
    combined = data3grams.iloc[index]['avg']
    individual_avg_sum = dictionary.get(player1)+dictionary.get(player2)+dictionary.get(player3)
    if(combined > individual_avg_sum):
        WI_beautiful3grams = WI_beautiful3grams.append({'player-1':player1, 'player-2':player2,'player-3':player3, 'combined_avg': combined, 'sum_of_individual':individual_avg_sum}, ignore_index=True)


# In[38]:


WI_beautiful3grams.head()


# In[39]:


WI_beautiful3grams.shape


# In[40]:


WI_beautiful3grams.to_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Batsman/West Indies/WI_beautiful3grams.csv')


# In[41]:


#Comparing individual avg with 4 grams combinations avg


# In[42]:


#load data file
data4grams = pd.read_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Batsman/West Indies/WI_4grams.csv')


# In[43]:


del data4grams["Unnamed: 0"]


# In[44]:


data4grams.head()


# In[45]:


data4grams.shape


# In[46]:


data4grams = data4grams[data4grams.avg != 0.0]


# In[47]:


data4grams.shape


# In[48]:


data4grams


# In[49]:


data4grams = data4grams.reset_index(drop=True)


# In[50]:


new_column_names = ["player-1", "player-2", "player-3", "player-4", "combined_avg","sum_of_individual"]

WI_beautiful4grams = pd.DataFrame(columns = new_column_names)


# In[51]:


for index, row in data4grams.iterrows():
    player1 = data4grams.iloc[index]['player-1']
    player2 = data4grams.iloc[index]['player-2']
    player3 = data4grams.iloc[index]['player-3']
    player4 = data4grams.iloc[index]['player-4']
    combined = data4grams.iloc[index]['avg']
    individual_avg_sum = dictionary.get(player1)+dictionary.get(player2)+dictionary.get(player3)+dictionary.get(player4)
    if(combined > individual_avg_sum):
        WI_beautiful4grams = WI_beautiful4grams.append({'player-1':player1, 'player-2':player2,'player-3':player3, 'player-4':player4,'combined_avg': combined, 'sum_of_individual':individual_avg_sum}, ignore_index=True)


# In[52]:


WI_beautiful4grams.head()


# In[53]:


WI_beautiful4grams.shape


# In[54]:


WI_beautiful4grams.to_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Batsman/West Indies/WI_beautiful4grams.csv')


# In[ ]:




