#https://practice.geeksforgeeks.org/problems/missing-number-in-array1416/1#

class Solution:
    def MissingNumber(self,array,n):
        # code here
        x=sum(array)
        total=(n*(n+1))//2
        return total-x