fe = [0]*100001

def prime_num(n):
    num = 0
    for i in range(1,int(n**0.5)+1):
        if n/i == i:
            num+=1
        elif n%i == 0:
            num+=2
            
    return num

def solution(number, limit, power):
    answer = 0
    for x in range(1, number+1):
        if fe[x] == 0:
            fe[x] = prime_num(x)

        if fe[x] > limit:
            answer+=power
        else:
            answer+=fe[x]
        
    return answer