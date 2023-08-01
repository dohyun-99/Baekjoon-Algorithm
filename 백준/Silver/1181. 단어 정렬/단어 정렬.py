N = int(input())

word_dict = [[] for _ in range(51)]

for _ in range(N):
    word = str(input())
    word_dict[len(word)].append(word)

for x in word_dict:
    if x != []:
        temp = sorted(set(x))
        for y in temp:
            print(y)