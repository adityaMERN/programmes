class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack=''
        for i in s:
            stack+=i
            if len(stack)>=k:
                if stack[-k:]==i*k:
                    stack = stack[:-k]
        return stack
                
#         stack=[]
#         count=1
#         for i in range(len(s)):
#             if len(stack)==0:
#                 stack.append(s[i])
#             elif stack[-1]!=s[i]:
#                 stack.append(s[i])
#                 count=1
#             elif stack[-1]==s[i] :
#                 stack.append(s[i])
#                 if count!=k:
                    
#                     count+=1
#                     if count==k:
#                         for ka in range(k):
#                             stack.pop()
#                         x=len(stack)
#                         if x==0:
#                             continue
#                         elif x<k:
#                             y=stack[-1]
                            
#                         count=1
#         string=""
#         for each in stack:
#             string+=each
#         return string
          
        