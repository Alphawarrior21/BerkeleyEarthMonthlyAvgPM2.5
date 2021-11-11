#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[18]:


colnames=["Year", "Month","Day", "UTC Hour","PM2.5","PM10_mask","Retrospective"] 
df=pd.read_table('http://berkeleyearth.lbl.gov/air-quality/maps/cities/India/NCT/Delhi.txt',names=colnames,
    #usecols=["Year ", "Month","Day", "UTC Hour","PM2.5","PM10_mask","Retrospective"],
    skiprows=[i for i in range(0, 10) ])


# In[19]:


df


# In[22]:


rf=df.loc[(df['Year'] == 2021) & (df['Month'] == 10)]


# In[23]:


rf


# In[24]:


rf.isnull().values.any()


# In[26]:


rf.describe()


# In[33]:


rf.groupby(['Year','Month','Day', 'PM2.5']).mean()


# In[38]:


sf=rf.drop(['UTC Hour', 'PM10_mask','Retrospective'], axis = 1)


# In[39]:


sf


# In[45]:


sf.describe()


# In[50]:


sf.columns


# In[52]:


sf.groupby(['Year','Month','Day', 'PM2.5']).mean()


# In[55]:


grouped_df = df.groupby(['Year','Month','Day'])


# In[126]:


with open('C:/Users/admin/PM2.5.txt') as f:
    lines = f.read().splitlines()
print(lines)


# In[127]:


lines


# In[128]:


import urlparse
url='http://berkeleyearth.lbl.gov/air-quality/maps/cities/India/West_Bengal/Kolkata.txt'
#res=urlparse.urlparse(url)
#res.query


# In[129]:


from urllib.parse import urlparse
o=urlparse('http://berkeleyearth.lbl.gov/air-quality/maps/cities/India/West_Bengal/Kolkata.txt')
o.path
state_City=o.path.replace("/air-quality/maps/cities/India/","")
state_City=state_City.replace(".txt","")


# In[130]:


index=state_City.index("/")
State=state_City[:index]
City=state_City[index+1:]
print(City)
print(State)


# In[131]:


StateCityDict={}

print(StateCityDict)
lines
    


# In[132]:


for entry in lines:
    from urllib.parse import urlparse
    o=urlparse(entry)
    o.path
    state_City=o.path.replace("/air-quality/maps/cities/India/","")
    state_City=state_City.replace(".txt","")
    index=state_City.index("/")
    State=state_City[:index]
    City=state_City[index+1:]
    StateCityDict[State]=City


# In[133]:


print(StateCityDict)


# In[134]:


CityLevelDict={}
colnames=["Year", "Month","Day", "UTC Hour","PM2.5","PM10_mask","Retrospective"] 
cityNames=[]
for entry in lines:
    from urllib.parse import urlparse
    o=urlparse(entry)
    o.path
    state_City=o.path.replace("/air-quality/maps/cities/India/","")
    state_City=state_City.replace(".txt","")
    index=state_City.index("/")
    State=state_City[:index]
    City=state_City[index+1:]
    cityNames.append(City)
    df=pd.read_table(entry,names=colnames,skiprows=[i for i in range(0, 10) ])
    CityLevelDict[City]=df
    #df['City'] = df['City'].astype(str)
    #for i, row in df.iterrows():
        #df.at[i,'City']='KolKatta'
    
        


# In[135]:


CityLevelDict


# In[ ]:




