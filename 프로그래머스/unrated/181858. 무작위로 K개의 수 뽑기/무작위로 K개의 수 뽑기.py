def solution(arr, k):
    rand = []
    for x in arr:
        if x not in rand:
            rand.append(x)

    answer = [-1 for _ in range(k)]
    if len(rand) >= k :
        return list(rand)[:k]
    else:
        answer[:len(rand)] = list(rand)
        return answer