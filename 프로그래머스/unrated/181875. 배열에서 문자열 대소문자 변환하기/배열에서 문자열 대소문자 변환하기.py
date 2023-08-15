def solution(strArr):
    answer = []
    for x in range(len(strArr)):
        if x % 2 == 0:
            answer.append(strArr[x].lower())
        else:
            answer.append(strArr[x].upper())
    return answer