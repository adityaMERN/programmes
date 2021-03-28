
#https://www.codechef.com/COOK127B/problems/CONDEL

t=int(input())
for _ in range(t):
    n,k=map(int,input().split(" "))
    l=list(map(int,input().split( " ")))
    sumOfk=sum(l[:k])
    minimum=sumOfk
    for i in range(k,n):
        sumOfk+=l[i]
        sumOfk-=l[i-k]
        minimum=min(minimum,sumOfk)
    res=sum(l)-minimum
    answer=res+(minimum*(minimum+1))//2
    print(answer)
    
