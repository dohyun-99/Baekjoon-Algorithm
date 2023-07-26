N = int(input())
students=list(map(int,input().split()))
B,C = map(int,input().split())

total=[]
for i in students:
    answer = 1
    if i<=B:
        pass
    else:
        i-=B
        if i%C==0:
            answer+=i//C 
        else:
            answer+=(i//C+1)
    total.append(answer)
    
print(int(sum(total)))