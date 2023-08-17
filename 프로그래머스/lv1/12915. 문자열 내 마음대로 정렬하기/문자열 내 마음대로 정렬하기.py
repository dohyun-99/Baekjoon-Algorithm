def solution(strings, n):
    temp = [[i[n],i] for i in strings]
    temp.sort()
    return [tmp[1] for tmp in temp]