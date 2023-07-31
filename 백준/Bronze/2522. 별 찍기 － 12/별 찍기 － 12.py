N = int(input())

for i in range(1, N):
    print(' '*(N-i)+'*'*(i))

for i in range(N):
    print(' '*(i)+'*'*(N-i))