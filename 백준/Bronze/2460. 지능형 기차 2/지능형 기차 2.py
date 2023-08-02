train = [0 for _ in range(11)]

for x in range(1, 11):
    takeoff, ride = map(int, input().split())
    train[x] = train[x-1] - takeoff + ride

print(max(train))