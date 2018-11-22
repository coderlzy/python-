#encoding=utf-8

import numpy as np

def main():
    list1=[[1,3,5],[2,4,6]]
    print(type(list1))

    np_list1=np.array(list1)
    print(type(np_list1))

    print(np_list1.shape) #形状
    print(np_list1.ndim)  #维度
    print(np_list1.dtype) #类型
    print(np_list1.itemsize) #ndarray中每个元素的大小
    np_list1=np.array(list1,dtype=np.float)
    print(np_list1.dtype)
    print(np_list1.itemsize)  # ndarray中每个元素的大小
    print(np_list1.size) #一共有几个元素




main()