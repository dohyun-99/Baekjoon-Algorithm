while True:
    try:
        n = int(input())
    except:
        break

    one = '1'
    while int(one) % n != 0:
        one+='1'
    print(len(one))