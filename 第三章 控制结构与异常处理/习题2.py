#输入一个整数，判断这个数是正数、负数、还是0

#用时：2分钟

#没有判断输入的是否是正整数

try:
    n=int(input("请输入一个整数："))
    
    if(n>0):
        print(n,"是正数")
    elif(n<0):
        print(n,"是负数")
    else:
        print("这个数是0")
except ValueError:
    print("输入错误，请输入一个正整数！正整数！")


