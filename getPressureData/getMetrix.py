"""
    读数据的形成矩阵

"""
import time

import numpy as np
import wntr
from commandLine import callCommandLineLeak
from commandLine import callCommandLineNormal

from getPressureData.getDataFromReport import getDataFromRptAfterLeak
from getPressureData.getDataFromReport import getDataFromRptNormal


def readSimulationNodes(inpPath):
    inpFile = inpPath
    wn = wntr.network.WaterNetworkModel(inpFile)
    nodesIndexs = {}  #存储节点名称 键：序号，值：名称  如nodesIndexs={1:'43',2:'44',....}
    n = 1
	#得到节点列表
    for m in wn.node_name_list:
        nodesIndexs.update({n: m}) #nodesIndexs={1:'43',2:'44',....}
        n += 1

    simuNodesIndex=[] #存储模拟漏损节点的序号
    for key in nodesIndexs.keys():##nodesIndexs包括所有节点序号和节点名称节点序号（索引）是从1开始的
        simuNodesIndex.append(key)  #   key=1-1317

	#nodesIndexs包括所有节点序号和节点名称，simuNodesIndex模拟节点的序号，这个序号和nodesIndexs中对应节点匹配。
    return simuNodesIndex,nodesIndexs		#返回模拟的(全部)节点编号（索引）列表和全部节点的编号，名称字典
def getMatrix(exePath,choose1,choose2,inpPath,rptPathNormal,rptPathLeak,setFlow,when,leakNums):
    """
    :param exePath: D:\keyanshuju\EpanetSimulation\Debug\EpanetSimulation.exe
    :param choose1: 1
    :param choose2: 2
    :param inpPath: ky8.inp
    :param rptPathNormal: Normal.rpt
    :param rptPathLeak: lastLeak.rpt
    :param setFlow: 12
    :param when: 0
    :return:

    """
    callCommandLineNormal(exePath,choose1, inpPath, rptPathNormal)	#调用命令行，正常状态下，只生成一次

    pressureDataNormalOneTime= getDataFromRptNormal(rptPathNormal, 3, '  J-',when)		#获得正常工况的数据，从生成的正常报告文件读取数据

    simuNodesIndex,nodesIndexs=readSimulationNodes(inpPath)		#读取要模拟的节点，返回包括节点编号列表和节点编号，名称字典

    matrixAfterLeak = []    #存放泄露后压力矩阵
    validSimuNodesID=[]  #存放有效模拟节点索引
    LeakNodeID=[]       #可能带待模拟的节点列表，包含无效模拟节点

    # 这里要改变
    # 这里要改变
    # 这里要改变
    # 这里要改变
    # 这里要改变
    # for i in range(0,len(simuNodesIndex)-15):		#模拟 ， 搞个循环，依次提交漏损节点到命令行然后再循环体内处理生成的报告文件
    for i in range(0, leakNums):                          #控制泄露的节点（循环）
        LeakNodeID.append(nodesIndexs[simuNodesIndex[i]])   #可能带待模拟的节点列表，包含无效模拟节点
        
        callCommandLineLeak(exePath,choose2, inpPath, rptPathLeak, setFlow, simuNodesIndex[i])

        pressureDataAfterLeakOneTime = getDataFromRptAfterLeak(rptPathLeak,3, '  J-',when)

        if(len(pressureDataAfterLeakOneTime)):  # 有效的模拟节点才产生压力数据，记录还剩三个节点没有记录
            print(i)
            matrixAfterLeak.append(pressureDataAfterLeakOneTime[:])  # 把发生漏损时刻的节点压力拿出来
            validSimuNodesID.append(nodesIndexs[simuNodesIndex[i]])

    matrixAfterLeak=np.array(matrixAfterLeak)
    #print(matrixAfterLeak)
    #print('1',matrixAfterLeak.shape)
    return pressureDataNormalOneTime,matrixAfterLeak,validSimuNodesID,nodesIndexs,LeakNodeID

# 得到残差矩阵
def getResidualsmatrix(exePath,choose1,choose2,inpPath,rptPathNormal,rptPathLeak,setRMLeakFlow,when,leakNums):
    """
    :param setRMLeakFlow: 残差矩阵的泄露量，与灵敏度矩阵的泄露量设置不同
    :return: 残差矩阵，节点字典，泄露ID列表

    """
    pressureDataNormalOneTime, matrixAfterLeak, validSimuNodesID, nodesIndexs, LeakNodeID=getMatrix(exePath, choose1, choose2, inpPath, rptPathNormal, rptPathLeak, setRMLeakFlow, when,leakNums)

    Residualsmatrix=matrixAfterLeak-pressureDataNormalOneTime
    return Residualsmatrix,nodesIndexs,validSimuNodesID


    """
        函数返回灵敏度矩阵
    """

def getSensitivityMatrix(exePath,choose1,choose2,inpPath,rptPathNormal,rptPathLeak,setSMLeakFlow,when,leakNums):
    """
        :param setRMLeakFlow: 灵敏度矩阵的泄露量，与残差矩阵的泄露量设置不同
        :return: 残差矩阵，节点字典，泄露ID列表

    """
    pressureDataNormalOneTime, matrixAfterLeak, validSimuNodesID, nodesIndexs, LeakNodeID=getMatrix(exePath, choose1, choose2, inpPath, rptPathNormal, rptPathLeak, setSMLeakFlow, when,leakNums)
    # 这里需要处理控制小数保留位数
    """
    报错
     SensitivityMatrix=(matrixAfterLeak-pressureDataNormalOneTime)/(setSMLeakFlow/0.063)     #单位GPM
    ValueError: operands could not be broadcast together with shapes (50,) (1317,) 
    """
    #print('2',matrixAfterLeak.shape)
    #print('3',pressureDataNormalOneTime.shape)
    # print('type(matrixAfterLeak)',type(matrixAfterLeak))
    # print('type(pressureDataNormalOneTime)',type(pressureDataNormalOneTime))

    SensitivityMatrix=(matrixAfterLeak-pressureDataNormalOneTime)/(setSMLeakFlow/0.063)     #单位GPM


    return SensitivityMatrix


if __name__ == "__main__":
    import pandas as pd
    start = time.clock()
    # pressureDataNormalOneTime,matrixAfterLeak,validSimuNodesID,nodesIndexs,LeakNodeID=getMatrix("D:\keyanshuju\EpanetSimulation\Debug\EpanetSimulation.exe",1,2,"ky8.inp","Normal.rpt","lastLeak.rpt",6.3,0)
    # Residualsmatrix, nodesIndexs, validSimuNodesID=getResidualsmatrix("D:\keyanshuju\EpanetSimulation\Debug\EpanetSimulation.exe",1,2,"ky8.inp","Normal.rpt","lastLeak.rpt",12,0)
    # Residualsmatrix, nodesIndexs, validSimuNodesID=getResidualsmatrix("D:\keyanshuju\EpanetSimulation\Debug\EpanetSimulation.exe",1,2,"ky8.inp","Normal.rpt","lastLeak.rpt",12,0)
    # print('Running time: %s Seconds' % (end - start))
    # print("残差矩阵", Residualsmatrix)
    # print('节点索引', nodesIndexs)
    # print('模拟节点', validSimuNodesID)
    #Residualsmatrix, nodesIndexs, validSimuNodesID=getResidualsmatrix("D:\keyanshuju\EpanetSimulation\Debug\EpanetSimulation.exe",1,2,"ky8.inp","Normal.rpt","lastLeak.rpt",12,0)

    SensitivityMatrix=getSensitivityMatrix("D:\keyanshuju\EpanetSimulation\Debug\EpanetSimulation.exe",1,2,"ky8.inp","Normal.rpt","lastLeak.rpt",12,0,100)
    # df=pd.DataFrame(SensitivityMatrix)
    # df.to_csv('df.csv')
    end = time.clock()
    print('Running time: %s Seconds' % (end - start))
    # print("残差矩阵", Residualsmatrix)
    # print(type(Residualsmatrix))
    # print(Residualsmatrix.shape)
    print('灵敏度矩阵',SensitivityMatrix)








