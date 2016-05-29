def recurPowerNew(base, exp):
    if exp%2!=0:
        return base*recurPowerNew(base, exp-1)
    if exp>0 and exp%2==0:
        return recurPowerNew(base, exp/2)*recurPowerNew(base, exp/2)
    if exp==0:
        return 1