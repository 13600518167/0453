import math
for i in range(1000,10000):
    string=str(i)
    s=int(math.sqrt(i))
    if string[0]==string[1] and string[2]==string[3]:
        if s**2==i:
           print(i)
            
