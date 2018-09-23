####求直角三角形的斜边长度
####用勾股定理
# python0102.py
# 2018
###########################
from math import * #导入函数库
a=float (input("请输入斜边1 的长度："))
b=float (input("请输入斜边2的长度："))
c=a*a+b*b
c=sqrt(c)#开方
print("三角形的斜边长度是：",c)
