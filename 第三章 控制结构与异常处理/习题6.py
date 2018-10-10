#10个评委打分，歌手最后得分是减去一个最高分减去一个最低分后的分数的平均分。

#用时：

#学到一个新的：一次性输入几个数，用空格隔开，把他们放到列表里面
# li=list(map(int,input().split()))
#首先使用split()函数将输入根据空格转换为字符串的列表，
#再使用map()函数将字符串列表中的每个字符串 ‘1’ 转化为int整型数值  1 ，
#最后将map返回的对象转为数值列表li 最后列表中的便是需要的列表了：

li=list(map(int,input("请输入10个分数，用空格间隔:").split()))
sum1=0
max=1
min=100
for i in li:
    sum1+=i
    if(i>=max):
        max=i
    if(i<=min):
        min=i
sum2=sum1-max-min
avr=sum2/8
print("10个得分分别是：",li)
print("最高分是：",max,"，最低分是：",min)
print("最终平均分是：",avr)

    
    
