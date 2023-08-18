def solution(s):
    alpha_dict = {}
    for x in range(len(s)):
        if s[x] in alpha_dict.keys():
            alpha_dict[s[x]].append(x)
        else:
            alpha_dict[s[x]] = [x]
            
    answer = [-1] * len(s)
    for y in alpha_dict:
        if len(alpha_dict[y]) > 1:
            for z in range(1, len(alpha_dict[y])):
                answer[alpha_dict[y][z]] = alpha_dict[y][z] - alpha_dict[y][z-1]
    return answer