#   变异
import random

def mutation(pop, pm):  #变异
    pop_length = len(pop)
    chrom_length = len(pop[0])
    for i in range(pop_length):
        if (random.random() < pm):
            a=i
            # print('sss')
            mpoint = random.randint(0, chrom_length - 1)  # mpoint[0-79]
            flag=0
            # print(pop[i])
            while(flag==0):
                x = random.randint(1, 1317)
                if(x not in pop[i]):
                    pop[i][mpoint]=x
                    # print('变异点',mpoint)# 报错，当10节点漏，迭代10代list assignment index out of range
                    # print('x',x)
                    flag = 1
                    # print(pop[i])

if __name__ == '__main__':
    from geneEncoding import geneEncoding
    import time
    import operator
    import numpy as np

    start = time.clock()  # 开始计时
    pop=geneEncoding(100,5)
    print(pop)
    mutation(pop,0.01)
    print(pop)



    # print(pop)


