# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def partition(self, head: ListNode, x: int) -> ListNode:
        a=a_next=ListNode(0)
        b=b_next=ListNode(0)
        while head:
            if head.val<x:
                a.next=head
                a=a.next
            else:
                b.next=head
                b=b.next
            head=head.next
        b.next=None
        a.next=b_next.next
        return a_next.next