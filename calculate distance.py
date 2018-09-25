#输入平面上两点的坐标（x1,y1）(x2,y2),计算两点距离并输出
from math import *
#绝对值 abs（x）

print("请按提示输入两点坐标")
x1=float(input("输入第一个点的横坐标："))
y1=float(input("输入第一个点的纵坐标："))
x2=float(input("输入第二个点的横坐标："))
y2=float(input("输入第二个点的纵坐标："))
a=abs(x1-x2)
b=abs(y1-y2)
l=sqrt(a*a+b*b)
print("点(",x1,",",y1,")","和点（",x2,",",y2,")的距离为：",l)

##这题我觉得自己做得不错，嘻嘻
##第一张最后一题终于写完了，速度真的蜗牛一般
