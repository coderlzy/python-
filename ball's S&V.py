#输入球体半径，计算球体表面积和体积并输出，版半径为实数
from math import *
print("计算球体表面积和体积")
## 错误写法：float r=input("请输入球体半径，半径为实数：")
##invalid syntax:float ss=4*pi*r*r
##invalid syntax:float v=(4*pi*r*r)/3
r=float(input("请输入球体半径，半径为实数："))
#if (r.isdigit()):    ###判断我是不是实数我暂时还不Ok,这个搁置，有空解决
    #s=4*pi*r*r
    #v=(4*pi*r*r*r)/3
#else:
   #r=input("您输入的半径不是数字，请重新输入：")
s=4*pi*r*r
v=(4*pi*r*r*r)/3
print("球体表面积为：",s)
print("球体体积为：",v)
