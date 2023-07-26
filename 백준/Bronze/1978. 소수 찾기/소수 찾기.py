def prime_num(num):
    if num == 1:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True

N=int(input())
numbers=list(map(int,input().split()))

answer=0
for i in numbers:
    if prime_num(i)==True:
        answer+=1
print(answer)