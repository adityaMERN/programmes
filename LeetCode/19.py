class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        l = []
        
        while(head):
            l.append(head.val)
            head = head.next
        
        l.pop(len(l)-n)
        i = ListNode()
        temp = i
        for j in l:
            i.next = ListNode(j)
            i = i.next
        return temp.next