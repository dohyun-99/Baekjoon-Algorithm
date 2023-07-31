N,M = map(int, input().split())
basket=[x for x in range(N+1)]

for _ in range(M):
    i,j = map(int, input().split())
    basket[i], basket[j] = basket[j], basket[i]

for y in range(1,N+1):
    print(basket[y], end=" ")