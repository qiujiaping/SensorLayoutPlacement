# 0.0 coding:utf-8 0.0
import random
def geneEncoding(pop_size,chrom_length):
    """

    :param pop_size: 种群规模
    :param chrom_length: 染色体长度
    :param nodesIndexs: 节点索引，ID
    :param validSimuNodesID: 模拟泄露节点索引
    :return: 种群

    """
    pop=[]  #存放个体的种群容器
    for i in range(pop_size):
        s=[]                             #个体
        while(len(s)<chrom_length):     #随机生成的不重复的数字，代表选择传感器的位置,对应索引。大小为chrom_length个代表50个传感器
            x = random.randint(1, 1317)  #因有1317个索引位置，故生成的位置可能介于1-1317之间
            if x not in s:
                s.append(x)
        pop.append(s)
    return pop[:]                       #pop=[500*80]二维数组（列表）

if __name__ == '__main__':
    pop_size = 500		# 种群数量
    chrom_length = 80		# 染色体长度
    pop=geneEncoding(pop_size, chrom_length)
    print(pop)
    print(len(pop))
    print(type(pop))


