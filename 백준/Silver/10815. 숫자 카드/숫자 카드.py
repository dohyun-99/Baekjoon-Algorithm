import sys

answer=[]
cards=[0]*20000000

N = int(sys.stdin.readline())
for i in list(map(int, sys.stdin.readline().split())):
    cards[i+10000000]=1
    
M = int(sys.stdin.readline())
for j in list(map(int, sys.stdin.readline().split())):
    if cards[j+10000000]==1:
        print(1, end=" ")
    else:
        print(0, end=" ")
