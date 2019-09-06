import sys
sys.path.append('D:\keyanshuju\sensorsPlacementLayout\getPressureData')    #对于模块和自己写的脚本不在同一个目录下，在脚本开头加sys.path.append('xxx')：
from getPressureData.getMetrix import getMatrix,getResidualsmatrix,getSensitivityMatrix,readSimulationNodes
from geneEncoding import geneEncoding
from calobjValue import calobjValue
from best import best
from geneDecode import geneDecode
from selection import selection
from crossover import crossover
from mutation import mutation
import matplotlib.pyplot as plt
import numpy as np
import time
import wntr


exePath='D:\keyanshuju\EpanetSimulation\Debug\EpanetSimulation.exe'
inpPath="D:\keyanshuju\sensorsPlacementLayout\getPressureData\\ky8.inp"
NormalrptPath="D:\keyanshuju\sensorsPlacementLayout\getPressureData\\Normal.rpt"
LeakrptPath="D:\keyanshuju\sensorsPlacementLayout\getPressureData\\Leak.rpt"

"""
    关于灵敏度矩阵是不是得模拟1317个节点
    残差矩阵是随意个
    关于灵敏度矩阵是不是得模拟1317个节点
    残差矩阵是随意个
    关于灵敏度矩阵是不是得模拟1317个节点
    残差矩阵是随意个
    关于灵敏度矩阵是不是得模拟1317个节点
    残差矩阵是随意个
    关于灵敏度矩阵是不是得模拟1317个节点
    残差矩阵是随意个
    
"""
start = time.clock()        #开始计时
# 获得残差矩阵，节点索引，有效的泄露节点
# Residualsmatrix,nodesIndexs,validSimuNodesID=getResidualsmatrix(exePath, 1, 2, inpPath,NormalrptPath, LeakrptPath, 15, 0,100)
# # # 获得灵敏度矩阵
# SensitivityMatrix=getSensitivityMatrix(exePath, 1, 2, inpPath,NormalrptPath, LeakrptPath, 12, 0,200)
file_RM='Residualsmatrix100.npy'
file_SM='SensitivityMatrix200.npy'
# np.save(file_RM,Residualsmatrix)
# np.save(file_SM,SensitivityMatrix)
Residualsmatrix=np.load(file_RM)
SensitivityMatrix=np.load(file_SM)
# print('Residualsmatrix',Residualsmatrix)
print(len(SensitivityMatrix))
print(len(SensitivityMatrix[0]))

pop_size = 40		# 种群数量
chrom_length = 80	# 染色体长度,代表传感器个数，隐含位置
pc = 0.6			# 交配概率
pm = 0.01           # 变异概率
results = [[]]		# 存储每一代的最优解，[[]]表示是二维数组。
fit_value = []		# 个体适应度

simuNodesIndex,nodesIndexs=readSimulationNodes(inpPath)
#产生初始种群
pop=geneEncoding(pop_size,chrom_length)     #pop中的个体原始为[421, 76, 213, 632, 1011, 102, 1289, 334,.......]代表其节点索引位置80个pop形状500*80

for i in range(500):	#共迭代500代
    # 对每一代做计算，判断优劣,获取当代最好个体
    start = time.clock()
    print('开始计算第%s代的适应度'%i)
    fit_value = calobjValue(pop,Residualsmatrix,SensitivityMatrix)  # 个体评价（适应度函数），obj_value放置对应每个个体的适应度值
    end1 = time.clock()
    print('完成适应度计算耗时%s'%(end1 - start),'适应度:',fit_value)

    best_individual, best_fit=best(pop, fit_value)  # 第一个存储最优的解对应的整数编码,第二个存储最优基因对应的适应度，值越小越好
    # end2 = time.clock()
    # print('完成挑选最好的耗时%s'%(end2-end1))
    print('最好的',best_fit)
    print('最好的个体',geneDecode(best_individual,nodesIndexs))
    results.append([best_fit, geneDecode(best_individual,nodesIndexs)]) ## 存储每一代的最优解,及其最终的节点ID,值越小越好

    #  遗传算法核心，生成种群，为下一次计算适应度做准备

    selection(pop, fit_value)   #选择
    # end3 = time.clock()
    # print('完成选择耗时%s'%(end3-end2))
    crossover(pop,pc)           #重组
    # end4 = time.clock()
    # print('完成crossover耗时%s' % (end4 - end3))
    mutation(pop, pm)           #变异
    # end5 = time.clock()
    # print('完成mutation耗时%s' % (end5 - end4))
    print('第%s代已完成'%i)


results = results[1:]

# results.sort()		#根据best_fit进行排序


print('最后一代最好的结果：',results[-1])     		# 打印最好的结果
print('最后一代最好的个体',best_individual)  	# 打印最后一代最好的二进制个体
print('最后一代个体最好的适应度',best_fit)				#打印最后一代最好的二进制个体成绩
#print('打印最后一代第一个个个体的分数fit_value',fit_value[1])			#打印最后一代每个个体的分数


print(pop)
print(results)
end = time.clock()
print('Running time: %s Seconds' % (end - start))
X = []
Y = []
for i in range(500):
	X.append(i)         #   x代表代数
	t = results[i][0]   #   t代表每代的最佳适应度
	Y.append(t)

plt.plot(X, Y)
plt.show()

