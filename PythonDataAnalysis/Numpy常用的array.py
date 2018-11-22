import numpy as np

#数字矩阵
print(np.zeros([2,4]))
print(np.ones([3,5],float))

#随机数矩阵
print(np.random.rand(2,4))
#生成一个随机数
print(np.random.rand())

#生成范围内的随机整数
print(np.random.randint(1,20))
print(np.random.randint(1,20,5))  #生成5个数

#标准正态分布随机数
print(np.random.randn())
print(np.random.randn(2,4))

#生成有选择的随机数
print(np.random.choice([1,2,3,4,5,6]))
print(np.random.choice([1,2,3,4,5,6],3))

#beta分布
print(np.random.beta(1,10,3))

