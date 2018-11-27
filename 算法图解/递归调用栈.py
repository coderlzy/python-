#原来递归的原理就是用到栈，函数调用其实就是进入调用栈，再弹出来返回东西

#求阶乘
def fact(x):
    if x==1:
        return 1
    else:
        return x*fact(x-1)

def main():
    print(fact(6))

main()