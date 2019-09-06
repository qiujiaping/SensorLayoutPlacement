# 交配（重组）

import random


def crossover(pop,pc):
    """
    :param pop: 种群形状500*80，二维数组
    :param pc:
    :return:
    """
    pop_len = len(pop)
    s=0
    for i in range(pop_len - 1):
        rd=random.random()
        # print('随机数',rd)
        if (rd < pc):
            s=s+1
            # print('s',s)
            cpoint = random.randint(0, len(pop[i]))
            #print('割点',cpoint)
            temp1 = []
            temp2 = []
            temp1.extend(pop[i][0:cpoint])
            # intersection有可能为空
            intersection=list(set(pop[i][0:cpoint])&set(pop[i + 1][cpoint:len(pop[i])]))    #不同染色体上下割点不同侧两段的交集
            differenceSet=list(set(intersection) ^ set(pop[i + 1][cpoint:len(pop[i])]))      ##被搬运那段染色体上同割点一侧差集
            #print('上交集长', len(intersection))
            #print('下差集长', len(differenceSet))
            if (len(intersection) == 0):    #intersection为空,上下片段不相同
                temp1.extend(pop[i + 1][cpoint:len(pop[i])])

            if(len(intersection)!=0):
                #print('上交集',intersection)
                #print('下差集',differenceSet)
                s1 = []
                while (len(s1) < len(intersection)):  # 随机生成的不重复的数字，代表选择传感器的位置,对应索引。大小为chrom_length个代表50个传感器
                    x = random.randint(1, 1317)  # 因有1317个索引位置，故生成的位置可能介于1-1317之间
                    if x not in pop[i][0:cpoint]:
                        s1.append(x)
                temp1.extend(s1)
                temp1.extend(differenceSet)

            temp2.extend(pop[i + 1][0:cpoint])
            intersection=list(set(pop[i+1][0:cpoint])&set(pop[i][cpoint:len(pop[i])]))    #不同染色体上下割点不同侧两段的交集
            differenceSet=list(set(intersection) ^ set(pop[i][cpoint:len(pop[i])]))      ##同一段染色体上同割点一侧差集
            if (len(intersection) == 0):    #intersection为空,上下片段不相同)
                temp2.extend(pop[i][cpoint:len(pop[i])])
            if(len(intersection) != 0):
                s2 = []
                while (len(s2) < len(intersection)):  # 随机生成的不重复的数字，代表选择传感器的位置,对应索引。大小为chrom_length个代表50个传感器
                    x = random.randint(1, 1317)  # 因有1317个索引位置，故生成的位置可能介于1-1317之间
                    if x not in pop[i+1][0:cpoint]:
                        s2.append(x)
                temp2.extend(s2)
                temp2.extend(differenceSet)
            #print('temp1', len(temp1))
            #print('temp2', len(temp2))
            pop[i] = temp1
            pop[i + 1] = temp2
if __name__ == '__main__':
    from geneEncoding import geneEncoding
    import operator
    import numpy as np

    pop = geneEncoding(500, 80)
    import time
    start = time.clock()  # 开始计时
    print('重组前',pop)
    a = np.array(pop[:])
    crossover(pop,0.6)
    print('重组后',pop)
    b = np.array(pop[:])

    print(a-b)
    end = time.clock()
    print('Running time: %s Seconds' % (end - start))


