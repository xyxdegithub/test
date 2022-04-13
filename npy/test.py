# -*- coding = utf-8 -*-
# @Time : 2022/4/10 17:11
# @Author : xyx
# @File : test.py
import numpy as np

# file=np.load(r"E:\数据集\CWRU2\CWRU files\featurized_data_labels.npy")
# txt=open("featurized_data_labels.txt","a")
# print(file,file=txt)

file=np.load(r"E:\数据集\CWRU2\CWRU files\featurized_data.npy")
txt=open("featurized_data.txt","a")
print(file,file=txt)