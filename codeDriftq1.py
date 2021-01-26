# class Node:
#      def __init__(self, data=None,next=None):
#         self.data = data
#         self.next = next
# class LinkedList:
#     def __init__(self):
#         self.head=None
#     def insert_at_end(self, data):
#         if self.head is None:
#             self.head = Node(data, None)
#             return
#         itr = self.head
#         while itr.next:
#             itr = itr.next
#         itr.next = Node(data, None)

#     def insert_values(self, data_list,t):
#         self.head = None
#         for data in data_list:
#             a = (int(data) // t) * t
#             b = a + t
#             if int(data)-a>b-int(data):
#                 x=b
#             else:
#                 x=a
#             #return (b if n - a > b - n else a)
#             self.insert_at_end(a)

#     def print(self):
#         if self.head is None:
#             print("Linked list is empty")
#             return

#         itr = self.head
#         llstr = ''
#         while itr:
#             llstr += str(itr.data) + ' -> '
#             itr = itr.next
#         llstr=llstr[:-3]
#         print(llstr)
# if __name__ == '__main__':
#     l=input()
#     b=int(input())
#     x = l.split("->")
#     ll=LinkedList()
#     ll.insert_values(x,b)
#     ll.print()


# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def solve(self, A, B):
        head=A
        while(head):
            head.val=head.val//B*B
            head=head.next
        return A