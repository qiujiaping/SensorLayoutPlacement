
import numpy as np

import pandas as pd
import wntr

#
# pressureDataNormal=[[1,2,3],[4,5,6],[7,8,9]]
# print(type(pressureDataNormal[0]))
# # print(pressureDataNormal)
# # np.set_printoptions(suppress=True)      # 取消科学计数法
# pressureDataNormal = np.array(pressureDataNormal)  # 把数组（列表）转化为np矩阵
# #
# print(pressureDataNormal)
# print(type(pressureDataNormal[0]))
# print(pressureDataNormal-[1,2,3])
# print(pressureDataNormal-pressureDataNormal[0])
# a=np.zeros(shape=(3,3))
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         a[i][j]=1
# print(pressureDataNormal[0].min())
# c=[2,3]
# d=[4,5,6]
# e=[]
# e.append(c)
# e.append(d)
# print(e)
# inp_file ="Net3.inp"
# wn = wntr.network.WaterNetworkModel(inp_file)
#
# pipeName=[]
# startNode=[]
# endNode=[]
# pipeLength=[]
#
# for i in wn.pipe_name_list:
#     pipeName.append(i)
#     # print(i)
#     s = wn.links._data[i]._start_node
#     print('开始节点',s)
    # startNode.append(s)
    # e = wn.links._data[i]._end_node
    # endNode.append(e)
    # length=wn.links._data[i].length
    # pipeLength.append(length)
inpFile = 'ky8.inp'
wn = wntr.network.WaterNetworkModel(inpFile)
nodesIndexs = {}  #存储节点名称 键：序号，值：名称  如nodesIndexs={0:'43',1:'44',....}
n = 1
#得到节点列表
for m in wn.node_name_list:
    print(m)

