N = int(input())

count = 100000

def dp(n, cnt):
    global count
    if cnt > count:
        return
    if n == 1:
        if cnt < count:
            count = cnt
        return
    if n % 3 == 0:
        cnt+=1
        dp(n//3, cnt)
        cnt-=1
    if n % 2 == 0:
        cnt+=1
        dp(n//2, cnt)
        cnt-=1
    cnt+=1
    dp(n-1, cnt)
    return

dp(N,0)
print(count)