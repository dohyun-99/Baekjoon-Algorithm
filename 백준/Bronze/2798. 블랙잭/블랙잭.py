N, M = map(int,input().split())
cards=list(map(int,input().split()))

card_sum=[]
for i in range(len(cards)-2):
    for j in range(i+1,len(cards)-1):
        for k in range(j+1, len(cards)):
            card_sum.append(int(cards[i]+cards[j]+cards[k]))

card_sum.sort()
maxnum=0
for n in range(len(card_sum)):
    if card_sum[n]<=M:
        maxnum=card_sum[n]

print(maxnum)