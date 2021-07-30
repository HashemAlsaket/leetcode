# Link to video: 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1:
            return head
        
        def rev(h):
            if not h or not h.next:
                return h
            p1, p2, p3 = h, h.next, h.next.next
            
            if not p2.next:
                p2.next = p1
                p1.next = None
                return p2
            
            p1.next = None
            p2.next = p1
            p1 = p2
            p2 = p3
            p3 = p3.next
            while True:
                if not p3:
                    p2.next = p1
                    return p2
                p2.next = None
                p2.next, p1 = p1, p2
                p2, p3 = p3, p3.next
            
        h = head
        p1, p2 = h, h
        
        # first rev
        for i in range(k - 1):
            if not p2.next:
                return rev(p1)
            p2 = p2.next
        p3 = p2.next
        p2.next = None
        p1, p2 = rev(p1), p1
        
        h = p1
        p2.next = p3
        p1, p2 = p2, p2.next
        while True:
            p1.next = None
            p3 = p2
            tf = True
            for i in range(k - 1):
                if not p3 or not p3.next:
                    p1.next = p2
                    tf = False
                    break
                p3 = p3.next
            if not tf:
                break
            p4 = p3.next
            p3.next = None
            p2, p3 = rev(p2), p2
            p1.next = p2
            p3.next = p4
            p1, p2, p3 = p3, p4, p4
        return h
        
        