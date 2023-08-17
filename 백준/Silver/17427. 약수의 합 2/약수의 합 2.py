import sys
N = int(sys.stdin.readline())

answer = 0
for x in range(1, N+1):
    answer+=(N//x)*x
print(answer)