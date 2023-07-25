import sys

N=int(sys.stdin.readline())
answer=0
num=1
while num < N:
    answer+= (num*N + num)
    num+=1

print(answer)