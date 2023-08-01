words=[list(str(input())) for _ in range(5)]

for i in range(15):
    for j in range(5):
        try:
            print(words[j][i], end='')
        except:
            pass