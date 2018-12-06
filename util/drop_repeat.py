import hashlib

import redis

"""
使用redis去重
"""

#  password = '123456',
class Drop_rep:
    def __init__(self):
        try:
            self.r = redis.Redis(host='localhost',port=6379, db=0)
        except Exception as e:
            print(e)

    def drop_re(self,key,title):
        sha1 = hashlib.sha1()
        sha1.update(title.encode())
        hashRs = sha1.hexdigest()
        flag = self.r.sadd(key, hashRs)
        return flag