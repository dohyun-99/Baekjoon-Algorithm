import sys
N = int(sys.stdin.readline())

cor_array = [list(map(int, sys.stdin.readline().split()))[::-1] for _ in range(N)]

cor_array.sort()

for x in cor_array:
    print(x[1], x[0])