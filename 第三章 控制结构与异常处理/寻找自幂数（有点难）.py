#寻找自幂数。用户输入位数n，找出并显示出所有n位数的自幂数。
#自幂数是一个n位正整数，它的各位数字的n次方的和加起来还等于这个数。

from math import *
n=int(input("请输入正整数的位数n（限制1-6之间，大于6退出程序）："))
d=0    #记分离的位数上的数
m=0    #用来分离位数
start=0 #n位数的最小值
end=0  #n位数的最大值

while(0<n<7):
# n 位数的最小值和最大值，我要依次遍历每个数字，从最小到最大
    start=int(pow(10,n-1))
    end=int(pow(10,n)-1)
    print(n,"位数的自幂数有：")
    
    
    for i in range(start,end+1):
    
        m=i ##################??!!
        sum1=0 #各位数的和
        while m!=0:
            d=m%10
            sum1=sum1+pow(d,n)
            m=m//10
        if sum1==i:
            print(str(i),end=" ") ##str()函数：将对象转化为适于人阅读的形式
    print(" ")
    n=int(input("请输入正整数的位数n（限制1-6之间，大于6退出程序）："))
    #为了持续输入~

else:
    print("输入的位数超出6位数，程序结束")

