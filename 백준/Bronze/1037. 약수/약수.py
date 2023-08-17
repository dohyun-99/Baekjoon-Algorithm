N = int(input())

if N == 1:
    print(int(input())**2)
else:
    nums = sorted(list(map(int, input().split())))
    print(nums[0]*nums[-1])