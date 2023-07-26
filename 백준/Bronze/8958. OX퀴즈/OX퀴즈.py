test=int(input())
quiz=[]
for i in range(test):
    quiz.append(str(input()))

def checking(prob):
    total=0
    temp=0
    for k in prob:
        if k == "O":
            temp+=1
            total+=temp
        elif k == "X":
            if temp != 0:
                temp=0
    
    print(total)

for j in quiz:
    checking(j)
