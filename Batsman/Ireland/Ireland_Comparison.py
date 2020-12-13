#!/usr/bin/env python
# coding: utf-8

# In[170]:


import numpy as np
import pandas as pd


# In[171]:


#load data file
data = pd.read_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Bat_Com_Avg/Ireland/Ireland.csv')


# In[172]:


data.head()


# In[173]:


players = ['P1','P2','P3','P4','P5','P6','P7','P8','P9','P10','P11']
player_scores = ['P1_S','P2_S','P3_S','P4_S','P5_S','P6_S','P7_S','P8_S','P9_S','P10_S','P11_S']


# In[174]:


x = set()


# In[175]:


for i in players:
    for j in range(len(data[i].unique())):
        x.add(data[i].unique()[j])


# In[176]:


print(x)


# In[177]:


len(x)


# In[178]:


unique_list = list(x)
print(unique_list)


# In[179]:


column_names = ["player_name", "sum", "avg"]

result = pd.DataFrame(columns = column_names)


# In[180]:


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


# In[181]:


#Comparing individual avg with 2 grams combinations avg


# In[182]:


#load data file
data2grams = pd.read_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Bat_Com_Avg/Ireland/Ireland_2grams.csv')


# In[183]:


data2grams.head()


# In[184]:


del data2grams["Unnamed: 0"]


# In[185]:


data2grams.head()


# In[186]:


data2grams.shape


# In[187]:


new_column_names = ["player-1", "player-2", "combined_avg","sum_of_individual"]

Ireland_beautiful2grams = pd.DataFrame(columns = new_column_names)


# In[188]:


for index, row in data2grams.iterrows():
    player1 = data2grams.iloc[index]['player-1']
    player2 = data2grams.iloc[index]['player-2']
    combined = data2grams.iloc[index]['avg']
    individual_avg_sum = dictionary.get(player1)+dictionary.get(player2)
    if(combined > individual_avg_sum):
        Ireland_beautiful2grams = Ireland_beautiful2grams.append({'player-1':player1, 'player-2':player2, 'combined_avg': combined, 'sum_of_individual':individual_avg_sum}, ignore_index=True)


# In[189]:


Ireland_beautiful2grams.head()


# In[190]:


Ireland_beautiful2grams.shape


# In[191]:


Ireland_beautiful2grams.to_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Bat_Com_Avg/Ireland/Ireland_beautiful2grams.csv')


# In[192]:


#Comparing individual avg with 3 grams combinations avg


# In[193]:


#load data file
data3grams = pd.read_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Bat_Com_Avg/Ireland/Ireland_3grams.csv')


# In[194]:


data3grams.head()


# In[195]:


del data3grams["Unnamed: 0"]


# In[196]:


data3grams = data3grams[data3grams.avg != 0.0]


# In[197]:


data3grams.head()


# In[198]:


data3grams = data3grams.reset_index(drop=True)


# In[199]:


data3grams.head()


# In[200]:


data3grams.shape


# In[201]:


new_column_names = ["player-1", "player-2", "player-3", "combined_avg","sum_of_individual"]

Ireland_beautiful3grams = pd.DataFrame(columns = new_column_names)


# In[202]:


for index, row in data3grams.iterrows():
    player1 = data3grams.iloc[index]['player-1']
    player2 = data3grams.iloc[index]['player-2']
    player3 = data3grams.iloc[index]['player-3']
    combined = data3grams.iloc[index]['avg']
    individual_avg_sum = dictionary.get(player1)+dictionary.get(player2)+dictionary.get(player3)
    if(combined > individual_avg_sum):
        Ireland_beautiful3grams = Ireland_beautiful3grams.append({'player-1':player1, 'player-2':player2,'player-3':player3, 'combined_avg': combined, 'sum_of_individual':individual_avg_sum}, ignore_index=True)


# In[203]:


Ireland_beautiful3grams.head()


# In[204]:


Ireland_beautiful3grams.shape


# In[205]:


Ireland_beautiful3grams.to_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Bat_Com_Avg/Ireland/Ireland_beautiful3grams.csv')


# In[206]:


#Comparing individual avg with 4 grams combinations avg


# In[207]:


#load data file
data4grams = pd.read_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Bat_Com_Avg/Ireland/Ireland_4grams.csv')


# In[208]:


del data4grams["Unnamed: 0"]


# In[209]:


data4grams.head()


# In[210]:


data4grams.shape


# In[211]:


data4grams = data4grams[data4grams.avg != 0.0]


# In[212]:


data4grams.shape


# In[213]:


data4grams


# In[214]:


data4grams = data4grams.reset_index(drop=True)


# In[215]:


new_column_names = ["player-1", "player-2", "player-3", "player-4", "combined_avg","sum_of_individual"]

Ireland_beautiful4grams = pd.DataFrame(columns = new_column_names)


# In[216]:


for index, row in data4grams.iterrows():
    player1 = data4grams.iloc[index]['player-1']
    player2 = data4grams.iloc[index]['player-2']
    player3 = data4grams.iloc[index]['player-3']
    player4 = data4grams.iloc[index]['player-4']
    combined = data4grams.iloc[index]['avg']
    individual_avg_sum = dictionary.get(player1)+dictionary.get(player2)+dictionary.get(player3)+dictionary.get(player4)
    if(combined > individual_avg_sum):
        Ireland_beautiful4grams = Ireland_beautiful4grams.append({'player-1':player1, 'player-2':player2,'player-3':player3, 'player-4':player4,'combined_avg': combined, 'sum_of_individual':individual_avg_sum}, ignore_index=True)


# In[217]:


Ireland_beautiful4grams.head()


# In[218]:


Ireland_beautiful4grams.shape


# In[219]:


Ireland_beautiful4grams.to_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Bat_Com_Avg/Ireland/Ireland_beautiful4grams.csv')


# In[ ]:




