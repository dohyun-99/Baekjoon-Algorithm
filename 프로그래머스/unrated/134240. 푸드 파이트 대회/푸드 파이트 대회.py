def solution(food):
    setting = ''
    for x in range(1, len(food)):
        setting+=str(x)*(food[x]//2)
    return ''.join([setting, '0', setting[::-1]])