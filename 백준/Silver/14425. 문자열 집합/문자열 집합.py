N, M = map(int, input().split())

word_set = [input() for _ in range(N)]
test_set = [input() for _ in range(M)]
cnt = 0

for x in test_set:
    if x in word_set:
        cnt += 1

print(cnt)