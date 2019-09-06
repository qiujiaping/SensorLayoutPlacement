import numpy as np

if __name__=='__main__':
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    # s = np.zeros((1317), dtype=np.int)
    # s=np.diag(s)

    # data=np.arange(16).reshape(4,4)
    # e=np.eye(4)
    # for i in range(2):
    #     r=np.random.randint(3)
    #     e[r][r]=0
    # print(e)
    # print(data)
    # print(data.dot(e))
    #
    # def f(a):
    #     b=a
    #     for i in range(len(b)):
    #         b[i]=i
    #     a=b
    # a = np.array([[4,5,6],[7,8,9]])
    # f(a)
    # # print(a)
    # b=np.arange(1,3 ).reshape(1, 2)
    # c=b[0]
    # # print(c)
    # X = []
    # Y = []
    # results=[x*x for x in range(-15,15)]
    # for i in range(30):
    #     X.append(i)  # x代表代数
    #     t = results[i]  # t代表每代的最佳适应度
    #     Y.append(t)
    #
    # plt.plot(X, Y)
    # plt.show()
pressureDataNormal=[[1,2,3,4],[5,6,7,8]]
pressureDataNormal = np.array(pressureDataNormal)  # 转化为np矩阵
pressureDataNormalOneTime=[]
pressureDataNormalOneTime=pressureDataNormal[0]   #取出某一时刻的漏损前压力数据
print(type(pressureDataNormalOneTime))
print(pressureDataNormalOneTime.shape)
print(pressureDataNormalOneTime)




