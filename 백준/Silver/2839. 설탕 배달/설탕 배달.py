N = int(input())

answer = 5000

for i in range(N//5+1):
    for j in range((N-5*i)//3+1):
        if 5*i+3*j == N:
            answer = min(answer,(i+j))

if answer == 5000:
    print(-1)
else:
    print(answer)