#输入一个ip地址，***，***，***，***（0-225）
#将IP地址转化为32位二进制形式输出，也就是将***转化为8位二进制数后依次连接起来形成32位二进制数


#判断输入的数据是否合法
#L是列表
def isvalidip(L):
    if len(L)!=4:
        return False
    #判断每个数是不是在0-255之间
    for i in L:
        # if i>225 or i<0 : (这样是错的因为没有转化成整形)
        if i.isdigit()==False or int(i)>255 or int(i)<0:
            return False
    return True

#十进制转化为二进制
def _10to2(num):
    res=""
    while True:

        #注意，之前报错，是因为num是字符串而不是数，%用在这里的话就被理解成格式化输出了，而不是取余了
        #在传入值的时候要保证传入的是一个数值

        res=str(num%2)+res
        #取余，转字符串，连接（倒序连接）
        num=num//2
        if num==0:
            break

        #高位补零补齐
    while len(res)<8:
        res='0'+res

    return res

#主函数
def main():
    ip=input("请输入合法的ip地址：")
    #分割，放入列表
    L=ip.split('.')
    if isvalidip(L)==False:
        print("ip地址不合法")
        return
    ss = ""

    for i in L:
        ss = ss+" "+_10to2(int(i)) #这里，要转成整型传入函数里计算，字符串没法计算

    print(ss)

main()
    



















    
    
