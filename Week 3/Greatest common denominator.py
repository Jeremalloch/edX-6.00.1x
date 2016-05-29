def gcdIter(a, b):
    x=max(a,b)
    y=min(a,b)
    ycopy=y
    while y>0:        
        if x%y==0 and ycopy%y==0:
            return y
        else:
            y-=1