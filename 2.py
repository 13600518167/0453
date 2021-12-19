def len(a,b,c,d):
    l=((a-c)**2+(b-d)**2)**0.5
    return l
a=float(input('请输入A的X坐标' ))
b=float(input('请输入A的Y坐标' ))
c=float(input('请输入B的X坐标' ))
d=float(input('请输入B的Y坐标' ))
print(round(len(a,b,c,d),3))
