def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    L1=aDict.values()
    L2=aDict.keys()
    L3=[]
    for e in L1:
        L3.append(len(e))
    counter=0
    if L3==[]:
        return
    for z in L3:
        if z==max(L3):
            h=counter
            break
        else:
            counter+=1
    return L2[h]