#question link: https://www.codechef.com/LTIME92C/problems/EVENDIFF

t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split(" ")))
    countofeven=0
    countofodd=0
    for i in range(n):
        if l[i]%2==0:
            countofeven+=1
        else:
            countofodd+=1
    print(min(countofodd,countofeven))