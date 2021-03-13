s=str(input())
d={}
for char in s:
    if char in d:
        d[char]+=1
    else:
        d[char]=1
frequency=[]
for key in d:
    frequency.append(d[key])
print(frequency)
c=0
if len(set(frequency))==1:
    print("YES")
else:
    for i in range(0,len(frequency)):
        #x=frequency[i]-1
        y=frequency[i]
        print(y)
        #frequency[i]-=1
        if frequency[i]==0:
            frequency.remove(0)
        if len(set(frequency))==1:
            m=2
            #print("YES")
            break
        else:
            index=i
            frequency.insert(index,y)
            frequency[i]=y
            m=3
            c+=1
    #print(frequency)
    if m==2:
        print("YES")
    elif c==len(frequency):
        print("NO")
