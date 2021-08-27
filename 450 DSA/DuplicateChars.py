s=str(input())
d={}
for each in s:
    if each in d:
        d[each]+=1
    else:
        d[each]=1
l=[]
for key in d:
    if d[key]>1:
        l.append(key)
print(l)
