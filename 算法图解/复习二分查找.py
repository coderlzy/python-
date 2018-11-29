#隔天，自己敲一遍二分查找
#前提是有序数列

def binary_search(list,item):
    low=0
    high=len(list)-1
    while low<=high:
        mid = (low + high) // 2  # 位置
        find = list[mid]  # mid位置对应的元素
        if find==item:  #item是目标元素
            return mid  #返回位置
        if find>item:
            high=mid-1
        if find<item:
            low=mid+1
    return None

def main():
    list1=[1,4,9,12,25,67,99,101]
    print(binary_search(list1,12))

main()

