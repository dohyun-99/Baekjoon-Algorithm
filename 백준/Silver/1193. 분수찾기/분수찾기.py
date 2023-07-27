import sys
N = int(sys.stdin.readline())

loc=0
cnt=0

while N > loc:
    cnt+=1
    loc+=cnt

move = loc - N

if cnt %2 == 0 : # 짝수라인
    print(f"{cnt-move}/{1+move}")
else: # 홀수 라인
    print(f"{1+move}/{cnt-move}")
