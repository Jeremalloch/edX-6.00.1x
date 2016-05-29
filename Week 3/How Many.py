def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    L1=aDict.values()
    howMany=0
    for e in L1:
        howMany+=len(e)
    return howMany