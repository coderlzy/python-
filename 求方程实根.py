#输入一元二次方程的系数，求实根，设输入的系数保证有实根、
#ax^2+bx+c=0

from math import *
print("请按提示输入一元二次方程的三个系数：")
a=float(input("系数a="))
b=float(input("系数b="))
c=float(input("系数c="))

"""float x
a*pow(x,2)+b*x+c=0
print("方程实根为：",x)"""
#我以为定义一个没有赋值的变量x,有一个表达式，就可以直接求出x
#不行，还是要变换着x=的表达式才能求出值，因为运算符的格式是左边变量右边值

#判断方程是否有实根
if(b*b-4*a*c>=0):
    x1=(-b+sqrt(b*b-4*a*c))/(2*a)
    x2=(-b-sqrt(b*b-4*a*c))/(2*a)
    print("方程两实根分别为：x1=",x1,",x2=",x2)
else:
    print("此方程没有实根！")
