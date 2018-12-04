#快速排序
#思路：分区，对中间值左边和右边的再快速排序
#基线条件：数组空或只有一个元素

def quicksort(arr):
    #less=[]
    #bigger=[]
    if len(arr)<2:
        return arr
    else:
        pivot=arr[0]
        """for i in arr[1:]:
            if i<=pivot:
                less.append(i)
            if i>pivot:
                bigger.append(i)"""
        #以上绿色部分，书上是这样写的；
        less = [i for i in arr[1:] if i <= pivot]
        bigger = [i for i in arr[1:] if i > pivot]
        #???????为什么可以这么写呢
        """哈哈哈我知道了！这个是python的列表生成式！"""

        #这里不小心报错了
        #return quicksort(less)+pivot+quicksort(bigger)
        #can only concatenate list (not "int") to list 只能将列表连接到列表，而不能将数连接，pivot少了中括号
        return quicksort(less) + [pivot] + quicksort(bigger)

def main():
    array1=[5,6,2,19,10]
    print(quicksort(array1))

main()
