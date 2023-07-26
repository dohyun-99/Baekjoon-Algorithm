import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N,M,start = map(int,input().split())

node=[[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    node[a].append(b)
    node[b].append(a)
     
for i in range(N):
    node[i] = sorted(node[i])

visited=[False]*(N+1)
seq=[]

def dfs(R):   # V : 정점 집합, E : 간선 집합, R : 시작 정점
    # 정점 R을 방문 했다고 표시한다.
    visited[R] = True
    seq.append(R)

    # node(R) : 정점 R의 인접 정점 집합.(정점 번호를 오름차순으로 방문한다)
    for x in node[R]:
        if visited[x] == False:
            dfs(x)
    return

dfs(start)

result=[0]*(N+1)
for i in range(len(seq)):
    result[seq[i]]=i+1
    
for j in result[1:]:
    print(j)