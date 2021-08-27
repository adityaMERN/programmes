class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left=0
        right=len(nums)-1
        current=len(nums)-1
        result=[0 for i in range(len(nums))]
        while current>=0:
            if abs(nums[left])>=abs(nums[right]):
                result[current]=nums[left]*nums[left]
                left+=1
            else:
                result[current]=nums[right]*nums[right]
                right-=1
            current-=1
        return result
                
        