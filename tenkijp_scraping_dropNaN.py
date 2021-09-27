import datetime
import os
from pathlib import Path
from dateutil.relativedelta import relativedelta

import pandas as pd


URL = 'https://tenki.jp/forecast/4/20/5610/17210/1hour.html'
dfs = pd.read_html(URL,encoding = "UTF-8",header=0,index_col=0)
# 翌日の天気予報
df = dfs[1]
cols = [0,1,2,4,5,7,8,9,10]

df  = df.iloc[cols]
df = df.T
indexlist = []
for index,hour in zip(df.index,df.iloc[:,1]):
    index = index.replace("明日 ","")[:11] + hour
    if int(index[11:]) <= 23:
        index = pd.to_datetime(index, format='%Y年%m月%d日%H')
        indexlist.append(index)
    else:
        index = pd.to_datetime(index[:-2]+"00", format='%Y年%m月%d日%H')
        index += relativedelta(days=1)
        indexlist.append(index)
df.index = indexlist

basedtime = datetime.date.today()
folder = Path(__file__).parent / "tenkijp_hakusan_dropNaN" / str(basedtime.year)
os.makedirs(folder,exist_ok=True)
folder = folder / str(basedtime.month)
os.makedirs(folder,exist_ok=True)
today = folder / f"{basedtime}.csv"
df.to_csv(today)


