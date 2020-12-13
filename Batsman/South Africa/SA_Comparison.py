#!/usr/bin/env python
# coding: utf-8

# In[220]:


import numpy as np
import pandas as pd


# In[221]:


#load data file
data = pd.read_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Bat_Com_Avg/South Africa/South_Africa.csv')


# In[222]:


data.head()


# In[223]:


players = ['P1','P2','P3','P4','P5','P6','P7','P8','P9','P10','P11']
player_scores = ['P1_S','P2_S','P3_S','P4_S','P5_S','P6_S','P7_S','P8_S','P9_S','P10_S','P11_S']


# In[224]:


x = set()


# In[225]:


for i in players:
    for j in range(len(data[i].unique())):
        x.add(data[i].unique()[j])


# In[226]:


print(x)


# In[227]:


len(x)


# In[228]:


unique_list = list(x)
print(unique_list)


# In[229]:


column_names = ["player_name", "sum", "avg"]

result = pd.DataFrame(columns = column_names)


# In[230]:


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


# In[231]:


#Comparing individual avg with 2 grams combinations avg


# In[232]:


#load data file
data2grams = pd.read_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Bat_Com_Avg/South Africa/SA_2grams.csv')


# In[233]:


data2grams.head()


# In[234]:


del data2grams["Unnamed: 0"]


# In[235]:


data2grams.head()


# In[236]:


data2grams.shape


# In[237]:


new_column_names = ["player-1", "player-2", "combined_avg","sum_of_individual"]

SA_beautiful2grams = pd.DataFrame(columns = new_column_names)


# In[238]:


for index, row in data2grams.iterrows():
    player1 = data2grams.iloc[index]['player-1']
    player2 = data2grams.iloc[index]['player-2']
    combined = data2grams.iloc[index]['avg']
    individual_avg_sum = dictionary.get(player1)+dictionary.get(player2)
    if(combined > individual_avg_sum):
        SA_beautiful2grams = SA_beautiful2grams.append({'player-1':player1, 'player-2':player2, 'combined_avg': combined, 'sum_of_individual':individual_avg_sum}, ignore_index=True)


# In[239]:


SA_beautiful2grams.head()


# In[240]:


SA_beautiful2grams.shape


# In[241]:


SA_beautiful2grams.to_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Bat_Com_Avg/South Africa/SA_beautiful2grams.csv')


# In[242]:


#Comparing individual avg with 3 grams combinations avg


# In[243]:


#load data file
data3grams = pd.read_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Bat_Com_Avg/South Africa/SA_3grams.csv')


# In[244]:


data3grams.head()


# In[245]:


del data3grams["Unnamed: 0"]


# In[246]:


data3grams = data3grams[data3grams.avg != 0.0]


# In[247]:


data3grams.head()


# In[248]:


data3grams = data3grams.reset_index(drop=True)


# In[249]:


data3grams.head()


# In[250]:


data3grams.shape


# In[251]:


new_column_names = ["player-1", "player-2", "player-3", "combined_avg","sum_of_individual"]

SA_beautiful3grams = pd.DataFrame(columns = new_column_names)


# In[252]:


for index, row in data3grams.iterrows():
    player1 = data3grams.iloc[index]['player-1']
    player2 = data3grams.iloc[index]['player-2']
    player3 = data3grams.iloc[index]['player-3']
    combined = data3grams.iloc[index]['avg']
    individual_avg_sum = dictionary.get(player1)+dictionary.get(player2)+dictionary.get(player3)
    if(combined > individual_avg_sum):
        SA_beautiful3grams = SA_beautiful3grams.append({'player-1':player1, 'player-2':player2,'player-3':player3, 'combined_avg': combined, 'sum_of_individual':individual_avg_sum}, ignore_index=True)


# In[253]:


SA_beautiful3grams.head()


# In[254]:


SA_beautiful3grams.shape


# In[255]:


SA_beautiful3grams.to_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Bat_Com_Avg/South Africa/SA_beautiful3grams.csv')


# In[256]:


#Comparing individual avg with 4 grams combinations avg


# In[257]:


#load data file
data4grams = pd.read_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Bat_Com_Avg/South Africa/SA_4grams.csv')


# In[258]:


del data4grams["Unnamed: 0"]


# In[259]:


data4grams.head()


# In[260]:


data4grams.shape


# In[261]:


data4grams = data4grams[data4grams.avg != 0.0]


# In[262]:


data4grams.shape


# In[263]:


data4grams


# In[264]:


data4grams = data4grams.reset_index(drop=True)


# In[265]:


new_column_names = ["player-1", "player-2", "player-3", "player-4", "combined_avg","sum_of_individual"]

SA_beautiful4grams = pd.DataFrame(columns = new_column_names)


# In[266]:


for index, row in data4grams.iterrows():
    player1 = data4grams.iloc[index]['player-1']
    player2 = data4grams.iloc[index]['player-2']
    player3 = data4grams.iloc[index]['player-3']
    player4 = data4grams.iloc[index]['player-4']
    combined = data4grams.iloc[index]['avg']
    individual_avg_sum = dictionary.get(player1)+dictionary.get(player2)+dictionary.get(player3)+dictionary.get(player4)
    if(combined > individual_avg_sum):
        SA_beautiful4grams = SA_beautiful4grams.append({'player-1':player1, 'player-2':player2,'player-3':player3, 'player-4':player4,'combined_avg': combined, 'sum_of_individual':individual_avg_sum}, ignore_index=True)


# In[267]:


SA_beautiful4grams.head()


# In[268]:


SA_beautiful4grams.shape


# In[269]:


SA_beautiful4grams.to_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Bat_Com_Avg/South Africa/SA_beautiful4grams.csv')


# In[ ]:




