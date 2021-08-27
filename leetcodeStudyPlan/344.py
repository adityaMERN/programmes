class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left=0
        right=len(s)
        for i in range(len(s)//2):
            temp=s[i]
            b=s[len(s)-i-1]
            s[i]=b
            s[len(s)-i-1]=temp
        