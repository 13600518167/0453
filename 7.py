a=int(input('请输入一个年份' ))
if a%100==0:
    if a%400==0:
        print('该年份是闰年')
    else:
        print('该年份不是闰年')
elif a%4==0:
    print('该年份是闰年')
else:
    print('该年份不是闰年')


