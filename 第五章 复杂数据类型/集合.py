#通过对集合和列表进行下列操作：

#（1）向列表添加10000个元素，向集合添加10000个元素
#（2）再向列表插入10000个元素，再向集合添加10000个元素
#（3）判断10000个元素是否在列表中，判断10000个元素是否在集合中
#（4）从列表中删除10000个元素，从集合中删除10000个元素
#比较集合类型和列表类型的相似操作在时间效率上的差异


#记录操作时间，导入时间模块time time.time()活得当前时刻

import time

def main():
    list1=[]  #列表
    s=set()   #集合


#向列表添加元素
    starttime=time.time()  #获取列表添加的开始时间
    for i in range(10000):
        list1.append(i)
    endtime=time.time()   #列表添加的结束时间
    listtime1=(endtime-starttime)*1000
    print("append向列表添加元素的时间为：","%5.1f"%listtime1,"毫秒")

#向集合添加元素
    starttime=time.time()
    for i in range(10000):
        s.add(i)
    endtime=time.time()
    stime1=(endtime-starttime)*1000
    print("add向集合添加元素时间为：","%5.1f"%stime1,"毫秒")

#向列表插入元素：
    starttime=time.time()
    for i in range(10000):
        list1.insert(10,i)
    endtime=time.time()
    listtime2=(endtime-starttime)*1000
    print("insert向列表插入元素时间为：","%5.1f"%listtime2,"毫秒")

#向集合添加元素
    starttime=time.time()
    for i in range(10000):
        s.add(i)
    endtime=time.time()
    stime1=(endtime-starttime)*1000
    print("add向集合添加元素时间为：","%5.1f"%stime1,"毫秒")

#判断10000个元素是否在列表中
    starttime=time.time()
    for i in range(10000):
       i in list1
    endtime=time.time()
    listtime3=(endtime-starttime)*1000
    print("判断是否在列表中耗时：","%5.1f"%listtime3,"毫秒")

#判断是否在集合中
    starttime=time.time()
    for i in range(10000):
        i in s
    endtime=time.time()
    stime1=(endtime-starttime)*1000
    print("判断是否在集合中耗时：", "%5.1f" % stime1, "毫秒")

# 从列表中删除元素
    starttime=time.time()
    for i in range(10000):
        list1.remove(i)
    endtime=time.time()
    stime1=(endtime-starttime)*1000
    print("remove删除列表元素耗时：", "%5.1f" % stime1, "毫秒")

# 从集合表中删除元素
    starttime=time.time()
    for i in range(10000):
        s.remove(i)
    endtime=time.time()
    stime1=(endtime-starttime)*1000
    print("remove删除集合元素耗时：", "%5.1f" % stime1, "毫秒")


main()

