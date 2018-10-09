#对列表x中的元素求和，舍弃数值为2的元素，并将得到的结果输出

# pass的作用是：什么也不做

x=[1,2,3,4,5]
sum1=0
for i in x:
    if(i==2):
        pass
    else:
        sum1+=i
        print("the number is :",str(i))
print("sum=",sum1)
