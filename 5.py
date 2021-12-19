def hellen(a,b,c):
    p=(a+b+c)/2
    s=p*(p-a)*(p-b)*(p-c)**0.5
    return s
a=int(input('请输入三角形的边长a：' ))
b=int(input('请输入三角形的边长b：' ))
c=int(input('请输入三角形的边长c: ' ))
if a+b>=c and a+c>=b and b+c>=a:
    print(round(hellen(a,b,c),3))
else:
    print('? 这TM是三角形？')
