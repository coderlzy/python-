#用户输入一个4位的整数，如果是回文数显示True，如果不是回文数显示False
#回文数就是反过来和正着的数字是相同的，比如1221

##算法思想：
##1、输入四位数
##2、提取四位数的四个数字abcd
##3、用dcba组合出新数字
##4、比较新旧是否一样

num1=int(input("请输入一个四位数的整数："))
a=num1//1000
b=num1//100%10
c=num1//10%10
d=num1%10
num2=int(d*1000+c*100+b*10+a)
if(num1==num2):
    print("True")
else:
    print("False")


#也可以用result==(num1==num2)
#==的返回值就是True or False

num1=int(input("请输入一个四位数的整数："))
a=num1//1000
b=num1//100%10
c=num1//10%10
d=num1%10
num2=int(d*1000+c*100+b*10+a)
result=(num1==num2)
print("回文判断结果：",result)

