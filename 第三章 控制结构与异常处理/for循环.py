#求1-n之间正整数的平方和

n=int(input("请输入正整数n："))
sum=0
for i in range(1,n+1,1):
    sum=sum+i*i
print("1-",n,"之间正整数的平方和是：",sum)
