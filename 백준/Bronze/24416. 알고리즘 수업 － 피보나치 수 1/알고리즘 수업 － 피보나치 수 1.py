import sys
num = int(sys.stdin.readline())

# 재귀호출
def fib(n):
    f=[1,1]
    for i in range(2,n):
        f.append(f[i-1]+f[i-2])
    return f[n-1]

print(fib(num), num-2)