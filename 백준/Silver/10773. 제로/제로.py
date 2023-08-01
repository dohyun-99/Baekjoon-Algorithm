import sys

K = int(sys.stdin.readline())

total = []
for _ in range(K):
    num = int(sys.stdin.readline())
    if num == 0:
        total.pop()
    else:
        total.append(num)

print(sum(total))