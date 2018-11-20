#验证哥德巴赫猜想：任何一个超过2的偶数都可以写成2个素数之和，如4=2+2，8=5+3等
#要求根据用户输入的偶数N，找出其素数和的分解形式

def main():
    #输入待验证的偶数
    n=int(input("请输入一个大于2的偶数："))
    while n < 3 or n%2!=0:
        print("您输入的不是偶数，请重新输入！")
        n=int(input("请输入一个大于2的偶数："))

    #生成素数表
    s=set()  #创建空集
    for i in range(2,n+1):
        s.add(i)
    for i in range(2,n+1):

        #这里比较难，删除除i之外i的所有倍数
        if i in s:
            for k in range(2*i,n+1,i):
                if k in s:
                    s.remove(k)

    #验证该偶数是否能分解为两个素数之和
    for i in s:
        f=n-i  #分解：一个和数+一个素数
        if f>i and f in s:
            print(n,"=",i,"+",f)

main()