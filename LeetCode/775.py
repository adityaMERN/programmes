class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        maximum=-1
        for i in range(1,len(A)):
            if A[i]<maximum:
                return False
            else:
                maximum=max(A[i-1],maximum)
        return True
        
        