import sys


def dice_score(trial):
    same_dice=len(set(trial))
    
    # 같은 눈이 4개 나왔을 때
    if same_dice == 1:    
        return 50000+trial[0]*5000

    elif same_dice == 2:
        # 같은 눈이 2개씩 두 쌍
        if trial[1]!=trial[2]:
            return 2000+(trial[1]+trial[2])*500
        
        # 같은 눈이 3개
        else:
            return 10000+trial[1]*1000
    
    # 같은 눈이 2개만 나왔을 때 
    elif same_dice == 3:
        for x in range(3):
            if trial[x]==trial[x+1]:
                return 1000+trial[x]*100
    
    # 모두 다른 눈이 나왔을 때
    else:
        return trial[-1]*100

N = int(sys.stdin.readline())

dice = [dice_score(sorted(list(map(int, input().split())))) for i in range(N)]

print(max(dice))