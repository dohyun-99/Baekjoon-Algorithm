N = int(input())

if N == 1:
    print('*')

else: 
    print(' '*(N-1)+'*')

    for i in range(1,N-1):
        print(' '*(N-i-1)+'*'+' '*(2*i-1)+'*')

    print('*'*(2*N-1))