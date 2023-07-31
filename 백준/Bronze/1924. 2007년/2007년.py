import sys
x,y = map(int, sys.stdin.readline().split())

month = [31,28,31,30,31,30,31,31,30,31,30,31]
days=['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

for i in range(x-1):
    y += month[i]

print(days[y%7])