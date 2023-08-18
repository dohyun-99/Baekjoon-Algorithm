def solution(k, m, score):
    score = sorted(score)
    return sum([score[x]*m for x in range(len(score)%m, len(score), m)])