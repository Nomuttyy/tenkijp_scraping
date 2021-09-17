# -*- coding: utf-8 -*-
from pathlib import Path
from ftplib import FTP
import datetime
import json


basedtime = datetime.date.today()
localdirtoday = Path(__file__).parent / "tenkijp_hakusan_dropNaN" / str(basedtime.year) / str(basedtime.month) / f"{basedtime}.csv"
year = f"/ftp/tenkijp_hakusan_dropNaN/{basedtime.year}"
month = f"{year}/{basedtime.month}"
today = f"{month}/{basedtime}.csv"
with open('/home/nomura/Documents/tenkijp_scraping/config.json') as f:
	conf = json.load(f)
	ftp = FTP(conf["ip"],conf["username"],conf["password"])
if year in ftp.nlst("/ftp/tenkijp_hakusan_dropNaN/") :
	pass
else :
	ftp.mkd(year)
if month in ftp.nlst(year) :
	pass
else :
	ftp.mkd(month)
if today in ftp.nlst(month) :
	pass
else :
	with open(localdirtoday,"rb") as f:
		ftp.storbinary(f"STOR {today}",f)