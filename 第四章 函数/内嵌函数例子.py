#内嵌函数的例子

def f1():
    x=y=2
    def f2():
        y=3
        print("f2函数内x=",x)
        print("f2函数内y=",y)
    f2()
    print("f1函数内X=",x)
    print("f1函数内Y=",y)
f1()
