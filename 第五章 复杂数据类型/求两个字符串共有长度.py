#输入两个字符串，求两个字符串共有的最长子串。

s1=input("字符串1：")
s2=input("字符串2：")
r=""  #存放公共字符串
m=0   #最长字符串的长度

if (len(s1)>len(s2)):
    min_s=s2
    max_s=s1
else:
    min_s=s1
    max_s=s2

#比较S1,S1长度，遍历短的字符串比较省时间

for i in range(0,len(min_s)):
    for j in range(i,len(min_s)+1):
        if min_s[i:j] in max_s and j-i>m:
            r=min_s[i:j]
            m=j-i
print("共有最长字符串为：",r)
