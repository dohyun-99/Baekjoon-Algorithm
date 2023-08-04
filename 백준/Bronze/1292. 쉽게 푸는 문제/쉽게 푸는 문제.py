A, B = map(int, input().split())

series  = [1 for _ in range(1002)]

cnt = 1
num = 1

while cnt <= B:
    for x in range(num):
        series[cnt] = num
        cnt+=1
        if cnt > 1000:
            break
    num+=1

print(sum(series[A:B+1]))