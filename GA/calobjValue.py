
"""

    解码并计算,返回0,1矩阵500行


"""
import numpy as np
import pandas as pd
def decodechrom(pop):                       # pop=[500*80]-->搞成每行如[0,0,1,1,.............]是np矩阵500行形状是[500*1317]
    temp1=[]
    for i in range(len(pop)):
        s=np.zeros((1317), dtype=np.int)    #先生成1317个全为0的行向量
        for j in range(len(pop[i])):
            sensorlocal=pop[i][j]           #得出传感器索引，即位置
            s[sensorlocal-1]=1  #若pop[i][j]=1317,则是s[1316]=1
        temp1.append(s)
    temp1=np.array(temp1)
    return temp1[:]

"""
考虑投影向量是负数的情况如何
"""
def calobjValue(pop,Residualsmatrix,SensitivityMatrix) :

    # 放置每个个体对应的函数值的列表
    obj_value = []
    temp1 = decodechrom(pop)            #获得论文中的Q=[0,0,1,1,.............]Pop是np矩阵500*1317形状
    Q = []                              #500个1317*1317个的对角化个体
    for i in range(len(temp1)):
        Q.append(np.diag(temp1[i]))     #将temp1中的每行0，1对角化存入Q中

    for j in range(len(Q)):             #开始计算每个个体
        individual=Q[j]                 #每个个体
        row=len(Residualsmatrix)
        column=len(SensitivityMatrix[:,0])              #后来加的
        projectionMatrix=np.empty((row, column))         #投影矩阵形状[row*row]->[row*column]
        choose_sensor_RM=Residualsmatrix.dot(individual)    #在全部节点的残差数据中选择传感器可读的压力数据"矩阵"
        choose_sensor_SM=SensitivityMatrix.dot(individual)  #在全部节点的灵敏度数据中选择传感器可读的压力数据"矩阵"
        # print('第%s个个体残差矩阵'%j,choose_sensor_RM)
        # print(choose_sensor_RM.shape)
        # print('第%s个个体灵敏度矩阵' % j, choose_sensor_SM)
        # print(choose_sensor_SM.shape)
        choose_sensor_SM_transpose=choose_sensor_SM.T           #把10*1317的灵敏度矩阵构造成1317*10，便于与公式一致
        for row in range(len(choose_sensor_RM)):                 #矩阵的乘积
            vectorLength1 = np.linalg.norm(choose_sensor_RM[row])
            for column in range(len(choose_sensor_SM_transpose[0])):
                #vectorLength1=np.linalg.norm(choose_sensor_RM[row])         #可以把这个提到循环前去
                vectorLength2=np.linalg.norm(choose_sensor_SM_transpose[:, column])
                projectionMatrix[row][column] =(choose_sensor_RM[row].dot(choose_sensor_SM_transpose[:,column]))/(vectorLength1*vectorLength2)
        erroLocalcount=0
        #print('打印第%s个投影矩阵'%j,projectionMatrix)
        for k in range(len(projectionMatrix)):              #遍历矩阵寻找每行最大值的位置，k代表行索引
            lineMaxvalue=projectionMatrix[k].max()
            tempList=list(projectionMatrix[k])              #变为list数组，使其具有index属性
            index=tempList.index(lineMaxvalue)               #可能报 nan is not in the list错误 index代表列索引
            if(index != k):                                 #若行位置和列位置不等则错误定位
                erroLocalcount=erroLocalcount+1
        individual_value=erroLocalcount/len(projectionMatrix)  #
        obj_value.append(individual_value)

    # print(obj_value)
    # print(type(obj_value))
    return obj_value[:]


if __name__ == '__main__':
    from geneEncoding import geneEncoding
    import pandas as pd
    import sys
    sys.path.append('D:\keyanshuju\sensorsPlacementLayout\getPressureData')
    from getPressureData.getMetrix import getMatrix, getResidualsmatrix, getSensitivityMatrix

    exePath = 'D:\keyanshuju\EpanetSimulation\Debug\EpanetSimulation.exe'
    inpPath = "D:\keyanshuju\sensorsPlacementLayout\getPressureData\\ky8.inp"
    NormalrptPath = "D:\keyanshuju\sensorsPlacementLayout\getPressureData\\Normal.rpt"
    LeakrptPath = "D:\keyanshuju\sensorsPlacementLayout\getPressureData\\Leak.rpt"
    # 获得残差矩阵，节点索引，有效的泄露节点
    Residualsmatrix, nodesIndexs, validSimuNodesID = getResidualsmatrix(exePath, 1, 2, inpPath, NormalrptPath,
                                                                        LeakrptPath, 12, 0)
    # # 获得灵敏度矩阵
    SensitivityMatrix = getSensitivityMatrix(exePath, 1, 2, inpPath, NormalrptPath, LeakrptPath, 6.3, 0)
    pop_size = 50  # 种群数量
    chrom_length = 80  # 染色体长度
    pop = geneEncoding(pop_size, chrom_length)
    print(calobjValue(pop,Residualsmatrix,SensitivityMatrix))
    # temp1=decodechrom(pop)
    # Q = []
    # for i in range(len(temp1)):
    #     Q.append(np.diag(temp1[i]))
    # for j in range(len(Q)):
    #     individual=Q[j]
    #     print(individual)







