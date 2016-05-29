def lenIter(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    n=0
    result=0
    while aStr[n:]!='':
        result+=1
        n+=1
    return result