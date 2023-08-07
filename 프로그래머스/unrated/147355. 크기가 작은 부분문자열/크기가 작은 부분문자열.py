def solution(t, p):
    part = [int(t[i:i+len(p)]) for i in range(0,len(t)-len(p)+1)] 
    
    answer = 0
    for x in part:
        if x <= int(p):
            answer +=1
    return answer