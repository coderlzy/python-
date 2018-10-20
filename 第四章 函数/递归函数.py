#简单的递归函数例子 求n！

def f(n):
    if n==1:
        return 1
    return n*f(n-1)
n=int(input("请输入一个整数n："))
print("n!=",f(n))
