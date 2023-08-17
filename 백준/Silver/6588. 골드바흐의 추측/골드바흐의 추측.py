import sys

answer = [True] * (1000001)
answer[1] = False

for i in range(2, 1000001):
        if answer[i] == True:
            for j in range(i+i, 1000001,i):
                answer[j] = False

while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break

    cnt = True
    for y in range(3, (N+1)//2+1 , 2):
        if answer[y] and answer[N-y]:
            print(f'{N} = {y} + {N-y}')
            cnt = False
            break
    if cnt == True:
        print("Goldbach's conjecture is wrong.")