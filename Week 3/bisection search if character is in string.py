def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    while len(aStr)>1:
        if char == aStr[len(aStr)/2]:
            return True
        elif char < aStr[len(aStr)/2]:
            return isIn(char, aStr[:(len(aStr)/2)])
        elif char > aStr[len(aStr)/2]:
            return isIn(char, aStr[(len(aStr)/2):])
    if len(aStr) == 1:
        return char == aStr
    if len (aStr) == 0:
        return False