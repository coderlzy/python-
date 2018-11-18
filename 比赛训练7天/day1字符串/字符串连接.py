#不借用任何字符串库函数实现无冗余地接受两个字符串，然后把它们无冗余的连接起来。

#str1=input("请输入第一个字符串：")
#str2=input("请输入第二个字符串：")
#print(str1+str2)

str1=input("请输入两个字符串，空格隔开：")
list1=str1.split(" ")
s1=""
for i in list1:
    s1+=str(i)
print(s1)
