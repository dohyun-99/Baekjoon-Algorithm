while True:
    N=int(input())
    if N == -1:
        break

    # N의 약수 구하기
    prime_num=[]
    for i in range(1,N):
        if N%i ==0:
            prime_num.append(i)

    if sum(prime_num) == N:
        print(f'{N} = {prime_num[0]}', end='')
        for x in prime_num[1:]:
            print(f' + {x}', end='')
        print()

    else:
        print(f'{N} is NOT perfect.')