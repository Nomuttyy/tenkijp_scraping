# -*- coding: utf-8 -*-
from ftplib import FTP
import json

with open('/home/nomura/Documents/tenkijp_scraping/config.json') as f:
	conf = json.load(f)
	ftp = FTP(conf["ip"],conf["username"],conf["password"])
with open("/home/nomura/Documents/tenkijp_scraping/test.txt", "rb") as f:
	ftp.storbinary("STOR /ftp/test.txt", f)
	
# ローカルパス
# local_path = '_____ローカル パス_____'

# # サーバーパス
# server_path = '_____サーバー パス_____'

# # アップロードするファイルリスト
# file_list = [
# 	'index.html',
# 	'/img/photo.jpg'
# ]