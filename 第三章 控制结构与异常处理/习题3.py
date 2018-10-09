#输入一个正整数n，利用for语句，计算n!

#用时：3分钟
try:
    n=int(input("请输入一个正整数n:"))
    sum1=1
    for i in range(1,n+1):
        sum1*=i
    print("n=",n,",",n,"!=",sum1)
except ValueError:
    print("输入错误，应该输入正整数")
        
