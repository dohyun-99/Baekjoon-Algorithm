max_num=0
max_loc=[1,1]

for i in range(1,10):
    temp=list(map(int,input().split()))
    if max(temp) > max_num:
        max_num = max(temp)
        max_loc=[i,temp.index(max_num)+1]

print(max_num)
print(max_loc[0], max_loc[1])