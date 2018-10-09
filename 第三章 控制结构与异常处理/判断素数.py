#对输入的每一个数，判断是否为素数

n=int(input("请输入一个大于0的自然数："))
m=0  #计数
while(n>0):
    for i in range(2,n-1):
        if(n%i==0):
            print(n,"不是素数")
            break
        else:
            m+=1

    if(m==(n-2)):   #全都无法被整除
        print(n,"是素数")
        break
        
else:
    print("输入的不是大于零的自然数，请重新输入！")
    n=int(input("请输入一个大于0的自然数："))
    
        
