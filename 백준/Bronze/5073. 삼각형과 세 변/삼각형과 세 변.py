while True:
    nums = sorted(list(map(int, input().split())))

    if sum(nums) == 0:
        break
    elif nums[2] >= sum(nums[0:2]):
        print('Invalid')
    else:
        if len(set(nums)) == 1:
            print('Equilateral')
        elif len(set(nums)) == 2:
            print('Isosceles')
        else:
            print('Scalene')
