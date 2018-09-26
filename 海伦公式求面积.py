#2.1输入三角形三边长，用海伦公式求面积
#p=(a+b+c)/2,s=sqrt(p*(p-a)*(p-b)*(p-c))

"""from math import *
print("请按提示输入三角形三边长")
a=float(input("第一个边长："))
b=float(input("第二个边长："))
c=float(input("第三个边长："))
p=(a+b+c)/2
s=sqrt(p*(p-a)*(p-b)*(p-c))
print("由海伦公式求得三角形面积为：",s)"""

##程序改进，输入数据合理化，三角形两边之和大于第三边

from math import *
print("请按提示输入三角形三边长")
a=float(input("第一个边长："))
b=float(input("第二个边长："))
c=float(input("第三个边长："))
##判断输入的数是否构成三角形，比较两边之和是否大于第三边
##思路：比较三个数大小，两两比较，选出最大的，另外两个小的求和于最大的比较
"""if(a>b):
    if(a>c):
        if(a>b+c):
            p=(a+b+c)/2
            s=sqrt(p*(p-a)*(p-b)*(p-c))
            print("由海伦公式求得三角形面积为：",s)
        else:
            #重新输入
    else if(c>a+b):
        p=(a+b+c)/2
            s=sqrt(p*(p-a)*(p-b)*(p-c))
            print("由海伦公式求得三角形面积为：",s)
        else:
            #重新输入
else if(b>c):
     if(b>a+c):
          p=(a+b+c)/2
          s=sqrt(p*(p-a)*(p-b)*(p-c))
          print("由海伦公式求得三角形面积为：",s)
        else:
            #重新输入
    else:"""
##这样太复杂的写不下去了

while(a>b and a>c):
    if(a<b+c):
        p=(a+b+c)/2
        s=sqrt(p*(p-a)*(p-b)*(p-c))
        print("由海伦公式求得三角形面积为：",s)
        break  ##之前忘记写break，循环着停不下来了，哈哈哈！
        
    else:
        print("输入的数据不构成三角形，请重新输入！")
        a=float(input("第一个边长："))
        b=float(input("第二个边长："))
        c=float(input("第三个边长："))


while(b>a and b>c):
    if(b<a+c):
        p=(a+b+c)/2
        s=sqrt(p*(p-a)*(p-b)*(p-c))
        print("由海伦公式求得三角形面积为：",s)
        break
        
    else:
        print("输入的数据不构成三角形，请重新输入！")
        a=float(input("第一个边长："))
        b=float(input("第二个边长："))
        c=float(input("第三个边长："))        

while(c>a and c>b):
    if(c<a+b):
        p=(a+b+c)/2
        s=sqrt(p*(p-a)*(p-b)*(p-c))
        print("由海伦公式求得三角形面积为：",s)
        break
        
    else:
        print("输入的数据不构成三角形，请重新输入！")
        a=float(input("第一个边长："))
        b=float(input("第二个边长："))
        c=float(input("第三个边长："))     

##这样可以，但是还是太复杂了，求小许帮我想更简单的方法！
