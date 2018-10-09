#编写程序，求三个数中的最大数

#用时：5分钟

print("请按提示输入三个数，本题求其最大值")
a1=float(input("请输入第一个数："))
a2=float(input("请输入第二个数："))
a3=float(input("请输入第三个数："))
if(a1>a2):
    if(a1>a3):
        print("最大数为a1=",a1)
    else:
        print("最大数为a3=",a3)
elif(a2>a3):
    print("最大数为a2=",a2)
else:
    print("最大数为a3=",a3)
    
        
