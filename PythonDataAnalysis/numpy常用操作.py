#Array Opes

import numpy as np

#产生一个等差数列
print(np.arange(1,11,2)) #差是2
print(np.arange(1,11).reshape([5,2]))

#axis=？对不同层次求和

list1=np.array([[[1,2,3,4,],[4,5,6,7]],[[5,6,7,8,],[8,9,10,11]],[[11,12,13,14],[15,16,17,18]]])
print()
print()
print(list1.sum(axis=2))
print(list1.sum(axis=1))
print("最外层")
print(list1.sum(axis=0))
print("最大")
print(list1.max(axis=0))
print("最小")
print(list1.min(axis=2))

#加减乘除乘方

list1=np.array([1,2,3,4])
list2=np.array([10,20,30,40])
print("加减乘除")
print(list1+list2)
print(list1-list2)
print(list1*list2)
print(list1/list2)
print(list1**3)

#连接
print("点乘")  #矩阵的乘法
print(np.dot(list1.reshape([2,2]),list2.reshape([2,2])))

print("连接一行，concatenate")
print(np.concatenate((list1,list2)))
print("连接两行，vstack")
print(np.vstack((list1,list2)))
print("连接一行，hstack")
#print(np.hstack(list1,list2)) #注意这些个hstack（）,vstack（）,concatenate()括号里还要括号（list1,list2）才可以
print(np.hstack((list1,list2)))

#拆分
print("拆分成几分")
print(np.split(list1,2))

#复制
print("复制")
print(np.copy(list1))
