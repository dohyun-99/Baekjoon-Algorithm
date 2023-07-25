import sys
N = int(sys.stdin.readline())

nums=[int(sys.stdin.readline()) for i in range(N)]

if nums[0]+nums[2] == 2* nums[1]:
    # 등차 수열
    Q = nums[1]-nums[0]
    print(nums[-1]+Q)
else:
    # 등비 수열
    Q = nums[1]//nums[0]
    print(nums[-1]*Q)