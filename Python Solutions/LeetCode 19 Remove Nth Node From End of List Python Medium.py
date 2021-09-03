# Link to video: https://youtu.be/vm4BKlzpMUs

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head or not head.next:
            return
        
        m = n
        n = 0
        h = head
        
        while h:
            n += 1
            h = h.next
        
        # if equal, remove first node
        if m == n:
            head = head.next
            return head
        
        # general case
        h = head
        for i in range(n - m - 1):
            h = h.next
        
        # if second to last node
        if not h.next.next:
            h.next = None
            return head
        
        h.next = h.next.next
        
        return head