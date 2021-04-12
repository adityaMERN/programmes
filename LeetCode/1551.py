class Solution:
    def minOperations(self, n: int) -> int:
        arr=[]
        for i in range(n):
            arr.append((2*i)+1)
        n=len(arr)
        if n%2!=0:
            median=arr[(n-1)//2]
            summ=0
            for i in range(0,(n-1)//2):
                summ+=(median-arr[i])
                
                
        else:
            summ=0
            median=(arr[n//2]+arr[n//2-1])//2
            for i in range(0,n//2):
                summ+=(median-arr[i])
        return summ
        
        