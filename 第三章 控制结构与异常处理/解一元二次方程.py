#解决一元二次方程，输入系数abc，如果有实根显示，没有实根显示没有

from math import *

##输入不是数字的时候，我抛出异常了
try:
    print("求一元二次方程ax^2+bx+c=0的根")
    a=float(input("请输入一元二次方程系数a="))
    b=float(input("请输入一元二次方程系数b="))
    c=float(input("请输入一元二次方程系数c="))
    print("您输入的方程为：%dx*x+%dx+%d=0"%(a,b,c))

    while(a==0 and b==0):
        print("输入的系数不构成方程，请重新输入：")
        a=float(input("请输入一元二次方程系数a="))
        b=float(input("请输入一元二次方程系数b="))
        c=float(input("请输入一元二次方程系数c="))

    
    if(a==0):
        x=-(c/b)
        print("此方程为一次方程，根为：",x)
    elif(b*b-4*a*c>=0):
        x1=(-b+sqrt(b*b-4*a*c))/2*a
        x2=(-b-sqrt(b*b-4*a*c))/2*a
        ##保留三位小数
        x1=float('%10.3f'%x1)
        x2=float('%10.3f'%x2)
        print("有实根，一元二次方程两实根分别为：x1=",x1,",x2=",x2)
    else:
        x1=(-b)/(2*a)                   #实部
        x2=(sqrt(-(b*b-4*a*c)))/2*a          #虚部

        #转换精度，只保留三位小数
        x1=float('%10.3f'%x1)
        x2=float('%10.3f'%x2)
        print("没有实根，有复根，他们分别是：",end="")  #不换行，end默认换行，现在给个空格
        print("x1=",complex(x1,x2),",x2=",complex(x1,-x2))

except ValueError:
    print("输入了非法数据！")

