# 0.0 coding:utf-8 0.0
# 选择

import random
import numpy as np


#为方便求概率，适应度最小转化为最大求
def minTomax(fit_value):
    new_fit_value=[]
    for i in range(len(fit_value)):
        temp=1-fit_value[i]
        new_fit_value.append(temp)
    #print('minTomax',new_fit_value)
    return new_fit_value[:]

def cumsum(Probability_Container):
    sum = 0
    for i in range(len(Probability_Container)):
        sum += Probability_Container[i]
        Probability_Container[i] = sum


def selection(pop,fit_value):
    """
    :param pop: 500个个体，染色体长度为80
    :param fit_value: 数组长度为 500
    :return: 返回选择后的pop
    """
    new_fit_value=minTomax(fit_value)   #因越小值概率越大，故1-fit_value[i]就变换为大的，好求概率的比

    total=np.sum(new_fit_value)

    Probability_Container= []       # 先放置对应每个个体的概率列表，后转换为存放累计概率
    for i in range(len(new_fit_value)):     #求个体概率
        individual_Probability=new_fit_value[i]/total
        Probability_Container.append(individual_Probability)
    #print('Probability_Container',Probability_Container)
    cumsum(Probability_Container)       # 计算累计概率
    #print('---',Probability_Container)
    ms=[]
    pop_len = len(pop)
    for i in range(pop_len):        # 这里相当于转了500次轮盘其数值放在ms中
        ms.append(random.random())
    ms.sort()
    #print(ms)
    fitin = 0
    newin = 0       #已选择个体的个数
    newpop = pop
    # 转轮盘选择法
    while(newin<pop_len):   #如果选择的个体个数等于原种群的个数停止循环
        if(ms[newin]<=Probability_Container[fitin]):
            newpop[newin]=pop[fitin]
            newin+=1
        else:
            fitin+=1

    pop=newpop



if __name__ == '__main__':
    import operator
    a=np.arange(200).reshape(8,25)
    p=[0.7,0.5,0.3,0.2,0.1,0.05,0.04,0.0001]
    print(a)
    # sum=0
    # b=np.arange(175,200).reshape(1,25)

    for i in range(200):
        selection(a,p)
        # if(operator.eq(a[7],b[0])):
        #     sum+=1
        print('===%s'%i,a)

