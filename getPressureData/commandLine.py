import os
# from getDataFromReport import getDataFromRptBeLeak
# from getDataFromReport import getDataFromRptAfterLeak

def callCommandLineLeak(exePath, choose,inpPath, rptPathAfterLeak,setFlow,nodeIndex):   #调用命令行，模拟泄露
    """
    :param exePath: EPANET的exe文件路径
    :param inpPath: inp管网模型文件路径
    :param rptPathAfterLeak: 漏损模拟后输出报告
    :param setFlow: 设置漏损流量以计算流量系数
    :param nodeIndex:  模拟漏损的位置
    :return:
    """
    t = exePath + " " + str(choose)+" "+inpPath + " " + rptPathAfterLeak+" "+str(setFlow)+" "+str(nodeIndex)
    os.system(t)


def callCommandLineNormal(exePath,choose,inpPath,rptPath):      #调用命令行，正常状态下
    t =exePath + " "+str(choose)+" " + inpPath + " "+rptPath
    os.system(t)

if __name__ == "__main__":

    '''
    inpPath = "ky8.inp"
    exePath2 ="E:/n/epanetSimulation/Debug/EpanetSimulation.exe"
    rptPath = "After_p2.rpt"
    setFlow=6.3
    matrixAfterLeak=[]
    matrixFlow=[]

    callCommandLine(exePath2, inpPath, rptPath, setFlow, 1)
    list1,list2= getDataFromRptAfterLeak(rptPath,1, '  P',1,'  J')
    matrixAfterLeak.append(list1[:])
    matrixFlow.append(list2[:])

    print(len(matrixAfterLeak))
    print(len(matrixAfterLeak[0]))
    print(matrixAfterLeak[0])
    print(matrixFlow)
    print(len(matrixFlow))
    print(len(matrixFlow[0]))
	
    '''
    exePath = "D:\keyanshuju\EpanetSimulation\Debug\EpanetSimulation.exe"
    inpPath ="ky8.inp"
    rptLeakPath = "CommandLineLeak.rpt"
    rptNormalPath="CommandLineNormal.rpt"
    # callCommandLineNormal(exePath,1, inpPath, rptNormalPath)
    callCommandLineLeak(exePath,2,inpPath,rptLeakPath,6.3,10)













