#link: https://www.codechef.com/FEB21C/problems/MAXFUN

t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split(" ")))
    l.sort()
    x=l[0]
    y=l[n-1]
    print(2*(y-x))
    # final=[]
    # final.append(l[0])
    # final.append(l[1])
    # final.append(l[n-1])
    # ans=abs(final[0]-final[1])+abs(final[1]-final[2])+abs(final[2]-final[0])
    # print(ans)