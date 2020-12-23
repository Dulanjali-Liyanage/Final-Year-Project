#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


#load data file
data = pd.read_csv('aus_data1.csv')


# In[3]:


data.head()


# In[4]:


data = data[data.Result == 'won']


# In[5]:


data


# In[6]:


del data['Result']


# In[7]:


data = data.reset_index(drop=True)


# In[8]:


x = set()
print(x)


# In[9]:


players = ['p1','p2','p3','p4','p5','p6','p7','p8','p9','p10','p11']


# In[10]:


for i in players:
    for j in range(len(data[i].unique())):
        x.add(data[i].unique()[j])


# In[11]:


print(x)


# In[12]:


len(x)


# In[13]:


import itertools 
# def findsubsets(s, n): 
def findsubsets(s, n): 
    return [set(i) for i in itertools.combinations(s, n)] 


# In[14]:


sub2 = findsubsets(x,2)


# In[15]:


len(sub2)


# In[16]:


for t in sub2:
    new_list = list(t)
    df = data[np.equal.outer(data.to_numpy(copy=False),  new_list).any(axis=1).all(axis=1)]
    df = df.reset_index(drop=True)
    isempty = df.empty
    if(isempty):
        sub2.remove(t)


# In[17]:


len(sub2)


# In[18]:


#load data file which includes both won lost data
data_all = pd.read_csv('aus.csv')


# In[19]:


column_names = ["player-1", "player-2", "avg"]

result_2grams = pd.DataFrame(columns = column_names)


# In[20]:


player_scores = ['p1-s','p2-s','p3-s','p4-s','p5-s','p6-s','p7-s','p8-s','p9-s','p10-s','p11-s']


# In[21]:


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


# In[22]:


unique_list = list(x)
print(unique_list)  


# In[23]:


column_names = ["player_name", "sum", "avg"]

result = pd.DataFrame(columns = column_names)


# In[24]:


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


# In[25]:


result_2grams.head()


# In[26]:


result_2grams.shape


# In[27]:


result_2grams = result_2grams[result_2grams.avg != 0.0]


# In[28]:


result_2grams.shape


# In[29]:


result_2grams = result_2grams.reset_index(drop=True)


# In[30]:


new_column_names = ["player-1", "player-2", "combined_avg","sum_of_individual"]

afg_beautiful2grams = pd.DataFrame(columns = new_column_names)


# In[31]:


for index, row in result_2grams.iterrows():
    player1 = result_2grams.iloc[index]['player-1']
    player2 = result_2grams.iloc[index]['player-2']
    combined = result_2grams.iloc[index]['avg']
    individual_avg_sum = dictionary.get(player1)+dictionary.get(player2)
    if(combined > individual_avg_sum):
        afg_beautiful2grams = afg_beautiful2grams.append({'player-1':player1, 'player-2':player2, 'combined_avg': combined, 'sum_of_individual':individual_avg_sum}, ignore_index=True)


# In[32]:


afg_beautiful2grams.head()


# In[33]:


afg_beautiful2grams.shape


# In[34]:


afg_beautiful2grams.to_csv('aus2grams_won.csv')


# In[ ]:




