import sys
input = sys.stdin.readline
N=int(input())
people=[]
for i in range(N):
    people.append(list(map(int, input().split())))

for i in people:
    win=1
    for j in people:
        if j[0]>i[0] and j[1]>i[1]:
            win+=1
    print(win, end = " ")