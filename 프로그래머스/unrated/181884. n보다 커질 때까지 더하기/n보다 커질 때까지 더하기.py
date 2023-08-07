def solution(numbers, n):
    answer = numbers[0]
    cnt = 1
    while answer <= n and cnt < len(numbers):
        answer+=numbers[cnt]
        cnt+=1
    return answer