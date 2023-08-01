N=int(input())

div = 2
answer=[]

while N != 1:
    if N % div == 0:
        answer.append(div)
        N = N//div
    else:
        div+=1

for i in answer:
    print(i)