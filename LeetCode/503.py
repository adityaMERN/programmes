class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
            if(nums == []):
                return []
        
            if(len(nums) == 1):
                return [-1]
        
        
            stack = []
            stack.append(0)
            ans = [-1] * len(nums)
        
            for i in range(1,len(nums)):
            
                while(stack and nums[stack[-1]] < nums[i]):
                    ans[stack.pop()] = nums[i]
                
                stack.append(i)
            
        
            for i in range(len(nums)):
            
                while(stack and nums[stack[-1]] < nums[i]):
                    ans[stack.pop()] = nums[i]
                
            return ans