#已知平面上若干点坐标为：A0(1,2),A1(-1,3),A2(2,1.5),A3(-2,0),A4(4,2)
# 计算任意两点的距离并且生成距离矩阵，其中矩阵元素（i，j）表示Ai和Aj之间的距离
#最后输出距离矩阵和任意两点的最大距离


#思路：用列表X和Y分别存储点的横纵坐标，循环计算ij距离，保存在一个二维列表中

#计算两点距离
import math
def juli(x1,y1,x2,y2):
    return math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))

def main():
    X=[1,-1,2,-2,4]
    Y=[2,3,1.5,0,2]
    M=[]  #存储距离矩阵
    s=0   #最大距离初始化等于0
    for i in range(len(X)):
        M.append([])
        for j in range(len(X)):
            V=juli(X[i],Y[i],X[j],Y[j])
            M[i].append(V) #添加到M的第一行

            if s<M[i][j]:
                s=M[i][j] #保存最大距离

    #打印
    for i in range(len(X)):
        for j in range(len(X)):
            print("%5.2f"%M[i][j],end=" ")
        print()

    print("任意两点的最大距离是：","%5.2f"%s)

main()


