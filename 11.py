dic={1:'星期一',2:'星期二',3:'星期三',4:'星期四',5:'星期五',6:'星期六',7:'星期日'}
dic1={1:'MONDAY',2:'TUESDAY',3:'WEDNESDAY',4:'THURSDAY',5:'FRIDAY',6:'SATURDAY',7:'SUNDAY'}
a=int(input())
if 1<=a<=7:
    print(dic[a],dic1[a])
else:
    print('input error')
