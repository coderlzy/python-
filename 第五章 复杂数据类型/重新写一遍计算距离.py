#计算各个点之间的距离并且输出最大值

#计算距离的函数
from math import *

def distance(x1,y1,x2,y2):
    return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))

#主函数
def main():
    X=[1,-1,2,-2,4]
    Y=[2,3,1.5,0,2,]
    M=[] #存储各个点的距离
    s=0 #最大距离

    for i in range(len(X)):
        M.append([])
        for j in range(len(Y)):
            V=distance(X[i],Y[i],X[j],Y[j])
            M[i].append(V)
            if s<M[i][j]:
                s=M[i][j]

    for i in range(len(X)):
        for j in range(len(Y)):
            print("%5.3f"%M[i][j],end=" ")
        print()
    print("最大距离为：","%5.3f"%s)

main()
