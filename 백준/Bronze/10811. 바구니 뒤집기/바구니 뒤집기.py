N,M = map(int, input().split())
basket=[x for x in range(N+1)]

for _ in range(M):
    i,j = map(int, input().split())
    for x in range((j-i)//2+1):
        basket[i+x], basket[j-x] = basket[j-x], basket[i+x]

for y in range(1,N+1):
    print(basket[y], end=" ")