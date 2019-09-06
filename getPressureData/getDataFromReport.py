import re
import numpy as np
#'  [0-9]'=regularMatchNodeAndLink getDataFromRptNormal(rptPathNormal, 1, 3, '  [0-9]',when)
#从正常报告得到数据
def getDataFromRptNormal(rptpathBeforeLeak,pressureIndex,regularMatchNodeAndLink,when):
    """
    :param rptpathBeforeLeak: 正常工况下水力计算输出报告文件路径
    :param pressureIndex: 节点压力信息列号索引

    :param regularMatchNodes: 节点正则表达式匹配条件
    :return:pressureDataNormalOneTime
    """
    f1 = open(rptpathBeforeLeak, "r")
    fileList1 = f1.readlines()	#读取数据生成list，每个单元为一行
    pressureDataNormal=[]		#放置全部时刻的压力数据

    
    rMatchNodes='  Node Results'  #以文本中空白行为分界线进行匹配

    pattern = re.compile(regularMatchNodeAndLink)  # 正则匹配 只选取有节点的数据行
    end=re.compile('  O-Pump')
    patternNodes=re.compile(rMatchNodes)
    n=0		#记录记录了多少次节点压力数据
    row=0  #记录读取到哪一行
    readOne=0
    columnPressure=[]  #记录压力值所在列数据
    #judgeNodeOrLink=0   #相当于开关。
    for line in fileList1:
        str = line
		#匹配节点
        match = re.match(pattern, str, flags=0)
		#通知节点开始记录（标记）。
        isNodeResults=re.match(patternNodes,str,flags=0)
        isPump=re.match(end, str, flags=0)
        row+=1

        if(row>397):
            if (n>0 and isNodeResults):
                n=0
            if(isPump and n==1317):
                pressureDataNormal.append(columnPressure[:])
                columnPressure.clear()
                readOne += 1
                n += 1
            if (n > 1317):
                continue
            if(match):
                line = line.split()
                columnPressure.append(float(line[pressureIndex]))
                n +=1
    np.set_printoptions(suppress=True)      # 取消科学计数法
    pressureDataNormal = np.array(pressureDataNormal)  # 转化为np矩阵
    pressureDataNormalOneTime=[]
    pressureDataNormalOneTime=pressureDataNormal[when]   #取出某一时刻的漏损前压力数据

    f1.close()

    return pressureDataNormalOneTime   #返回某一个时刻正常的压力数据 类型<class 'numpy.ndarray'>如[1 2 3 4]


#从泄露报告得到数据
def getDataFromRptAfterLeak(rptpathAfterLeak,pressureIndex,regularMatchNodes,when):
    """
    :param rptpathAfterLeak: 模拟漏损后水力计算输出报告文件路径
    :param pressureIndex: 压力数据所在列索引号
    :param regularMatchNodes: 节点正则表达式匹配条件
    :return:
    """
    #从漏损后生成的文件中读取压力数据，构成矩阵
    f2 = open(rptpathAfterLeak, "r")
    fileList2 = f2.readlines()
    pressureDataAfterLeak = []
    Nodes = re.compile(regularMatchNodes)  # 正则匹配 只选取有节点数据的行
    rMatchNodes='  Node Results'
    end = re.compile('  O-Pump')
    patternNodes=re.compile(rMatchNodes)

    n = 0
    row = 0  # 记录读取到哪一行
    columnPressure2 = []
    for line2 in fileList2:
        str2 = line2
        matchOfNodes = re.match(Nodes, str2, flags=0)
        NodeResults=re.match(patternNodes,str2,flags=0)
        isPump = re.match(end, str2, flags=0)

        row += 1
        if(row>362):
            if (n>0 and NodeResults):
                n=0
            if (isPump and n == 1317):
                pressureDataAfterLeak.append(columnPressure2[:])
                columnPressure2.clear()
                n += 1
            if (n > 1317):
                continue
            if matchOfNodes:
                line2 = line2.split()  # 以空格区分一行内的字符串
                columnPressure2.append(float(line2[pressureIndex]))  # 压力数据的索引列
                n +=1

    np.set_printoptions(suppress=True)  # 取消科学计数法
    pressureDataAfterLeak = np.array(pressureDataAfterLeak)  # 转化为np矩阵
    pressureDataAfterLeakOneTime=[]
    if(len(pressureDataAfterLeak)):
        pressureDataAfterLeakOneTime = pressureDataAfterLeak[0]  # 取出某一次漏损下，0时刻的压力数据为矩阵
    f2.close()

    return pressureDataAfterLeakOneTime

if __name__ == "__main__":
    # pressureDataNormalOneTime=getDataFromRptNormal('CommandLineNormal.rpt', 3, '  J-', 0)
    pressureDataAfterLeakOneTime=getDataFromRptAfterLeak("CommandLineLeak.rpt", 3, '  J-', 0)
    print(len(pressureDataAfterLeakOneTime))
    print(pressureDataAfterLeakOneTime)