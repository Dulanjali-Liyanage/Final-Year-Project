#!/usr/bin/env python
# coding: utf-8

# In[22]:


import numpy as np
import pandas as pd


# In[23]:


#load data file
data = pd.read_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Batsman/India/India_win_data.csv')


# In[24]:


data


# In[25]:


data = data[data.Result == 'won']


# In[26]:


data


# In[27]:


del data['Result']


# In[28]:


data


# In[29]:


data = data.reset_index(drop=True)


# In[30]:


data


# In[31]:


x = set()
print(x)


# In[32]:


players = ['P1','P2','P3','P4','P5','P6','P7','P8','P9','P10','P11']


# In[33]:


for i in players:
    for j in range(len(data[i].unique())):
        x.add(data[i].unique()[j])


# In[34]:


print(x)


# In[35]:


len(x)


# In[36]:


import itertools 
# def findsubsets(s, n): 
def findsubsets(s, n): 
    return [set(i) for i in itertools.combinations(s, n)] 


# In[37]:


sub2 = findsubsets(x,2)


# In[38]:


print(sub2)


# In[39]:


len(sub2)


# In[40]:


for t in sub2:
    new_list = list(t)
    df = data[np.equal.outer(data.to_numpy(copy=False),  new_list).any(axis=1).all(axis=1)]
    df = df.reset_index(drop=True)
    isempty = df.empty
    if(isempty):
        sub2.remove(t)


# In[41]:


len(sub2)


# In[42]:


#load data file which includes both won lost data
data_all = pd.read_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Batsman/India/India.csv')


# In[43]:


data_all


# In[44]:


column_names = ["player-1", "player-2", "avg"]

result_2grams = pd.DataFrame(columns = column_names)


# In[45]:


player_scores = ['P1_S','P2_S','P3_S','P4_S','P5_S','P6_S','P7_S','P8_S','P9_S','P10_S','P11_S']


# In[46]:


for t in sub2:
    new_list = list(t)
    df = data_all[np.equal.outer(data_all.to_numpy(copy=False),  new_list).any(axis=1).all(axis=1)]
    count = 0;
    df = df.reset_index(drop=True)
    isempty = df.empty
    if(isempty):
        result_2grams = result_2grams.append({'player-1':new_list[0], 'player-2':new_list[1], 'avg':0.0}, ignore_index=True)
        continue
    for index, row in df.iterrows():
        for ind, p in enumerate(players):
                if(df.iloc[index][p] == new_list[0] ):
                    count = count + df.iloc[index][player_scores[ind]]
                if(df.iloc[index][p] == new_list[1] ):
                    count = count + df.iloc[index][player_scores[ind]]
    avg = count/df.shape[0]
    result_2grams = result_2grams.append({'player-1':new_list[0], 'player-2':new_list[1], 'avg':avg}, ignore_index=True)


# In[47]:


unique_list = list(x)
print(unique_list)


# In[48]:


column_names = ["player_name", "sum", "avg"]

result = pd.DataFrame(columns = column_names)


# In[49]:


dictionary = dict()

for indx, name in enumerate(unique_list):
    count = 0
    sum = 0
    for index, row in data_all.iterrows():
        for ind, p in enumerate(players):
                if(data_all.iloc[index][p] == name ):
#                     print(name)
                    sum = sum + data_all.iloc[index][player_scores[ind]] 
                    count += 1
    avg = round((sum/count),2)
    print(name," : sum=",sum," , count=",count," , average=",round(avg,2))    
    dictionary[name] = avg
    result = result.append({'player_name':name, 'sum':sum, 'avg':avg}, ignore_index=True)
    
print(dictionary)


# In[50]:


result_2grams.head()


# In[51]:


result_2grams.shape


# In[52]:


result_2grams = result_2grams[result_2grams.avg != 0.0]


# In[53]:


result_2grams.shape


# In[54]:


result_2grams = result_2grams.reset_index(drop=True)


# In[56]:


new_column_names = ["player-1", "player-2", "combined_avg","sum_of_individual"]

India_beautiful2grams = pd.DataFrame(columns = new_column_names)


# In[57]:


for index, row in result_2grams.iterrows():
    player1 = result_2grams.iloc[index]['player-1']
    player2 = result_2grams.iloc[index]['player-2']
    combined = result_2grams.iloc[index]['avg']
    individual_avg_sum = dictionary.get(player1)+dictionary.get(player2)
    if(combined > individual_avg_sum):
        India_beautiful2grams = India_beautiful2grams.append({'player-1':player1, 'player-2':player2, 'combined_avg': combined, 'sum_of_individual':individual_avg_sum}, ignore_index=True)


# In[58]:


India_beautiful2grams


# In[59]:


India_beautiful2grams.shape


# In[61]:


India_beautiful2grams.to_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Batsman/India/IND2grams_won.csv')


# In[ ]:




