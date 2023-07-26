T=int(input())

for i in range(T):
    sentence=list(map(str,input().split()))
    for k in sentence:
        print(k[::-1], end=' ')
    print()