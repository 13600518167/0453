import math
e=1
n=int(input('请输入n的值;'  ))
for i in range(1,n+1):
    a=math.factorial(i)
    b=1/a
    e+=b
print(round(e,10))
