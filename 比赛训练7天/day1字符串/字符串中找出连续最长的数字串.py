#读入一个字符串str，输出字符串str中的连续最长的数字串

str1=input("请输入一个字符串：")

count=0
l=0
strmax=[]
list1=[] #空列表存放数字字符串
#for i in str1[:len(str1)-1]: #这样不行，改为range下标的
for i in range(len(str1)):
    if str1[i].isdigit():
        count+=1
        list1.append(str1[i])
    else:
        if l<count:
            l=count
            strmax=list1.copy()  #把list1复制到这里
            list1.clear()  #清空list1
            count=0
        else:             #如果字符串较短，也要清空原来的
            list1.clear()
            count=0

#卡在这里卡了好久，其实最后多加一个判断list1和strmax就好了，因为字符串最后一个是数字的话，不执行else的，就没法存入strmax
if len(strmax)>len(list1):
    for i in strmax:
        print(i,end="")
else:
    for i in list1:
        print(i, end="")


