def solution(num_list):

    temp = 1
    for i in num_list:
        temp *= i
        
    if temp < sum(num_list)**2:
        return 1
    else:
        return 0