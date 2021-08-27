l=list(map(int,input().split(" ")))
low=min(l)
high=max(l)
while low<=high:
    mid=low+(high-low)//2
    