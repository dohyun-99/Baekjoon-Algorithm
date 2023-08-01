N = int(input())
cor = list(map(int,input().split()))

sorted_list = sorted(set(cor))

num_dict = {}
for i in range(len(sorted_list)):
    num_dict[sorted_list[i]] = i

for i in cor:
    print(num_dict[i], end=' ')