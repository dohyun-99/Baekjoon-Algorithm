N = int(input())

members = []

for _ in range(N):
    age, name = input().split()
    members.append([int(age), str(name)])

members.sort(key=lambda x:x[0])

for x in members:
    print(x[0], x[1])