def solution(k, score):
    return [min(sorted(score[:x+1])[-k:]) for x in range(len(score))]