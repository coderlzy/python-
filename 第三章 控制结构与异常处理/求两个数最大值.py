#从键盘键入两个数，求他们的最大值

num1=input("please input the first number:")
num2=input("plesse input the second number:")
if(num1>num2):
    print("the big number is:",num1)
else:
    print("the big number is:",num2)
    
##课本写法
num1=input("please input the first number:")
num2=input("plesse input the second number:")
max_num=num1
if (max_num<num2):
    max_num=num2
    
print("the big number is:",max_num)


