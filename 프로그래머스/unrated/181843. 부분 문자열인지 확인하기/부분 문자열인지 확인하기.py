def solution(my_string, target):
    for x in range(len(my_string)-len(target)+1):
        if my_string[x:x+len(target)] == target:
            return 1
    return 0