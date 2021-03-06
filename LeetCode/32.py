class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[-1]
        res=0
        for i in range(len(s)):
            if s[i]=="(":
                stack.append(i)
            else:
                if len(stack)!=0:
                    stack.pop()
                if len(stack)!=0:
                    res=max(res,i-stack[len(stack)-1])
                else:
                    stack.append(i)
        return res
                
        