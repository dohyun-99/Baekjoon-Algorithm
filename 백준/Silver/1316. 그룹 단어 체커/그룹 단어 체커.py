N=int(input())
group_words=0

for i in range(N):
    word = str(input())
    temp=[word[0]]
    for i in range(1, len(word)):
        if word[i-1] != word[i]:
            temp.append(word[i])

    if len(temp) == len(set(word)):
        group_words += 1

print(group_words)