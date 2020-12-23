#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd


# In[3]:


#load data file
data = pd.read_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Batsman/India/India_win_data.csv')


# In[4]:


data


# In[5]:


data = data[data.Result == 'won']


# In[6]:


data


# In[7]:


del data['Result']


# In[8]:


data


# In[9]:


data = data.reset_index(drop=True)


# In[10]:


data


# In[11]:


x = set()
print(x)


# In[12]:


players = ['P1','P2','P3','P4','P5','P6','P7','P8','P9','P10','P11']


# In[13]:


for i in players:
    for j in range(len(data[i].unique())):
        x.add(data[i].unique()[j])


# In[14]:


print(x)


# In[15]:


len(x)


# In[16]:


import itertools 
# def findsubsets(s, n): 
def findsubsets(s, n): 
    return [set(i) for i in itertools.combinations(s, n)] 


# In[17]:


sub2 = findsubsets(x,2)


# In[18]:


print(sub2)


# In[19]:


len(sub2)


# In[20]:


for t in sub2:
    new_list = list(t)
    df = data[np.equal.outer(data.to_numpy(copy=False),  new_list).any(axis=1).all(axis=1)]
    df = df.reset_index(drop=True)
    isempty = df.empty
    if(isempty):
        sub2.remove(t)


# In[21]:


len(sub2)


# In[22]:


#load data file which includes both won lost data
data_all = pd.read_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Batsman/India/India.csv')


# In[23]:


data_all


# In[24]:


column_names = ["player-1", "player-2", "avg"]

result_2grams = pd.DataFrame(columns = column_names)


# In[25]:


player_scores = ['P1_S','P2_S','P3_S','P4_S','P5_S','P6_S','P7_S','P8_S','P9_S','P10_S','P11_S']


# In[26]:


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


# In[27]:


unique_list = list(x)
print(unique_list)


# In[28]:


column_names = ["player_name", "sum", "avg"]

result = pd.DataFrame(columns = column_names)


# In[29]:


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


# In[30]:


result_2grams.head()


# In[31]:


result_2grams.shape


# In[32]:


result_2grams = result_2grams[result_2grams.avg != 0.0]


# In[33]:


result_2grams.shape


# In[34]:


result_2grams = result_2grams.reset_index(drop=True)


# In[35]:


new_column_names = ["player-1", "player-2", "combined_avg","sum_of_individual"]

India_beautiful2grams = pd.DataFrame(columns = new_column_names)


# In[36]:


for index, row in result_2grams.iterrows():
    player1 = result_2grams.iloc[index]['player-1']
    player2 = result_2grams.iloc[index]['player-2']
    combined = result_2grams.iloc[index]['avg']
    individual_avg_sum = dictionary.get(player1)+dictionary.get(player2)
    if(combined > individual_avg_sum):
        India_beautiful2grams = India_beautiful2grams.append({'player-1':player1, 'player-2':player2, 'combined_avg': combined, 'sum_of_individual':individual_avg_sum}, ignore_index=True)


# In[37]:


India_beautiful2grams


# In[38]:


India_beautiful2grams.shape


# In[39]:


India_beautiful2grams.to_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Batsman/India/IND2grams_won.csv')


# In[40]:


#3 grams


# In[41]:


sub3 = findsubsets(x,3)


# In[42]:


print(sub3)


# In[43]:


len(sub3)


# In[44]:


for t in sub3:
    new_list = list(t)
    df = data[np.equal.outer(data.to_numpy(copy=False),  new_list).any(axis=1).all(axis=1)]
    df = df.reset_index(drop=True)
    isempty = df.empty
    if(isempty):
        sub3.remove(t)


# In[45]:


len(sub3)


# In[46]:


#load data file which includes both won lost data
data_all = pd.read_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Batsman/India/India.csv')


# In[47]:


data_all


# In[59]:


column_names = ["player-1", "player-2", "player-3","avg"]

result_3grams = pd.DataFrame(columns = column_names)


# In[60]:


player_scores = ['P1_S','P2_S','P3_S','P4_S','P5_S','P6_S','P7_S','P8_S','P9_S','P10_S','P11_S']


# In[63]:


for t in sub3:
    new_list = list(t)
    df = data_all[np.equal.outer(data_all.to_numpy(copy=False),  new_list).any(axis=1).all(axis=1)]
    count = 0;
    df = df.reset_index(drop=True)
    isempty = df.empty
    if(isempty):
        result_3grams = result_3grams.append({'player-1':new_list[0], 'player-2':new_list[1], 'player-3':new_list[2],'avg':0.0}, ignore_index=True)
        continue
    for index, row in df.iterrows():
        for ind, p in enumerate(players):
                if(df.iloc[index][p] == new_list[0] ):
                    count = count + df.iloc[index][player_scores[ind]]
                if(df.iloc[index][p] == new_list[1] ):
                    count = count + df.iloc[index][player_scores[ind]]
                if(df.iloc[index][p] == new_list[2] ):
                    count = count + df.iloc[index][player_scores[ind]]
    avg = count/df.shape[0]
    result_3grams = result_3grams.append({'player-1':new_list[0], 'player-2':new_list[1], 'player-3':new_list[2],'avg':avg}, ignore_index=True)


# In[64]:


unique_list = list(x)
print(unique_list)


# In[65]:


column_names = ["player_name", "sum", "avg"]

result = pd.DataFrame(columns = column_names)


# In[66]:


dictionary = dict()


# In[67]:


for indx, name in enumerate(unique_list):
    count = 0
    sum = 0
    for index, row in data_all.iterrows():
        for ind, p in enumerate(players):
                if(data_all.iloc[index][p] == name ):
#                     print(name)
                    sum = sum + data_all.iloc[index][player_scores[ind]] 
                    count += 1
    avg = round((sum/count),3)
    print(name," : sum=",sum," , count=",count," , average=",round(avg,2))    
    dictionary[name] = avg
    result = result.append({'player_name':name, 'sum':sum, 'avg':avg}, ignore_index=True)


# In[68]:


print(dictionary)


# In[69]:


result_3grams.head()


# In[70]:


result_3grams.shape


# In[71]:


result_3grams = result_3grams[result_3grams.avg != 0.0]


# In[72]:


result_3grams.shape


# In[73]:


result_3grams = result_3grams.reset_index(drop=True)


# In[74]:


new_column_names = ["player-1", "player-2", "player-3","combined_avg","sum_of_individual"]


# In[75]:


India_beautiful3grams = pd.DataFrame(columns = new_column_names)


# In[76]:


for index, row in result_3grams.iterrows():
    player1 = result_3grams.iloc[index]['player-1']
    player2 = result_3grams.iloc[index]['player-2']
    player3 = result_3grams.iloc[index]['player-3']
    combined = result_3grams.iloc[index]['avg']
    individual_avg_sum = dictionary.get(player1)+dictionary.get(player2)+dictionary.get(player3)
    if(combined > individual_avg_sum):
        India_beautiful3grams = India_beautiful3grams.append({'player-1':player1, 'player-2':player2,'player-3':player3, 'combined_avg': combined, 'sum_of_individual':individual_avg_sum}, ignore_index=True)


# In[77]:


India_beautiful3grams


# In[78]:


India_beautiful3grams.shape


# In[79]:


India_beautiful3grams.to_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Batsman/India/IND3grams_won.csv')


# In[ ]:




