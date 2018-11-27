#图解算法第二章：选择排序，每次都找到最小元素，放入新列表，运算时间O（n^2）
#排序之后才能进行二分查找

#找出最小元素
def findsmallest(arr):

    #smallest=0  #这里有问题，不是直接0，而是等于第一个位置的！

    smallest=arr[0]
    smallest_index=0  #元素和位置初始化零
    for i in range(len(arr)):
        if arr[i]<smallest:
            smallest=arr[i]
            smallest_index=i
    return smallest_index  #返回最小元素的位置  #aaaaa这里我放错位置了！放到循环体内就不循环了！

#放入新的数组
def arrangearr(arr):
    newarr=[] #新数组初始化
    for i in range(len(arr)):
        smllest=findsmallest(arr)
        newarr.append(arr.pop(smllest))  #调用函数输出并删除,放入新数组中 pop()函数：如 L.pop([i])/arr.pop(i)
    return newarr

def main():
    arr1=[5,3,6,2,9]
    print(arrangearr(arr1))

main()

