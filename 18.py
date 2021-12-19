k=int(input('请输入k的值：' ))
a,b,i=0,1,1
while i<k:
    a,b=b,a+b
    i+=1
print('菲波那切数列的第',k,'个数是',b)



