import random
o=0
n=int(input('请输入n' ))
if 1<n<=20:
    print(n)
    a=random.randint(0,10000)
    b=random.randint(0,a)
    print(a,b)
    while o<n:
        c=random.randint(0,10000)
        d=random.randint(0,c)
        print(c,d)
        if d/c-b/a>0.05:
            print('better')
        elif d/c==b/a:
            print('same')
        else:
            print('worse')
        o=o+1




