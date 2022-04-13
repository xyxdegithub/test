# -*- coding = utf-8 -*-
# @Time : 2022/4/11 17:23
# @Author : xyx
# @File : out.py

import numpy as np
# 设置全部数据，不输出省略号
import sys
np.set_printoptions(threshold=sys.maxsize)
data=np.load(r"E:\数据集\CWRU2\CWRU files\featurized_data_labels.npy")
print(data)
#np.savetxt('featurized_data_labels.txt',data,fmt='%s',newline='\n')
np.savetxt('featurized_data_labels.txt',data,fmt="%.0f")
