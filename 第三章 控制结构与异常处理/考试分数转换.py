##将百分制成绩转换为5分制成绩

grace=float(input("请输入学生的考试成绩："))
a=grace
if grace>=90:            
    a=5
elif grace>=80:             ##是在if grace>=90的情况中的else
    a=4
elif grace>=70:
    a=3
elif grace>=60:
    a=2
else:
    a=1
print("学生成绩：",grace,",转换百分制后的成绩为：",a)
