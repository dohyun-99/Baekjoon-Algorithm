import sys

N = int(sys.stdin.readline())

for i in range(N):
    change = int(sys.stdin.readline())
    for x in [25,10,5,1]:
        print(change//x, end=" ")
        change = change%x