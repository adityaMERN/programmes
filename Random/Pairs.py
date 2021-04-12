# can we divide an array with even length into n/2 pairs such that each pair is divisible by k
def count(l,n,k):
    f=[0]*k
    for i in range(n):
        f[l[i]%k]+=1
    summ=f[0]*(f[0]-1)/2
    i=1
    while i<k//2 and i!=k-i:
        summ+=f[i]*f[k-i]
        i+=1
    if k%2==0:
        summ+=f[k//2]*(f[k//2]-1)/2
    return int(summ)
l=list(map(int,input().split(" ")))
k=int(input())
n=len(l)
print(count(l,n,k))