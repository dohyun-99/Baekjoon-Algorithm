paper=[[0 for _ in range(100)] for _ in range(100)]
N = int(input())

for _ in range(N):
    a,b = map(int, input().split())
    for x in range(a, a+10):
        for y in range(b, b+10):
            paper[x][y] = 1

black=0
for x in paper:
    black+=x.count(1)
print(black)