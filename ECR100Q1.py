t=int(input(""))
anslist=[]
for _ in range(t):
    a,b,c=map(int,input().split(" "))
    if (a+b+c)%9==0:
        if min(a,b,c)>=(a+b+c)/9:
            anslist.append("YES")
        else:
            anslist.append("NO")
    else:
        anslist.append("NO")
for j in anslist:
    print(j)

#This question was from Edi=ucational round 100 question name was Dungeon.
# Link:  https://codeforces.com/contest/1463