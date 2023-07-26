num=int(input())
comp=list(map(int, input().split()))
comp.sort()
print(comp[0], comp[-1])