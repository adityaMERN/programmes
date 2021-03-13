#Question: Bubble Sort is the simplest sorting algorithm that works by 
# repeatedly swapping the adjacent elements if they are in wrong order.

l=list(map(int,input().split(" ")))
for i in range(len(l)):
    for j in range(len(l)-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)

#time complexity=O(n2)
#space complexity=O(1)