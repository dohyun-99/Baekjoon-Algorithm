def solution(n, m, section):
    answer = 0
    wall = [1 for _ in range(n)]
    for x in section:
        wall[x-1] = 0
    
    y = 0
    while y < n:
        if wall[y] == 0:
            answer += 1
            for z in range(m):
                try:
                    wall[y+x] = 1
                except:
                    pass
            y += m
        else:
            y += 1
        
    return answer