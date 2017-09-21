# Ganuscheak Vlad's code

file = open("input.txt","r")

nonterminal_symbol = []
string = []
counter = 0

for line in file:
    if counter % 2 < 1:
        nonterminal_symbol.append(line[:len(line) - 1:])
    else:
        string.append(line[:len(line) - 1:])
    counter += 1

type_two = type_three = True

left_most_derivation = right_most_derivation = False
eps = False

for i in range(counter // 2):
    if len(nonterminal_symbol[i]) > 1:
        type_two = type_three = False
        break

    non_term1 = term1 = -1
    non_term2 = term2 = -1
    for j in range(len(string[i])):
        if string[i][j] >= 'A' and string[i][j] <= 'Z':
            if non_term1 < 0:
                non_term1 = j
            non_term2 = j
        else:
            if term1 < 0:
                term1 = j
            term2 = j

        #cases when type 2 or type 3 are impossible!
        if len(string[i]) == 1 and string[i][0] >= 'A' and string[i][0] <= 'Z':
            type_three = False
        
        if (term1 < non_term1 and term2 > non_term1) or (non_term1 < term1 and non_term2 > term1):
            type_three = False

        if term1 >= 0 and non_term1 >= 0:
            if term1 < non_term1:
                right_most_derivation = True
            else:
                left_most_derivation = True

        if string[i] == "":
            eps = True

        for j in range(1, len(string[i])):
            if string[i][j - 1] >= 'A' and string[i][j - 1] <= 'Z':
                if string[i][j] >= 'A' and string[i][j] <= 'Z':
                    type_three = False
                    break
                
        
if (left_most_derivation == right_most_derivation) and (right_most_derivation == True):
    type_three = False

if eps == True and left_most_derivation == True:
    type_two = False

def ans(T1, T2):
    if T2:
        return "Type III"
    if T1:
        return "Type II"
    return "Type 0"

print(ans(type_two, type_three))
