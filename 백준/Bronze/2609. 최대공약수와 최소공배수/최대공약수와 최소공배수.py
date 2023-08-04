A, B = map(int, input().split())
least, greatest = 1, 1

n = 2

while A > 1 or B > 1:
    if A % n == 0 and B % n == 0:
        least *= n
        greatest *= n
        A = A//n
        B = B//n
    elif A % n == 0 and B % n != 0 :
        greatest *= n
        A = A//n
    elif A % n != 0 and B % n == 0:
        greatest *= n
        B = B//n
    else:
        n += 1

print(least)
print(greatest)