def genPrimes():
    listPrimes = []
    last = 1
    while True:
        last +=1
        for p in listPrimes:
            if last%p == 0:
                break
        else:
            listPrimes.append(last)
            yield last
            
def genPrimesFn():
    '''Function to return 1000000 prime numbers'''
    primes = []   # primes generated so far
    last = 1      # last number tried
    while len(primes) < 1000000:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
    return primes