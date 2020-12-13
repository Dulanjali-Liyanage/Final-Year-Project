#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


#load data file
data = pd.read_csv('/home/e15202/My/CO425/WI/WI.csv',sep= ',')


# In[3]:


data.head()


# In[4]:


players = set()
print(players)


# In[5]:


player_names = ['P1','P2','P3','P4','P5','P6','P7','P8','P9','P10','P11']


# In[6]:


for i in player_names:
    for j in range(len(data[i].unique())):
        players.add(data[i].unique()[j])


# In[7]:


print(players)


# In[8]:


print(len(players))


# In[9]:


player_scores = ['P1_S','P2_S','P3_S','P4_S','P5_S','P6_S','P7_S','P8_S','P9_S','P10_S','P11_S']


# In[10]:


import itertools 
# def findsubsets(s, n): 
def findsubsets(s, n): 
    return [set(i) for i in itertools.combinations(s, n)] 


# In[30]:


print(len(findsubsets(players,3)))


# In[31]:


#find the 2 gram player combinations
sub3 = findsubsets(players,3)


# In[32]:


column_names = ["player-1", "player-2","player-3","avg"]

result_3grams = pd.DataFrame(columns = column_names)


# In[33]:


for t in sub3:
    new_list = list(t)
    df = data[np.equal.outer(data.to_numpy(copy=False),  new_list).any(axis=1).all(axis=1)]
    count = 0;
    df = df.reset_index(drop=True)
    isempty = df.empty
    if(isempty):
        result_3grams = result_3grams.append({'player-1':new_list[0], 'player-2':new_list[1],'player-3':new_list[2],'avg':0.0}, ignore_index=True)
        continue
    for index, row in df.iterrows():
        for ind, p in enumerate(player_names):
                if(df.iloc[index][p] == new_list[0] ):
                    count = count + df.iloc[index][player_scores[ind]]
                if(df.iloc[index][p] == new_list[1] ):
                    count = count + df.iloc[index][player_scores[ind]]
                if(df.iloc[index][p] == new_list[2] ):
                    count = count + df.iloc[index][player_scores[ind]]
    avg = count/df.shape[0]
    result_3grams = result_3grams.append({'player-1':new_list[0], 'player-2':new_list[1], 'player-3':new_list[2],'avg':avg}, ignore_index=True)


# In[34]:


result_3grams.head()


# In[41]:


result_3grams.to_csv('/home/e15202/My/CO425/WI/WI_3grams.csv',sep= ',')


# In[ ]:




