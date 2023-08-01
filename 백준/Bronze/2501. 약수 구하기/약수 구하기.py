N,K = map(int, input().split())

# N의 약수 구하기
prime_num=[]
for i in range(1,N+1):
    if N%i ==0:
        prime_num.append(i)

if len(prime_num) < K:
    print(0)
else:
    print(prime_num[K-1])