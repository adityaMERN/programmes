# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        q,lastlevel=[root],[]
        while q:
            nextlevel=[]
            n=len(q)
            for _ in range(n):
                node=q.pop()
                for child in node.left,node.right:
                    if child:
                        nextlevel.append(child)
            q=nextlevel
            if nextlevel:
                lastlevel=nextlevel[:]
        return sum(node.val for node in lastlevel)
        