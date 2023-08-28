num = [[0,0] for _ in range(10)]

def solution(X, Y):
    answer = ""
    for x in X:
        num[int(x)][0]+=1
    for y in Y:
        num[int(y)][1]+=1
    
    for i in range(10):
        answer+=str(i)*min(num[i])

    if answer == "":
        return "-1"
    elif set(answer) == {'0'}:
        return "0"
    else:
        return answer[::-1]