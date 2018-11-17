#输入字符串然后倒置
str1=input("请输入字符串：")
list1=str1.split(" ") #把字符串分割放入列表
list1.reverse()  #反转列表
for i in list1[:(len(list1)-1)]:
    print(i,end=" ")
for i in list1[(len(list1)-1):len(list1)]:
    print(i,end="")


#方法2
str2=input("方法二请输入字符串：").split(" ")
s=" ".join(str2[::-1]) #join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串
print(s)