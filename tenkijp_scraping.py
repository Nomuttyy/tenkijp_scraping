#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import datetime


# In[6]:


URL = 'https://tenki.jp/forecast/4/20/5610/17210/1hour.html'
dfs = pd.read_html(URL,encoding = "UTF-8",header=0,index_col=0)


# In[9]:


# df = pd.read_html(URL, header = 0)


# In[11]:


dfs[0].head()


# In[20]:


today = datetime.date.today()
today = today.strftime("%Y%m%d")
today = "/home/nomura/Documents/tenkijp_scraping/tenkijp_hakusan/" + today + '.csv'
dfs[0].to_csv(today)
# today


# In[ ]:




