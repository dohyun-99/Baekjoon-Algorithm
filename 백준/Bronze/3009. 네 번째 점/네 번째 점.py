x, y = [], []

for i in range(3):
    a,b = map(int, input().split())
    x.append(a)
    y.append(b)

x.sort()
y.sort()

if x[1] == x[0]:
    print(x[2], end=" ")
else:
    print(x[0], end=" ")

if y[1] == y[0]:
    print(y[2])
else:
    print(y[0])
