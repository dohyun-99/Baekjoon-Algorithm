import sys
input=sys.stdin.readline

N,M=map(int,input().split())
numbers=list(map(int,input().split()))

numbers.sort()

visited=[False]*N

def dfs(depth,n):
    # depth+=1
    visited[n]=True
    result.append(numbers[n])
    depth+=1 
    
    # 조건을 만족하면 출력
    if depth == M:
        print(' '.join(map(str,result)))
        return
      
    for i in range(n+1,N):
        if visited[i] == False:
            dfs(depth,i)
            result.pop()
            visited[i]=False
    return
            
for x in range(len(numbers)):
    result=[]
    dfs(0,x)
