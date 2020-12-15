#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# # Finding individual averages of batsmen

# In[2]:


#load data file
data = pd.read_csv('F:/8TH SEM/CO425-FYP/NewZealand/NewZealand.csv')


# In[3]:


data.head()


# In[4]:


players = ['p1','p2','p3','p4','p5','p6','p7','p8','p9','p10','p11']
player_scores = ['p1-s','p2-s','p3-s','p4-s','p5-s','p6-s','p7-s','p8-s','p9-s','p10-s','p11-s']


# In[5]:


x = set()


# In[6]:


# finding unique players
for i in players:
    for j in range(len(data[i].unique())):
        x.add(data[i].unique()[j])


# In[7]:


print(x)


# In[8]:


len(x)


# In[9]:


#set -> list
unique_list = list(x)
print(unique_list)    


# In[10]:


column_names = ["player_name", "sum", "avg"]

result = pd.DataFrame(columns = column_names)


# In[11]:


# finding the individual averages of players=> total score/no.of matches played
dictionary = dict()

for indx, name in enumerate(unique_list):
    count = 0
    sum = 0
    for index, row in data.iterrows():
        for ind, p in enumerate(players):
                if(data.iloc[index][p] == name ):
#                     print(name)
                    sum = sum + data.iloc[index][player_scores[ind]] 
                    count += 1
    avg = round((sum/count),2)
    print(name," : sum=",sum," , count=",count," , average=",round(avg,2))    
    dictionary[name] = avg
    result = result.append({'player_name':name, 'sum':sum, 'avg':avg}, ignore_index=True)
    
print(dictionary)


# In[12]:


result.head(13)


# In[13]:


result.to_csv('F:/8TH SEM/CO425-FYP/NewZealand/indv_results/NewZealand_ind.csv',sep=',')


# # 2 grams - combinational averages Vs sum of individual averages

# In[14]:


#load data file-combinational avgs of 2-grams
data2grams = pd.read_csv('F:/8TH SEM/CO425-FYP/NewZealand/Combined averages/NewZealand_2g.csv',sep=',')


# In[15]:


data2grams.head()


# In[16]:


data2grams = data2grams[data2grams.avg != 0.0]


# In[17]:


data2grams.head()


# In[18]:


data2grams.shape


# In[19]:


data2grams = data2grams.reset_index(drop=True)


# In[20]:


data2grams.head()


# In[21]:


new_column_names = ["player-1", "player-2", "combined_avg","sum_of_individual"]

comparison_2grams = pd.DataFrame(columns = new_column_names)


# In[22]:


for index, row in data2grams.iterrows():
    player1 = data2grams.iloc[index]['player-1']
    player2 = data2grams.iloc[index]['player-2']
    combined = data2grams.iloc[index]['avg']
    individual_avg_sum = dictionary.get(player1)+dictionary.get(player2)
    if(combined > individual_avg_sum):
        comparison_2grams = comparison_2grams.append({'player-1':player1, 'player-2':player2, 'combined_avg': combined, 'sum_of_individual':individual_avg_sum}, ignore_index=True)


# In[23]:


comparison_2grams.head()


# In[24]:


comparison_2grams.shape


# In[25]:


comparison_2grams.to_csv('F:/8TH SEM/CO425-FYP/NewZealand/Comparative analysis/NewZealand_comparison_2grams.csv')


# # 3 grams - combinational averages Vs sum of individual averages

# In[26]:


#load data file-combinational avgs of 3-grams
data3grams = pd.read_csv('F:/8TH SEM/CO425-FYP/NewZealand/Combined averages/NewZealand_3g.csv',sep=',')


# In[27]:


data3grams.head()


# In[28]:


data3grams.shape


# In[29]:


data3grams = data3grams[data3grams.avg != 0.0]


# In[30]:


data3grams.shape


# In[31]:


data3grams = data3grams.reset_index(drop=True)


# In[32]:


data3grams.head()


# In[33]:


new_column_names = ["player-1", "player-2", "player-3", "combined_avg","sum_of_individual"]

comparison_3grams = pd.DataFrame(columns = new_column_names)


# In[34]:


for index, row in data3grams.iterrows():
    player1 = data3grams.iloc[index]['player-1']
    player2 = data3grams.iloc[index]['player-2']
    player3 = data3grams.iloc[index]['player-3']
    combined = data3grams.iloc[index]['avg']
    individual_avg_sum = dictionary.get(player1)+dictionary.get(player2)+dictionary.get(player3)
    if(combined > individual_avg_sum):
        comparison_3grams = comparison_3grams.append({'player-1':player1, 'player-2':player2,'player-3':player3, 'combined_avg': combined, 'sum_of_individual':individual_avg_sum}, ignore_index=True)


# In[35]:


comparison_3grams.head()


# In[36]:


comparison_3grams.shape


# In[37]:


comparison_3grams.to_csv('F:/8TH SEM/CO425-FYP/NewZealand/Comparative analysis/NewZealand_comparison_3grams.csv')


# # 4 grams - combinational averages Vs sum of individual averages

# In[38]:


#load data file-combinational avgs of 4-grams
data4grams = pd.read_csv('F:/8TH SEM/CO425-FYP/NewZealand/Combined averages/NewZealand_4g.csv',sep=',')


# In[39]:


data4grams.head()


# In[40]:


data4grams.shape


# In[41]:


data4grams = data4grams[data4grams.avg != 0.0]


# In[42]:


data4grams.shape


# In[43]:


data4grams = data4grams.reset_index(drop=True)


# In[44]:


data4grams.head()


# In[45]:


new_column_names = ["player-1", "player-2", "player-3", "player-4", "combined_avg","sum_of_individual"]

comparison_4grams = pd.DataFrame(columns = new_column_names)


# In[46]:


for index, row in data4grams.iterrows():
    player1 = data4grams.iloc[index]['player-1']
    player2 = data4grams.iloc[index]['player-2']
    player3 = data4grams.iloc[index]['player-3']
    player4 = data4grams.iloc[index]['player-4']
    combined = data4grams.iloc[index]['avg']
    individual_avg_sum = dictionary.get(player1)+dictionary.get(player2)+dictionary.get(player3)+dictionary.get(player4)
    if(combined > individual_avg_sum):
        comparison_4grams = comparison_4grams.append({'player-1':player1, 'player-2':player2,'player-3':player3, 'player-4':player4,'combined_avg': combined, 'sum_of_individual':individual_avg_sum}, ignore_index=True)


# In[47]:


comparison_4grams.head()


# In[48]:


comparison_4grams.shape


# In[49]:


comparison_4grams.to_csv('F:/8TH SEM/CO425-FYP/NewZealand/Comparative analysis/NewZealand_comparison_4grams.csv')


# In[ ]:




