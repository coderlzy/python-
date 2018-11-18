#输入一段英文，统计出现的英文单词及其出现次数。要求程序可以过滤掉常见的标点符号，并按下面要求输出：
#1、将次数大于2的单词按字典序输出并输出其出现次数
#2、将出现次数大于2的单词按单词出现次数从大到小排序并输出次数

#获取值的函数
def getnum(s):
    return s[1]

def main():
    txt=input("请输入一段英文：")
    for i in txt:
        if i in "!@.,;'()-#$%^& ":
            txt=txt.replace(i,",")
    l=txt.split(",")
    l.sort()  #按字母顺序排序，空串就到了第一个位置了
    #去掉数字和空串
    while l[0].isdigit() or l[0]=="":
        del l[0]

    #统计单词出现次数
    wordcount={} #存放单词的字典
    for i in l:
        if i in wordcount:
            wordcount[i]+=1
        else:
            wordcount[i]=1
    print("按字典顺序输出单词及其出现次数（次数大于2）：")

    words=list(wordcount.keys())  #得到关键字列表

    words.sort()
    print(words)
    for i in words:
        if wordcount[i]>2:
            print(i,wordcount[i])

    print("按单词出现次数排序")
    times=list(wordcount.items())
    times.sort(key=getnum,reverse=True)
    for i in range(len(times)):
        if times[i][1]>2:
            print(times[i][0],times[i][1])

main()
