#在屏幕输出m行n列由某种符号构成的空心矩形

#这个是我上个星期看过书的，然后今天自己写出来了，虽然写了10分钟

def drawpic(m,n=5,char='*'):
    for i in range(1,n+1): #打印第一行
        print(char,end="")
    print()

     #打印中间m-2行
    for i in range(1,m-1):
        print(char,end="")
        for j in range(2,n):
            print(" ",end="")
        print(char)
    
     #打印最后一行
    for i in range(1,n+1):
        print(char,end="")
    print()

drawpic(3)
drawpic(m=6,n=4,char="@")
drawpic(m=4,n=6,char="#")

        
