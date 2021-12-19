n=int(input('请输入一个数' ))
a=0
b=0
for i in range(1,n+1):
    if i%2==0:
        a=a+i
    else:
        b+=i
print('奇数之和为',a,'偶数之和为',b)



