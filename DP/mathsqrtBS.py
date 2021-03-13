n=int(input())
ans=0
start=1
end=n
while start<=end:
    mid=(start+end)//2
    if mid*mid==n:
        print(mid)
    elif mid*mid<n:
        start=mid+1
        ans=mid
    else:
        end=mid-1
print(ans)
    