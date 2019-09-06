"""
    找出最优解和最优解的基因编码

"""
def best(pop, fit_value):
    best_individual = []
    best_fit = fit_value[0]
    best_individual = pop[0]
    for i in range(1,len(pop)):
        if(fit_value[i]<best_fit):
            best_fit=fit_value[i]
            best_individual=pop[i]
    return [best_individual,best_fit]

if __name__=='__main__':
    import numpy as np
    pop=np.arange(0,12).reshape(3,4)

    fit_value=list(range(3))
    print(pop)
    print(fit_value)
    best_individual, best_fit=best(pop,fit_value)
    print('最好的个体',best_individual)
    print('最好的适应度',best_fit)

