#输入一个正整数，利用while语句，计算[1,n]内所有奇数的和

#用时：6分钟

#我用while的时候经常出现死循环，因为没有配合 break 使用，以后要记住

n=int(input("请输入一个正整数："))
sum1=0
for i in range(1,n+1):  
    while(i%2!=0):
        sum1+=i
        break
print("[1,n]内所有奇数的和是：",sum1)
    
