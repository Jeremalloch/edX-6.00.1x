s = 'uvgrdmyvmqqkwwojjcjtms'
s='a'+s
lengthTrue=[]
startTrue=[]
endTrue=[]
i=0
while i<(len(s)-2):
    if s[i]<=s[i+1] and s[i-1]>s[i]:
        startTrue.append(i)
        lengthTruecounter=1
        i+=1
        if s[i]<=s[i+1] and s[i+1]>s[i+2]:
            lengthTruecounter+=1
            lengthTrue.append(lengthTruecounter)
            endTrue.append(i+1)
            i+=1
        elif s[i]<=s[i+1]:
            i+=1
            lengthTruecounter+=1
    if s[i]>s[i+1]:
        i+=1