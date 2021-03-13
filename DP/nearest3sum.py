array=list(map(int,input().split(" ")))
target=int(input())
array.sort()
initial=sum(array[:3])
for i in range(len(array)-2):
    left=i+1
    right=len(array)-1
    while left<right:
        newsum=array[i]+array[left]+array[right]
        if abs(newsum-target)<abs(initial-target):
            initial=newsum
        if newsum<target:
            left+=1
        else:
            right-=1
print(initial)