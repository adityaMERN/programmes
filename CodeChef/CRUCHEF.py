a=int(input())
b=list(map(int,input().split(" ")))
d={}
for i in range(len(b)):
    if b[i] in d:
        d[b[i]]+=1
    else:
        d[b[i]]=1
print(dict(sorted(d.items(), reverse=True,key=lambda item: item[1])))

