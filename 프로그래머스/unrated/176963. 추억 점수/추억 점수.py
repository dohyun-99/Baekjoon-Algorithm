def solution(name, yearning, photo):
    answer = []
    yearn_dict = {}
    
    for i in range(len(name)):
        yearn_dict[name[i]] = yearning[i]
        
    for cut in photo:
        temp = 0
        for j in cut:
            try:
                temp += yearn_dict[j]
            except:
                pass
        answer.append(temp)
    return answer