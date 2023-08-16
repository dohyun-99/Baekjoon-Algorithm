def solution(d, budget):
    total=0
    cnt=0
    d.sort()
    for x in d:
        if total+x <= budget:
            cnt+=1
            total+=x
    return cnt