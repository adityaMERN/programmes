#question link: https://www.codechef.com/FEB21C/problems/TEAMNAME
def function(a,b):
    s=len(set(a+b))
    return s
t=int(input())
for _ in range(t):
    n=int(input())
    l=input().split(" ")
    d={}
    for each in l:
        slicer=each[1:]
        if slicer in d:
            d[slicer].append(each[0])
        else:
            d[slicer]=[each[0]]
    #print(d)
    d1=list(d.keys())
    #print(d1)
    s=0
    for i in range(len(d)):
        for j in range(i+1,len(d)):
            temp=function(d[d1[i]],d[d1[j]])
            s+=(temp-len(d[d1[i]]))*(temp-len(d[d1[j]]))
    print(2*s)