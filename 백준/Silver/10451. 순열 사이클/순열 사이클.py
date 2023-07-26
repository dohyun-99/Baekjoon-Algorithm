import sys
sys.setrecursionlimit(2000)
# 한 사이클의 끝까지 가야함
def dfs(visited,curr,graph):
    if visited[curr]==True:
        # 사이클 탐색 완료
        return
    else:
        visited[curr]=True
        curr=graph[curr-1][1]
        dfs(visited,curr,graph)
    return


T= int(input())
for i in range(T):
    N=int(input())
    nodes=list(zip([i for i in range(1,N+1)], list(map(int,input().split()))))

    check=[False]*(N+1)

    cycle=0
    for i in range(1,N+1):
        if check[i] == False:
            dfs(check,i,nodes)
            cycle+=1
    print(cycle)