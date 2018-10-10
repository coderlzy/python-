#输入高度（行数），输出一个用*构成的等腰三角形

#从空格开始考虑

n=int(input("请输入高度(行数)n:"))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print("",end=" ")
    for k in range(n-i+1,n+i):
        print("*",end="")
    print("")

#这是我自己想出来的
#注意控制行数和列数的方法，使用嵌套，然后注意使用

#这是答案，用了函数
'''def showSanjiao(n):
    n = n+1
    for i in range(n):
        for j in range(0,n-i):
            print(end=' ')
        for k in range(n-i,n):
            print('*',end=' ')
        print('')
 
m= int(input('输入行数：'))
showSanjiao(m)'''

