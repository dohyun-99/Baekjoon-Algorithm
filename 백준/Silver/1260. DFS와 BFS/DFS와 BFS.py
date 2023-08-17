N, M, V =map(int, input().split())

graph=[[] for _ in range(N+1)]
for i in range(M):
    start,end = map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)

for x in graph:
    x=x.sort()

# DFS -> 깊이 우선 탐색
visited_dfs=[]
def dfs(graph_list, curr, visited):
    visited.append(curr)
    print(curr, end=' ')
    
    for i in graph_list[curr]:
        if i not in visited:
            dfs(graph_list, i, visited)          
    return

dfs(graph, V, visited_dfs)
print()


# BFS -> 너비 우선 탐색
from collections import deque
visited_bfs=[]
def bfs(graph_list, curr, visited):
    queue = deque([curr])
    visited.append(curr)
    
    while queue:
        v=queue.popleft()
        print(v, end=' ')
        for i in graph_list[v]:
            if i not in visited:
                queue.append(i)
                visited.append(i)

    return

bfs(graph, V, visited_bfs)


