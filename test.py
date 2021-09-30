#import myMath
#from myMath import add, sub
#from myMath import *
import myMath as mm
import random as r
import math as m
import time
#import sys 다른 폴더에 모듈
#sys.exit()
#sys.path.append("c:\Temp")

x = mm.add(23,41)
print(x)

y = mm.sub(81,23)
print(y)

print(mm.msg)
print(__name__) # 시스템 변수(모듈명)

print(r.randrange(10))
print(r.randrange(4, 10))
print(r.randrange(6, 15, 2))

print(r.choice("abcde"))
print(r.choice([10, 24, 30, 'a']))

print(r.randint(3,4))

a = [1,2,3,4,5]
print(r.shuffle(a))

print(r.sample(a,2))

print(m.pi)

print(m.pow(2, 4))
print(2 ** 4)
print(m.sqrt(16))

print(time.time())
print(time.ctime())

t = time.time()
print(time.localtime(t))

start = time.time()

for x in range(5, -1, -1):
    print(x)
    time.sleep(1)

end = time.time()

print("%.6f초 " % (end - start))
print("%.6f초 ", end - start)

