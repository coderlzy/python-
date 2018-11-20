#编程实现两个字符串s1和s2的字典序比较。（保证每一个字符串不是另一个的前缀，且长度在100以内）。
# 若s1和s2相等，输出0；若它们不相等，则指出其第一个不同字符的ASCII码的差值：
# 如果s1>s2，则差值为正；如果s1<s2，则差值为负。

#输入样例: java basic
#输出：8
import operator
str1=input("请输入两个字符串，空格隔开：")
list1=str1.split(" ")
s1=list1[0]
s2=list1[1]
a1=ord(s1[0])
a2=ord(s2[0])

if operator.eq(s1,s2):
    print("0")
else:
    print(a1-a2)




