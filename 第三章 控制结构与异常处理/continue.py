#在若干成绩中，统计及格的人的平均成绩

x=[98,72,80,45,30,89,92,54,48,82,67,76]
sum1=0
m=0
k=0 #记录个数
for i in x:
    m=i
    if(m>=60):
        sum1+=m
        k+=1
        continue
if(m!=0):
    avr=sum1/k
    print("及格人数为：",k,",平均成绩为：",avr)
else:
    print("全都不及格！")
        

