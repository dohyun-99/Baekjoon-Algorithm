total=int(input())
stuffs=int(input())
cal=0
for i in range(stuffs):
    price,num=map(int,input().split())
    cal+=price*num
if cal == total:
    print("Yes")
else:
    print("No")