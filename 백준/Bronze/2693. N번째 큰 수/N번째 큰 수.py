N = int(input())

for _ in range(N):
    temp = sorted(list(map(int, input().split())))
    print(temp[7])