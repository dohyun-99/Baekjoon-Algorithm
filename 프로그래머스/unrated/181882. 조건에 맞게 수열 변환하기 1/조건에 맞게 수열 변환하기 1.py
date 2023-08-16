def solution(arr):
    answer = []
    for x in arr:
        if x >= 50 and x%2 == 0:
            answer.append(x//2)
        elif x < 50 and x%2 == 1:
            answer.append(x*2)
        else:
            answer.append(x)
            
    return answer