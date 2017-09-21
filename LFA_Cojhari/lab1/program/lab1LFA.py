# Ganuscheak Vlad's code

file = open("input.txt","r")

counter = 0
nonterminal_symbol = []
string = []

for line in file:
    if counter % 2 < 1:
        nonterminal_symbol.append(line[:len(line) - 1:])
    else:
        string.append(line[:len(line) - 1:])
    counter += 1

def BFS(length, nonterminal_symbol, string, key_word):
    queue = []
    for i in range(length):
        if nonterminal_symbol[i] == "S":
            queue.append(string[i])
    first = 0
    def term(string, nonterminal_symbol):
        nonterm = 0
        for i in range(len(string)):
            for j in range(len(nonterminal_symbol)):
                if string[i] == nonterminal_symbol[j]:
                    nonterm += 1
                    break
        return len(string) - nonterm
    
    length_of_key_word = len(key_word)
    while first < len(queue):
        if term(queue[first], nonterminal_symbol) <= length_of_key_word:
            for i in range(len(queue[first])):
                for j in range(length):
                    if queue[first][i] == nonterminal_symbol[j]:
                        queue.append(queue[first][:i:] + string[j] + queue[first][i + 1::])
        #print(queue[first])
        if queue[first] == key_word:
            return True
        first += 1
    return False

print("Enter the word which should be verified in our grammar:")

print(BFS(counter // 2, nonterminal_symbol, string, input()))

    
file.close()
