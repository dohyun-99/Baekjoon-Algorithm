N = int(input())

cor_dict = {}
for i in range(N):
    x,y = map(int, input().split())
    if x not in cor_dict:
        cor_dict[x] = [y]
    else:
        cor_dict[x].append(y)

temp = sorted(list(cor_dict.keys()))
for x in temp:
    for y in sorted(cor_dict[x]):
        print(x, y)