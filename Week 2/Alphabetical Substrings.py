s = 'uvgrdmyvmqqkwwojjcjtms'
a=[0]
for i in range(len(s)-2):    
    if (s[i]<=s[i+1])!=(s[i+1]<=s[i+2]):
        a.append(i+1)
a.append(len(s)-1)
b=[]
for j in range(len(a)-1):
    b.append(a[j+1]-a[j])
c=max(b)
for k in range(len(b)):
    if b[k]==c:
        d=k
e=a[d]
f=a[d+2]
print('Longest substring in alphabetical order is: ' + s[e:f])