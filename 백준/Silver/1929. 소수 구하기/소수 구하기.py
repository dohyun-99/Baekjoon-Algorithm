N,M = map(int, input().split())

answer = [True] * (M+1)
answer[1] = False

for i in range(2, M+1):
    if answer[i] == True:
        for j in range(i+i,M+1,i):
            answer[j] = False

for x in range(N, M+1):
    if answer[x] == True:
        print(x)