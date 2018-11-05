#已知一个字符串包含许多组英文单词和中文解释，英文和中文交错排列。请将中文和英文分开，将中文链接后输出，将英文连接后输出。要求词汇之间以空格分开。

#判断是否为中文字符的函数
def is_chinese(unchar):
    ch2=ord(unchar)  #转化为ascii码
    if ch2>=0 and ch2<=127:
        return False
    else:
        return True

def main():
    s="china中国shanxi山西省Xi'an西安市"
    s1=""   #存放所有中文
    s2=""   #存放所有英文
    deal=1  #1：正在处理英文，0 正在处理中文
    for unchar in s:
        if is_chinese(unchar):  #是中文
            if deal==1:
                s2=s2+" "
                deal=0
            s1+=unchar
        else:                   #是英文
            if deal==0:
                s1=s1+""
                deal=1
            s2+=unchar

    print(s1)
    print(s2)

main()

#思路：1，两个变量，一个放中文一个放英文
#       2、判断英文的结束和中文的结束，设置正在处理变量，循环，用ascii码判断中英文

                 
            
                
