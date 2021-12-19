import random
n=int(input('请输入n' ))
a=0
c=0
d=0
while a<n:
    b=random.randint(0,1000)
    a+=1
    print(b)
    if b%2==0:
        c+=1
    else:
        d+=1
print(n,'个数中有偶数',c,'个','奇数有',d,'个')
