#!/usr/bin/env python
# coding: utf-8

# In[2]:

from pathlib import Path
import re
import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import datetime


# In[3]:


URL = 'https://tenki.jp/forecast/4/20/5610/17210/1hour.html'
dfs = pd.read_html(URL,encoding = "UTF-8",header=0,index_col=0)


# In[4]:


# df = pd.read_html(URL, header = 0)


# In[12]:


df = dfs[0]


# In[14]:


cols = [0,1,2,4,5,7,8,9,10]
df  = df.iloc[cols]


# In[20]:


today = datetime.date.today()
today = today.strftime("%Y%m%d")
today = Path(__file__).parent / "tenkijp_hakusan_dropNaN" / f"{today}.csv"
# today = "/home/nomura/Documents/tenkijp_hakusan_dropNaN/" + today + '.csv'
df.to_csv(today)
# today


# In[ ]:




