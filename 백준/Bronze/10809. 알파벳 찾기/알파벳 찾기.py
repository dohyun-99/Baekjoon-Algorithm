alphabet_dict = {}

for i in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
    alphabet_dict[i] = -1

word = str(input())

for j in range(len(word)):
    if alphabet_dict[word[j]]==-1:
        alphabet_dict[word[j]] = j

for x in alphabet_dict:
    print(alphabet_dict[x], end=' ')