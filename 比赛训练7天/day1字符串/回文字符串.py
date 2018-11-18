#给出一个长度不超过1000的字符串，判断它是不是回文

str1=input("请输入一个字符串：")
if str1[::-1]==str1:
    print("Yes!")
else:
    print("No!")