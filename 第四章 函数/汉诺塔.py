#汉诺塔，三个塔，每次只能移动一个盘子，保持大盘子在下小盘在下,把A塔的盘子全部移到C塔上

def hanoi(n,ch1,ch2,ch3):  #n 盘子个数，ch1初始位置，ch2借助位置，ch3最终位置
    if n==1:
        print(ch1,"->",ch3)
    else:
        hanoi(n-1,ch1,ch3,ch2)
        print(ch1,"->",ch3)
        hanoi(n-1,ch2,ch1,ch3)
N=int(input("请输入盘子数："))

hanoi(N,'A','B','C')
