import sys
sentence = str(sys.stdin.readline())

for i in range(len(sentence)//10+1):
    print(sentence[10*i:10*i+10])