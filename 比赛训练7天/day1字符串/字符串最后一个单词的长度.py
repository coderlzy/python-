#计算字符串最后一个单词的长度，单词以空格隔开。

str1=input("请输入字符串：")
list1=str1.split(" ")
count=0
lenght=0
for i in range(len(list1)):
    count+=1

str2=list1[count-1]
for i in str2:
    lenght+=1
print(lenght)