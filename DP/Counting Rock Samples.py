s,r=map(int,input().split(" "))
arr=list(map(int,input().split(" ")))
rangePpm=[]
for _ in range(r):
    r1,r2=map(int,input().split(" "))
    rangePpm.append([r1,r2])
ans=[]
for i in rangePpm:
    count=0
    for j in arr:
        if i[0]<=j<=i[1]:
            count+=1
    ans.append(count)
    count=0
for k in ans:
    print(k,end=" ")