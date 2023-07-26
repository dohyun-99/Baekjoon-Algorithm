numbers=[]
rest=[]

for i in range(10):
    numbers.append(int(input()))
    rest.append(numbers[i]%42)

count={}
for i in rest:
    try: count[i] += 1
    except: count[i]=1
print(len(count))