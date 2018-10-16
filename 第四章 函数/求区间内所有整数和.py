#求区间[i,j]内所有整数和

"""def tosum(i,j):
    sum1=0
    for k in range(i,j+1):
        sum1+=k
    return sum1
print(tosum(1,100))"""


def mysum(i,j):
    sum1=0
    for k in range(i,j+1):
        sum1+=k
    return sum1

i=int(input("请输入区间值i："))
j=int(input("请输入区间值j："))
print("区间[i，j]内所有整数和为：",mysum(i,j))


