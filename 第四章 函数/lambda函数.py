#lambda函数可以定义一个简单的函数
#函数名=lambda 参数：返回值

g1=lambda x,y:x+y
print(g1(5,4))

g2=lambda x,y=1,z=2:x+y+z
print(g2(7))

print((lambda x,y:x*y)(5,6))

