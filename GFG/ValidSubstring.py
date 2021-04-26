#https://practice.geeksforgeeks.org/problems/3b47f0ad00f953dd514235ddec54e39fdc297dda/1/#

def findMaxLen(ob, S):
        # code here 
        stack=[]
        count=0
        stack.append(-1)
        for i in range(len(S)):
            if S[i]=="(":
                stack.append(i)
            else:
                if len(stack)!=0:
                    stack.pop()
                if len(stack)!=0:
                    count = max(count,
                             i - stack[len(stack)-1])
                else:
                    stack.append(i)
        return count