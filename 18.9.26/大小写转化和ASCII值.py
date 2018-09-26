#将大写字母转换为小写字母并显示ascii值
##判断大小写，用ascii码，a-z的是97-122，A-Z的是65-90
##ord()：输出ascii码， chr()，返回ascii对应的字符

"""ch=input("请输入一个字母：")
a1=ord(ch)
if(a1<ord("a")):
    b1=chr(a1+32)
    print(ch,"是大写字母，转换为小写字母的结果是：",b1)
    print(ch,"的ASCII码是：",a1,",",b1,"的ASCII码是：",a1+32)
else:
    print(ch,"是小写字母")"""

##python的多行注释："""括起来"""


##这个不完善，因为没有考虑到在[97,122]和[65,90]范围之外的就不是字母了
##改进一下

ch=input("请输入一个字母：")
a1=ord(ch)
while(ord("Z")<a1<ord("a") or a1>ord("z") or a1<ord("A")):
    print("您输入的不是字母，请重新输入")
    ch=input("请输入一个字母：")
    a1=ord(ch)
if(a1<ord("a")):
    b1=chr(a1+32)
    print(ch,"是大写字母，转换为小写字母的结果是：",b1)
    print(ch,"的ASCII码是：",a1,",",b1,"的ASCII码是：",a1+32)
else:
    print(ch,"是小写字母")
