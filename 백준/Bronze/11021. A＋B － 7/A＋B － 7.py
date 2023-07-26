import sys

test = int(sys.stdin.readline().rstrip())
for i in range(test):
    a, b = sys.stdin.readline().rstrip().split()
    print(f"Case #{i+1}: {int(a)+int(b)}")