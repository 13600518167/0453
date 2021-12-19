
import random
k=int(input("请输入k的值"  ))
if 1<k<5:
    m=str(random.randint(2,9999))
    print(k)
    while m.count('3')!=k:
        m=str(random.randint(2,9999))
        break
    print(m)
    if int(m)%19==0:
        print('YES')
    else:
        print('NO')
else:
    print('傻逼')





