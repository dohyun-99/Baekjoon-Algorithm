def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        wall = ''
        tmp1 = bin(arr1[i])[2:].zfill(n)
        tmp2 = bin(arr2[i])[2:].zfill(n)
        for j in range(n):
            if int(tmp1[j])|int(tmp2[j]) == 1:
                wall+='#'
            else:
                wall+=' '
        answer.append(wall)
    return answer