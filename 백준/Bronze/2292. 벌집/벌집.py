import sys
N = int(sys.stdin.readline())

floor = 1
addr = 1

while N > addr:
    addr += 6*floor
    floor += 1

print(floor)