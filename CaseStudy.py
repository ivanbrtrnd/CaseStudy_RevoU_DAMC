#!/usr/bin/env python
# coding: utf-8

# In[61]:


# Questions:
# 1. Which game is the oldest and newest in the dataset?
# 2. Which publisher published the most games?
# 3. Which developer developed the most games?
# 4. Which series has the most sales?
# 5. which series has the most games?


# In[62]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# # Read Data from Google Sheets

# In[63]:


sheet_url = 'https://docs.google.com/spreadsheets/d/1z46qH9il8OfVkYBZMMDUYq_GYHp77_prgkKq6HysZts/edit#gid=1485085913'
sheet_url_trf = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
print(sheet_url_trf)


# # Data Cleansing

# In[64]:


df = pd.read_csv(sheet_url_trf)
df['Release'] = pd.to_datetime(df['Release'])
df = df.drop_duplicates()
df.info()
df.head()


# # Which Game is the Oldest and Newest in the Dataset?

# In[65]:


df[['Name', 'Release']].sort_values('Release', ascending=True).head()


# In[66]:


df[['Name', 'Release']].sort_values('Release', ascending=False).head()


# In[67]:


# The oldest game in the dataset is 'Hydlide' released in 1984.
# The newest game in the dataset is 'Valheim' released in 2021.


# # Which Publisher Published the Most Games?

# In[68]:


agg_publisher = df.groupby('Publisher', as_index=False)['Name'].nunique()
agg_publisher.sort_values('Name', ascending=False)


# In[69]:


plt.rcParams['figure.figsize'] = (20, 10)
sns.barplot(x='Publisher', y='Name', data=agg_publisher.sort_values('Name', ascending=False).head(10))


# In[70]:


# The publisher that published the most games is 'Electronic Arts' with 19 games.


# # Which Developer Developed the Most Games?

# In[71]:


agg_developer = df.groupby('Developer', as_index=False)['Name'].nunique()
agg_developer.sort_values('Name', ascending=False)


# In[72]:


plt.rcParams['figure.figsize'] = (20, 10)
sns.barplot(x='Developer', y='Name', data=agg_developer.sort_values('Name', ascending=False).head(10))


# In[73]:


# The developer that developed the most games is 'Blizzard Entertainment' with 8 games.


# # Which Series has the Most Sales?

# In[74]:


agg_series_sales = df.groupby('Series', as_index=False)['Sales'].sum()
agg_series_sales.sort_values('Sales', ascending=False)


# In[75]:


plt.rcParams['figure.figsize'] = (20, 10)
sns.barplot(x='Series', y='Sales', data=agg_series_sales.sort_values('Sales', ascending=False).head(10))


# In[76]:


# The series that has the most sales is 'Minecraft' with 33 sales.


# # Which Series has the Most Games?

# In[77]:


agg_series_games = df.groupby('Series', as_index=False)['Name'].nunique()
agg_series_games.sort_values('Name', ascending=False)


# In[78]:


plt.rcParams['figure.figsize'] = (20, 10)
sns.barplot(x='Series', y='Name', data=agg_series_games.sort_values('Name', ascending=False).head(10))


# In[79]:


# The series that has the most games is 'Command & Conquer' with 5 games.

