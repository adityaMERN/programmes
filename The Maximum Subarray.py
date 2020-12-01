import sys
t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split(" ")))
    def maxSumSubarray(arr,n):
        max_so_far=-sys.maxsize-1
        max_ending_here=0
        for i in range(n):
            max_ending_here=max_ending_here+arr[i]
            if max_so_far<max_ending_here:
                max_so_far=max_ending_here
            if max_ending_here<0:
                max_ending_here=0
        return max_so_far
    def maxSumSubsequence(arr,n):
        c=0
        for i in arr:
            if i<0:
                c+=1
        if c==n:
            arr.sort()
            return arr[-1]
        else:
            count=0
            for i in arr:
                if i>0:
                    count+=i
            return count
    x=maxSumSubarray(arr,n)
    y=maxSumSubsequence(arr,n)
    print(x,y)

#hackerank question:The maximum subarray
#link:   https://www.hackerrank.com/challenges/maxsubarray/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign