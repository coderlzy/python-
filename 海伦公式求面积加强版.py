from math import *

isTriangle = False
while not isTriangle:
    print("请按提示输入三角形三边长")
    a = float(input("第一个边长："))
    b = float(input("第二个边长："))
    c = float(input("第三个边长："))
    if a == max(a, b, c):
        if a < b + c:
            isTriangle = True
        else:
            isTriangle = False
            print("不是三角形，请重新输入")
            continue

    if b == max(a, b, c):
        if b < a + c:
            isTriangle = True
        else:
            isTriangle = False
            print("不是三角形，请重新输入")
            continue

    if c == max(a, b, c):
        if c < a + b:
            isTriangle = True
        else:
            isTriangle = False
            print("不是三角形，请重新输入")
            continue

p = (a + b + c) / 2
s = sqrt(p * (p - a) * (p - b) * (p - c))
print("由海伦公式求得三角形面积为：", s)
