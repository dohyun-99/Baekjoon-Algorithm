while True:
    A,B = map(int, input().split())
    if [A,B] == [0,0]:
        exit()
    if B%A == 0 :
        print('factor')
    elif A%B == 0:
        print('multiple')
    else:
        print('neither')