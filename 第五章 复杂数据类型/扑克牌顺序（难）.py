#题目：将扑克牌按花色+大小顺序排序输出，重复的删除

#定义一个对“黑红梅方”四个字重新编号的函数

def Rebianhao(s):
    if s[0:2]=="黑桃":
        return 4
    elif s[0:2]=="红桃":
        return 3
    elif s[0:2]=="梅花":
        return 2
    elif s[0:2]=="方块":
        return 1
    else:
        return 0

#定义一个获取牌点数的函数

def Getnum(s):
    if s[2:]=="J":
        return 11
    elif s[2:]=="Q":
        return 12
    elif s[2:]=="K":
        return 13
    elif s[2:]=="A":
        return 14
    else:
        return int(s[2:])  ##这里我没有注意，输出的应该要转为整型而不是字符串型

#定义一个删除重复的牌的函数

def Removesame(l):
    for e in l : #l为一手牌的列表
        for i in range(1,l.count(e)): #count()统计每个元素出现的次数
            #如果出现2次，就删掉！SO EASY 啊可是就是想不到
            l.remove(e) #移除列表l中的e元素

#主函数

def main():
    #自己定义一手牌
    l=["梅花A","方块4","红桃7","黑桃Q","梅花J","方块9","红桃5","黑桃3","方块4","黑桃3","黑桃10","梅花K"]

    #先按花色排序
    l.sort(key=Rebianhao,reverse=True) #这里：sort(key=函数/表达式)，这里函数只能由一个参数，且默认带入的数据就是列表中的每一个元素
    print(l)

    #同种花色按点数排列
    #思路：提取列表中同花色的值放入新的列表进行排序，然后再连接，提取的过程比较难，要找到临界点
    l2=[] #存放排好序的牌
    s=[] #临时存放同种花色排好序的牌
    p=["黑桃","红桃","梅花","方块"]

    i=0
    j=0

    #对应每一种花色的循环
    for k in range(4):
        i=j #i=j,j是这一手牌中，这一花色的牌的起始下标
        #找出某一花色的最后一张牌的下一个位置，放入
        while j<len(l) and p[k] in l[j]: ###这个非常重要  # in 判断某个元素是否在列表中
            j=j+1
        s=l[i:j] #将l中同花色的值提取出来放到s里面排序
        s.sort(key=Getnum,reverse=True) #这里如果reverse=None,默认从小到大，如果从大到小就是True
        l2=l2+s
    l=l2
    print(l)

    #去掉重复牌
    Removesame(l)
    print(l)

main()







