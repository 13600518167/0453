
n=int(input('请输入人数' ))
a=0
list1=[ ]
list2=[ ]
dic={ }
dic2={ }
dic3={ }
while a!=n:
    name=input('请输入姓名' )
    score=input('请输入分数' )
    dic[name]=score
    dic2[name[0]]=name
    dic3[score]=name[0]
    b=ord(name[0])
    list1.extend([b])
    list1.sort(reverse=True)
    c=score
    list2.extend([c])
    list2.sort(reverse=True)
    a+=1

for i in list2:
    print(dic2[dic3[i]]," ",dic[dic2[dic3[i]]])



