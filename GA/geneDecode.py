"""
    把80个节点索引对应生成80个节点ID
"""
def geneDecode(best_individual,nodesIndexs):
    """

    :param best_individual: 最好的个体
    :param nodesIndexs:节点字典
    :return:最好个体位置索引对应的节点ID  列表类型 len=80个
    """
    ID_Container=[]
    for nodeIndex in best_individual:
        nodeID=nodesIndexs.get(nodeIndex)
        ID_Container.append(nodeID)
    return ID_Container[:]

if __name__ == '__main__':
    """
    import sys
    sys.path.append('D:\keyanshuju\sensorsPlacementLayout\getPressureData')   #没有追加这个路径会报ModuleNotFoundError: No module named 'commandLine'错误
    from getPressureData.getMetrix import readSimulationNodes
    from geneEncoding import geneEncoding
    pop = geneEncoding(1, 80)
    # print(pop[0])
    # print(type(pop[0]))
    inpPath = "D:\keyanshuju\sensorsPlacementLayout\getPressureData\\ky8.inp"
    simuNodesIndex, nodesIndexs=readSimulationNodes(inpPath)
    ID_Container=geneDecode(pop[0],nodesIndexs)
    print(ID_Container)
    
    测试没问题
    
    """
