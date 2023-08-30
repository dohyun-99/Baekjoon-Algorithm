N,M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

def dfs(answer,nums):
    if len(answer) == M:
        print(' '.join(map(str, answer)))
        return
    for x in range(len(nums)):
        answer.append(nums[x])
        dfs(answer,nums[x:])
        answer.pop()
    return

dfs([], numbers)