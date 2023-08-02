N,M = map(int,input().split())
maze=[]
for i in range(N):
    maze.append(list(map(int,list(input()))))
    
from collections import deque  


 
def bfs(x,y):  
    queue = deque([(x,y)])
    
    while queue:
        x,y = queue.popleft()
        
        for j in [[-1,0],[1,0],[0,-1],[0,1]]:
            next_x = x+j[0]
            next_y = y+j[1]
            if 0<=next_x<N and 0<=next_y<M:
                if maze[next_x][next_y]==1:
                    queue.append((next_x, next_y))
                    maze[next_x][next_y] = maze[x][y]+1
                    
    return maze[N-1][M-1]

print(bfs(0,0))  