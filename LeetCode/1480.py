#link: https://leetcode.com/problems/running-sum-of-1d-array/

def runningSum( nums) :
        for i in range(1,len(nums)):
            nums[i]=nums[i]+nums[i-1]
        return nums
nums=list(map(int,input().split(" ")))
print(runningSum(nums))