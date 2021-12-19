# 在这里写上你的代码 :-)
import random

k = int(input("请输入整数k:"))
n = 0
c = " "
if 1 < k < 100:
    while n <= k:
        a = str(random.randint(1, 10))
        n += 1
        b = a + ","
        c += b
    print(c)
    print("整数1出现的次数", c.count("1"))
    print("整数5出现的次数", c.count("5"))
    print("整数10出现的次数", c.count("10"))
else:
    print("什么牛马那么大")
