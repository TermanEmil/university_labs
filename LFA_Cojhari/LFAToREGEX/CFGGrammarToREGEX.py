# Helper function for the function below.
def findBrackets(stri, n):
    counter = -1
    for i in range (n - 2, -1, -1) :
        if stri[i] == ')' :
            counter -= 1
        elif  stri[i] == '(' :
            counter += 1
        if counter ==  0 :
            break

    counter = -1

    for j in range (n + 2, len(stri)) :
        if stri[j] == '(' :
            counter -= 1
        elif  stri[j] == ')' :
            counter += 1
        if counter ==  0 :
            break

    return i, j

# Remove repeating cycles (ab)*(ab)* == (ab)*
def deleteingMultipleLoops(stri):
    i = 0
    while i < len(stri) :
        if stri[i] == '*' and i != len(stri) - 1:
            left , rigt  = findBrackets(stri , i)
            boolean_1 = stri[left : i ] == stri[i + 1 : rigt + 1]
            boolean_2 = boolean_1 and (rigt < len(stri) - 1)

            if boolean_2 and stri[rigt + 1] == '*' :
                new_i = i - len(stri[left : i + 1])
                stri = stri[: left ] + stri[ i + 1 :]
                i = new_i
        i += 1
    return stri

# Remove a line and acolumn from the given Matrix.
def delete(Matrix, k, nonterminals):
    for i  in nonterminals:
        for  j in nonterminals :
            item = Matrix.get((i, j), None)
            if item != None:
                if i == k or j == k :
                    del Matrix[i, j]
                else :
                    Matrix [i ,j] = '(' +  Matrix [i ,j] + ')'

# Remove unecessary stuf from the given regex.
def simplifyREGEX(strregex):
    newlist = newlist0 = []
    strregex = strregex.replace("$*", "$")
    strregex = strregex.replace("$+", "")
    strregex = strregex.replace("$", "")

    if strregex == '' :
        return '$'

    strregex = strregex.split("+")

    for i in range (len(strregex)):
        if '(' not in strregex[ i ] and ')' not in strregex[ i ] and strregex[ i ] not in newlist0:
            newlist0.append (strregex[i])

    i = 0
    while i != len (strregex ) -1 :
        boolean1_1 = '(' in strregex[i]   or ')' in strregex[i]
        boolean1_2 = '(' in strregex[i+1]  or ')' in strregex[i+1]
        boolean2_1 = False
        if len(strregex[i]) > 1 and (strregex[i][-2:-1] != ')*' ) :
            boolean2_1 = True
        boolean2_2 = boolean2_1 and (strregex[i][-1] != ')' )
        boolean2 =  boolean2_2 and (strregex[i+1][0] != '(' )
        if boolean1_1 and boolean1_2 and boolean2 :
            strregex[i] = strregex[i] + '+' + strregex[i + 1]
            del strregex[i +1]
            i -= 1
        i += 1

    for i in range(len(strregex))  :
        strregex[i] = deleteingMultipleLoops(strregex[i])

    if len(newlist0 ) == 0 :
        newlist0 = strregex

    for x in newlist0 :
        if x not in newlist:
            newlist.append(x)
    strregexing = ''

    for x in range( len(newlist) ) :
        strregexing = strregexing + newlist [x] + '+'
    return strregexing[:-1]

def reduceNode(Matrix, nodeIndex, nonterminals):
    for i  in nonterminals:
        for  j in nonterminals:
            if i != nodeIndex and j != nodeIndex:
                Matrix[i, i] += '+' + Matrix[i, nodeIndex] + (Matrix[nodeIndex, nodeIndex]) + '*' + Matrix[nodeIndex, i]
                Matrix [i, i] = simplifyREGEX( Matrix[i,i])
                Matrix[j, j] += '+' +  Matrix[j, nodeIndex] + (Matrix[nodeIndex, nodeIndex]) + '*' + Matrix[nodeIndex, j]
                Matrix [j, j] = simplifyREGEX( Matrix[j, j])
                Matrix[i, j] += '+' +  Matrix[i, nodeIndex] + (Matrix[nodeIndex, nodeIndex]) + '*' + Matrix[nodeIndex, j]
                Matrix [i, j] = simplifyREGEX( Matrix[i, j])
                Matrix[j, i] += '+' +  Matrix[j, nodeIndex] + (Matrix[nodeIndex, nodeIndex]) + '*' + Matrix[nodeIndex, i]
                Matrix [j, i] = simplifyREGEX(Matrix[j, i])

def readMatrixFromFile(fileName):
    file = open(fileName, "r")
    nonterminals, terminals = set(), set()
    Matrix = dict()
    for line in file:
        tmp = line[:-1].split(" -> ")
        tmp += list(tmp.pop(-1))
        N1, T, N2 = tmp
        nonterminals.update(N1, N2)
        terminals.add(T)
        item = Matrix.get((N1, N2), None)

        if item == None:
            Matrix[N1, N2] = T
        else:
            Matrix[N1, N2] = '(' + item + '+' + T + ')'

    file.close()
    return Matrix, N1, T, N2, nonterminals

def fillMainDiagonalWithEpsiolons(Matrix, nonterminals):
    for x in nonterminals:
        item = Matrix.get((x, x), None)
        if item == None:
            Matrix[x, x] = '$'

def removeAllIntermediateStates(Matrix, nonterminals):
    while len(nonterminals) > 1:
        for x in nonterminals:
            if x != nonterminals[0]:
                reduceNode(Matrix, x, nonterminals)
                delete(Matrix, x, nonterminals)
                del nonterminals [1]

# The inputFile contains CFG grammar
def toRegex(inputFile):
    Matrix, N1, T, N2, nonterminals = readMatrixFromFile(inputFile)
    nonterminals = sorted (nonterminals)

    fillMainDiagonalWithEpsiolons(Matrix, nonterminals)
    removeAllIntermediateStates(Matrix, nonterminals)
    return Matrix['1', '1'] + '*'

print(toRegex("input.txt"))