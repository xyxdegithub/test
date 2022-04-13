# -*- coding = utf-8 -*-
# @Time : 2022/4/6 14:12
# @Author : 谢扬筱
# @File : test.py

import requests
import URL

response=requests.get(url="https://engineering.case.edu/sites/default/files/97.mat",stream=True)
total=int(response.headers.get("content-length"))
print(total)

for save_name,url in URL.URLS["Normal Baseline Data"].items():
    print(save_name)
    print(url)