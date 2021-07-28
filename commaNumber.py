def commaNumber(num):
    'This function takes a numeric type (int/float) and returns a striing representation with commas seperating groups of three digits starting with the ones, tens, and hundreds place in the first (right-most) group'
    fullNumberStr = str(num)
    strList = []
    numList = fullNumberStr.split('.')
    intStr = numList[0]
    while len(intStr) > 0:
        strList.append(intStr[-3:]) # Builds a list with groups of three digits on the lhs of the .
        intStr = intStr[:-3]
    fStr = ''
    for i in range(len(strList)):
        fStr += strList.pop()
        if len(strList) > 0:
            fStr += ','
    for elem in numList[1:]:
        fStr += '.' + elem # Adds the rhs of the . to the string
    return fStr
# print(commaNumber(12345.678)) # Example usage
