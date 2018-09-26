#用户输入年份，闰年是True,不是就False
##能被4整除且不能被100整除的，或者能被400整除的年份是闰年
##（哇原来闰年的规则这么复杂！！！）
##算法思想：取余%

year=int(input("请输入年份："))
a=year%4
b=year%100
c=year%400
result=((a==0 and b!=0) or c==0)
print("年份结果:",result)

#在python中用and/or/not 表示与或非，而不是&&，||
