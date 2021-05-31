class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        x=max(nums)
        flag=0
        for i in nums:
            if i!=x and i*2>x:
                flag=1
                break
        if flag==1:
            return -1
        else:
            return nums.index(x)
        