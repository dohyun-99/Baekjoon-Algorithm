A,B,V = map(int, input().split())

loc,day = 0,1

if V>A:
    day+=(V-A)//(A-B)
    if (V-A)%(A-B) != 0:
        day +=1
print(day)