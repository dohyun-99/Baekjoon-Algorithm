import sys

N = int(sys.stdin.readline())

nums = [int(sys.stdin.readline()) for i in range(N)]
nums.sort()

for i in nums:
    print(i)