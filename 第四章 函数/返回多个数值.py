#python中的return语句可以返回多个数值

#编写函数计算三门课程的总分和平均分

def calculate(math,english,chinese):
    sum1=float(math+english+chinese)
    avr=sum1/3
    return sum1,avr                      #返回多个值

sumofgrade,gpa=calculate(99,78,66)       #调用函数的同时接收多个返回值

print("总成绩：",sumofgrade)
print("平均分：",gpa)

##函数的返回值仍是一个对象，但是这个对象是一个元组！
##多个变量可以同时接收一个元组的信息，按位置将元组中对应的值赋给这些变量~
