import math
n=int(input('请输入n的值:' ))
list=[ ]
a=1
b=1
while a<=n:
    c=math.factorial(b)
    list.extend([c])
    a+=1
    b+=1
d=sum(list)
print(d)

