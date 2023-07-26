import sys
sys.setrecursionlimit(15000)

N= int(input())

area = [list(map(int,input().split())) for _ in range(N)]

# BFS / DFS 다 가능
from collections import deque

low_area=min(map(min,area))
high_area=max(map(max,area))

def dfs(loc):
    check[loc[0]][loc[1]]=True
    for i in [[0,1],[0,-1],[1,0],[-1,0]]:
        next_x=loc[0]+i[0]
        next_y=loc[1]+i[1]
        if 0<=next_x<N and 0<=next_y<N:
            if check[next_x][next_y] == False:
                if area[next_x][next_y] > height:
                    dfs([next_x,next_y])
    return   

if low_area == high_area:
    print(1)
else:
    safe=0
    for height in range(low_area, high_area):

        check=[[False]*N for _ in range(N)]
        
        temp_safe=0
        
        for i in range(N):
            for j in range(N):
                if check[i][j] == False :
                    if area [i][j] > height:
                        dfs([i,j])
                        temp_safe+=1
        safe=max(temp_safe,safe)
        
    print(safe)