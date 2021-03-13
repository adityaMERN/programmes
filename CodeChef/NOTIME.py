#link: https://www.codechef.com/MARCH21C/problems/NOTIME

n,h,x=map(int,input().split(" "))
l=list(map(int,input().split(" ")))
c=0
for i in range(n):
    if x+l[i]>=h:
        print("YES")
        break
    else:
        c+=1
if c==n:
    print("NO")