import sys
A,B = map(int,sys.stdin.readline().split())

if A>B:
    A,B=B,A

print(B*(B+1)//2 - (A-1)*A//2)