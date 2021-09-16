import datetime
import os
from pathlib import Path

import pandas as pd


URL = 'https://tenki.jp/forecast/4/20/5610/17210/1hour.html'
dfs = pd.read_html(URL,encoding = "UTF-8",header=0,index_col=0)
df = dfs[0]
cols = [0,1,2,4,5,7,8,9,10]
df  = df.iloc[cols]

basedtime = datetime.date.today()
folder = Path(__file__).parent / "tenkijp_hakusan_dropNaN" / str(basedtime.year)
os.makedirs(folder,exist_ok=True)
folder = folder / str(basedtime.month)
os.makedirs(folder,exist_ok=True)
today = folder / f"{basedtime}.csv"
df.to_csv(today)


