def solution(s):
    answer = 0
    temp = s[0]
    start = 0
    cnt = [1,0]
    
    for x in range(1, len(s)):
        if cnt[0] == 0:
            start = x
            temp = s[x]
            cnt = [1, 0]
        else:
            if s[x] == temp:
                cnt[0]+=1
            else:
                cnt[1]+=1

            if cnt[0] == cnt[1]:
                answer+=1
                cnt = [0,0]

    if cnt != [0,0]:
        answer+=1
    return answer