#重新自己敲一遍扑克牌排序
#1按花色大小排序输出
#2在花色大小的基础上按A-2排序输出
#3去掉重复的牌输出


#对花色重新编号的函数
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

#对牌点数大小获取的函数
def Getpoint(s):
    if s[2:]=="A":
        return 14
    elif s[2:]=="K":
        return 13
    elif s[2:]=="Q":
        return 12
    elif s[2:]=="J":
        return 11
    else:
        return int(s[2:])

#删除重复牌的函数
def Removesame(L):
    #用count函数统计出现次数，循环删除
    for e in L:
        for i in range(1,L.count(e)):
            L.remove(e)


def main():
    #设置一手牌，放在列表L里面
    L=["方块2","黑桃9","方块K","梅花7","红桃5","黑桃3","红桃J","方块7","梅花A","黑桃8","黑桃9","梅花7","方块Q","梅花6","红桃10","红桃Q"]

    #1、按花色顺序输出
    L.sort(key=Rebianhao, reverse=True)
    print(L)

    #2、在花色的基础上按大小排序输出
    #思路没忘，就是找到每种花色的起始位置，把他们放到临时的列表里面排序，再把列表连接

    L2=[] #放排好序的列表
    s=[] #用来排序的临时列表
    p=["黑桃","红桃","梅花","方块"]
    i=0
    j=0
    for e in range(4):
            i=j
            while j<len(L) and p[e] in L[j]:
                j=j+1
            s=L[i:j]
            s.sort(key=Getpoint,reverse=True)
            L2=L2+s
    L=L2
    print(L)

    #删除重复
    Removesame(L)
    print(L)

main()



