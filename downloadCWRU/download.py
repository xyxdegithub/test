# -*- coding = utf-8 -*-
# @Time : 2022/4/6 13:47
# @Author : xyx
# @File : downloadCWRU.py
from pathlib import Path

import URL
import requests
from tqdm.auto import tqdm
import os


def download(url: str, save_dir: str, save_name: str, suffix=None):
    if save_name==None:
        fileName=url.split("/")[-1]
    else:
        fileName=save_name+suffix
    filePath=save_dir+fileName
    if  filePath:
        print(f"正在下载{filePath}")
        with open(filePath,"wb") as f:
            response=requests.get(url,stream=True)
            total = int(response.headers.get('content-length'))
            with tqdm(total=total, unit='B', unit_scale=True, desc=fileName) as pbar:
                for data in response.iter_content(chunk_size=1024 * 1024):
                    f.write(data)
                    pbar.update(1024 * 1024)
    else:
        return filePath
    return filePath


if __name__== "__main__":
    category1="Normal Baseline Data"
    category2="12k Drive End Bearing Fault Data"
    category3 = "48k Drive End Bearking Fault Data"
    category4 = "12k Fan End Bearing Fault Data"

    path=f"./CWRU/{category2}/"

    if not os.path.exists(path):
        os.makedirs(path)

    save_dir=path

    for save_name,url in URL.URLS[category2].items():
        download(url,save_dir,save_name,suffix=".mat")
        print(f"下载{category3}完成")

