# -*- coding = utf-8 -*-
# @Time : 2022/4/11 17:27
# @Author : xyx
# @File : out2.py
'''
把一个文件夹下的.npy文件保存为txt文件
'''
import os
import numpy as np

path=r"E:\数据集\CWRU2\CWRU files"
txtpath=r'E:\code\pythoncode\test\npy2\output'

namelist=[x for x in os.listdir(path)]

print("需要转换的文件名称：")
print(namelist)
for i in range( len(namelist) ):
    datapath=os.path.join(path,namelist[i])
    #print(namelist[i])
    data = np.load(datapath)
    np.savetxt('%s/%s.txt'%(txtpath,namelist[i]),data)
print ("转换完成！")


