#!/usr/bin/env python
# coding: utf-8

# In[69]:


import pandas as pd
import pandas_gbq
import os
import requests
from bs4 import BeautifulSoup


# In[51]:


#extraindo os dados e guardando na variável response
url = 'https://api.steampowered.com/ISteamApps/GetAppList/v2/'
response = requests.get(url)


# In[53]:


#checando se a requisição foi feita com sucesso
if response.status_code == 200:
    data = response.json()
else:
    print('Falha ao acessar a API:', response.status_code)


# In[55]:


# criando o dataframe
df = pd.DataFrame.from_dict(data)
df


# In[65]:


#tranformando cada elemento em uma nova linha no DataFrame.
exploded_df = df.explode('applist')


# In[66]:


#expandido em colunas separadas
exploded_applist = exploded_df.applist.apply(pd.Series)
exploded_applist


# In[74]:


exploded_applist.dtypes


# In[73]:


exploded_applist['appid'] = exploded_applist['appid'].astype(int)
exploded_applist['name'] = exploded_applist['name'].astype(str)


# #  ENVIANDO AO BIGQUERY

# In[70]:


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'case-tecnico-392418-f9d07e9de3e0.json'


# In[76]:


project_id = 'case-tecnico-392418'
dataset_id = 'steamdb'
table_name = 'Aplicações_steamDB'

pandas_gbq.to_gbq(exploded_applist, f'{project_id}.{dataset_id}.{table_name}', project_id=project_id, if_exists='replace')


# In[63]:





# In[ ]:




