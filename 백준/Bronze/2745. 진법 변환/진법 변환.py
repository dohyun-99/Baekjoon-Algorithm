alphabet_dict = {}
capital_alphabet = ['0', '1', '2', '3', '4', '5', '6', '7','8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
for i in range(len(capital_alphabet)):
    alphabet_dict[capital_alphabet[i]] = i

N, B = input().split()

ten = 0
for j in range(len(N)):
    ten+=alphabet_dict[N[j]]*(int(B)**(len(N)-j-1))
print(ten)