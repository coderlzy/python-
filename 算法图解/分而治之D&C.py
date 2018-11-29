#D&C原理：1、找出最简单的基线条件，一般是空数组或只包含一个元素的数组
#2、不断缩小规模直到符合基线条件
#递归问题的解决方式

#编写sum(2,4,6)的算法
print("4.1练习")

def sum(arr):
    if arr==[]:
        return 0
    else:
        i=arr[0]
        del arr[0]
    return i+sum(arr)

def main1():
    arr1=[2,4,6]
    print("元素之和为：",sum(arr1))

main1()

#卧槽居然自己写出来递归了！

#编写一个递归函数来计算列表包含的元素数
print("4.2练习")

#基线条件：list中没有元素
def countnum(list):
    if list==[]:
        return 0
    else:
        del list[0]
        count=1+countnum(list)
    return count

#更优化的答案：就每次都往后移开一个，不用每次都删除了
#def count（list）：
    #if list==0:
        #return 0
    #else:
        #return 1+count(list[1:])


def main2():
    list1=[2,9,11,2,4,6,7,22]
    print("元素个数为：",countnum(list1))

main2()


#找出列表中的最大数字
print("4.3练习")

#基线条件：最大
max=0
def findmax(list):
    if len(list)==2:
        if list[0]>list[1]:
            return list[0]
        else:
            return list[1]
    sub_max=findmax(list[1:]) #这里，程序第一次执行到这里的时候，就已经调用了N次findmax了，不停调用执行上面那段，已经找出最大的了
    if list[0]>sub_max:       #接下来就用那个最大的去比较了
        return list[0]
    else:
        return sub_max
#牛皮，不是我自己想出来的，看答案的

def main3():
    list1=[5,3,2,89,13,4,27]
    print(findmax(list1))

main3()

