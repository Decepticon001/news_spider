import time
import random
class Get_time:
    def Get_Time(self):
        a1=(2018,3,23,0,0,0,0,0,0)              #设置开始日期时间元组（1976-01-01 00：00：00）
        a2=(2018,3,23,23,59,59,0,0,0)    #设置结束日期时间元组（1990-12-31 23：59：59）
        start=time.mktime(a1)    #生成开始时间戳
        end=time.mktime(a2)
        t = random.randrange(start,end)
        local_time = time.localtime(t)
        data_head = time.strftime("%H:%M:%S", local_time)
        time_stamp = "%s.%s" % (data_head, str(t)[-3:])
        return time_stamp
