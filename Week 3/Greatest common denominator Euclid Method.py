def gcdRecur(a, b):
    x=max(a,b)
    y=min(a,b)
    if x%y==0:
        return y
    else:
        return gcdRecur(y,x%y)