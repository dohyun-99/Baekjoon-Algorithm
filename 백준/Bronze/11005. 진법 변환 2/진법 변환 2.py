alphabet_dict = {}
capital_alphabet = ['0', '1', '2', '3', '4', '5', '6', '7','8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
for i in range(len(capital_alphabet)):
    alphabet_dict[i] = capital_alphabet[i]

N, B = map(int, input().split())
num=str()

while N > B:
    num+=alphabet_dict[N%B]
    N = N//B

num+= alphabet_dict[N%B]
if N//B != 0:
    num+=alphabet_dict[N//B]

print(num[::-1])