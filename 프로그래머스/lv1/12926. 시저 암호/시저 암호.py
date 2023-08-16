def solution(s, n):
    low = 'abcdefghijklmnopqrstuvwxyz'
    up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    answer = ''
    for x in s:
        if x in low:
            answer+=low[low.index(x)+n-26]
        elif x in up:
            answer+=up[up.index(x)+n-26]
        else:
            answer+=x
    return answer