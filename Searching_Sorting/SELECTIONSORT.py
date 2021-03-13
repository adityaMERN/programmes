# #Explanation: The selection sort algorithm sorts an array by repeatedly finding the minimum element 
# (considering ascending order) from unsorted part and putting it at the beginning. 
# The algorithm maintains two subarrays in a given array.
# 1) The subarray which is already sorted.
# 2) Remaining subarray which is unsorted.
# In every iteration of selection sort, the minimum element (considering ascending order) 
# from the unsorted subarray is picked and moved to the sorted subarray.



l=list(map(int,input().split(" ")))

for i in range(len(l)):
    minindex=i
    for j in range(i+1,len(l)):
        if l[minindex]>l[j]:
            minindex=j
    l[i],l[minindex]=l[minindex],l[i]
print(l)


#Time complexity=O(n^2)
#Auxillary Space=O(1)