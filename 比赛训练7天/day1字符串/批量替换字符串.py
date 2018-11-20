while True:
	try:
		str1=input("请输入一个字符串：")
	#手动替换
		list1=list(str1)
		for i in range(len(list1)):
			if list1[i] is " ":
				list1[i]="%20"
			print("".join(list1[i]),end="")
	except EOFError:
		break
