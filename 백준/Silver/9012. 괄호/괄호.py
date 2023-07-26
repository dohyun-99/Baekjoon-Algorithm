T=int(input())
cases=[]
for i in range(T):
    cases.append(list(str(input())))

def VPS(strings):
    if len(strings)%2==1 or strings[0]==')':
        print('NO')
    else:
        stack=[]
        try:
            for i in strings:
                if i == '(':
                    stack.append(i)
                else:
                    stack.pop()
            if len(stack)==0:
                print('YES')
            else:
                print('NO')
        except:
            print('NO')
            
for a in cases:
    VPS(a)