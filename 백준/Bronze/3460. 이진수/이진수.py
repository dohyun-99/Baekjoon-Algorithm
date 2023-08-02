T = int(input())

for _ in range(T):
    N = int(input())
    cnt = 0
    while N >= 2:
        if N % 2 == 1:
            print(cnt, end=' ')
        N = N//2
        cnt += 1

    if N % 2 == 1:
        print(cnt, end=' ')