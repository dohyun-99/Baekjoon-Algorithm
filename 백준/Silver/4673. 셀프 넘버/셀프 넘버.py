def d_sum(num):
    result=num
    for i in str(num):
        result+=int(i)
    return result

test=[]
for i in range(10000):
    if d_sum(i) not in test:
        test.append(d_sum(i))

for j in range(10000):
    if j not in test:
        print(j)