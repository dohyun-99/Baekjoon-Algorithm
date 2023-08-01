N = int(input())

cor_array = [list(map(int, input().split())) for i in range(N)]

cor_array.sort()

for x in cor_array:
    print(x[0], x[1])
