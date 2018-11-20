#求出5个字符串中最长的字符串。每个字符串长度在100以内，且全为小写字母。
#输入样例: one two three four five
#输出样例：three

str1=input("请输入字符串：")
list1=str1.split(" ")
lengh=0
s=""
for i in range(len(list1)):
    if len(list1[i])>lengh:
        lengh=len(list1[i])
        s=list1[i]
print(s)
