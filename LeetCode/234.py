# https://leetcode.com/problems/palindrome-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slowptr=head
        stack=[]
        while slowptr!=None:
            stack.append(slowptr.val)
            slowptr=slowptr.next
            
        while head!=None:
            i=stack.pop()
            if head.val==i:
                isPal=True
            else:
                isPal=False
                break
            head=head.next
        return isPal
        