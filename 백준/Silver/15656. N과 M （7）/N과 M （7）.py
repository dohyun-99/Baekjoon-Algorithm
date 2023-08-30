N,M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

def dfs(answer):
    if len(answer) == M:
        print(' '.join(map(str, answer)))
        return
    for x in numbers:
        answer.append(x)
        dfs(answer)
        answer.pop()
    return

dfs([])