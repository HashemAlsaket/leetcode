# Link to video: https://youtu.be/APil_B8COxU

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        p1, p2, p3 = None, head, head.next
        if not p3.next:
            p2.next = None
            p3.next = p2
            return p3
        
        while True:
            p2.next = None
            p2.next = p1
            if not p3:
                return p2
            p1, p2, p3 = p2, p3, p3.next
        