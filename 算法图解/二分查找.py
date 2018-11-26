#第一章
#二分查找：从中间开始找，运行时间O（log n）,适用于有序的元素列表

#二分查找
import time #我算下时间
def binary_search(list,item):
    low=0
    high=len(list)-1

    while low<=high:
        # mid=(low+high)/2  #这样写会报错，因为如果是基数就要取整
        # 应该这样
        mid = (low + high) // 2  # 自动向下取整
        guess = list[mid]  # 把中间位置转换成列表

        if guess==item:
            return mid  #这里返回位置
        if guess<item:
            low=mid+1
        else:
            high=mid-1
    return None   #程序运行遇到的第一个return返回，不会再运行第二个了

def main():
    starttime=time.time()
    list1=[1,3,4,6,8,9,12]
    print(binary_search(list1, 4))
    endtime=time.time()
    t=endtime-starttime
    print("用时：",t,"豪秒")

main()

