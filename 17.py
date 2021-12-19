a=int(input('请输入三位数' ))
if 100<=a<=999:
    if int(str(a)[0])**3+int(str(a)[1])**3+int(str(a)[2])**3==a:
        print(a,'是秋水仙数')
    else:
        print(a,'不是秋水仙数')
else:
    print('这TM是三位数？')
