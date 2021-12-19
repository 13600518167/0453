a=0
m=int(input('请输入m' ))
n=int(input('请输入n' ))
if 0<m<n<10000:
    for i in range(m,n+1):
       if i%17==0:
          a+=i
    print(a)
else:
    print('数不符合要求')
